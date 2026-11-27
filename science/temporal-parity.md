# Source-only readout with temporal parity

Two calls to a detector with memory can return fair individual signs and still carry information in their product. In the [shared result](https://github.com/GoGoKo699/Quantum-Temporal-Readout/blob/8e7b5b56458eef3ec19a5b7d3f31390ea8667dbe/science/source-only-parity.md), the two moment circuits of this repository use the same temporal parity as their readout. The detector can have arbitrary causal classical or quantum memory. The protocol uses only copies of the source and trusted controls.

## The two physical calls

Prepare $`k`$ fresh copies with $`2\le k\le K`$ and apply a trusted joint unitary before either call. Send two designated outputs $`H,T`$ to the same detector at fixed times. The second output can require coherent storage until its scheduled call. The protocol schedules both inputs before seeing either report. Apply private local Pauli masks and correct the two reports using the private bit flips. The fresh copies and detector memory are independent conditional on the earlier data, and the timing and external signals match between arms. Each block charges all $`k`$ copies and both detector calls.

At width two, use either the identity or a CNOT from $`H`$ to $`T`$. With the identity, the ideal parity $`Z_H Z_T`$ has expectation $`z^2`$. With CNOT, that parity pulls back to $`Z_T`$ and has expectation $`z`$. With larger blocks, dephase the copies in the target basis and compress two disjoint groups into $`H`$ and $`T`$. The two choices then give $`f_m(z)^2`$ and $`f_m(z)`$, using the [same compressor](minimax.md#construct-two-moments-with-one-report-per-block).

Use a private fair coin to interleave the two choices. The masked block measurement gives both arms the same conditional parity contrast $`\kappa_t`$. The average predictable means in a phase are $`(\bar\kappa f_m(z),\bar\kappa f_m(z)^2)`$. The precision guarantee assumes a known floor $`|\bar\kappa|\ge\kappa_*`$ for the average predictable contrast in each acquisition phase. The contrasts can vary between blocks and the phase averages may differ in sign or magnitude.

## Compare the two-report models

| Two scheduled outputs at width two | Informative population means | Worst-case copy cost at fixed confidence |
| --- | --- | --- |
| CNOT followed by two conditionally independent calls | $`bz`$ and $`b^2z`$ from separate functions of the same pair of reports | $`\Theta(\epsilon^{-2})`$ |
| Identity or CNOT followed by two causal, potentially correlated calls | $`\bar\kappa z^2`$ and $`\bar\kappa z`$ from interleaved blocks | $`\Theta(\epsilon^{-4})`$ |

The independent-report row uses the [stationary detector comparator](minimax.md#a-second-physical-report-changes-the-rate). In the hard instance for correlated readout, the first report is fair and independent of the pair's parity, which carries the information about $`z`$. Under separate single-copy rotations on the two slots, that parity has the same distribution at opposite polarizations along the measured axis. The pre-block CNOT makes one arm sensitive to the sign. Its action on diagonal source states suffices for the example.

For arbitrary $`K\ge2`$, the correlated model has the copy law $`\Theta_{\kappa_*}(\max\{\epsilon^{-2},\epsilon^{-4}/K\})`$ at fixed confidence. The full converse covers protocols that keep both raw reports and their private controls. [Causal model, estimator and proof](https://github.com/GoGoKo699/Quantum-Temporal-Readout/blob/8e7b5b56458eef3ec19a5b7d3f31390ea8667dbe/science/source-only-parity.md)
