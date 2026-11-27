# The minimax copy law

The statistical difficulty occurs near zero polarization. Any one-copy experiment has response linear in the state and detector gain. Once those linear responses are matched for two distinct states, an arbitrary joint block can distinguish them only through its terms of degree at least two. The circuit below amplifies those terms.

## Cancel the detector offset

For each report, independently draw a uniform sign $`S\in\{-1,1\}`$. Apply $`X`$ to the measured qubit when $`S=-1`$ and record $`W=SY`$. If its intended ideal polarization is $`g`$, then $`\mathbb E[Y\mid S]=a+bSg`$ and $`\mathbb E W=bg`$. The flip and its sign correction add no detector calls.

When only the $`Z`$ expectation is sought, independently dephase every input with a fair $`I/Z`$ choice. After averaging these internal coins, the inputs are a diagonal product with independent ideal signs of mean $`z`$. This construction uses the supplied copies throughout.

## Construct two moments with one report per block

Use $`m`$ signal copies and one extra target copy. For a computational-basis input write their signs as $`x_1,\ldots,x_m`$ and $`x_0`$. Apply CNOTs controlled by the target copy to the $`m`$ signal copies. The signal outputs then store $`r_i=x_0x_i`$. Apply a $`Y`$ rotation to the target with angle $`\pi/2-t\sum_i r_i`$. One fixed rotation by $`\pi/2-mt`$ and $`m`$ rotations by $`2t`$ controlled on $`r_i=-1`$ implement the angle. Its ideal final $`Z`$ mean on the given basis input is

```math
x_0\cos\!\left(\frac{\pi}{2}-t\sum_i r_i\right)
=\sin\!\left(t\sum_i x_i\right).
```

The target sign cancels on every basis input. After averaging over the source, the output expectation is

```math
f_m(z)=\mathrm{Im}\bigl[(\cos t+i z\sin t)^m\bigr].
```

Call the detector on that target with the offset cancellation to obtain mean $`\mu=b f_m(z)`$. In a separate set of experiments, run two independent compressors on $`2m+2`$ copies, apply a CNOT between the targets, and read only its target. The measured $`Z`$ pulls back to the product of the two compressor target observables. Its mean after offset cancellation is $`\nu=b f_m(z)^2`$. Each circuit uses $`O(m)`$ elementary gates and one report. At $`K=2`$ or $`3`$, use direct readout and one CNOT parity readout, with response $`f(z)=z`$.

Choose $`t=c/\sqrt m`$ for a fixed sufficiently small $`c>0`$. On $`|z|\sqrt m\le A`$ for any fixed $`A\ge1`$, the response is odd, and

```math
f_m'(z)=m\sin(t)\mathrm{Re}\bigl[(\cos t+i z\sin t)^{m-1}\bigr]
\asymp_A\sqrt m.
```

Indeed, the modulus of the power is at least $`\cos^{m-1}(t)`$, bounded below away from zero, and at most one on $`|z|\le1`$. Its phase has magnitude at most $`(m-1)|z|\tan(t)\le 2Ac`$. Choose $`c`$ so this is at most $`\pi/3`$. The slope bound also yields $`|f_m(z)|\asymp_A\sqrt m\,|z|`$ on this interval.

## Uniform inversion and adaptive width

For $`K\ge4`$, choose

```math
L=\min\{\lfloor K/2\rfloor-1,\ \lfloor\epsilon^{-2}\rfloor\}.
```

Estimate $`u=bz`$ to accuracy $`1/(4\sqrt L)`$ with $`O(L\log(1/\delta))`$ direct single-copy reports. From their mean $`\widehat u`$, form

```math
q=\max\{|\widehat u|, L^{-1/2}\},\qquad m=\lfloor q^{-2}\rfloor.
```

The pilot average lies in $`[-1,1]`$, so $`1\le m\le L`$ and $`m\ge q^{-2}/2`$. On its success event, $`|z|\sqrt m\le 5/(4b_{\min})`$. Choose $`A=2/b_{\min}`$. Fit the two subsequent empirical means to $`(b f_m(z),b f_m(z)^2)`$ by minimizing their absolute residual sum over $`|z|\le\min(1,A/\sqrt m)`$ and $`b\in[b_{\min},1]`$. The compact fitting domain includes the true pair on the pilot event.

The fit is uniform even near $`z=0`$. Let $`r=f_m(z)`$ and $`\widetilde r=f_m(\widetilde z)`$ be two allowed responses, with mean pairs $`(\mu,\nu)`$ and $`(\widetilde\mu,\widetilde\nu)`$. Use

```math
\nu-\widetilde\nu
=\widetilde r(\mu-\widetilde\mu)+\mu(r-\widetilde r)
```

and the same identity with the two roles swapped. Since both responses lie in $`[-1,1]`$, the slope bound implies

```math
|\mu-\widetilde\mu|+|\nu-\widetilde\nu|
\ge b_{\min}\max(|r|,|\widetilde r|)|r-\widetilde r|
\ \gtrsim_{b_{\min}}\
m\max(|z|,|\widetilde z|)|z-\widetilde z|.
```

If $`|\widetilde z-z|>\epsilon`$, the right side is at least a constant times $`m\epsilon^2`$. A more polarized source gives the stronger separation $`m|z|\epsilon`$.

- If $`q\le 2/\sqrt L`$, then $`m\ge L/8`$. Estimate each mean to a sufficiently small constant times $`m\epsilon^2`$. Hoeffding's inequality gives $`O((m\epsilon^2)^{-2}\log(1/\delta))`$ reports per moment, or $`O((L\epsilon^4)^{-1}\log(1/\delta))`$ copies.
- If $`q>2/\sqrt L`$, then $`|\widehat u|=q`$ and $`|z|\ge|u|\ge7q/8`$ on the pilot event. Thus $`\sqrt m\,|z|`$ has a positive constant lower bound. Estimate each mean to a sufficiently small constant times $`\sqrt m\,\epsilon`$. This costs $`O((m\epsilon^2)^{-1}\log(1/\delta))`$ reports per moment, or $`O(\epsilon^{-2}\log(1/\delta))`$ copies.

Choose the moment precision with room for the fitting residual, which is at most the residual at the true pair. The three sampling events can each be allotted failure probability $`\delta/3`$. The budget bounds follow from the enforced width choice, even on histories where the pilot errs. At $`K=2,3`$, the same separation inequality with $`r=z`$ uses precision of order $`\epsilon^2`$ and gives $`O(\epsilon^{-4}\log(1/\delta))`$ copies without a pilot. Accounting for the pilot and the extra target copies yields the upper bound in [the model](model.md#copy-complexity).

## Adaptive lower bound

Let $`b_0,b_1`$ be two distinct gains strictly between $`b_{\min}`$ and $`1`$, with both offsets zero. Choose positive $`z_0,z_1=\Theta_{b_{\min}}(\epsilon)`$ satisfying

```math
b_0 z_0=b_1 z_1,\qquad |z_0-z_1|>2\epsilon.
```

Such a choice exists for all sufficiently small $`\epsilon`$. The hard source states are $`\rho_j=(I+z_jZ)/2`$.

Condition on the same transcript and random choices under both hypotheses. A $`k`$-copy block measures one pulled-back observable $`O=U^\dagger Z_\ell U`$ of normalized trace zero and operator norm one. For $`S\subseteq\{1,\ldots,k\}`$, let $`Z_S`$ be the tensor Pauli string with $`Z`$ on $`S`$. The normalized Hilbert–Schmidt expansion gives

```math
2^k\rho_j^{\otimes k}=\sum_{S\subseteq [k]} z_j^{|S|} Z_S .
```

The constant term contributes zero. The first-degree term is common after multiplication by $`b_j`$. Orthogonality of the remaining strings and Cauchy–Schwarz bound the squared difference of report means by

```math
\sum_{r=2}^{k}\binom{k}{r}(b_0 z_0^r-b_1 z_1^r)^2
\ \lesssim_{b_{\min}}\
k^2\epsilon^4
\qquad(k\epsilon^2\le1).
```

For the last estimate, use $`|z_j|\le C_{b_{\min}}\epsilon`$ and $`\sum_{r\ge2}\binom{k}{r}v^r\le \tfrac12(kv)^2e^{kv}`$ for $`v\ge0`$. Because the two gains are bounded away from one, every report probability remains bounded away from zero and one. The conditional Bernoulli relative entropy is at most a constant times the squared difference of means. When $`k\epsilon^2>1`$, the probability bounds instead give a constant relative entropy bound. The combined per-block bound is

```math
D_{\mathrm{block}}
\lesssim_{b_{\min}}
\min\{k\epsilon^2,\ k^2\epsilon^4\}.
```

The relative entropy chain rule applies to transcripts of adaptive actions. Conditioned on the previous transcript, the classical algorithm chooses actions from the same distribution under both hypotheses. Pad terminated runs with deterministic symbols if a protocol may stop early. For a total pathwise budget $`N`$ and block bound $`K`$, the accumulated relative entropy is

```math
D(P_0\Vert P_1)
\lesssim_{b_{\min}} N\min\{\epsilon^2,K\epsilon^4\}.
```

The two success intervals for the estimate are disjoint. A uniform estimator would therefore give a binary test with each error probability at most $`\delta`$. Pinsker's inequality gives a constant required relative entropy at fixed error below $`1/2`$. For $`\delta\le1/8`$, the testing inequality $`2\delta\ge \tfrac12 e^{-D(P_0\Vert P_1)}`$ gives a required relative entropy of order $`\log(1/\delta)`$. Together these prove the lower bound. For $`k=1`$ the higher-degree tail vanishes, so the hard pair can give exactly the same transcript law for any number of one-copy experiments.

## A second physical report changes the rate

Apply CNOT to two source copies. Let $`x_1,x_2`$ be the input ideal $`Z`$ signs. The ideal output signs are $`x_1,x_1x_2`$, so the first output and the product of the outputs both have expectation $`z`$. Apply independent output flips for offset cancellation and read both outputs. With conditionally independent detector reports, the corrected signs $`W_1,W_2`$ obey

```math
A=\mathbb E[W_1]=bz,\qquad B=\mathbb E[W_1W_2]=b^2z.
```

Estimate both means to accuracy of order $`\epsilon`$ and fit $`(A,B)`$ to the allowed compact domain. To see its uniform stability for the state, two candidate pairs satisfy $`B-\widetilde B=b(A-\widetilde A)+(b-\widetilde b)\widetilde A`$. Since $`z=A/b`$, this gives

```math
|z-\widetilde z|
\le \frac{|A-\widetilde A|}{b_{\min}}
 +\frac{|B-\widetilde B|+|A-\widetilde A|}{b_{\min}^2}.
```

There is no division by an estimated small moment. Hoeffding's inequality yields $`O(\epsilon^{-2}\log(1/\delta))`$ copies. For the converse, fix a detector, and take diagonal source states with polarizations separated by more than $`2\epsilon`$ and both near zero. The relative entropy of the input states is $`O(\epsilon^2)`$ per copy. Data processing and the same testing bound give the matching copy lower bound, even for general collective readout of the input states.
