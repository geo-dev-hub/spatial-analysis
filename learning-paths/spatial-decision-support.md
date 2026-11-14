# Spatial decision support: make the criteria and trade-offs visible

Spatial decisions rarely depend on one measurement. Choosing a site, comparing service locations or identifying areas for conservation can involve access, cost, environmental conditions, risk, equity and legal constraints.

This path introduces different ways to structure those choices. It does not turn a decision into objective truth: criteria, value functions, weights, thresholds and constraints all reflect evidence and judgement.

## 1. Define the decision

Before choosing a method, identify:

- the decision objective and whether you are comparing a finite set of alternatives or evaluating every cell in a continuous region;
- the people and organisations affected;
- the criteria that influence preference;
- hard constraints that exclude alternatives;
- the data, spatial units, time period and scale;
- the evidence that could be used to evaluate the result.

Keep factors that contribute to preference separate from constraints that make an alternative ineligible.

## 2. Decide how criteria should be combined

These methods are related, but they do different jobs:

- [Boolean and fuzzy overlay](../methods/boolean-and-fuzzy-overlay.md) distinguishes hard true/false conditions from graded membership and compares logical and fuzzy operators.
- [Weighted linear combination](../methods/weighted-linear-combination.md) combines standardised criterion scores using named criterion weights. It is compensatory.
- [Analytic Hierarchy Process](../methods/analytic-hierarchy-process.md) derives relative criterion priorities from pairwise judgements. It is a weighting method, not an overlay rule.
- [Ordered Weighted Averaging](../methods/ordered-weighted-averaging.md) attaches weights to rank positions after values are sorted at each location. In its GIS weighted form it can also retain named criterion weights.
- [TOPSIS](../methods/topsis.md) ranks a finite set of alternatives by distance from constructed positive and negative ideals.
- [ELECTRE](../methods/electre-outranking.md) uses concordance and discordance to establish pairwise outranking relations. It is a family of methods and the current record is a researched overview, not an implementation.

Read the assumptions before choosing. A hard exclusion, a graded membership, a compensatory score, an ideal-distance ranking and an outranking relation are not interchangeable.

## 3. Run the practical examples

Start with the [tested WLC Python implementation](../implementations/python/weighted-overlay/README.md) and its [intern walkthrough](../implementations/python/weighted-overlay/implementation-walkthrough.md). Experiment with the [interactive suitability lab](../notebooks/weighted-linear-combination-lab.ipynb).

The AHP, Boolean/fuzzy, OWA and TOPSIS packages each include tested numerical baselines and step-by-step walkthroughs. Their input contracts deliberately do not pretend to align GIS rasters or validate stakeholder judgements.

## 4. Connect suitability to location and access

Two existing methods answer related but different questions:

- [p-median facility location](../algorithms/optimization/p-median.md) selects a fixed number of facilities to minimise weighted demand-to-facility cost under its stated model.
- [Two-Step Floating Catchment Area (2SFCA)](../algorithms/optimization/two-step-fca.md) estimates potential spatial accessibility by relating provider supply and population demand within catchments.

A suitability score, an optimal facility configuration and an accessibility measure are not interchangeable outputs. Choose the one that matches the decision question.

## 5. Practise and challenge the model

Complete the [spatial decision-support exercises](../exercises/spatial-decision-support.md). Compare the same hypothetical decision under Boolean constraints, WLC, fuzzy overlay and OWA. Then compare a finite set of candidate sites using TOPSIS. Identify where ELECTRE's non-compensatory outranking perspective might be more appropriate.

## What remains open

Weights of evidence, a specific tested ELECTRE variant, broader uncertainty and group-decision methods, and evidence-backed domain case studies remain future work. The source section also includes many environmental, ecological, climate, health, urban, energy and marine models; this path is not a claim that those domains have been covered.

**Status:** five decision-support methods have researched records and tested numerical packages (WLC, AHP, Boolean/fuzzy overlay, OWA and TOPSIS). ELECTRE has a researched method-family overview only. The broader Section 7 path remains in progress.
