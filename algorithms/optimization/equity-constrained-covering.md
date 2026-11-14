# Equity-constrained maximal covering: protect minimum group access

Stable ID: SA-OPT-EQUITY-COVER · Draft 0.1 · Source compendium section 6

## The planning question

Maximal covering chooses at most p facilities to maximise the total demand reached within a service threshold. But an unconstrained optimum can concentrate coverage where it earns the greatest total weight and leave one group below an acceptable minimum.

An equity-constrained version adds explicit minimum coverage requirements for caller-defined groups. It makes the policy trade-off visible: the model must satisfy the floors before maximising the overall objective.

## Mathematical formulation

Let I be demand rows, J candidate sites, G mutually exclusive groups, c_ij the travel cost, T the service threshold, q_i population weight, v_i objective weight, alpha_g the minimum population coverage share for group g, and p the facility budget.

Let y_j be the binary opening decision and z_i indicate whether demand i is covered by at least one selected site within T.

\[
\max \sum_{i\in I}v_i z_i
\]

subject to:

\[
z_i\leq\sum_{j:c_{ij}\leq T}y_j,\quad z_i,y_j\in\{0,1\},
\]

\[
\sum_{i\in g}q_i z_i\geq\alpha_g\sum_{i\in g}q_i
\quad \forall g\in G,
\qquad
\sum_{j\in J}y_j\leq p.
\]

The model maximises weighted covered demand after requiring every group to meet its declared coverage floor. Population weights q_i define the group coverage denominator. Objective weights v_i define the total benefit. Keep them separate.

## A practical comparison

Run the [equity-constrained covering lab](../../notebooks/equity-constrained-covering-lab.ipynb). Start with zero group floors to recover ordinary maximal covering. Then increase one group's minimum and inspect whether the selected facilities, total covered weight or number of sites changes.

An [exact small-instance Python implementation with unit tests](../../implementations/python/equity-covering/README.md) enumerates candidate subsets. It is intended as a transparent teaching oracle, not a city-scale optimiser.

## What the model assumes

- Each demand row belongs to exactly one declared group.
- Coverage is binary: cost at or below T counts as covered.
- Demand weights are non-negative and each group has positive total demand.
- Group floors lie between zero and one.
- Facilities open at most p sites; opening costs and capacity are not modelled.
- Travel costs are static and deterministic.
- The objective weights and group floors are analyst-supplied.

## Equity is a policy choice, not an algorithm setting

The model does not discover the morally correct groups, floors or priorities. A 60% coverage floor is not inherently fair, and a group label can conceal different needs within it. Consult affected communities, justify the minimum standard and test multiple plausible thresholds. Report both total benefit and group-specific outcomes.

A constrained optimum can reduce the overall objective while improving a group's minimum coverage. That is a real trade-off, not a model failure. Also inspect the absolute accessibility distribution and lower-tail values using the [equity diagnostics lesson](accessibility-equity.md).

## Exercise

Use the [equity-constrained covering exercise](../../exercises/equity-constrained-covering.md) to compare the unconstrained and constrained facility sets, vary the group floors and explain the trade-off.

## References

- Church, R. L., & ReVelle, C. S. (1974). The maximal covering location problem. *Papers of the Regional Science Association*, 32(1), 101–118. https://doi.org/10.1111/j.1435-5597.1974.tb00902.x
- Church, R. L., & ReVelle, C. S. (1976). Theoretical and computational links between the p-median, location set-covering, and the maximal covering location problem. *Geographical Analysis*, 8(4), 406–415. https://doi.org/10.1111/j.1538-4632.1976.tb00547.x
- Pereira, R. H. M., Schwanen, T., & Banister, D. (2017). [Distributive justice and equity in transportation](https://doi.org/10.1080/01441647.2016.1257660). Transport Reviews, 37(2), 170–191.

Scope: deterministic group-constrained maximal covering with binary catchments and an exact tiny-instance enumerator; not a complete theory of fairness.
