# Maximum expected covering: account for busy facilities

Stable ID: SA-OPT-MEXCLP · Draft 0.1 · Location-science extension

## The planning question

A demand area may have several facilities within the response-time standard, yet every nearby unit can be busy when a new request arrives. Maximum expected covering (MEXCLP) estimates the share of demand that can be reached by at least one available unit, using a simplified busy-probability model.

It is different from deterministic maximal covering and deterministic backup coverage: those count nearby selected facilities, while MEXCLP discounts the chance that those facilities are unavailable.

## Model

Let i index demand locations and j candidate sites. Let a_i be non-negative demand weight, d_ij the travel impedance, S the service threshold, p the number of units to deploy, and q the common probability that any one unit is busy.

Let k_i be the number of deployed units at sites within the threshold of demand i. Under the model's independence and equal-busy-probability assumptions, the probability that all k_i covering units are busy is q raised to k_i. Therefore the probability that at least one is available is:

\[
P(\text{available for }i)=1-q^{k_i}.
\]

The objective is:

\[
\max \sum_{i\in I} a_i(1-q^{k_i}).
\]

The teaching solver treats p as an exact number of units. It permits multiple units at the same candidate site, matching a common MEXCLP modelling feature. The site list returned by the solver can therefore contain repeated candidate indices.

## A small worked example

Suppose a demand area has weight 100 and two units can reach it. If each unit is busy with probability q = 0.3 and their states are independent, then:

\[
P(\text{at least one available})=1-0.3^2=0.91.
\]

Its expected covered demand contribution is 100 × 0.91 = 91. With only one covering unit, the contribution is 100 × 0.7 = 70. A second nearby unit adds expected coverage, but not another full 100 units.

## Exact teaching implementation

The [Python package](../../implementations/python/mexclp/README.md) enumerates all multisets of p unit placements over m candidate sites. The number of placements is:

\[
\binom{m+p-1}{p}
\]

for p greater than zero. This is an exact small-instance reference, not a metropolitan-scale optimisation method. The solver maximises expected covered demand and uses lexicographic candidate-index order to break ties.

## Assumptions and limits

- Every unit has the same busy probability q.
- Unit busy states are treated as independent.
- Busy probability does not vary by location, time of day, unit or demand area.
- The input cost matrix and threshold determine which units can reach each demand location.
- Multiple units may be placed at one candidate site; no station-capacity limit is enforced.
- The model estimates expected coverage at an instant. It does not model queued calls, dispatch priorities, travel-time uncertainty, correlated outages, staffing constraints or the full spatial interaction among emergency units.
- The busy fraction must be estimated from an appropriate operational period and workload definition. It should not be selected merely to improve the result.

MEXCLP is not a queueing model. An M/M/c queue estimates waiting in a shared service system under different assumptions; the hypercube queueing model represents spatially differentiated emergency-service systems in more detail.

## How to use it responsibly

1. Define the demand unit, time period and service threshold.
2. Build a cost matrix from an appropriate network or travel model.
3. Estimate the busy fraction from observed workload and unit availability.
4. State why equal busy probabilities and independence are defensible approximations—or explicitly label them as scenarios.
5. Compare deterministic MCLP, r-covering and MEXCLP using the same demand, candidate sites and threshold.
6. Test several plausible busy fractions and report how selected locations and expected coverage change.
7. Validate any operational deployment with richer dispatch, capacity and reliability models.

## References

- Daskin, M. S. (1983), “A maximum expected covering location model: Formulation, properties and heuristic solution,” Transportation Science, 17(1), 48–70. https://doi.org/10.1287/trsc.17.1.48
- Batta, R., Dolan, J. M. and Krishnamurthy, N. (1989), “The maximal expected covering location problem: Revisited,” Transportation Science, 23(4), 277–287. https://doi.org/10.1287/trsc.23.4.277
- Daskin, M. S. (2013), Network and Discrete Location: Models, Algorithms, and Applications, 2nd ed., Wiley.

**Scope:** exact enumeration for small finite candidate sets, fixed p, one common service threshold, one common busy fraction and independent unit availability. It is a transparent MEXCLP teaching baseline, not a reproduction of the adjusted MEXCLP or hypercube queueing models.
