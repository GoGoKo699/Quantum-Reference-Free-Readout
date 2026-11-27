# Project understanding map

The **12 background milestones** build the measurement model and the statistical tools for comparing experiments. The **18 research milestones** follow the ambiguity, circuit, matching bound and two-report comparison in that order. Use the [Watrous bridge](WATROUS_BRIDGE.md) for the single educational anchor and the [worked examples](WORKED_EXAMPLES.md) for concrete circuits and report distributions.

| Milestones | Reading goal |
| --- | --- |
| M01–M04 | Identify the source, detector and resources of a block. |
| M05–M08 | Connect circuits to report means and organize their tensor terms. |
| M09–M12 | Connect finite samples, distinguishability and the exact task. |
| M13–M19 | Break the single-copy ambiguity and build a stable amplified estimator. |
| M20–M25 | Count the circuit's copies and derive the converse for adaptive protocols. |
| M26–M30 | Explain the two-report comparison, scope and scientific contributions. |

## Phase I — Background and preliminaries

### M01 Qubit state and Pauli expectation

What does the unknown source parameter describe?

Read $`z=\mathrm{Tr}(Z\rho)`$ as an ideal mean of a qubit, and distinguish it from the probability of the positive outcome. A trusted basis rotation makes the same question apply to any Bloch coordinate.

**Prerequisites.** None. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Detector model](../science/model.md)

### M02 Independent preparations

What is available when several copies enter a block?

Use $`\rho^{\otimes k}`$ for $`k`$ fresh independent preparations. Product expectations and the converse's tensor expansion both require this independence.

**Prerequisites.** M01. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Detector model](../science/model.md)

### M03 A detector with offset and gain

How does a real report differ from the ideal Pauli outcome?

Obtain the binary probabilities from $`E_s=(I+s(aI+bZ))/2`$ and explain the physical constraint $`|a|+b\le 1`$. The same unknown offset and gain enter every detector call.

**Prerequisites.** M01. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Detector model](../science/model.md)

### M04 Block boundaries and charged copies

Which resources can the readout protocol use?

Separate maximum simultaneous copies $`K`$, total fresh copies $`N`$, and physical detector calls. Track which registers may be processed jointly and which outcomes or registers persist between blocks.

**Prerequisites.** M02 M03. **Read.** [Detector model](../science/model.md)

### M05 Pulling a local detector through a circuit

What makes a local output measurement sensitive to several inputs?

Write the ideal report mean using $`U^\dagger Z_jU`$ on the full input space. Use unitarity to preserve the trace and operator norm, the two properties needed for the converse.

**Prerequisites.** M02–M04. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Detector model](../science/model.md)

### M06 Private random signs

How can trusted controls cancel an offset?

Average a final random bit flip and the corresponding classical sign correction. The two runs have opposed offsets in the corrected sign convention and a shared gain.

**Prerequisites.** M03 M05. **Read.** [Detector model](../science/model.md) · [Worked example 1](WORKED_EXAMPLES.md#1-one-detector-two-possible-sources)

### M07 Pauli products from CNOT

Which input quantity does one output report test?

Pull $`Z`$ on the target backward through CNOT to obtain $`Z\otimes Z`$. Independence turns the expectation into a square. Keep this separate from measuring both outputs and multiplying their reports.

**Prerequisites.** M02 M05. **Read.** [Detector model](../science/model.md) · [Worked example 1](WORKED_EXAMPLES.md#1-one-detector-two-possible-sources) · [Worked example 4](WORKED_EXAMPLES.md#4-two-reports-change-the-scaling)

### M08 Orthogonal tensor characters

How do we separate the terms of a many-copy expectation?

Write products $`Z_S`$ on the subsets $`S`$ of registers and use their normalized Hilbert–Schmidt orthogonality. This measures the combined size of all high-degree coefficients.

**Prerequisites.** M02 M05. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Worked example 3](WORKED_EXAMPLES.md#3-the-coefficients-that-survive-matching)

### M09 Finite precision of a report mean

What does sampling a detector mean cost?

Use bounded independent signs and Hoeffding's inequality to convert precision $`\eta`$ into order $`\eta^{-2}`$ calls at fixed confidence. Convert calls to copies using the size of each sampled arm.

**Prerequisites.** M03 M04 M06. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Minimax result and proof](../science/minimax.md)

### M10 Information in a binary report

How much does a small change in a report mean reveal?

Relate the relative entropy of two Bernoulli laws to the square of their mean gap when the probabilities stay away from zero and one. This is the bridge from bias cancellation to a copy lower bound.

**Prerequisites.** M03 M09. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Worked example 3](WORKED_EXAMPLES.md#3-the-coefficients-that-survive-matching)

### M11 Testing from an estimator

Why can two candidate experiments prove a lower bound?

Turn an accurate estimate into a test between two values separated by more than $`2\epsilon`$. For adaptive controls, add the conditional relative entropies along the observation history.

**Prerequisites.** M04 M10. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Minimax result and proof](../science/minimax.md)

### M12 The reference-free estimation task

What exactly must a successful protocol estimate?

State the worst-case error guarantee over the source and detector parameters, the positive gain floor, and the one-report rule. Distinguish minimizing the charged copy count from separately minimizing the report count.

**Prerequisites.** M01–M11. **Read.** [Detector model](../science/model.md) · [Minimax result and proof](../science/minimax.md)

## Phase II — Narrative and innovation

### M13 The single-copy ambiguity

Can more runs with one copy distinguish gain from polarization?

Construct distinct source–detector pairs with identical offset and gain–bias product. Their report law agrees for every trusted one-copy rotation, so even adaptive repetitions cannot identify the state.

**Prerequisites.** M05 M06 M12. **Read.** [Worked example 1](WORKED_EXAMPLES.md#1-one-detector-two-possible-sources) · [Minimax result and proof](../science/minimax.md)

### M14 Making the source its own reference

How does a second copy remove the exact ambiguity?

Use direct and parity experiments to obtain $`bz`$ and $`bz^2`$ with the same gain. The ratio identifies nonzero $`z`$, while the geometry of the moments near zero sets the large sampling cost.

**Prerequisites.** M07 M09 M13. **Read.** [Worked example 1](WORKED_EXAMPLES.md#1-one-detector-two-possible-sources) · [Minimax result and proof](../science/minimax.md)

### M15 Compressing signals into a source copy

How can a block amplify a weak bias without an initialized target?

Use the target's sign to encode the relative input signs, then control a rotation of that same target. The target sign cancels in its output mean, leaving a sine of the signal sum.

**Prerequisites.** M02 M05 M07 M14. **Read.** [Worked example 2](WORKED_EXAMPLES.md#2-amplifying-the-bias-with-source-copies) · [Minimax result and proof](../science/minimax.md)

### M16 Choosing the rotation scale

What makes the compressed response usable for estimation?

Factor the characteristic function of independent signs to get $`f_m(z)`$. Set the rotation per signal to order $`m^{-1/2}`$ and confine the fit to an interval where the derivative is positive and of order $`\sqrt m`$.

**Prerequisites.** M09 M15. **Read.** [Worked example 2](WORKED_EXAMPLES.md#2-amplifying-the-bias-with-source-copies) · [Minimax result and proof](../science/minimax.md)

### M17 Choosing the block width

How does the protocol find a useful response interval with unknown polarization?

Use a bounded-precision pilot for $`bz`$ and the known lower gain bound to choose $`m`$. Larger blocks amplify nearby weak states, while a smaller block keeps stronger states on the invertible part of the response.

**Prerequisites.** M09 M16. **Read.** [Minimax result and proof](../science/minimax.md)

### M18 A square with the same gain

How does the amplified experiment still admit reference-free inference?

Combine two independent compressed targets with a final CNOT and read its target once. The two mean reports are $`bf_m(z)`$ and $`bf_m(z)^2`$, with only one detector gain factor in each.

**Prerequisites.** M07 M15–M17. **Read.** [Worked example 2](WORKED_EXAMPLES.md#2-amplifying-the-bias-with-source-copies) · [Minimax result and proof](../science/minimax.md)

### M19 Inversion near zero

Why does the fit remain well posed at exactly zero polarization?

Fit the pair of moments over the allowed response interval and gain range. Show that separated polarizations force a resolvable moment gap even when a ratio of the raw empirical means would be unstable.

**Prerequisites.** M09 M16–M18. **Read.** [Minimax result and proof](../science/minimax.md)

### M20 The copy cost of the circuit

How do the pilot and both measurement arms add up?

Count the pilot, source-copy targets and parity blocks. Identify the weak-state width-limited term $`\epsilon^{-4}/K`$ and the usual $`\epsilon^{-2}`$ term, including the small-width special case.

**Prerequisites.** M12 M14 M17–M19. **Read.** [Minimax result and proof](../science/minimax.md)

### M21 Choosing a matched hard pair

Which pair of experiments can defeat every allowed circuit?

Take distinct interior gains and source biases of order $`\epsilon`$ with shared linear detector response. The two sources should be separated by more than twice the target error.

**Prerequisites.** M11 M13 M14. **Read.** [Worked example 3](WORKED_EXAMPLES.md#3-the-coefficients-that-survive-matching) · [Minimax result and proof](../science/minimax.md)

### M22 Matching the constant and linear terms

Why does matching one product limit a general collective circuit?

Expand both tensor inputs and pair them with the pulled-back observable. The circuit preserves tracelessness, and matching $`bz`$ cancels all the degree-one terms for every circuit choice.

**Prerequisites.** M05 M08 M21. **Read.** [Worked example 3](WORKED_EXAMPLES.md#3-the-coefficients-that-survive-matching) · [Minimax result and proof](../science/minimax.md)

### M23 Bounding the remaining information per block

How do all higher-order terms combine as the block grows?

Use orthogonality to bound the report mean gap by order $`k\epsilon^2`$ when $`k\epsilon^2`$ is bounded. Bound the relative entropy by its square in that regime and by a constant for larger blocks.

**Prerequisites.** M08 M10 M21 M22. **Read.** [Worked example 3](WORKED_EXAMPLES.md#3-the-coefficients-that-survive-matching) · [Minimax result and proof](../science/minimax.md)

### M24 The adaptive lower bound

Why does the hard pair survive data-dependent controls and block sizes?

Condition on each report history and sum the corresponding information bounds. The constraints $`k\le K`$ and total charged copies $`N`$ give a single bound on the distinguishing power of the transcript.

**Prerequisites.** M04 M11 M21–M23. **Read.** [Minimax result and proof](../science/minimax.md)

### M25 The sharp copy–width law

Where does the cost cross over between the two regimes?

Compare the constructed and necessary copy budgets. The width-limited cost falls as $`K`$ increases until blocks of order $`\epsilon^{-2}`$ reach the usual $`\epsilon^{-2}`$ total-copy scale.

**Prerequisites.** M20 M24. **Read.** [Minimax result and proof](../science/minimax.md)

### M26 Independent reports and the two-copy comparison

What changes when the detector reports both output signs?

Derive the report product mean $`b^2z`$ from CNOT and independent detector noise. Combine it with $`bz`$ to obtain stable state estimation to precision $`\epsilon`$ using order $`\epsilon^{-2}`$ copies at width two. For the correlated detector, use the identity and CNOT arms to derive the moments $`\bar\kappa z^2`$ and $`\bar\kappa z`$. Explain how the same call count can give a different copy cost.

**Prerequisites.** M06 M07 M19 M25. **Read.** [Worked example 4](WORKED_EXAMPLES.md#4-two-reports-change-the-scaling) · [Minimax result and proof](../science/minimax.md) · [Temporal parity](../science/temporal-parity.md)

### M27 From a coordinate to a qubit state

Which quantities can the data determine uniformly?

Repeat the procedure in three trusted Pauli bases and interpret the resulting Bloch vector. Explain why there is still no guaranteed detector-gain estimate at the maximally mixed source.

**Prerequisites.** M01 M03 M25 M26. **Read.** [Detector model](../science/model.md) · [Minimax result and proof](../science/minimax.md)

### M28 Control errors and moment precision

How do imperfect gates enter an estimate from the two moments?

Translate a control-channel deviation into a shift of the relevant mean and compare it with the inverse fit's tolerance. In the separate target-only CNOT fault model, explain why a basis change moves certain faults to unmeasured control phases and why the native fanout faults can enter as a single unknown visibility.

**Prerequisites.** M05 M16 M19 M25. **Read.** [Watrous bridge](WATROUS_BRIDGE.md) · [Control-error analysis](../science/robustness.md)

### M29 Control depth and detector calls

How do connectivity and detector calls affect the readout cost?

Connect the backward light cone of the detector to the effective copy width in the converse, and the fanout circuit to the attained depth on a lattice. Distinguish the proved copy complexity from the separate report-count bounds.

**Prerequisites.** M04 M15 M24–M26 M28. **Read.** [Control and resource bounds](../science/robustness.md) · [Verification](../verification/README.md)

### M30 The complete readout argument

How do the circuit and the obstruction explain the same resource tradeoff?

Connect single-copy ambiguity, amplification by independent copies, the matched higher-order converse, and the different gain dependence of two reports. Identify the earlier two-copy gain cancellation and state what the width-dependent result adds for this detector interface. State which detector assumptions let the same copy law transfer to temporal parity.

**Prerequisites.** M12 M25–M29. **Read.** [Detector model](../science/model.md) · [Minimax result and proof](../science/minimax.md) · [Control and resource bounds](../science/robustness.md) · [Related work](../science/related-work.md)
