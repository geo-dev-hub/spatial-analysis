# Equity-constrained maximal covering

This exact small-instance model selects at most p candidate facilities to maximise weighted demand reached within a travel-cost threshold, while requiring each declared group to reach a minimum population-weighted coverage share.

It is a constrained variant of maximal covering, not a universal fairness model.

## Quick start

~~~python
from equity_covering import equity_maximal_covering

result = equity_maximal_covering(
    travel_costs=[[2, 9, 8], [3, 8, 9], [9, 2, 8], [9, 3, 8]],
    groups=["outer", "outer", "inner", "inner"],
    group_minimum_coverage={"outer": 0.5, "inner": 0.5},
    max_facilities=2,
    max_cost=5,
    demand_weights=[100, 200, 150, 100],
)
print(result["selected_facilities"], result["group_coverage"])
~~~

## Model

Let y_j indicate whether candidate j opens, and z_i indicate whether demand i is covered by at least one selected facility within threshold T. Let q_i be population represented and v_i the objective weight. Let G be the caller-defined mutually exclusive groups and alpha_g their minimum coverage targets.

\[
\max \sum_i v_i z_i
\]

subject to:

\[
z_i \leq \sum_{j:c_{ij}\leq T} y_j,\quad z_i,y_j\in\{0,1\},
\]

\[
\sum_{i\in g}q_i z_i \geq \alpha_g\sum_{i\in g}q_i \quad \forall g\in G,
\qquad \sum_j y_j\leq p.
\]

A demand row is covered if any selected candidate is within the stated threshold. The group constraints use population weights q_i; the objective uses v_i. They may be equal, but that is a modelling choice.

## Input contract

- Matrix rows are demand units; columns are candidate facilities.
- Costs are non-negative and finite; positive infinity represents an unreachable pair.
- Every demand row belongs to exactly one non-empty group label.
- A coverage floor is required for every observed group and must lie in [0, 1].
- Demand weights define the group coverage denominator; every group must have positive total demand.
- Objective weights are separate and non-negative.
- Exactly at-threshold costs count as covered.
- The solver opens at most p facilities. Ties prefer fewer facilities, then the lexicographically smallest candidate-index tuple.
- If no facility set satisfies all group floors, the function raises an explicit infeasibility error.

## Scope and limitations

The implementation enumerates all candidate subsets up to p and is intended for tiny teaching instances and test oracles, not city-scale optimisation. It uses a deterministic static coverage matrix; it does not model capacity, queues, stochastic service, split demand, group overlap, costs of opening, or trade-offs among multiple fairness principles. Groups and targets are policy inputs, not inferred truths.

A higher floor for one group can reduce the total objective or force more facilities. Report both the group coverage rates and total weighted coverage; do not hide the trade-off behind one headline score.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

See the [canonical lesson](../../../algorithms/optimization/equity-constrained-covering.md), [intern walkthrough](implementation-walkthrough.md) and [exercise](../../../exercises/equity-constrained-covering.md).
