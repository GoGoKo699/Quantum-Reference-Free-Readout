# Reproduce the finite checks

Run from the repository root with Python 3.10 or newer. The script uses the standard library.

```bash
python3 verification/check_readout.py
```

| Check | What it verifies |
|---|---|
| Compressor | Applies the CNOTs and controlled rotations to small state vectors. Checks the signal on every basis input, averages phase-twirl branches for inputs with transverse coherence, and checks parity of two independently compressed outputs. |
| Native CNOT faults | Enumerates independent target-bit faults after native CNOTs. Checks that the fanout reduces the effective input polarization by the predicted factor while the reversed CNOTs used in the controlled rotations and parity leave the moments unchanged. |
| Detector reports | Enumerates the private output flips and binary detector outcomes. Checks offset cancellation and both moments of the two-report CNOT experiment. |
| Walsh tail | Uses paired state and gain values with identical gain-weighted polarization. Checks exact cancellation of the degree-one coefficient, the remaining polynomial contribution, and its finite norm bound. |
| Inversion | Exercises both pilot regimes, three gains, both polarization signs, and the maximally mixed case. Adds signed perturbations directly to the population moments and checks the resulting polarization error. |

The checks cover finite instances in floating point. The [scientific account](../science/README.md) gives the guarantees for arbitrary admissible block widths, adaptive measurements, and statistical sampling.
