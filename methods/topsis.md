# TOPSIS: ranking alternatives by distance from ideal and anti-ideal solutions

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) ranks a finite set of alternatives. It asks which alternative is simultaneously close to a constructed positive ideal and far from a constructed negative ideal.

This is not a raster overlay operator. It is most natural when the alternatives are explicit objects—candidate sites, projects, plans or service configurations—and each has a measured performance on several criteria.

## Decision matrix

Let X contain m alternatives and n criteria. Each row is an alternative and each column is a criterion. Criteria may be benefits (larger is better) or costs (smaller is better).

A common classical procedure uses vector normalisation:

\[
r_{ij}=\frac{x_{ij}}{\sqrt{\sum_{i=1}^{m}x_{ij}^{2}}},\qquad
v_{ij}=w_jr_{ij},\qquad \sum_jw_j=1.
\]

The positive ideal takes the best weighted value for each criterion; the negative ideal takes the worst:

\[
v_j^+=\begin{cases}\max_i v_{ij}&\text{benefit}\\\min_i v_{ij}&\text{cost}\end{cases},
\quad
v_j^-=\begin{cases}\min_i v_{ij}&\text{benefit}\\\max_i v_{ij}&\text{cost}\end{cases}.
\]

Then calculate Euclidean separation:

\[
D_i^+=\sqrt{\sum_j(v_{ij}-v_j^+)^2},\qquad
D_i^-=\sqrt{\sum_j(v_{ij}-v_j^-)^2}.
\]

Relative closeness is:

\[
C_i=\frac{D_i^-}{D_i^++D_i^-}.
\]

Higher values indicate alternatives closer to the positive ideal and farther from the negative ideal. If an alternative coincides with both ideals because all alternatives are identical, the ratio is undefined; the companion code returns a neutral 0.5 for that degenerate case and flags neither separation as meaningful.

## Practical cautions

- Normalisation choices matter. Vector normalisation is a common classical choice, not a universal requirement.
- The ideal and anti-ideal are constructed from the alternatives being compared. Adding or removing alternatives can change them and therefore change rankings.
- TOPSIS is compensatory: a strong criterion can offset a weak one.
- Criteria weights require their own justification. AHP may be one way to derive them, but it is not the only one.
- Correlated or duplicated criteria can effectively count the same concept more than once.
- The ranking is relative to the chosen alternatives, criteria, weights, normalisation and distance metric. It is not an absolute suitability probability.

## Spatial decision workflow

1. Define a finite and defensible set of candidate alternatives.
2. Measure each candidate against the same criteria and time frame.
3. Convert cost criteria and benefit criteria into the correct ideal directions; retain original units in the data dictionary.
4. Choose and disclose a normalisation method.
5. Derive and disclose criterion weights.
6. Calculate ideals, separations and closeness coefficients.
7. Inspect the best and worst alternatives on each criterion; explain why trade-offs produced the final ranking.
8. Run sensitivity analysis over weights, normalisation and candidate sets.
9. Validate the ranking with independent evidence and stakeholder review.

## Implementation

The companion NumPy implementation uses vector normalisation and Euclidean distance for a small finite decision matrix. It is a transparent baseline, not a universal TOPSIS specification or a spatial raster engine.

- [Python implementation and tests](../implementations/python/topsis/README.md)
- [Intern walkthrough](../implementations/python/topsis/implementation-walkthrough.md)
- [AHP weighting](analytic-hierarchy-process.md)
- [OWA aggregation](ordered-weighted-averaging.md)

## References

- Hwang, C.-L. & Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer.
- Opricović, S. & Tzeng, G.-H. (2004). Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS. European Journal of Operational Research, 156(2), 445–455.
- Behzadian, M. et al. (2012). A state-of the-art survey of TOPSIS applications. Expert Systems with Applications, 39(17), 13051–13069.

This lesson covers a classical TOPSIS variant. Different normalisation and distance conventions must be named when used.
