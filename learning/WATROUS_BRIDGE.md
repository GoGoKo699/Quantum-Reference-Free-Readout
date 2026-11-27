# From Watrous to reference-free readout

The educational anchor is **John Watrous, *The Theory of Quantum Information***, Cambridge University Press, 2018. The sections below follow the [author's 2018 prepublication manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf). The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) links each chapter and identifies the April 2018 publication. The [publisher's contents](https://assets.cambridge.org/97811071/80567/toc/9781107180567_toc.pdf) give the corresponding chapter and section numbers.

The book develops the toolkit for states, measurements, channel distances and information. The project applies that toolkit to a particular physical restriction: every block ends with one local destructive call to the same uncalibrated detector. The [milestone map](MILESTONES.md) follows the project's argument. Open the sections below when the corresponding step needs them.

## Readings and their role

| Watrous manuscript sections | Use in this project | Milestones |
| --- | --- | --- |
| [§§2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Represent a qubit by a density operator, independent inputs by its tensor power, and a discarded system by a partial trace. | M01–M02, M14 |
| [§§2.2.1–2.2.3 and 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Convert a local two-effect POVM into a bit distribution and pull it back through an input circuit. Theorem 2.37 identifies measurements with channels whose outputs are classical. | M03–M07, M13, M18, M26 |
| [§§1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Expand in tensor products of Pauli operators and use the Hilbert–Schmidt inner product to bound the effect of higher-order terms. The project normalizes this inner product by the register dimension. | M08, M22–M23 |
| [§1.2.2, especially Theorem 1.16](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Turn bounded detector outcomes into finite-sample mean estimates with Hoeffding's inequality. | M09, M16–M19 |
| [§§5.1.1–5.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) and [§3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Use classical relative entropy to compare report distributions, and distinguish estimating a parameter from testing two candidate experiments. The classical transcript permits a direct two-hypothesis argument. | M10–M11, M21–M24 |
| [§§3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Bound the change in an output moment under a perturbation of the control channel. | M28–M29 |

## Translate the measurement

For Watrous's measurement effects $`\mu(a)`$ indexed by outcomes, write this project's two effects as $`E_s=(I+s(aI+bZ))/2`$, with $`s\in\{-1,+1\}`$. Here $`a`$ is the detector offset and $`b>0`$ is its gain. The two values of $`s`$ label the report; they are distinct from the detector parameter $`a`$. If the block input is $`\rho^{\otimes k}`$ and the circuit is $`U`$, the Born rule gives

```math
\Pr(s)=\frac{1+s\left(a+b\mathrm{Tr}(M_U\rho^{\otimes k})\right)}2,
\qquad M_U=U^\dagger(Z_j\otimes I_{\mathrm{rest}})U .
```

Here $`Z_j`$ denotes the ideal Pauli observable on the measured output. The unknowns appear in the probability law after the same known circuit. The pulled-back operator $`M_U`$ is a traceless Hermitian contraction. A binary measurement realized by many physical detector calls can have a different dependence on the gain, so the proof tracks the calls as well as the classical outcome alphabet. [Model and exact resource definition](../science/model.md)

## Follow the project-specific steps

The source bias $`z=\mathrm{Tr}(Z\rho)`$ enters the single-copy data through a product with $`b`$. A CNOT creates a second experiment with expectation $`bz^2`$. With more copies, the local measurement sees an amplified response $`f_m(z)`$, and a separate block produces its square with the same factor $`b`$. The circuit and the pilot that chooses its working region are specific to the project. [Two-copy and amplified examples](WORKED_EXAMPLES.md#2-amplifying-the-bias-with-source-copies)

For the converse, choose two admissible gains and states with identical $`bz`$. The term linear in the source bias then agrees for every allowed circuit. The tensor expansion, Cauchy–Schwarz and the classical relative-entropy chain rule bound the total information from the remaining terms even under adaptive block choices. This is where the block-width dependence enters. [Matched lower bound](../science/minimax.md)

Finally, compare two independently echoed reports after a CNOT. Their product carries $`b^2z`$, which changes the information available per width-two block. A reader can inspect both circuits before comparing their copy costs. [Report comparison](WORKED_EXAMPLES.md#4-two-reports-change-the-scaling)

For the [temporal parity comparison](../science/temporal-parity.md), use §§2.2–2.3 to model the pair of scheduled reports by one four-outcome POVM conditional on prior data. Its parity is the score. Pull the two-output Pauli product back through the pre-block CNOT and compare it with the pulled-back operator for the local report. Then apply the relative-entropy comparison from §§5.1.1–5.1.2 to the hard detector, where one fair report and the parity determine both raw reports. The drift bound uses martingale concentration over blocks.
