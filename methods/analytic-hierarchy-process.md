# Analytic Hierarchy Process (AHP): deriving criterion weights

AHP is a structured way to elicit and organise relative judgements. In GIS multi-criteria work it is often used to derive criterion weights before a separate decision rule—such as weighted linear combination—combines standardised criterion scores.

**Keep these jobs separate:** AHP derives priorities from pairwise judgements. It does not standardise rasters, define hard exclusions, choose an aggregation rule or prove that the criteria represent the decision well.

## Pairwise comparison matrix

For n criteria, construct a positive reciprocal matrix A:

\[
A=[a_{ij}],\quad a_{ii}=1,\quad a_{ji}=1/a_{ij}.
\]

The entry a_ij expresses the judged relative importance of criterion i over criterion j. Saaty's commonly used fundamental scale runs from 1 (equal importance) through 9 (extreme importance), with reciprocals for the opposite direction. This is a structured elicitation convention, not a measurement instrument that removes judgement.

The priority vector is commonly estimated as the principal right eigenvector:

\[
Aw=\lambda_{\max}w,\qquad \sum_iw_i=1,\qquad w_i>0.
\]

Weights express relative priorities; they do not establish causal importance or universal preference.

## Consistency diagnostic

Perfectly consistent judgements satisfy a_ik = a_ij a_jk, giving lambda_max = n. A conventional diagnostic is:

\[
CI=\frac{\lambda_{\max}-n}{n-1},\qquad CR=\frac{CI}{RI_n}.
\]

RI_n is a reference average consistency index for random reciprocal matrices of order n.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RI | 0 | 0 | 0.58 | 0.90 | 1.12 | 1.24 | 1.32 | 1.41 | 1.45 | 1.49 |

For n=1 or n=2, CR is not meaningfully available under this reference table. A CR near or below 0.10 is often used as a prompt for review, not a universal pass/fail law. Consistency is not validity: consistent judgements can still encode weak evidence, omitted criteria or stakeholder bias.

## GIS workflow

1. Define one decision question and spatial unit (cell, parcel, catchment or candidate site).
2. Build a hierarchy of relevant, sufficiently distinct criteria and subcriteria.
3. Define what more preferred means for every criterion before eliciting weights.
4. Collect pairwise judgements from identified stakeholders; record who judged, when and under what framing.
5. Derive weights and inspect consistency.
6. Discuss the judgements behind large inconsistencies; do not mechanically edit values to force a threshold.
7. Standardise criterion layers separately, preserving units and benefit/cost direction.
8. Choose the aggregation rule separately. For compensatory WLC, keep hard constraints outside the weighted sum.
9. Test rankings and mapped patterns under plausible alternative judgements and stakeholder groups.
10. Publish the matrix, scale, derivation method, CR, missing-data policy and sensitivity results.

## Worked miniature

For road access, terrain and low flood exposure, consider this teaching matrix (not expert evidence):

\[
A=\begin{bmatrix}1&3&5\\1/3&1&2\\1/5&1/2&1\end{bmatrix}.
\]

Its principal eigenvector gives a priority vector summing to one. These priorities can be passed to WLC only after the three criterion rasters have been standardised to a common preference scale and aligned to the same grid.

## What AHP does not solve

- It does not select criteria or detect double-counting.
- It does not turn ordinal labels into defensible cardinal measurements automatically.
- It does not standardise, align or fill raster layers.
- It does not decide whether compensation is acceptable.
- It does not remove stakeholder disagreement; an average can hide it.
- It does not guarantee robust rankings under small changes in judgements or alternatives.

Pairwise input grows quadratically within each comparison group. For large hierarchies, consider direct weighting, swing weighting, group elicitation or another MCDA family.

## Companion implementation

- [Python implementation and tests](../implementations/python/ahp-weights/README.md)
- [Intern walkthrough](../implementations/python/ahp-weights/implementation-walkthrough.md)
- [Weighted linear combination](weighted-linear-combination.md)

## References

- Saaty, T. L. (1994). How to Make a Decision: The Analytic Hierarchy Process. Interfaces, 24(6), 19–43. https://doi.org/10.1287/inte.24.6.19
- Ishizaka, A. & Labib, A. (2011). Review of the main developments in the analytic hierarchy process. Expert Systems with Applications, 38(11), 14336–14345. https://doi.org/10.1016/j.eswa.2011.04.143
- UK Department for Communities and Local Government (2009). Multi-criteria analysis: a manual, Appendix 5.
- Feizizadeh, B. & Blaschke, T. (2013). GIS-based spatially explicit sensitivity and uncertainty analysis for MCDA. https://pmc.ncbi.nlm.nih.gov/articles/PMC4375947/

Educational introduction only; not a substitute for a documented stakeholder decision process.
