# Spatial decision support: make the criteria and trade-offs visible

Spatial decisions rarely depend on one measurement. Choosing a site, comparing service locations or identifying areas for conservation can involve access, cost, environmental conditions, risk, equity and legal constraints.

This path introduces methods for structuring those choices. It does not turn a decision into an objective truth: criteria, value functions, weights and constraints all reflect evidence and judgement.

## 1. Define the decision

Before choosing a method, identify:

- the decision objective and the alternatives being compared;
- the people and organisations affected;
- the criteria that influence preference;
- hard constraints that exclude alternatives;
- the data, spatial units, time period and scale;
- the evidence that could be used to evaluate the result.

Keep factors that contribute to preference separate from constraints that make an alternative ineligible.

## 2. Combine standardised spatial criteria

[Weighted linear combination](../methods/weighted-linear-combination.md)

Learn how standardised criterion scores are multiplied by relative weights and added to form a composite score. The lesson explains the compensatory assumption, the difference between factors and constraints, strict NoData handling, spatial alignment, sensitivity analysis and validation.

Run the [tested Python implementation](../implementations/python/weighted-overlay/README.md), follow its [intern walkthrough](../implementations/python/weighted-overlay/implementation-walkthrough.md), and experiment with the [interactive suitability lab](../notebooks/weighted-linear-combination-lab.ipynb).

## 3. Connect suitability to location and access

Two existing methods answer related but different questions:

- [p-median facility location](../algorithms/optimization/p-median.md) selects a fixed number of facilities to minimise weighted demand-to-facility cost under its stated model.
- [Two-Step Floating Catchment Area (2SFCA)](../algorithms/optimization/two-step-fca.md) estimates potential spatial accessibility by relating provider supply and population demand within catchments.

A suitability score, an optimal facility configuration and an accessibility measure are not interchangeable outputs. Choose the one that matches the decision question.

## 4. Practise and challenge the model

Complete the [spatial decision-support exercises](../exercises/spatial-decision-support.md). Change the value functions and weights, compare the resulting maps and write down which assumptions cause the ranking to change.

## What comes next

The next records should examine Boolean constraints and overlay, AHP as a structured weighting method, fuzzy membership, ordered weighted averaging, TOPSIS, ELECTRE and weights of evidence. Each needs its own assumptions and evidence. They should not be collapsed into one generic “suitability algorithm”.

**Status:** first WLC lesson, implementation and interactive lab are available. The wider decision-support path remains in progress.
