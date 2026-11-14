# Weighted linear combination: combine spatial criteria transparently

A site can be close to a road but exposed to flooding. A conservation area may have high ecological value but be difficult to access. A planning decision often depends on several criteria at once.

A **weighted linear combination (WLC)** turns a set of standardised criterion scores into one composite score. In GIS, each criterion is usually represented by a raster layer or by values attached to candidate locations. The method is widely used in suitability analysis and spatial decision support.

It is simple to calculate. The difficult work is deciding what the criteria mean, how they are measured, how they are standardised, whose preferences the weights represent and how sensitive the result is to those choices.

## 1. Define the decision before combining layers

Write down the decision question in a form that can be examined:

- What is the objective?
- What are the alternatives: raster cells, parcels, candidate sites or administrative units?
- Which criteria influence preference?
- Which constraints exclude an alternative altogether?
- Who is affected by the decision, and who has a say in setting preferences?
- What evidence could be used to evaluate the result?

A **factor** contributes to the degree of preference. A **constraint** makes an alternative ineligible. Keep these roles separate.

For example, distance to a road might be a factor if access is desirable. A legally protected area might be a constraint if development is prohibited there. A high constraint score must not accidentally compensate for a legal exclusion.

## 2. Standardise criteria before adding them

Criteria often use incompatible units: metres, degrees, travel minutes, cost, population counts or qualitative classes. Adding their raw values has no coherent interpretation.

Transform each factor into a common preference scale. A simple scale is:

[
x_i(a) in [0,1]
]

where 0 means least preferred and 1 means most preferred for criterion (i) and alternative (a).

A linear benefit transformation for a raw value (r) is:

[
x(r)=rac{r-r_{min}}{r_{max}-r_{min}}
]

A linear cost transformation, where smaller raw values are preferred, is:

[
x(r)=rac{r_{max}-r}{r_{max}-r_{min}}
]

These formulas are examples, not universal suitability functions. A threshold, target range, distance-decay curve, fuzzy membership function or expert-defined value function may be more appropriate.

If (r_{max}=r_{min}), the linear transformation is undefined. Decide explicitly whether the criterion is uninformative, should be assigned a constant score or should be removed. Do not silently divide by zero.

Standardisation is a substantive modelling choice. It determines how differences in the original measurements become differences in preference.

## 3. Assign criterion weights

Let (w_i) be the relative importance assigned to criterion (i). For the usual WLC form, weights are non-negative and normalised to sum to one:

[
w_i geq 0,qquad sum_{i=1}^{m}w_i=1
]

Weights can come from a structured stakeholder process, expert judgement or a separate weighting method such as the Analytic Hierarchy Process (AHP). WLC is the **aggregation rule**; AHP is one possible way to elicit or derive weights. They are not the same method.

A weight is not a measure of data quality, causal influence or statistical significance. It expresses a preference or modelling judgement within the defined decision problem.

## 4. Calculate the composite score

For alternative (a), the weighted linear combination is:

[
S(a)=sum_{i=1}^{m}w_i x_i(a)
]

The calculation multiplies each standardised factor by its weight and adds the weighted scores.

Consider three factors for a hypothetical site:

| Factor | Standardised score | Weight | Contribution |
|---|---:|---:|---:|
| Road accessibility | 0.80 | 0.50 | 0.40 |
| Terrain suitability | 0.60 | 0.30 | 0.18 |
| Low flood exposure | 0.90 | 0.20 | 0.18 |
| **Total** | | **1.00** | **0.76** |

The composite score is:

[
S=0.50(0.80)+0.30(0.60)+0.20(0.90)=0.76
]

This is a relative model score under the stated criteria and weights. It is not a 76% probability that the site is suitable.

## 5. Apply constraints explicitly

A Boolean constraint (c_j(a)) is either 0 (excluded) or 1 (eligible). A common formulation is:

[
S_c(a)=S(a)prod_{j=1}^{q}c_j(a)
]

Equivalently, an implementation can mask excluded alternatives and mark their score as NoData. The teaching implementation in this repository uses a Boolean eligibility mask.

Do not replace a hard legal, safety or ecological exclusion with a low factor score unless the decision rules genuinely allow that trade-off.

## 6. Understand the compensation assumption

WLC is a **compensatory** decision rule. A high score on one factor can offset a low score on another.

That may be reasonable when the decision maker accepts trade-offs. It may be inappropriate when one criterion has a minimum acceptable threshold, when a constraint must never be traded away, or when a worst-case criterion should dominate.

Compare the decision rule with its alternatives:

| Rule | What it does | Important distinction |
|---|---|---|
| Boolean overlay | Combines eligible/ineligible conditions | Non-compensatory; a failed required condition can exclude a location |
| WLC | Adds weighted standardised factor scores | Compensatory; one factor can offset another |
| Ordered weighted averaging (OWA) | Adds order weights to the aggregation process | Can express different risk/compensation attitudes |
| Fuzzy overlay | Combines fuzzy membership values under a chosen operator | Membership and aggregation semantics must be stated |
| AHP | Structures pairwise preference judgements and can derive weights | A weighting/priority method, not the WLC aggregation itself |
| TOPSIS / ELECTRE | Rank or compare alternatives using different multi-criteria logic | Not interchangeable with a simple weighted sum |

## 7. A spatial analysis needs a spatial data contract

When criteria are raster layers, verify that they describe the same analysis grid:

- same coordinate reference system and coordinate units;
- same grid origin, resolution, dimensions and extent;
- appropriate resampling for each variable;
- documented NoData and mask semantics;
- consistent direction of preference after standardisation.

Resampling a categorical constraint with bilinear interpolation, for example, can create values that have no valid Boolean meaning. Use a method appropriate to the data type.

The example implementation requires all criterion arrays to have the same two-dimensional shape. A cell is scored only when every criterion is finite and the optional eligibility mask allows it. This strict common-footprint policy avoids silently changing the denominator or the relative influence of criteria from cell to cell.

## 8. Test sensitivity, not just arithmetic

The arithmetic can be correct while the decision model is fragile.

At minimum, examine:

1. **Weight sensitivity:** vary one weight at a time, renormalising the others, and observe changes in score and ranking.
2. **Standardisation sensitivity:** compare plausible linear and nonlinear value functions.
3. **Criterion sensitivity:** remove or replace a criterion and inspect the effect.
4. **Constraint sensitivity:** document how the eligible area changes under alternative defensible rules.
5. **Classification sensitivity:** if scores are grouped into classes, compare more than one classification scheme.
6. **Spatial sensitivity:** inspect whether results are stable across reasonable grid resolutions or spatial units.

A sensitivity analysis is not an optional decoration. It helps show which assumptions drive the result and where a decision is unstable.

## 9. Validate the decision model

There is no universal ground-truth layer for suitability. Validation depends on the decision question.

Possible checks include:

- compare predicted high-suitability areas with independently observed successful sites;
- ask domain experts and affected stakeholders to review the criteria and trade-offs;
- compare alternative weighting and standardisation scenarios;
- inspect known unsuitable locations and explain why they receive their scores;
- report disagreement and uncertainty rather than hiding it in a single composite map.

Do not present a suitability surface as an objective map of truth. It is a structured expression of evidence, preferences and constraints.

## Runnable material

- [Python implementation](../implementations/python/weighted-overlay/README.md)
- [Step-by-step implementation walkthrough](../implementations/python/weighted-overlay/implementation-walkthrough.md)
- [Interactive suitability lab](../notebooks/weighted-linear-combination-lab.ipynb)
- [Spatial decision-support learning path](../learning-paths/spatial-decision-support.md)

The code is intentionally a small aggregation baseline. It does not select criteria, standardise raw measurements, derive weights, validate a real-world decision or replace a stakeholder process.

## References

1. Malczewski, J. (2000). “On the Use of Weighted Linear Combination Method in GIS: Common and Best Practice Approaches.” *Transactions in GIS*, 4(1), 5–22. [Author-hosted paper](https://www.yorku.ca/gis/es7189/docs/malczewski00.pdf). This review is especially useful for understanding the assumptions and frequent misapplications of WLC.
2. Malczewski, J. (2006). “GIS-based multicriteria decision analysis: a survey of the literature.” *International Journal of Geographical Information Science*, 20(7), 703–726. [DOI: 10.1080/13658810600661508](https://doi.org/10.1080/13658810600661508).
3. Malczewski, J. and Rinner, C. (2015). *Multicriteria Decision Analysis in Geographic Information Science*. Springer. [DOI: 10.1007/978-3-540-74757-4](https://doi.org/10.1007/978-3-540-74757-4).
4. Malczewski, J. (2011). “Local Weighted Linear Combination.” *Transactions in GIS*, 15(4), 439–455. [DOI: 10.1111/j.1467-9671.2011.01275.x](https://doi.org/10.1111/j.1467-9671.2011.01275.x).

**Scope:** this is a researched introduction to global WLC and a tested numerical aggregation baseline. It does not claim to implement AHP, OWA, fuzzy overlay, TOPSIS, ELECTRE or local WLC.
