# Location science: choosing where services should go

**Status:** First facility-location model published; the wider optimisation and mobility path is still being developed.

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

### 3. Change the objective

Compare p-median with p-center, which minimises the maximum assignment cost, and maximal covering, which maximises demand served within a threshold. These models answer different planning questions.

### 4. Measure potential service accessibility

Read [Two-step floating catchment area](../algorithms/optimization/two-step-fca.md) and run the [2SFCA notebook](../notebooks/two-step-fca-accessibility-lab.ipynb). It compares provider supply with population demand in a travel catchment, then calculates an accessibility score for each population location. The baseline uses a binary catchment; distance-decay variants remain a separate extension.

### 5. Connect location to transport

A real cost matrix may require a directed road or transit network, mode restrictions, time-dependent travel times and access rules. Straight-line distance is only an initial approximation.

## Exercises

1. Solve the same instance for p=1, p=2 and p=3.
2. Increase one demand weight and inspect whether the facility choices change.
3. Replace Euclidean distance with a directed travel-time matrix.
4. Add a maximum service distance. Which assignments become infeasible?
5. Identify the capacity, equity, land availability and operating constraints that a real service plan needs.
6. Compare binary 2SFCA with a distance-decay catchment. Which assumptions change?

## What comes next

The wider source section includes p-center, maximal covering, capacitated and hub location, districting, metaheuristics, assignment, vehicle routing, enhanced 2SFCA, traffic assignment, transit planning, trajectory analysis, GNSS and robotics. Each requires a distinct problem definition and validation strategy.
