"""Finite checks for reference-free readout, using only the Python standard library."""

from itertools import product
from math import comb, cos, exp, isclose, pi, prod, sin, sqrt
from random import Random


def assert_close(actual, expected):
    assert isclose(actual, expected, abs_tol=3e-12, rel_tol=3e-12), (actual, expected)


def response(m, angle, z):
    return ((cos(angle) + 1j * z * sin(angle)) ** m).imag


def cnot(state, control, target):
    control_mask = 1 << control
    target_mask = 1 << target
    return [
        state[index ^ target_mask] if index & control_mask else state[index]
        for index in range(len(state))
    ]


def rotate_y(state, target, angle, control=None):
    target_mask = 1 << target
    control_mask = 0 if control is None else 1 << control
    output = list(state)
    cosine, sine = cos(angle / 2), sin(angle / 2)
    for index in range(len(state)):
        if index & target_mask or (control_mask and not index & control_mask):
            continue
        paired_index = index | target_mask
        output[index] = cosine * state[index] - sine * state[paired_index]
        output[paired_index] = sine * state[index] + cosine * state[paired_index]
    return output


def compressor(state, target, signals, angle):
    for signal in signals:
        state = cnot(state, target, signal)
    state = rotate_y(state, target, pi / 2 - len(signals) * angle)
    for signal in signals:
        state = rotate_y(state, target, 2 * angle, control=signal)
    return state


def hadamard(state, target):
    mask = 1 << target
    return [
        (state[index & ~mask] + (-1 if index & mask else 1) * state[index | mask])
        / sqrt(2)
        for index in range(len(state))
    ]


def native_cnot(state, control, target, fault):
    state = cnot(state, control, target)
    if fault:
        return [state[index ^ (1 << target)] for index in range(len(state))]
    return state


def reversed_cnot(state, control, target, fault):
    state = hadamard(hadamard(state, control), target)
    state = native_cnot(state, target, control, fault)
    return hadamard(hadamard(state, control), target)


def noisy_controlled_y(state, control, target, angle, faults):
    state = reversed_cnot(state, control, target, faults[0])
    state = rotate_y(state, target, -angle / 2)
    state = reversed_cnot(state, control, target, faults[1])
    return rotate_y(state, target, angle / 2)


def noisy_compressor(state, target, signals, angle, faults):
    m = len(signals)
    for signal, fault in zip(signals, faults[:m]):
        state = native_cnot(state, target, signal, fault)
    state = rotate_y(state, target, pi / 2 - m * angle)
    for index, signal in enumerate(signals):
        control_faults = faults[m + 2 * index:m + 2 * index + 2]
        state = noisy_controlled_y(state, signal, target, 2 * angle, control_faults)
    return state


def z_mean(state, targets):
    mask = sum(1 << target for target in targets)
    return sum((-1) ** ((index & mask).bit_count()) * abs(amplitude) ** 2
               for index, amplitude in enumerate(state))


def basis_state(width, index):
    state = [0j] * (1 << width)
    state[index] = 1
    return state


def pure_product(width, z, phase):
    alpha = sqrt((1 + z) / 2)
    beta = sqrt((1 - z) / 2) * complex(cos(phase), sin(phase))
    return [
        alpha ** (width - index.bit_count()) * beta ** index.bit_count()
        for index in range(1 << width)
    ]


def z_twirl_branch(state, mask):
    return [
        (-1) ** ((mask & index).bit_count()) * amplitude
        for index, amplitude in enumerate(state)
    ]


def check_compressor():
    for m in range(1, 7):
        angle = 0.25 / sqrt(m)
        width = m + 1
        signals = range(1, width)
        means = []
        for index in range(1 << width):
            state = compressor(basis_state(width, index), 0, signals, angle)
            signal_sum = m - 2 * (index >> 1).bit_count()
            mean = z_mean(state, (0,))
            assert_close(mean, sin(angle * signal_sum))
            means.append(mean)
        for z in (-0.9, -0.4, -0.1, 0, 0.3, 0.9):
            probabilities = [abs(x) ** 2 for x in pure_product(width, z, 0)]
            assert_close(sum(p * mean for p, mean in zip(probabilities, means)),
                         response(m, angle, z))

    for m in range(1, 5):
        width = m + 1
        angle = 0.25 / sqrt(m)
        for z, phase in product((-0.5, 0.0, 0.7), (0.1, 0.8, 2.3)):
            state = pure_product(width, z, phase)
            means = [
                z_mean(compressor(z_twirl_branch(state, mask), 0, range(1, width), angle),
                       (0,))
                for mask in range(1 << width)
            ]
            assert_close(sum(means) / len(means), response(m, angle, z))

    for z in (-0.7, 0, 0.6):
        angle = 0.3
        state = pure_product(6, z, 0.8)
        means = []
        for mask in range(1 << 6):
            branch = z_twirl_branch(state, mask)
            branch = compressor(branch, 0, (1, 2), angle)
            branch = compressor(branch, 3, (4, 5), angle)
            means.append(z_mean(cnot(branch, 0, 3), (3,)))
        assert_close(sum(means) / len(means), response(2, angle, z) ** 2)


def average_faulty_experiment(width, z, fault_probabilities, circuit, measured):
    mean = 0.0
    for faults in product((False, True), repeat=len(fault_probabilities)):
        fault_weight = prod(p if fault else 1 - p
                            for p, fault in zip(fault_probabilities, faults))
        for index, amplitude in enumerate(pure_product(width, z, 0)):
            state = circuit(basis_state(width, index), faults)
            mean += fault_weight * abs(amplitude) ** 2 * z_mean(state, measured)
    return mean


def check_native_target_faults():
    angle = 0.27
    fault_probability = 0.18
    attenuation = 1 - 2 * fault_probability

    def single_output(state, faults):
        return noisy_compressor(state, 0, (1, 2), angle, faults)

    def compressed_parity(state, faults):
        state = noisy_compressor(state, 0, (1,), angle, faults[:3])
        state = noisy_compressor(state, 2, (3,), angle, faults[3:6])
        return reversed_cnot(state, 0, 2, faults[6])

    for z in (-0.7, 0.0, 0.45):
        fault_probabilities = (fault_probability, fault_probability, 0.31, 0.09, 0.22, 0.17)
        single = average_faulty_experiment(3, z, fault_probabilities, single_output, (0,))
        assert_close(single, response(2, angle, attenuation * z))
        fault_probabilities = (fault_probability, 0.31, 0.09, fault_probability, 0.22, 0.17, 0.37)
        parity = average_faulty_experiment(4, z, fault_probabilities, compressed_parity, (2,))
        assert_close(parity, response(1, angle, attenuation * z) ** 2)


def detector_probability(report, echo, ideal_sign, offset, gain):
    return (1 + report * (offset + gain * echo * ideal_sign)) / 2


def echoed_mean(ideal_sign, offset, gain):
    return sum(
        echo * report * detector_probability(report, echo, ideal_sign, offset, gain) / 2
        for echo, report in product((-1, 1), repeat=2)
    )


def check_reports():
    for offset, gain in ((0.28, 0.54), (-0.12, 0.81), (0, 1)):
        for sign in (-1, 1):
            assert_close(echoed_mean(sign, offset, gain), gain * sign)
        for z in (-0.9, -0.25, 0, 0.35, 0.8):
            joint_moment = single_moment = 0.0
            for index, input_amplitude in enumerate(pure_product(2, z, 0)):
                output = cnot(basis_state(2, index), 0, 1)
                signs = [round(z_mean(output, (target,))) for target in range(2)]
                e0, e1 = (echoed_mean(sign, offset, gain) for sign in signs)
                probability = abs(input_amplitude) ** 2
                single_moment += probability * e0
                joint_moment += probability * e0 * e1
            assert_close(single_moment, gain * z)
            assert_close(joint_moment, gain ** 2 * z)


def normalized_walsh(diagonal):
    return [
        sum((-1) ** ((mask & index).bit_count()) * value
            for index, value in enumerate(diagonal)) / len(diagonal)
        for mask in range(len(diagonal))
    ]


def check_walsh():
    rng = Random(2026)
    gain_a, gain_b = 0.6, 0.75
    for width in range(1, 9):
        for z_a in (0.02, 0.11, 0.25):
            z_b = z_a * gain_a / gain_b
            diagonal = [-1, 1] * (1 << (width - 1))
            rng.shuffle(diagonal)
            coefficients = normalized_walsh(diagonal)
            assert_close(sum(value ** 2 for value in coefficients), 1)
            weights = [
                gain_a * z_a ** r - gain_b * z_b ** r
                for r in range(width + 1)
            ]
            assert_close(coefficients[0], 0)
            assert_close(weights[1], 0)
            exact_sum = sum(
                observation * (gain_a * abs(alpha) ** 2 - gain_b * abs(beta) ** 2)
                for observation, alpha, beta in zip(
                    diagonal, pure_product(width, z_a, 0), pure_product(width, z_b, 0)
                )
            )
            tail = sum(coefficients[mask] * weights[mask.bit_count()]
                       for mask in range(1, 1 << width) if mask.bit_count() >= 2)
            assert_close(exact_sum, tail)
            squared_tail_norm = sum(comb(width, r) * weights[r] ** 2
                                    for r in range(2, width + 1))
            assert abs(exact_sum) ** 2 <= squared_tail_norm + 3e-12
            q = width * max(z_a ** 2, z_b ** 2)
            assert squared_tail_norm <= 2 * exp(q) * q ** 2 + 3e-12


def invert_response(observed, forward, interval):
    lower, upper = -interval, interval
    for _ in range(50):
        midpoint = (lower + upper) / 2
        if forward(midpoint) < observed:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2


def check_finite_precision():
    gain_floor = 0.4
    seen_regimes = set()
    for width, z, gain, epsilon in product(
        (2, 3, 4, 16, 128, 1024),
        (-0.85, -0.09, 0, 0.016, 0.19, 0.8),
        (0.4, 0.73, 1),
        (0.025, 0.06),
    ):
        if width < 4:
            m, slope, interval = 1, 1, 1
            forward = float
            small_signal = True
        else:
            pilot_width = min(width // 2 - 1, int(epsilon ** -2))
            pilot_radius = 1 / (4 * sqrt(pilot_width))
            pilot_center = gain * z + (pilot_radius if z <= 0 else -pilot_radius)
            q = max(abs(pilot_center), pilot_width ** -0.5)
            m = max(1, int(q ** -2))
            angle = 0.12 / sqrt(m)
            interval = min(1, 2 / (gain_floor * sqrt(m)))
            slope = 0.09 * sqrt(m)

            def forward(value):
                return response(m, angle, value)

            small_signal = q <= 2 / sqrt(pilot_width)
            assert 2 * (m + 1) <= width
        seen_regimes.add(small_signal)
        assert abs(z) <= interval
        f = forward(z)
        # Worst-direction perturbations of the two population moments.
        # A small measured first moment returns zero to avoid unstable division.
        precision = (gain_floor * slope ** 2 * epsilon ** 2 / 20
                     if small_signal else 0.0005 * sqrt(m) * epsilon)
        threshold = gain_floor * slope * epsilon / 2
        for first_sign, second_sign in product((-1, 1), repeat=2):
            first = gain * f + first_sign * precision
            second = gain * f ** 2 + second_sign * precision
            estimate = (0 if abs(first) <= threshold
                        else invert_response(second / first, forward, interval))
            assert abs(estimate - z) <= epsilon, (width, z, gain, epsilon, estimate)
    assert seen_regimes == {False, True}


def main():
    checks = (
        (check_compressor, "Gate amplitudes, phase twirls, and compressed parity"),
        (check_native_target_faults, "Native target-bit faults and reversed-CNOT compilation"),
        (check_reports, "Offset echo and two-report CNOT moments"),
        (check_walsh, "Matched first moments and finite Walsh tails"),
        (check_finite_precision, "Finite-precision inversion in both pilot regimes"),
    )
    for check, label in checks:
        check()
        print(f"PASS  {label}")


if __name__ == "__main__":
    main()
