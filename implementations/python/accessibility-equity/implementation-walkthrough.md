# Intern walkthrough: accessibility distribution diagnostics

This analysis starts with accessibility scores that have already been calculated. It does not calculate routes or choose facilities.

1. **Inspect the inputs.** Open equity_diagnostics.py. It accepts finite, non-negative accessibility values and optional population weights. Invalid values, mismatched lengths and zero total weight are rejected.
2. **Choose the estimand.** Population weights answer a person-weighted question. Omitting weights treats every row equally and answers a place-weighted question. These are not interchangeable.
3. **Calculate the mean.** Each value contributes in proportion to its weight. A zone with 10,000 residents contributes more than one with 100 residents to a population-wide estimate.
4. **Build the Lorenz curve.** Sort observations by access, then accumulate population weight and weighted access. The curve begins at (0, 0). Its trapezoid area gives the Gini coefficient.
5. **Inspect the lower tail.** p10 and median describe low-access portions of the population. The optional threshold shortfall reports the weighted share below a stated standard. The standard is a policy choice, not a neutral technical constant.
6. **Compare groups.** Caller-supplied labels are summarised separately. Compare the group means and then inspect within-group distributions; group averages can hide unequal outcomes.
7. **Run tests.** Install requirements and run python -m pytest -q. Tests cover equality, inequality, weighted replication, zero access, Lorenz endpoints, quantiles, threshold shortfall and invalid inputs.
8. **Reproduce and challenge.** Preserve original units, repeat the analysis with alternative weights and thresholds, and record which choices are empirical versus normative.

This code does not estimate accessibility, create demographic groups, make causal claims, test significance, account for spatial dependence or optimise a facility plan.
