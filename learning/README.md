# Learning route

An unknown qubit arrives repeatedly, and the only detector reports one noisy sign. A trusted change of basis lets you choose which Pauli expectation to estimate, but the detector's unknown gain and the source polarization are inseparable in a single-copy run. This project uses independent copies to create another dependence on the same polarization. The two signals are enough to estimate the state, and the number of copies you can control together sets the precision cost.

1. Start with the [two candidate states](WORKED_EXAMPLES.md#1-one-detector-two-possible-sources). They give the same single-copy data, even with unlimited repetitions.
2. Use the [Watrous bridge](WATROUS_BRIDGE.md) for the quantum and statistical notation. Its reading pointers link to the relevant sections of one source.
3. Follow the [30 milestones](MILESTONES.md) from the detector model through the circuit construction, matching lower bound, and two-report comparison. Return to the [worked examples](WORKED_EXAMPLES.md) where the map links them.

The [scientific account](../science/README.md) gives the precise model, the minimax proof and the control-error analysis. The [verification guide](../verification/README.md) describes the checks for the circuit identities and finite examples.
