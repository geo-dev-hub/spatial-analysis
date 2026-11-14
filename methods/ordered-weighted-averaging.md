# Ordered Weighted Averaging (OWA) for spatial decision support

Ordered Weighted Averaging is an aggregation family in which weights attach to the rank position of a value after sorting, rather than permanently attaching only to a named criterion.

This distinction matters in GIS. **Criterion weights** express the relative importance of named factors. **Order weights** express how the decision rule treats the best, second-best, and lower-ranked criterion values at each location. They are not interchangeable.

## Standard OWA

At a location, sort the standardised criterion values in descending order:

\[
z_{i1}\geq z_{i2}\geq\dots\geq z_{in}.
\]

Then apply order weights \(\lambda_k\), constrained by \(0\leq\lambda_k\leq1\) and \(\sum_k\lambda_k=1\):

\[
OWA_i=\sum_{k=1}^{n}\lambda_k z_{ik}.
\]

The largest value always receives the first order weight, regardless of which criterion produced it.

## GIS weighted OWA

GIS-MCDA formulations can also retain named criterion importance weights \(w_j\). At each location, reorder those weights to follow the same sorted criterion values. If \(u_{ik}\) is the criterion weight that belongs to the criterion occupying sorted position k, a normalised weighted OWA form is:

\[
OWA_i=\frac{\sum_{k=1}^{n}\lambda_k u_{ik}z_{ik}}
{\sum_{k=1}^{n}\lambda_k u_{ik}}.
\]

The denominator is important: the product of order and criterion weights generally does not sum to one after reordering.

## What the order weights do

For descending sorted inputs:

- \(\lambda=(1,0,\ldots,0)\) selects the maximum: an OR-like, optimistic rule.
- \(\lambda=(0,\ldots,0,1)\) selects the minimum: an AND-like, conservative rule.
- Equal order weights yield an arithmetic average. In the weighted GIS form this reduces to WLC when the same named criterion weights are used.
- Intermediate order weights represent intermediate aggregation strategies.

One summary of the order vector is ORness:

\[
ORness(\lambda)=\frac{1}{n-1}\sum_{k=1}^{n}(n-k)\lambda_k.
\]

With one-based k, ORness is 1 for the maximum operator, 0 for the minimum operator and 0.5 for equal order weights. ORness describes the operator's position between these extremes; it is not a measure of model accuracy or real-world risk.

## Spatial workflow

1. Standardise every criterion so that larger values consistently mean more preferred.
2. Align grids, extents, resolution, coordinate reference systems and NoData semantics.
3. Elicit named criterion weights if using the GIS weighted form.
4. Choose order weights and explain the implied optimism/conservatism.
5. Apply the operator cell by cell, preserving which criterion generated each sorted value.
6. Compare maps across order-weight scenarios and test rank stability.
7. Keep hard constraints outside the compensatory aggregation.
8. Publish both weight vectors, the sorting convention, the denominator, and the sensitivity results.

## Do not confuse the weight systems

AHP can be used to derive the named criterion weights. It does not derive the OWA order weights automatically. OWA order weights are part of the aggregation strategy and need their own justification.

OWA is not the same as TOPSIS or ELECTRE. Those methods rank alternatives using different distance-to-ideal or outranking concepts; they should not be described as simple raster overlay operators.

## Implementation

The companion implementation supports standard OWA and the GIS weighted form for aligned 2D arrays, strict common-footprint NoData handling, and an ORness diagnostic.

- [Python implementation and tests](../implementations/python/owa/README.md)
- [Intern walkthrough](../implementations/python/owa/implementation-walkthrough.md)
- [AHP weighting](analytic-hierarchy-process.md)
- [Weighted linear combination](weighted-linear-combination.md)

## References

- Yager, R. R. (1988). On ordered weighted averaging aggregation operators in multicriteria decisionmaking. IEEE Transactions on Systems, Man, and Cybernetics, 18(1), 183–190.
- Malczewski, J. (2006). Integrating multicriteria analysis and geographic information systems: the ordered weighted averaging (OWA) approach. International Journal of Environmental Technology and Management, 6(1/2), 7–19. https://doi.org/10.1504/IJETM.2006.008251
- Malczewski, J. & Liu, X. (2014). Local ordered weighted averaging in GIS-based multicriteria analysis. Annals of GIS, 20(2), 117–129. https://doi.org/10.1080/19475683.2014.904439
