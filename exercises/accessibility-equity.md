# Exercise: who benefits from accessibility?

**Level:** Intermediate · **Time:** 45–60 minutes

## Scenario

A city has four synthetic neighbourhoods. Scores are outputs from a hypothetical accessibility model.

| Neighbourhood | Accessibility | Population |
|---|---:|---:|
| A | 2 | 100 |
| B | 4 | 300 |
| C | 8 | 200 |
| D | 10 | 100 |

These invented values are for learning only.

## Tasks

1. Calculate the unweighted mean and population-weighted mean. Which population does each represent?
2. Calculate unweighted and population-weighted Gini coefficients.
3. Plot both Lorenz curves. Why do they differ?
4. If the policy minimum is 5, calculate the population share below it.
5. Put A and B in one group and C and D in another. Compare weighted means and lower-tail quantiles.
6. Increase A's score from 2 to 4. Which statistics change most?
7. Construct a scenario where Gini falls but the weighted mean also falls. Explain why lower Gini alone is not evidence of a better policy.
8. List five assumptions to validate before using real accessibility data.

## Reflection

- Who chose the minimum standard and why?
- Could neighbourhood averages conceal variation within each area?
- Does the score account for affordability, disability access, safety, opening hours and service quality?
- What would you discuss with affected communities before interpreting the results?

Use the [implementation walkthrough](../implementations/python/accessibility-equity/implementation-walkthrough.md) and [notebook lab](../notebooks/accessibility-equity-lab.ipynb) for the extension.
