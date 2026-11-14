# Exercise: put a minimum coverage floor into a location plan

**Level:** Intermediate · **Time:** 45–60 minutes

## Scenario

Four demand zones belong to two groups. Three candidate facilities are available. Travel costs are:

| Demand | Group | Site 0 | Site 1 | Site 2 |
|---|---|---:|---:|---:|
| A1 | A | 1 | 9 | 8 |
| A2 | A | 1 | 8 | 9 |
| B1 | B | 9 | 1 | 8 |
| B2 | B | 9 | 1 | 8 |

The service threshold is 2 and the budget is one facility.

## Tasks

1. Solve ordinary maximal covering with no group floors. Which group receives coverage?
2. Add a 50% minimum coverage floor for both groups. Is one facility sufficient?
3. Increase the budget to two facilities. Which sites are selected?
4. Increase group B's floor to 100%. Does the solution change?
5. Assign unequal population weights to the zones. Recalculate the group coverage shares.
6. Keep population weights fixed but change objective weights. Explain why the selected plan can change without changing the coverage constraints.
7. Compare the total covered objective with group-specific coverage rates for every scenario.

## Reflection

- Who selected the groups and the coverage floors?
- Could one group contain people with very different needs?
- Is binary coverage within two minutes an adequate representation of access?
- What happens if travel costs are uncertain or service capacity is limited?

Use the [implementation walkthrough](../implementations/python/equity-covering/implementation-walkthrough.md) and [notebook lab](../notebooks/equity-constrained-covering-lab.ipynb) to extend the analysis.
