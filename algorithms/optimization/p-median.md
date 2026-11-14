# The p-median problem: where should p facilities be located?

Stable ID: `SA-OPT-P-MEDIAN` · Draft 0.1 · Source compendium section 6, page 10

## The planning question

Suppose a city has demand at a set of locations and a finite set of candidate sites for clinics, depots, libraries or service centres. If exactly p facilities can be opened, which candidates minimise the total demand-weighted cost of reaching a facility?

This is the p-median problem. It is a facility-location optimisation model, not a shortest-path algorithm. A routing method may supply the travel-cost matrix, but the location model decides which facilities to open.

## Mathematical formulation

Let:
- $i\in I$ index demand locations;
- $j\in J$ index candidate facility sites;
- $c_{ij}$ be the cost from demand $i$ to candidate $j$;
- $w_i\geq0$ be the demand weight;
- $y_j\in\{0,1\}$ indicate whether candidate $j$ is opened;
- $x_{ij}\in\{0,1\}$ indicate whether demand $i$ is assigned to facility $j$.

A common uncapacitated p-median formulation is:

$$
\min \sum_{i\in I}\sum_{j\in J}w_i c_{ij}x_{ij}
$$

subject to:

$$
\sum_{j\in J}x_{ij}=1 \quad \forall i\in I,
$$

$$
x_{ij}\leq y_j \quad \forall i\in I,j\in J,
$$

$$
\sum_{j\in J}y_j=p,
$$

$$
x_{ij},y_j\in\{0,1\}.
$$

Each demand point is assigned exactly once, only to an open facility, and exactly p facilities are opened.

## What counts as cost?

The cost matrix is part of the model. It might represent:
- Euclidean distance;
- network distance;
- travel time;
- monetary travel cost;
- a generalised impedance measure.

Those are not interchangeable. A straight-line distance matrix can be a useful first exercise, but a real service-planning question may require a directed network, mode-specific speeds, turn restrictions, access constraints or time-dependent travel times.

## Exact small-instance baseline

The [Python implementation](../../implementations/python/p-median/README.md) enumerates every p-facility combination and assigns each demand point to its least-cost open facility. It returns the chosen candidate indices, objective and assignment.

This is an exact baseline for small instances. Its number of candidate sets is:

$$
\binom{|J|}{p}
$$

so it becomes impractical as the candidate set grows. Use it as a transparent teaching implementation and a correctness oracle for small test cases—not as a city-scale solver.

## What this model leaves out

The basic p-median model is uncapacitated. It does not limit how much demand a facility can serve, include opening costs, require a maximum service distance, model queues, represent uncertainty or optimise equity directly. p-center minimises the maximum service cost; maximal covering maximises demand within a service threshold. These are different objectives and should not be conflated.

## A practical workflow

1. Define demand units and candidate sites.
2. Decide how demand weights are measured and normalised.
3. Construct a cost matrix using the appropriate distance or routing model.
4. State whether assignments are directed and whether any candidates are infeasible.
5. Solve the location model.
6. Inspect assignments, underserved locations and sensitivity to demand and cost assumptions.
7. Validate the selected facilities against operational, land, capacity and equity constraints omitted from the simple model.

## Exercises

1. Solve the same instance for p=1, p=2 and p=3. How does the objective change?
2. Increase one demand weight. Does the chosen facility set change?
3. Replace Euclidean costs with a directed travel-time matrix. Why might the optimal sites move?
4. Add a maximum service distance. Explain why this changes feasibility and the model.
5. Compare p-median with p-center and maximal covering.

## References

- Hakimi, S. L. (1964), [Optimum locations of switching centers and the absolute centers and medians of a graph](https://doi.org/10.1287/opre.12.3.450), *Operations Research*, 12(3), 450–459.
- Hakimi, S. L. (1965), [Optimum distribution of switching centers in a communication network and some related graph theoretic problems](https://doi.org/10.1287/opre.13.3.462), *Operations Research*, 13(3), 462–475.
- Daskin, M. S. (2013), *Network and Discrete Location: Models, Algorithms, and Applications*, 2nd ed., Wiley.

**Scope:** uncapacitated p-median with a finite candidate set and an exhaustive exact teaching solver; not a general facility-location library.
