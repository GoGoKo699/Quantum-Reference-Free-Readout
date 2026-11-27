# Quantum Reference-Free Readout

**Can copies of an unknown qubit provide their own reference for an uncalibrated detector?** Yes. A circuit that combines several copies into one measured qubit recovers a Pauli expectation even when the detector's gain and offset are unknown. The circuit uses only source copies and trusted gates.

With one physical binary report per block of at most $`K`$ copies, the minimax number of copies for absolute error $`\epsilon`$ and fixed confidence is

```math
N_*(K,\epsilon)=\Theta\!\left(\max\left\{\epsilon^{-2},\frac{\epsilon^{-4}}{K}\right\}\right),\qquad K\ge 2.
```

The constants depend on a fixed positive lower bound on detector gain. The scaling is uniform over the input qubit and the allowed detector parameters, including arbitrarily weak source polarization.

| Measurement access | Worst-case copy cost |
| --- | --- |
| One report on one copy | The expectation is unidentifiable |
| One report after a block of up to $`K\ge 2`$ copies | $`\Theta(\max\{\epsilon^{-2},\epsilon^{-4}/K\})`$ |
| Two independent reports after a two-copy CNOT | $`\Theta(\epsilon^{-2})`$ |

## Estimate one Pauli expectation

1. Choose the Pauli axis, rotate fresh copies of the same unknown qubit into the corresponding Z basis and independently apply a private fair I-or-Z choice to each copy. Use a stationary memoryless detector with a known positive lower bound on its gain. At a block cap of two or three copies, acquire one set of direct single-copy readings and a second set that applies a CNOT to two copies and reads only its target.
2. At a larger cap, use [direct pilot readings](science/minimax.md#uniform-inversion-and-adaptive-width) to choose a compressor width. Use one source copy as the target and ## Estimate one Pauli expectation

1. Choose the Pauli axis, rotate fresh copies of the same unknown qubit into the corresponding Z basis and independently apply a private fair I-or-Z choice to each copy. Use a stationary memoryless detector with a known positive lower bound on its gain. At a block cap of two or three copies, acquire one set of direct single-copy readings and a second set that applies a CNOT to two copies and reads only its target.
2. At a larger cap, use [direct pilot readings](science/minimax.md#uniform-inversion-and-adaptive-width) to choose a compressor width. m`$ copies as signal qubits. Apply CNOTs from the target to each signal. Rotate the target about Y through ## Estimate one Pauli expectation

1. Choose the Pauli axis, rotate fresh copies of the same unknown qubit into the corresponding Z basis and independently apply a private fair I-or-Z choice to each copy. Use a stationary memoryless detector with a known positive lower bound on its gain. At a block cap of two or three copies, acquire one set of direct single-copy readings and a second set that applies a CNOT to two copies and reads only its target.
2. At a larger cap, use [direct pilot readings](science/minimax.md#uniform-inversion-and-adaptive-width) to choose a compressor width. \pi/2-mt`$, then apply a ## Estimate one Pauli expectation

1. Choose the Pauli axis, rotate fresh copies of the same unknown qubit into the corresponding Z basis and independently apply a private fair I-or-Z choice to each copy. Use a stationary memoryless detector with a known positive lower bound on its gain. At a block cap of two or three copies, acquire one set of direct single-copy readings and a second set that applies a CNOT to two copies and reads only its target.
2. At a larger cap, use [direct pilot readings](science/minimax.md#uniform-inversion-and-adaptive-width) to choose a compressor width. 2t`$ Y rotation to the target controlled on the one state of each signal qubit in turn. The [circuit recipe](science/minimax.md#construct-two-moments-with-one-report-per-block) sets ## Estimate one Pauli expectation

1. Choose the Pauli axis, rotate fresh copies of the same unknown qubit into the corresponding Z basis and independently apply a private fair I-or-Z choice to each copy. Use a stationary memoryless detector with a known positive lower bound on its gain. At a block cap of two or three copies, acquire one set of direct single-copy readings and a second set that applies a CNOT to two copies and reads only its target.
2. At a larger cap, use [direct pilot readings](science/minimax.md#uniform-inversion-and-adaptive-width) to choose a compressor width. t=c/\sqrt m`$ with a small constant fixed by the gain floor. In one set of blocks read a single compressor target. In a separate set run two compressors on disjoint groups, apply a CNOT between their targets and read only the CNOT target.
3. Immediately before every detector call, including in the pilot, use a fresh fair sign to choose whether to apply X. Multiply the reported sign by the same sign. Average the corrected reports separately for the two data sets and [fit the two means](science/minimax.md#uniform-inversion-and-adaptive-width) over the admissible gain and expectation range by minimizing the sum of absolute residuals. Use the fitted expectation. The fit is defined even when both empirical means are near zero.

Discard the other outputs and keep only classical records between blocks. Charge every fresh copy, including each compressor target and the pilot copies, and one physical report per block. The compressor takes gates linear in its number of input copies. The [worked example](learning/WORKED_EXAMPLES.md#2-amplifying-the-bias-with-source-copies) follows the target rotation and moment response.

Repeating in three trusted bases extends the result to single-qubit tomography.

The copy law also holds under a specific noisy CNOT model with independent, stationary bit flips on the physical target. The construction redirects the faults in its controlled rotations and parity gate and fits the remaining attenuation using the same source copies. For ideal nearest-neighbor circuits, a light-cone bound gives a matching depth–copy tradeoff on fixed-dimensional lattices.

## Sister project

[Quantum Temporal Readout](https://github.com/GoGoKo699/Quantum-Temporal-Readout) studies detectors with memory. In the shared [source-only temporal parity result](science/temporal-parity.md), two scheduled calls can each be individually blind and still carry information in their joint parity. Trusted joint preprocessing recovers the same copy scaling under a lower bound on the phase-average parity contrast. The two independent calls in the comparison above yield a different width-two rate.

## Read the science

- [Model and measurement access](science/model.md) defines the detector, source, controls and charged resources.
- [Circuit and minimax proof](science/minimax.md) gives the estimator, the adaptive lower bound and the two-report comparison.
- [Control accuracy and circuit resources](science/robustness.md) tracks the accuracy needed for the construction and the cost of implementing it.
- [Related work](science/related-work.md) credits the two-copy readout ratio to Lin, Wallman, Hincks and Laflamme and relates the block circuit to polarization compression. See the [bibliography](references/references.bib) for citation details.

## Learn and verify

The educational anchor is John Watrous's *The Theory of Quantum Information* (2018). The [Watrous bridge](learning/WATROUS_BRIDGE.md) connects the textbook to the detector model and proof. The [learning route](learning/README.md) leads through 30 milestones and worked examples. The [reading guide](llms.txt) maps questions to their scientific sources.

Run the finite checks from the repository root.

```bash
python3 verification/check_readout.py
```

The [verification guide](verification/README.md) explains the checked identities, numerical tolerances and the role of the written proof.

## Scope

The main one-report model uses a memoryless, stationary detector. A report comes from one application of the detector to one output qubit. Classical outcomes may guide later blocks. All source copies, including those used as temporary circuit targets, count toward the budget. The guarantee concerns the state expectation. Detector gain is unidentifiable at the maximally mixed state. The two-report comparison requires conditionally independent readout noise. The [control bounds](science/robustness.md) state the distinct assumptions for circuit depth, small generic errors, and stationary target faults.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
