# Maximal covering: place facilities to reach the most demand

Stable ID: `SA-OPT-MAXIMAL-COVERING` · Draft 0.1 · Source compendium section 6, page 10

## The planning question

If an agency can open at most p facilities, and each facility can serve demand only within a specified distance or travel-time threshold, where should those facilities be placed to reach the greatest amount of demand?

The maximal covering location problem (MCLP) answers this question. It differs from p-median: p-median minimizes total weighted assignment cost, while MCLP maximizes demand covered within a service standard.

## Mathematical model

Let I be demand locations and J candidate sites. Let a_i be non-negative demand weight, d_ij the cost from demand i to candidate j, S the service threshold, and p the maximum number of facilities. Let x_j indicate whether candidate j is selected and y_i whether demand i is covered. Define N_i = {j : d_ij <= S}.

$$
\max \sum_{i\in I} a_i y_i
$$

subject to

$$
\sum_{j\in N_i}x_j \ge y_i \quad \forall i\in I,
\qquad
\sum_{j\in J}x_j \le p,
\qquad
x_j,y_i\in\{0,1\}.
$$

A demand point counts as covered when at least one selected facility is within the threshold. It is counted once, even if several selected sites can reach it.

This package uses **at most p** facilities. Some formulations require exactly p; that is a different budget convention. When objective values tie, this implementation prefers fewer sites, then lexicographically earlier candidate indices.

## Cost matrix and service standard

Rows represent demand locations and columns candidate facilities. Costs may be network travel time, distance, walking time or another impedance, but units and routing assumptions must be explicit. The matrix may be asymmetric, so directed travel costs are supported.

The threshold is a planning standard, not a parameter to tune merely to make coverage look good. State why it is appropriate for the service being planned.

## Exact small-instance baseline

The [Python package](../../implementations/python/maximal-covering/README.md) enumerates all subsets of size zero through p. For m candidate sites it examines:

$$
\sum_{k=0}^{p}\binom{m}{k}.
$$

This is exact and transparent but grows combinatorially. Use it for learning and as a small-instance oracle, not as a metropolitan-scale solver.

## Distinguish the models

- **p-median:** open exactly p sites and minimize weighted total assignment cost.
- **MCLP:** open at most p sites and maximize demand within a stated service threshold.
- **Set covering:** cover all specified demand with the fewest sites, if feasible.

MCLP is not an assignment or capacity model. It does not guarantee that a facility has enough staff, vehicles, beds or throughput to serve every covered person.

## Practical workflow

1. Define demand units, population weights and time period.
2. Define eligible candidate sites and excluded locations.
3. Build a cost matrix with explicit units, directionality and travel assumptions.
4. Choose and justify the service threshold.
5. Solve and map covered and uncovered demand.
6. Test sensitivity to p, threshold, candidates and demand weights.
7. Add capacity, equity, reliability and operational constraints when required.

## Exercises

1. Solve for p=1, 2 and 3. How much additional demand becomes covered?
2. Tighten and relax the threshold. Which locations change coverage status?
3. Replace symmetric distances with directed travel times. Explain the effect of one-way streets and barriers.
4. Compare MCLP and p-median using the same cost matrix.
5. Add capacity constraints conceptually. Why can simple coverage overstate actual service?
6. Explain why a threshold is a policy choice rather than a purely statistical parameter.

## References

- Church, R. and ReVelle, C. (1974), “The maximal covering location problem,” *Papers of the Regional Science Association*, 32(1), 101–118. https://doi.org/10.1007/BF01942293
- Church, R. and ReVelle, C. (1976), “Theoretical and computational links between the p-median, location set-covering, and the maximal covering location problem,” *Geographical Analysis*, 8(4), 406–415. https://doi.org/10.1111/j.1538-4632.1976.tb00547.x
- Daskin, M. S. (2013), *Network and Discrete Location: Models, Algorithms, and Applications*, 2nd ed., Wiley.

**Scope:** at-most-p maximal covering with finite candidate sites, non-negative weighted demand, a supplied cost matrix and one common threshold. No capacities, queueing, stochastic reliability or multi-period constraints.
