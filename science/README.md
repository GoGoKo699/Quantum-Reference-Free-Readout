# Reference-free qubit readout

A destructive detector returns a binary report with unknown offset and gain. A single unknown copy gives access only to the gain times the polarization. Joint control of several copies can produce a second response with the same gain and a different dependence on the state. The statistical question is how many copies this costs when only one physical report is allowed per block.

| Result | Scientific route |
| --- | --- |
| Single-copy ambiguity and the two report models | [Experiment and claims](model.md) |
| Joint block circuit, matching copy bounds, and the two-report construction | [Minimax copy law](minimax.md) |
| Gate depth, deterministic error tolerance, and report count | [Control and resource bounds](robustness.md) |
| Source-only estimation with a causal detector and two scheduled reports | [Temporal parity](temporal-parity.md) |
| State-preparation and measurement characterization, readout compression, and polarization compression | [Related work](related-work.md) |

The core result estimates an unknown Pauli expectation uniformly, including at the maximally mixed state. The ideal-control upper bound uses only copies of the unknown state and classical random bits. The converse allows arbitrary joint unitaries and classical feedback between blocks. The noisy-control result is an error budget for this particular implementation.
