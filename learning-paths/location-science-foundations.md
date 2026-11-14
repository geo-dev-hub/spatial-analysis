# Location science: choosing where services should go

**Status:** Facility-location, accessibility and equity models now include a deterministic backup-coverage extension. The wider optimisation and mobility path is still being developed.

## The question

You have demand in different places and a set of candidate sites for a service. How many facilities should open, which candidates should be selected and how should demand be assigned?

The answer depends on the objective and constraints. p-median, p-center and maximal covering are not three names for the same problem.

## Before you begin

It helps to understand:
- a cost matrix;
- weighted sums and minimum values;
- combinations and binary decisions;
- the difference between distance, travel time and generalised cost.

## Follow the path

### 1. Define demand and candidate sites

Read [The p-median problem](../algorithms/optimization/p-median.md). Demand points and candidate facilities play different roles. Decide what the weights represent and how the cost matrix is constructed.

### 2. Solve a small exact instance

Run the [p-median lab](../notebooks/p-median-facility-location-lab.ipynb). Inspect the selected facilities, objective and assignment of every demand point.

### 3. Add a capacity constraint

Read [Capacitated p-median](../algorithms/optimization/capacitated-p-median.md) and run the [capacitated p-median lab](../notebooks/capacitated-p-median-lab.ipynb). Compare the unconstrained assignment with one that respects finite facility capacities. Keep demand quantities (capacity load) separate from demand weights (objective importance). This baseline assumes indivisible demand zones and deterministic scalar capacity; it is not a queueing model.

### 4. Change the objective

Read [Location set covering](../algorithms/optimization/set-covering.md) and run the [set-covering lab](../notebooks/set-covering-lab.ipynb) to find the minimum number of sites needed to reach every demand point. Then read [Maximal covering location](../algorithms/optimization/maximal-covering.md) and run the [MCLP visual lab](../notebooks/maximal-covering-lab.ipynb). It selects at most p sites to maximize weighted demand reached within a stated service threshold. Change the budget and threshold and inspect who remains uncovered. Compare with p-median, which minimizes total weighted assignment cost, and [discrete p-center](../algorithms/optimization/p-center.md), which minimizes the maximum assignment cost. Run the [p-center lab](../notebooks/p-center-lab.ipynb) and inspect which demand point determines the service radius. These models answer different planning questions.

### 5. Measure potential service accessibility

Read [Two-step floating catchment area](../algorithms/optimization/two-step-fca.md) and run the [2SFCA notebook](../notebooks/two-step-fca-accessibility-lab.ipynb). It compares provider supply with population demand in a travel catchment, then calculates an accessibility score for each population location. The notebook compares the binary baseline with a separately named E2SFCA-style distance-decay extension, applying analyst-supplied travel-time-band weights in both steps. Change the band edges and weights and inspect how provider ratios and population scores respond.

### 6. Inspect who receives accessibility

Read [Accessibility equity diagnostics](../algorithms/optimization/accessibility-equity.md) and run the [equity lab](../notebooks/accessibility-equity-lab.ipynb). Compare place-weighted and population-weighted distributions, inspect the Lorenz curve and Gini, report lower-tail quantiles, and calculate the share below an explicitly chosen minimum standard. Compare caller-defined groups without treating their averages as causal explanations. The threshold and group definitions are policy choices that must be justified.

### 7. Add minimum group-coverage requirements

Read [Equity-constrained maximal covering](../algorithms/optimization/equity-constrained-covering.md) and run its [interactive lab](../notebooks/equity-constrained-covering-lab.ipynb). Begin with zero group floors, then add minimum coverage shares and inspect which facility sets remain feasible, how total covered demand changes and how population weights differ from objective weights. The model does not decide which groups or floors are fair; justify them with affected communities and policy evidence.

### 8. Test service redundancy

Read [Backup coverage (r-covering)](../algorithms/optimization/backup-coverage.md) and run the [backup-coverage lab](../notebooks/backup-coverage-lab.ipynb). Compare the share of demand reached by at least one facility with the share reached by at least two distinct facilities. Inspect the per-demand counts and challenge the independence assumption: two nearby facilities may share a bridge, power source, hazard zone or staff pool. This deterministic model does not calculate outage probabilities or guarantee spare capacity.

### 9. Connect location to transport

A real cost matrix may require a directed road or transit network, mode restrictions, time-dependent travel times and access rules. Straight-line distance is only an initial approximation.

## Exercises

1. Solve the same instance for p=1, p=2 and p=3.
2. Increase one demand weight and inspect whether the facility choices change.
3. Replace Euclidean distance with a directed travel-time matrix.
4. Add a maximum service distance. Which assignments become infeasible?
5. Identify the remaining equity, land availability, operating and service-quality constraints that a real service plan needs.
6. Compare binary 2SFCA with a distance-decay catchment. Which assumptions change?
7. Compare population-weighted and unweighted accessibility distributions. Why can the Gini fall while the mean also falls?
8. Add minimum coverage floors to the maximal-covering model. Explain the effect on total covered demand and group outcomes.
9. Compare one-cover and two-cover demand. Explain why two eligible sites do not necessarily provide independent backup.

## What comes next

The wider source section also includes capacitated variants with split demand, hub location, districting, metaheuristics, assignment, vehicle routing, enhanced 2SFCA, traffic assignment, transit planning, trajectory analysis, GNSS and robotics. Each requires a distinct problem definition and validation strategy.
