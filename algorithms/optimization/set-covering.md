# Set covering: the smallest network that reaches everyone

Stable ID: `SA-OPT-SET-COVER` · Draft 0.1 · Source compendium section 6, page 10

## The planning question

Suppose a service authority has a target: every demand location must be within a stated travel-time or distance standard of at least one facility. What is the smallest number of facilities needed to meet that standard?

The location set-covering problem minimizes the number of open facilities while requiring every demand point to be covered. It is a different objective from p-median, p-center and maximal covering.

## Mathematical formulation

Let I be demand locations and J candidate facility sites. Let d_ij be the cost from demand i to candidate j, S the service threshold, and x_j indicate whether candidate j is opened. Define N_i = {j : d_ij <= S}.

[
\min \sum_{j\in J}x_j
]

subject to:

[
\sum_{j\in N_i}x_j\ge1 \quad \forall i\in I,
\qquad
x_j\in\{0,1\}.
]

Every demand point must have at least one selected candidate within the threshold. Each facility has equal opening cost in this basic model, so the objective is the facility count.

## Feasibility comes first

If any demand point has no eligible candidate within S, the model is infeasible for the supplied candidate set and threshold. A solver should report that explicitly rather than quietly leave the demand uncovered.

A feasible solution does not imply that a facility can actually serve every person. The basic model has no capacity, queue, staffing, reliability or congestion constraints.

## Exact small-instance baseline

The [Python package](../../implementations/python/set-covering/README.md) enumerates candidate subsets in increasing cardinality. The first subset that covers all demand is a minimum-cardinality solution. For m candidate facilities, the worst-case number of subsets considered is (2^m). This is exact and transparent for small instances, not a large-scale solver.

## How the location models differ

- **Set covering:** minimize the number of facilities needed to cover all demand within S.
- **Maximal covering:** maximize covered demand subject to an at-most-p facility budget and threshold S.
- **p-center:** open exactly p facilities and minimize the worst nearest-facility cost.
- **p-median:** open exactly p facilities and minimize total weighted assignment cost.

Set covering treats the service threshold as a requirement. MCLP treats it as the boundary of what counts as covered while maximizing the amount reached. p-center minimizes the worst cost rather than requiring a preselected threshold.

## Practical workflow

1. Define demand units and the required service threshold.
2. Identify eligible candidate sites and any exclusions.
3. Build a cost matrix using the appropriate travel mode, direction and time period.
4. Check whether every demand row has at least one eligible candidate.
5. Solve and inspect the selected sites and coverage assignments.
6. Test sensitivity to the threshold and candidate set.
7. Add capacity, equity, redundancy and reliability constraints before operational use.

## Exercises

1. Solve the same instance at two service thresholds. How many facilities are required?
2. Remove one candidate site. Does the problem remain feasible?
3. Compare set covering with maximal covering for the same threshold.
4. Explain why a set-cover solution can be mathematically feasible but operationally inadequate when facilities have limited capacity.
5. Add unequal facility opening costs conceptually. How does the objective change?
6. Explain why an infeasible result may indicate a candidate-set problem rather than a solver defect.

## References

- Toregas, C., Swain, R., ReVelle, C. and Bergman, L. (1971), “The location of emergency service facilities,” *Operations Research*, 19(6), 1363–1373. https://doi.org/10.1287/opre.19.6.1363
- Church, R. and ReVelle, C. (1974), “The maximal covering location problem,” *Papers in Regional Science*, 32(1), 101–118. https://doi.org/10.1111/j.1435-5597.1974.tb00902.x
- Daskin, M. S. (2013), *Network and Discrete Location: Models, Algorithms, and Applications*, 2nd ed., Wiley.

**Scope:** uncapacitated discrete location set covering with equal facility costs, a finite candidate set and a supplied cost matrix/service threshold. No capacity, backup coverage, stochastic reliability or equity constraints.
