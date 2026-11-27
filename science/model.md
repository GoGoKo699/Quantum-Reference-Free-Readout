# Readout model and claims

## Experiment

The source supplies independent copies of an unknown qubit state $`\rho`$. The target is the expectation $`z=\operatorname{Tr}(Z\rho)\in[-1,1]`$. Trusted single-qubit basis rotations give the same question for any specified Pauli axis.

The detector has fixed, unknown parameters $`a,b`$. On a qubit in state $`\sigma`$ it returns $`Y\in\{-1,1\}`$ with effects and mean

```math
E_y=\frac{I+y(aI+bZ)}2,\qquad
\mathbb E[Y\mid \sigma]=a+b\operatorname{Tr}(Z\sigma).
```

A known contrast floor $`b_{\min}`$ satisfies $`0\lt b_{\min}\lt 1`$. The parameter domain is $`b\ge b_{\min}`$ and $`|a|+b\le1`$. The detector is destructive and memoryless. Detector uses have fresh reporting randomness, conditional on the quantum systems being measured. The diagonal effects also describe an ideal $`Z`$ read followed by a classical binary reporting channel with conditional mean $`a+b x`$ for ideal sign $`x`$.

A one-report protocol takes a fresh block of $`k\le K`$ copies, applies any trusted unitary on those copies, calls the detector once on one selected output, and discards the other outputs. It may choose the size, gates and measured qubit by classical feedback from prior blocks. Classical randomization and postprocessing are free. It has access to the supplied copies and no prepared probe of known polarization, measurement ancilla, reset, further state-dependent report, or persistent quantum register between blocks. Each copy entering any block counts toward the total budget $`N`$.

For the two-report comparator, a block may instead read both qubits after a two-copy unitary. The two detector calls have the same $`(a,b)`$ and independent reporting noise conditional on the two ideal signs. Grouping two calls into one externally transmitted bit still uses two physical reports.

## Copy complexity

At a fixed confidence, for example success probability at least $`2/3`$, the one-report minimax budget at $`K\ge2`$ is

```math
N_{\mathrm{one}}(K,\epsilon)
=\Theta_{b_{\min}}\!\left(
  \max\!\left\{\epsilon^{-2},\,\frac{\epsilon^{-4}}{K}\right\}
\right).
```

The statement is uniform over integer $`K\ge2`$ and all sufficiently small $`\epsilon>0`$. Success means $`|\widehat z-z|\le\epsilon`$ uniformly over the unknown state and physical detector parameters. At confidence $`1-\delta`$, for $`0\lt \delta\le1/4`$, the two terms acquire a factor $`\log(1/\delta)`$. The optimizer may know $`K`$, $`\epsilon`$, $`\delta`$ and $`b_{\min}`$.

At $`K=1`$, no number of reports gives uniform arbitrarily accurate estimates. At $`K=2`$, one report per block incurs order $`\epsilon^{-4}`$ copies. At width two with two reports per block the order is $`\epsilon^{-2}`$. The same parametric copy order is achievable with one report when width reaches order $`\epsilon^{-2}`$.

The target is the state expectation. When $`\rho=I/2`$, every allowed trusted unitary preserves the maximally mixed block, so those experiments supply no information about $`b`$. The proof uses the detector gain as a nuisance parameter. Three runs of the estimation procedure, in the three Pauli bases on disjoint source ensembles, yield Bloch-vector estimation with the same asymptotic law up to constants. Projection to the Bloch ball preserves its Euclidean guarantee.

## Why the resource restrictions matter

A prepared $`|0\rangle`$ supplies a unit polarization and a state-independent gain reference. An ideal reset would create that reference inside the block. These operations change the inference problem. The model counts unknown input copies and physical calls separately, with no claim that an unknown state is an economical replacement for an available reference.

The [minimax proof](minimax.md) establishes the ideal gate law. The [control bounds](robustness.md) distinguish gate depth and imperfect implementations from ideal copy complexity.
