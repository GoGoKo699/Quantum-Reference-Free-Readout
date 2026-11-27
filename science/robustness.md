# Control and resource bounds

## Tolerance to imperfect control

For fixed detector parameters, compare the actual and intended scored report means conditional on the classical history. Let the pilot bias bound be $`\eta_{\mathrm p}`$. Let $`\eta_m`$ bound the absolute bias of either compressed moment, including the parity circuit and the final echo. The estimator is unchanged. It retains the ideal copy order if the biases satisfy

```math
\begin{aligned}
\eta_{\mathrm p}&\le c_0/\sqrt L,\\
\eta_m&\le c_0m\epsilon^2
   &&(q\le 2/\sqrt L),\\
\eta_m&\le c_0\sqrt m\,\epsilon
   &&(q>2/\sqrt L),
\end{aligned}
```

for a sufficiently small constant $`c_0`$ depending on the contrast floor. At $`K=2,3`$ there is no pilot and both moment biases can be of order $`\epsilon^2`$. The bounds are required on the histories where the respective circuits are selected.

To see this, allot part of the [pilot and moment precision](minimax.md#uniform-inversion-and-adaptive-width) to these biases. For independent responses, Hoeffding's inequality controls the remaining statistical error. More generally, bounded differences about the conditional means give the same concentration order even if those means vary within the bias budget. The residual bound then applies on the same compact fitting domain. This result uses a fixed ideal detector response and a uniform conditional comparison to it.

A composable gate model gives a concrete sufficient condition. Let each implemented gate channel differ from its ideal channel by at most $`\gamma_g`$ in diamond norm on the registers it acts on. Compose the channels in the prescribed order. Replacing them one at a time and using contractivity of the remaining operations bounds the difference in any scored report mean by

```math
\eta\le \sum_g \gamma_g.
```

The scored report takes values in $`[-1,1]`$, which supplies the dual operator norm in this bound. The same estimate includes random choices of trusted basis, dephasing, and echo gates by conditioning on and then averaging over those choices. The gate model applies to ordinary composed channel errors. A device with correlated control memory requires a bound on its whole conditional circuit or an explicit channel comparison that includes its memory.

The direct pilot uses a constant number of elementary gates per copy. Each compressed moment uses at most $`Cm`$ gates for a fixed constant $`C`$. Consequently a per-gate diamond-norm error at most $`c_1\epsilon^2`$, for sufficiently small $`c_1`$ depending on $`b_{\min}`$, is a sufficient uniform specification. In the second branch, $`m\epsilon^2\le\sqrt m\,\epsilon`$ because $`m\le\epsilon^{-2}`$. The branch-specific bounds also permit a larger gate error when fewer gates are used. For example, the separated branch permits a uniform bound of order $`\epsilon/\sqrt m`$ on its moment gates. The optimal gate-error budget and hardware operating regime remain open.

## Exact tolerance to stationary target bit flips

An independent target-only bit-flip model allows constant-size CNOT noise. Use the star circuit from the proof, with ideal one-qubit gates and the same detector. Each native CNOT is followed by an independent $`X`$ fault on its physical target with fixed unknown probability $`p`$. Assume a known floor $`1-2p=\lambda\ge\lambda_{\min}>0`$. The construction can use both native CNOT directions. Errors on the two blocks used for a parity moment are independent.

Keep the initial fanout CNOTs in their native direction. On a computational-basis input the noisy sign on signal $`i`$ is $`x_0x_i e_i`$, where $`e_i`$ is the fault sign with mean $`\lambda`$. The resulting target mean is $`\sin(t\sum_i x_i e_i)`$, and its mean over inputs and faults is $`f_m(\lambda z)`$.

For the subsequent controlled rotations and the parity CNOT, implement an effective CNOT by surrounding a native CNOT in the reversed direction with Hadamards on both wires. The fault on the physical target then becomes a $`Z`$ on the effective control after the effective gate. A controlled $`R_y`$ uses two such effective CNOTs and exact one-qubit rotations on the rotation target. The transformed fault commutes through all remaining uses of the signal wire as a control and does not change the target statistics. Likewise the parity CNOT's transformed fault acts on the unmeasured control and leaves the measured parity unchanged. The effective parity also protects the width-two circuit.

For $`K\ge4`$, the ideal pilot still selects $`m`$. Estimate the direct mean $`u=bz`$ to order $`\epsilon`$ using $`O(\epsilon^{-2}\log(1/\delta))`$ further copies. Fit all three means over the original polarization and gain domain together with $`\lambda\in[\lambda_{\min},1]`$:

```math
u=bz,\qquad \mu=b f_m(\lambda z),\qquad \nu=b f_m(\lambda z)^2 .
```

Let tildes denote a second fit and label the larger-magnitude polarization $`z`$, with $`M=|z|>0`$. The slope bound gives $`\nu\gtrsim_{b_{\min},\lambda_{\min}}mM^2`$. The identity $`\mu^2=b\nu`$ gives

```math
\nu(b-\widetilde b)=(\mu^2-\widetilde\mu^2)-\widetilde b(\nu-\widetilde\nu).
```

Bounding $`|\widetilde u|\le M`$ and writing $`z=u/b`$ shows that

```math
|z-\widetilde z|
\lesssim_{b_{\min},\lambda_{\min}}
|u-\widetilde u|+
\frac{|\mu-\widetilde\mu|+|\nu-\widetilde\nu|}{mM}.
```

For any fit more than $`\epsilon`$ from the true value, $`M>\epsilon/2`$. In the separated pilot branch we also have $`M\gtrsim m^{-1/2}`$. Use the same compressed-moment precisions as in the ideal proof and minimize their absolute residuals together with the direct residual, each scaled by its own precision. These estimates again separate all such fits with the stated confidence. The additional direct copies preserve the ideal minimax copy order. The protected parity and direct readout give the original width-two and width-three law. The ideal case $`p=0`$ belongs to the permitted noise model, so the lower bound holds when the rate is required uniformly over $`p`$.

The exact treatment exploits stationarity, the target-only Pauli fault, and the explicit star circuit. The generic bias budget above covers other circuits with a certified conditional error bound. The depth refinements below assume ideal gates.

## Circuit depth and connectivity

Count two-qubit depth as the number of layers of disjoint two-qubit gates. Trusted single-qubit gates may be applied before, between and after those layers.

The basic compressor [described in the proof](minimax.md#construct-two-moments-with-one-report-per-block) uses a star of $`m`$ CNOTs followed by rotations controlled by the signal output signs. Both stars can be implemented using linear reversible operations on the signal copies and a single signal-to-target edge. Define the fanout unitary $`W`$ to add the target bit into every signal bit over $`\mathbb F_2`$. Pick a signal root and a reversible CNOT network $`V`$ on the signals whose binary action maps the root basis vector to the all-ones vector. Apply $`V^{-1}`$, a CNOT from the target into that root, and then $`V`$. The signals change by precisely the target bit times the all-ones vector, for arbitrary input bits. This identity holds as a unitary on superpositions as well. The same fanout transforms each signal $`Z_i`$ to $`Z_i Z_0`$ by conjugation, where site $`0`$ is the target. Thus the diagonal Ising star $`\prod_i \exp(i tZ_iZ_0/2)`$ follows from single-qubit rotations conjugated by $`W`$. A single-qubit change of target basis converts this star to the $`Y`$-axis controlled rotations. No clean register is needed for either step.

On all-to-all hardware, a binary broadcast tree gives $`O(m)`$ CNOT gates and $`O(\log(m+1))`$ depth for $`V`$. On a compact $`D`$-dimensional nearest-neighbor cubic lattice, a bounded-degree breadth-first spanning tree yields $`O(m)`$ CNOT gates and $`O_D(m^{1/D})`$ depth. The latter construction can use a cube with a target at one corner and the adjacent signal root. For the parity moment, run the compressors on adjacent disjoint blocks, with adjacent target sites for the final CNOT. Restricting the signal sizes to such cubes rounds the selected width down by at most a constant factor depending on $`D`$, using direct and two-copy circuits at the smallest widths.

Conversely, before the report, a depth-$`d`$ circuit can bring only a limited number of copies into the measured site's backward light cone. On all-to-all hardware each layer can at most double its size, and on a $`D`$-dimensional lattice the support stays within graph distance $`d`$ of the site. The pulled-back report observable is traceless on that support. Apply the [adaptive relative-entropy lower bound](minimax.md#adaptive-lower-bound) to this support, while charging every consumed copy. This gives, respectively,

```math
\begin{aligned}
N_{\mathrm{all}}(K,d,\epsilon)
&\gtrsim_{b_{\min}}
  \max\left\{\epsilon^{-2},\
       \frac{\epsilon^{-4}}{\min(K,2^d)}\right\},\\
N_{\mathrm{lattice}}(K,d,\epsilon)
&\gtrsim_{b_{\min},D}
  \max\left\{\epsilon^{-2},\
       \frac{\epsilon^{-4}}{\min(K,(d+1)^D)}\right\}.
\end{aligned}
```

These are fixed-confidence bounds. For lattice depth $`d\ge1`$, the construction attains the second order by selecting the algorithm's cap proportional to $`\min(K,(d+1)^D)`$, using a single CNOT and direct readout when that cap is bounded. At $`d=0`$, every report has a single-copy light cone, resulting in the [one-copy ambiguity](model.md#copy-complexity). When $`K\gtrsim\epsilon^{-2}`$, the depth needed for the parametric copy order is $`\Theta(\log(1/\epsilon))`$ with all-to-all gates and $`\Theta_D(\epsilon^{-2/D})`$ on the lattice. The intermediate all-to-all depth tradeoff remains open.

## Physical detector calls

The current pilot uses $`O(L\log(1/\delta))`$ calls. In its weak-polarization branch the two compressed moments use $`O((L\epsilon^2)^{-2}\log(1/\delta))`$ calls. The separated branch uses $`O((m\epsilon^2)^{-1}\log(1/\delta))`$, with $`m`$ selected by the pilot. Thus one bound uniform in the unknown state is

```math
R\lesssim_{b_{\min}}
  \left(\epsilon^{-2}+\frac{1}{L^2\epsilon^4}\right)
  \log(1/\delta),
\qquad
L\asymp \min(K,\epsilon^{-2}),
```

where the width-two and width-three direct circuits also satisfy the bound with $`L=1`$.

There are two report-count lower bounds at fixed confidence. For the matched-gain pair the relative entropy of a report is at most order $`\min(1,K^2\epsilon^4)`$. Testing requires $`R\gtrsim_{b_{\min}}\max(1,K^{-2}\epsilon^{-4})`$. Independently, pack order $`\epsilon^{-1}`$ distinct polarizations with a fixed detector. Conditional on the protocol's private coins, a transcript of at most $`R`$ binary reports contains at most $`R`$ bits about the chosen polarization, since gate choices and stopping are determined by those coins and the previous binary reports. The required estimation accuracy gives an identification test for the packing, and Fano's inequality yields $`R\gtrsim \log(1/\epsilon)`$. In particular the protocol matches the copy and report orders when $`2\le K\lesssim\epsilon^{-1}`$ at fixed confidence. The optimal report count at larger widths and the resulting time tradeoffs remain open.
