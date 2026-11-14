# Boolean and fuzzy overlay: constraints versus graded membership

Boolean and fuzzy overlays both combine spatial criteria, but they answer different questions.

- **Boolean overlay** asks whether each condition is satisfied. Each input is a true/false mask; intersection, union and difference produce hard inclusion rules.
- **Fuzzy overlay** represents degree of membership in a defined concept, usually on [0,1]. Operators combine graded memberships, but the membership functions and operator choice remain modelling decisions.

Neither approach automatically identifies the right criteria, calibrates thresholds or establishes that the resulting map is a probability.

## Boolean overlay

For Boolean masks B_1,...,B_k:

\[
B_{AND}=\bigwedge_i B_i,\qquad B_{OR}=\bigvee_i B_i.
\]

AND is appropriate when every constraint must be met. OR is appropriate when satisfying any one alternative is sufficient. A hard exclusion should not be converted into a soft factor merely to make the map look less restrictive.

Boolean rules are transparent, but threshold choices can create abrupt boundaries. Document units, inclusivity at the threshold, and the treatment of unknown or missing values.

## Fuzzy membership

A membership function maps a measured criterion x to a degree mu(x) in [0,1]. For a monotonically increasing benefit criterion, a simple linear ramp between a and b is:

\[
\mu(x)=\begin{cases}
0 & x\leq a,\\
(x-a)/(b-a) & a<x<b,\\
1 & x\geq b.
\end{cases}
\]

For a cost criterion the direction is reversed. More complex curves may be appropriate, but their parameters need domain justification. A membership of 0.8 means strong membership under the chosen function; it is not an 80% chance that a location is suitable.

## Common fuzzy operators

For memberships mu_i:

- Fuzzy AND (minimum): min_i(mu_i), conservative and controlled by the weakest criterion.
- Fuzzy AND (product): product_i(mu_i), increasingly restrictive as criteria accumulate.
- Fuzzy OR (maximum): max_i(mu_i), controlled by the strongest criterion.
- Probabilistic sum: 1 - product_i(1-mu_i), an alternative graded OR.

The fuzzy gamma combination interpolates between fuzzy product and fuzzy sum:

\[
\mu_\gamma = (\mu_{sum})^\gamma(\mu_{product})^{1-\gamma},\quad 0\leq\gamma\leq1.
\]

At gamma=0 it is the fuzzy product; at gamma=1 it is the probabilistic sum. Intermediate values balance the two behaviours. This parameter is not learned automatically and should be explored through sensitivity analysis.

## Spatial workflow

1. Define the concept being mapped and the spatial unit.
2. Separate hard constraints from graded factors.
3. Choose and justify membership functions for each factor; record breakpoints and direction.
4. Align all layers to a common grid and coordinate reference system before combining them.
5. State how NoData propagates. This teaching implementation uses a strict common-footprint rule.
6. Compare more than one operator and gamma value.
7. Check whether the spatial pattern is stable under plausible thresholds and membership curves.
8. Validate against independent observations or expert review where possible.
9. Publish the membership curves, operator, parameters, constraints and data provenance.

## A useful comparison

| Question | Boolean overlay | Fuzzy overlay | WLC |
|---|---|---|---|
| Input meaning | Condition met / not met | Degree of membership | Standardised preference score |
| Main combination | AND / OR / NOT | Min, product, max, sum, gamma | Weighted sum |
| Compensation | No | Depends on operator | Yes |
| Key judgement | Thresholds and logical rule | Membership curve and operator | Weights and standardisation |
| Output | Boolean eligibility | Graded membership | Composite score |

Do not compare output numbers as though they share the same meaning. A fuzzy membership of 0.7 is not equivalent to a WLC score of 0.7.

## Implementation

The companion NumPy package provides Boolean AND/OR, fuzzy minimum/product/maximum/probabilistic-sum and gamma combination for aligned 2D arrays. It is a small numerical baseline, not a raster alignment or GIS I/O system.

- [Python implementation and tests](../implementations/python/fuzzy-overlay/README.md)
- [Intern walkthrough](../implementations/python/fuzzy-overlay/implementation-walkthrough.md)
- [Weighted linear combination](weighted-linear-combination.md)
- [Analytic Hierarchy Process](analytic-hierarchy-process.md)

## References

- Eastman, J. R. (1999). Multi-criteria evaluation and GIS. In *Geographical Information Systems*, 2nd ed. (foundational GIS-MCE discussion; consult the full publication for context).
- Malczewski, J. (2000). On the Use of Weighted Linear Combination Method in GIS: Common and Best Practice Approaches. Transactions in GIS, 4(1), 5–22.
- Malczewski, J. (2006). GIS-based multicriteria decision analysis: a survey of the literature. International Journal of Geographical Information Science, 20(7), 703–726.

This lesson introduces operator families. Real decisions require defensible membership functions, stakeholder involvement and independent validation.
