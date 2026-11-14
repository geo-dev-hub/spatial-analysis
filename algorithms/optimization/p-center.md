# The p-center problem: minimize the worst service distance

Stable ID: `SA-OPT-P-CENTER` · Draft 0.1 · Source compendium section 6, page 10

## The planning question

If exactly p facilities must be opened, how can we choose their locations so that the most poorly served demand point is as close as possible to its assigned facility?

The p-center problem minimizes the maximum service cost. It is a minimax objective: it focuses on the worst-served demand location, not the average or total cost.

## Mathematical formulation

Let I be demand locations, J candidate sites, d_ij the cost from demand i to site j, and p the required number of facilities. Let x_j indicate an opened site, y_ij assign demand i to site j, and R be the maximum assignment cost.

$$
\min R
$$

subject to:

$$
\sum_{j\in J} y_{ij}=1 \quad \forall i\in I,
\qquad
y_{ij}\le x_j \quad \forall i,j,
$$

$$
\sum_{j\in J}x_j=p,
\qquad
\sum_{j\in J}d_{ij}y_{ij}\le R \quad \forall i,
$$

$$
x_j,y_{ij}\in\{0,1\}, \quad R\ge0.
$$

For any chosen facility set, assigning each demand to its nearest open facility minimizes the worst assignment cost for that set. The small-instance implementation therefore enumerates facility sets and computes the maximum of the nearest-site costs.

## What does the objective prioritize?

- **p-median** minimizes the sum of weighted assignment costs. It can accept a long trip for a small number of people if doing so reduces total cost elsewhere.
- **p-center** minimizes the worst assignment cost. It protects the most distant demand point under the stated cost matrix.
- **MCLP** maximizes demand reached within a fixed service threshold. Demand outside the threshold remains uncovered.

The p-center objective is sensitive to outliers and the definition of the demand set. A single remote point can determine the result. This can be desirable for a worst-case service guarantee, but it should be understood before interpreting the selected sites.

## Exact small-instance baseline

The [Python package](../../implementations/python/p-center/README.md) enumerates all $\binom{|J|}{p}$ candidate sets. For each set it assigns every demand point to its least-cost open facility and evaluates the largest resulting cost.

This is exact and transparent for small instances, but combinatorial in the number of candidate sites. It is not a large-scale optimization solver.

## Cost matrix contract

Rows are demand locations and columns candidate facilities. Values can represent network distance, travel time or another non-negative impedance. The units, directionality, time of day and routing assumptions must be stated. The implementation accepts asymmetric cost matrices.

## Practical workflow

1. Define the demand population and candidate sites.
2. Choose the cost unit and build the appropriate cost matrix.
3. Decide whether the worst-case objective is appropriate for the service.
4. Solve for exactly p sites and inspect assignments.
5. Inspect the demand point determining the radius.
6. Test sensitivity to outliers, candidate eligibility and travel assumptions.
7. Add capacities, reliability, equity and operational constraints as needed.

## Exercises

1. Solve the same cost matrix for p=1, 2 and 3.
2. Add one remote demand point. How does the selected set and radius change?
3. Compare p-center, p-median and MCLP on the same data.
4. Replace symmetric distances with a directed travel-time matrix.
5. Explain when minimizing the worst travel time is a more appropriate policy than minimizing total travel time.

## References

- Hakimi, S. L. (1964), “Optimum locations of switching centers and the absolute centers and medians of a graph,” *Operations Research*, 12(3), 450–459. https://doi.org/10.1287/opre.12.3.450
- Daskin, M. S. (2013), *Network and Discrete Location: Models, Algorithms, and Applications*, 2nd ed., Wiley.

**Scope:** uncapacitated discrete p-center with exactly p facilities, finite candidates and a supplied non-negative cost matrix; no capacity, uncertainty or equity constraints.
