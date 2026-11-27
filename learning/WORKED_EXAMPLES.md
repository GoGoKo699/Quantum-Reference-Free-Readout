# Worked examples

These examples keep the detector, circuit and report counts explicit. Start with one-copy data and use the later examples alongside the [milestone map](MILESTONES.md).

## 1. One detector, two possible sources

Take a diagonal source $`\rho=(I+zZ)/2`$ and a fixed-offset detector with mean $`a+bz`$. The following two source–detector pairs are allowed when $`b_{\min}\le 0.4`$.

| Case | Source bias | Detector offset | Detector gain | Mean report |
| --- | --- | --- | --- | --- |
| A | $`z=0.20`$ | $`a=0.10`$ | $`b=0.60`$ | 0.22 |
| B | $`z=0.30`$ | $`a=0.10`$ | $`b=0.40`$ | 0.22 |

A one-copy rotation replaces $`z`$ by $`n_z z`$ for some known real $`n_z`$ with $`|n_z|\le 1`$. The two pairs have the same $`bz`$, so both still give $`a+n_z bz`$, and the binary report probabilities coincide. The argument also covers adaptive choices of the next rotation because each conditional report law coincides.

A uniform final choice between $`I`$ and $`X`$, followed by a matching sign change in the recorded value, removes the offset. Both cases then give the same mean $`\mu=bz=0.12`$. Now take two copies, apply CNOT, and read its target once with the same sign correction. Its ideal $`Z`$ expectation is $`z^2`$. The reported mean $`\nu=bz^2`$ is 0.024 in A and 0.036 in B. The population ratio $`\nu/\mu`$ recovers the correct $`z`$ in either case. At small $`z`$ the estimate uses a constrained moment fit to control finite-sample uncertainty. [Model and two-copy setup](../science/model.md)

## 2. Amplifying the bias with source copies

Use three signal copies and an additional copy as the rotation target. After dephasing in the measured basis, their input signs are $`x_1,x_2,x_3,x_0`$. Apply CNOTs from the target register to the signal registers so they store $`r_i=x_0x_i`$. Rotate the target by $`\pi/2-t(r_1+r_2+r_3)`$ about its $`Y`$ axis. On this input the target's mean $`Z`$ becomes

```math
x_0\cos\left(\frac{\pi}{2}-t\sum_{i=1}^3 r_i\right)
=\sin\left(t\sum_{i=1}^3 x_i\right).
```

Even though the target begins in another unknown copy, its input sign cancels. Averaging over the three independent signal copies gives $`f_3(z)=\operatorname{Im}[(\cos t+iz\sin t)^3]`$. Take $`t=\pi/6`$ in this example. Then

```math
f_3(z)=\frac{9z-z^3}{8},
\qquad
f_3'(0)=\frac98 .
```

When $`z=0.20`$ the ideal expectation rises to 0.224. Read one target with an offset echo to estimate $`bf_3(z)`$. Use two independent four-copy circuits, followed by a CNOT between their target registers, to estimate $`bf_3(z)^2`$ with one report. The first experiment spends four copies and the second spends eight. The general protocol chooses the angle and block width before the main measurements so that the response is invertible with slope of order $`\sqrt m`$ on the pilot interval. [Construction and width choice](../science/minimax.md)

## 3. The coefficients that survive matching

Return to cases A and B and set the common detector offset to zero. On two copies,

```math
4\rho^{\otimes2}=I\otimes I+z(Z\otimes I+I\otimes Z)+z^2 Z\otimes Z .
```

Every allowed block circuit pulls the local detector's ideal Pauli back to a traceless contraction $`M_U`$. The identity term contributes zero to the difference of mean reports, and the linear terms have common coefficient $`bz=0.12`$. The quadratic coefficient changes from 0.024 to 0.036. Choosing a CNOT and reading its target tests the corresponding $`Z\otimes Z`$ term directly.

If the two biases are scaled down together in proportion to a target error $`\epsilon`$, their two-copy mean gap is of order $`\epsilon^2`$. Their binary likelihoods stay in the interior of the probability interval, so the relative entropy per report is of order $`\epsilon^4`$. For general width $`k`$, the degree-two and higher terms are orthogonal in the normalized Hilbert–Schmidt inner product. When $`k\epsilon^2`$ is small, the sum of their squared coefficients gives a bound of order $`k^2\epsilon^4`$ on the relative entropy per block. Larger blocks and adaptive measurements are covered by the full converse. [Minimax lower bound](../science/minimax.md)

## 4. Two reports change the scaling

On the same pair of input copies, the ideal CNOT output signs are $`x_1`$ and $`x_1x_2`$. Their product is $`x_2`$, with mean $`z`$. Read both outputs, use an independent offset echo on each, and keep both report values. The mean of the first corrected report is $`A=bz`$. Conditional independence of the detector reports given the ideal signs makes the corrected report product have expectation $`B=b^2z`$. In the two examples above, $`A`$ is 0.12 in both cases, while $`B`$ is 0.072 in A and 0.048 in B.

For nonzero $`z`$, recover it with $`A^2/B`$. The allowed moments satisfy $`B=bA`$, so the ratio extends to zero with bounded sensitivity on this set when $`b\ge b_{\min}>0`$. Fitting empirical moments to the allowed set therefore requires precision of order $`\epsilon`$ in each moment to estimate $`z`$ to that precision. This comparison uses two physical detector calls within each two-copy block, even if you store only their product after the run. [Two-report comparison](../science/minimax.md)
