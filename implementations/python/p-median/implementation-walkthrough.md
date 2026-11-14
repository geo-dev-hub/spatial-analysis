# Intern walkthrough: solving a small p-median problem exactly

## 1. State the decision

There are demand locations and candidate facility sites. Choose exactly p sites to open. Each demand location is assigned to the cheapest open facility.

The input matrix has one row per demand point and one column per candidate site. A cell contains the cost of serving that demand point from that candidate.

## 2. Write the objective

Let $c_{ij}$ be the cost from demand point $i$ to candidate facility $j$, $w_i$ the demand weight, and $y_j$ indicate whether facility $j$ is open. The p-median objective is:

$$
\min \sum_i w_i\min_{j:y_j=1} c_{ij}
$$

subject to exactly p facilities being selected. The implementation uses this assignment structure directly rather than introducing a separate mixed-integer solver.

## 3. Enumerate candidate sets

For every combination of p candidate facilities:
1. extract the corresponding columns of the cost matrix;
2. find the minimum-cost open facility for each demand row;
3. calculate the demand-weighted objective;
4. retain the best solution.

Combinations are generated in lexicographic order. When objective values tie, strict-improvement replacement retains the first combination, making tie behaviour reproducible.

## 4. Understand the growth in work

There are $\binom{m}{p}$ possible facility sets for m candidates. Each set requires assigning every demand row. This grows quickly and is why the exact enumeration is limited to small teaching instances.

For larger instances, use a mathematical-programming solver, decomposition or a suitable heuristic, and validate it against small exact cases.

## 5. Do not mistake this for every location model

This package does not include capacities, fixed opening costs, maximum service distance, queueing, stochastic demand, equity objectives or multi-level facilities. Those changes alter the optimisation problem, not just the implementation detail.

## 6. Verify the result

Tests cover a known optimum, demand weights, deterministic ties, opening all candidates, invalid p values and invalid costs. A useful extension is to compare a solver's result with brute force on small random matrices.
