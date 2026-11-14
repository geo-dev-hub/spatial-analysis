# Exercise: backup coverage and service redundancy

## Learning goal

Distinguish ordinary reachability from redundant potential access. You will test whether demand has one or multiple distinct selected facilities within a service threshold.

## Starter material

Use the [backup-coverage implementation](../implementations/python/backup-coverage/README.md) and [visual lab](../notebooks/backup-coverage-lab.ipynb). The lab creates a small synthetic demand–facility cost matrix; no external dataset is required.

## Tasks

1. Predict which demand locations can be covered twice when r=2 and p=2.
2. Run the model for r=1 and r=2 with the same p and threshold. Explain the difference in the objective and per-demand counts.
3. Increase p by one. Does every additional facility improve backup coverage?
4. Tighten the service threshold. Which demand locations lose their second eligible facility first?
5. Create an asymmetric matrix and explain why return travel or direction-specific access may change backup status.
6. Identify two candidate facilities that share a vulnerable dependency. Explain why the model overstates redundancy for those demand locations.
7. Propose a disruption-scenario table with facility availability states. What additional data would be needed to estimate service reliability rather than deterministic backup coverage?

## What to submit

- A table of selected candidate indices, covered weight and per-demand eligible-facility counts.
- A comparison of r=1 and r=2.
- A short map or sketch showing covered, singly reached and unreached demand.
- A paragraph naming at least three assumptions that prevent the result from being interpreted as a reliability probability.

## Check your work

A demand row counts only if at least r **distinct selected candidate columns** are within the inclusive service threshold. It is counted once, regardless of whether r or more facilities can reach it. The selected set contains no more than p candidates.

Do not describe the output as “probability of surviving an outage.” No probabilities or failure dependencies are present in this model.
