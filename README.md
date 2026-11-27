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

A random output flip cancels the detector offset. A block circuit increases the slope of the response to weak polarization. Reading one compressed output or the parity of two independent outputs gives two means with a common unknown gain. Fitting these moments identifies the Pauli expectation. Repeating in three trusted bases extends the result to single-qubit tomography.

The copy law also holds under a specific noisy CNOT model with independent, stationary bit flips on the physical target. The construction redirects the faults in its controlled rotations and parity gate and fits the remaining attenuation using the same source copies. For ideal nearest-neighbor circuits, a light-cone bound gives a matching depth–copy tradeoff on fixed-dimensional lattices.

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

The detector is memoryless and stationary. A report comes from one application of the detector to one output qubit. Classical outcomes may guide later blocks. All source copies, including those used as temporary circuit targets, count toward the budget. The guarantee concerns the state expectation. Detector gain is unidentifiable at the maximally mixed state. The two-report comparison requires conditionally independent readout noise. The [control bounds](science/robustness.md) state the distinct assumptions for circuit depth, small generic errors, and stationary target faults.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
