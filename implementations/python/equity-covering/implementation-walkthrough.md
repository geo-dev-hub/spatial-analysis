# Intern walkthrough: equity-constrained maximal covering

1. **Read the matrix.** Each row is a demand unit and each column a candidate facility. A cost at or below the threshold means that candidate can cover that row. Positive infinity marks an unreachable pair.
2. **Separate the weights.** Demand weights define the population denominator for each group's coverage floor. Objective weights determine which covered rows contribute to the maximised total. Do not silently use one for both.
3. **Set group floors.** Every observed group needs a target between zero and one. These are policy requirements, not parameters discovered by the algorithm.
4. **Enumerate candidate sets.** The exact solver checks every subset containing at most p sites. For each subset it marks covered demand rows, calculates population coverage by group and rejects any set that misses a floor.
5. **Choose the best feasible set.** Among feasible sets it maximises total objective weight. Exact ties prefer fewer sites and then the lexicographically smallest candidate-index tuple.
6. **Inspect the result.** Report selected sites, covered rows, total objective and every group's coverage rate. Also compare with ordinary maximal covering to expose the cost of the added constraints.
7. **Run tests.** Install the package requirements and run python -m pytest -q. Tests cover equity constraints, separate weights, infeasibility, unreachable pairs, ties and invalid inputs.

This is a tiny-instance teaching oracle. It does not infer which groups should receive priority or what a fair coverage floor should be.
