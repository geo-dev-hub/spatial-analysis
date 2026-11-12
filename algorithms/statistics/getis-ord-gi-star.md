# Getis-Ord Gi*: where are the hotspots and coldspots?

Stable ID: `SA-STAT-LOCAL-GETIS-ORD-GI-STAR` · Draft 0.1 · Source compendium section 2

## Start with a different question

You have a map of daily service requests, property prices, reported incidents or another positive measurement.

You want to know where high values are concentrated, and where low values are concentrated. Not just where nearby values are similar, but where the values around a location add up to an unusually high or low concentration.

**Getis-Ord Gi* identifies local concentrations of high values (hotspots) and low values (coldspots).**

It is not the same as Local Moran's I. Gi* is designed to detect concentrations; it does not classify High–Low and Low–High spatial outliers in the same way.

## What the statistic looks at

For each location, Gi* considers the values in its neighbourhood, including the focal location itself. The neighbourhood is defined by a spatial weights matrix.

- A large positive z-score indicates a concentration of high values around the location.
- A large negative z-score indicates a concentration of low values.
- A z-score near zero indicates that the observed local concentration is not far from its reference expectation.

The result is a local statistic and z-score for every location. The z-score and its p-value answer different questions: the z-score gives direction and strength relative to the reference distribution; the p-value measures how unusual the result is under the selected null.

## Why the asterisk matters

Getis-Ord's local $G_i$ and $G_i^*$ are related, but they do not use the same neighbourhood sum.

- $G_i$ excludes the focal observation.
- $G_i^*$ includes the focal observation.

The star is not decoration. It changes which values contribute to the local sum. This lesson focuses on $G_i^*$, the commonly used hotspot statistic.

## Choose the weights deliberately

For the standard Gi* workflow, use binary spatial weights and explicitly include the focal observation.

- A weight of one means the unit contributes to the focal location's neighbourhood sum.
- A weight of zero means it does not contribute.
- The focal unit must be included for $G_i^*$.

The official PySAL example uses a binary contiguity graph and `star=True`. Do not row-standardise the weights by habit. If you change the weight transformation, you change the statistic and its interpretation.

The neighbourhood definition also matters: Queen contiguity, Rook contiguity, a distance band and nearest neighbours produce different hotspot maps.

## Hotspot or coldspot?

| Result | Interpretation |
|---|---|
| Positive and statistically significant z-score | Hotspot: high values are concentrated in the neighbourhood |
| Negative and statistically significant z-score | Coldspot: low values are concentrated in the neighbourhood |
| Not statistically significant | The local concentration does not pass the chosen test threshold |

A hotspot does not necessarily mean the focal unit has the highest value in the dataset. It means the focal unit's neighbourhood, including itself, has an unusually high concentration relative to the null model.

Likewise, a coldspot is not simply a location with a low value. Its surrounding neighbourhood must also form an unusually low concentration.

## How it differs from Local Moran

| Question | Local Moran's I | Getis-Ord Gi* |
|---|---|---|
| What is compared? | Focal deviation and neighbourhood lag | Sum of values in the neighbourhood, including the focal unit |
| What patterns are identified? | HH, LL clusters and HL, LH outliers | Hotspots and coldspots |
| Can it identify a high value among low neighbours? | Yes, as a High–Low outlier | Not as a separate outlier category |
| Main use | Local spatial association | Local concentration of high or low values |

Use Local Moran when spatial outliers matter. Use Gi* when the question is specifically about concentrations of high or low values.

## Inference and multiple testing

A Gi* z-score should be interpreted with its inference method. The PySAL API offers analytical and permutation-based quantities. Its permutation p-values are documented as one-sided; the `alternative` option controls the conditional randomisation alternative. State which output you report and how you interpret its tail.

Local analysis runs one test per spatial unit. If the study contains many locations, some results may pass an unadjusted threshold by chance. The tests are also spatially dependent because neighbouring neighbourhoods share observations.

For a responsible hotspot analysis:
- report the number of local tests;
- state the null hypothesis, permutation count and random seed;
- identify whether you use analytical or permutation-based inference;
- consider an FDR correction across the local p-values;
- distinguish raw significance from multiple-testing-adjusted significance;
- compare the map with the underlying variable and the global spatial pattern.

## PySAL example

The official PySAL guide uses this pattern:

```python
from esda import G_Local, fdr
from libpysal import graph

# Keep the GeoDataFrame and attribute in exactly the same row order.
y = gdf["value"].to_numpy()
w = graph.Graph.build_contiguity(gdf, rook=False)

gi_star = G_Local(
    y,
    w,
    transform="B",
    star=True,
    permutations=999,
    seed=12345,
    alternative="two-sided",
)

fdr_cutoff = fdr(gi_star.p_sim, alpha=0.05)
passes_fdr = gi_star.p_sim <= fdr_cutoff
hotspots = passes_fdr & (gi_star.Zs > 0)
coldspots = passes_fdr & (gi_star.Zs < 0)
```

Here Queen contiguity is used with binary weights. `star=True` includes the focal observation. The FDR function returns a cutoff, not a vector of adjusted p-values.

The data should be positive and have a meaningful zero, such as counts or prices. Do not add an arbitrary constant to force a variable with zero or negative values into a form where Gi* appears applicable.

## Explore the calculation

The accompanying notebook uses a synthetic ring graph with positive values. It:
- builds binary neighbour weights;
- computes Gi* z-scores and permutation p-values;
- identifies hot and cold concentrations;
- applies an FDR cutoff;
- changes the values while leaving the graph unchanged.

- [Interactive Getis-Ord Gi* notebook](../../notebooks/getis-ord-gi-star-lab.ipynb)

The synthetic graph is not a geographic map. Use the official PySAL guide for a full polygon-data example with mapped neighbourhoods.

## What to report

Record:
- the variable, units and reason its values are suitable for Gi*;
- the spatial units and study area;
- the weights construction and why the focal unit is included;
- whether weights are binary and how islands are treated;
- the inference method, alternative, permutation count and seed;
- the multiple-testing correction and threshold;
- the z-score and p-value interpretation;
- how the hotspot map compares with Local Moran and the raw variable.

## References

- Getis, A., and Ord, J. K. (1992). “The Analysis of Spatial Association by Use of Distance Statistics.” *Geographical Analysis*, 24(3), 189–206. [https://doi.org/10.1111/j.1538-4632.1992.tb00261.x](https://doi.org/10.1111/j.1538-4632.1992.tb00261.x)
- PySAL `esda`. [Hotspot Analysis with Getis-Ord G and G*](https://pysal.org/esda/stable/user-guide/local_getisord.html).
- PySAL `esda`. [G_Local API reference](https://pysal.org/esda/stable/generated/esda.G_Local.html).

## What this lesson does not claim

- A high or low z-score is not automatically statistically significant.
- A hotspot is not a causal explanation.
- Gi* does not identify High–Low and Low–High outliers.
- A hotspot result depends on the weights definition and the inclusion of the focal unit.
- A variable with arbitrary zero or negative values should not be forced into a positive-value concentration analysis.

## Change history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-13 | Initial reader-facing research draft with official PySAL workflow and interactive notebook |
