# Exercise: expected coverage when units are busy

Read the [MEXCLP lesson](../algorithms/optimization/mexclp.md), then run the [MEXCLP lab](../notebooks/mexclp-lab.ipynb).

## 1. Calculate before running code

A demand area has weight 120. One unit can reach it, and that unit is busy with probability 0.25. Calculate its expected coverage contribution.

Now suppose two eligible units have independent busy states with the same busy probability. Calculate the new contribution. How much did the second unit add?

## 2. Compare placement choices

Use three demand areas with weights 100, 80 and 60, and three candidate sites. Construct a cost matrix in which one candidate reaches all three areas, while two other candidates reach different pairs.

Place two units. Does the best solution put both units at one site or spread them out? Explain the trade-off.

## 3. Change the busy fraction

Run the same instance with q = 0, 0.25, 0.5 and 0.8. Record the selected placements and expected coverage. Does the ranking of placements change?

## 4. Compare three models

Use identical demand, candidates and threshold to compare:
- deterministic maximal covering;
- deterministic two-cover backup coverage;
- MEXCLP expected coverage.

Explain why their objective values are not directly interchangeable.

## 5. Challenge the assumptions

Describe an emergency-service system where unit availability is correlated. Could a shared hospital handover queue, a major road closure or a common incident violate independence? What data would be needed to estimate local busy fractions?

## Check your work

For k eligible units, the availability probability under the MEXCLP assumptions is 1 - q^k. With q = 0.25, one unit gives 0.75 availability and two independent units give 0.9375. The implementation returns one candidate index per unit; repeated indices mean more than one unit at the same site.
