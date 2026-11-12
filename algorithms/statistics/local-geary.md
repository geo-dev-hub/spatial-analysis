# Local Geary: where are neighbouring values alike or different?

Stable ID: `SA-STAT-LOCAL-GEARY` · Draft 0.1 · Source compendium section 2

## Start with neighbouring differences

Global Geary's C gives one summary of how different neighbouring values are across the study area. But one number cannot show which locations have especially similar neighbours, or which locations sit beside very different values.

Local Geary looks at that question one unit at a time.

**Local Geary gives each spatial unit a measure of how different its value is from the values around it.**

It is a Local Indicator of Spatial Association (LISA). Small local values point to places whose neighbours are similar; large local values point to places whose neighbours are different. Statistical inference is needed before interpreting a local pattern as unusual.

## The local statistic

For location (i), Local Geary uses the weighted squared differences between the focal value and its neighbours:

$$
c_i = \sum_{j=1}^{n} w_{ij}(x_i-x_j)^2
$$

where:
- (x_i) is the value at location (i);
- (x_j) is the value at neighbouring location (j);
- (w_{ij}) is the spatial weight connecting them.

This is the local counterpart to the pairwise-difference idea behind global Geary's C. It does not compare the focal value with the overall mean.

A small (c_i), relative to its reference distribution, suggests the focal location has similar neighbours. A large (c_i) suggests dissimilar neighbours and a possible spatial outlier.

## What the result can look like

Local Geary focuses on similarity and difference between a unit and its neighbours.

| Local pattern | What it means |
|---|---|
| Cluster | The focal unit has values similar to its neighbours |
| Outlier | The focal unit has values dissimilar to its neighbours |
| Other | The local result does not fit the cluster/outlier classification |
| Not significant | The result does not pass the selected significance threshold |

The labels describe local relationships. They do not mean that a high or low value is inherently good or bad.

## Why it complements Local Moran

Local Moran compares the focal unit and its neighbourhood through their positions relative to the overall mean. Its four quadrants distinguish High–High, Low–Low, High–Low and Low–High patterns.

Local Geary instead compares the focal value directly with neighbouring values through squared differences. It distinguishes local similarity from local dissimilarity without using the global mean as the reference.

| | Local Moran's I | Local Geary |
|---|---|---|
| Main comparison | Focal deviation and neighbourhood lag | Focal value against each neighbour |
| Mathematical idea | Product of standardised deviations | Weighted squared differences |
| Main local interpretation | HH, LL clusters and HL, LH outliers | Similar-neighbour clusters and dissimilar-neighbour outliers |
| Useful emphasis | Position relative to the overall distribution | Local contrast between connected values |

The two methods can highlight related patterns, but their statistics and labels are not interchangeable.

## Inference: keep the focal value fixed

A local statistic is tested separately for each spatial unit. For Local Geary, conditional permutations work like this:

1. Select a focal unit.
2. Keep its observed value fixed.
3. Shuffle the other values among the remaining locations.
4. Recalculate the local statistic using the focal value and its newly assigned neighbours.
5. Repeat for the chosen number of permutations.
6. Compare the observed local statistic with its simulated reference distribution.

This produces a local reference distribution for each focal unit. The permutation count and random seed should be recorded.

## Many locations mean many tests

If there are 300 spatial units, a local analysis produces 300 tests. Some small p-values can appear by chance, and local tests are dependent because nearby locations share neighbours.

For responsible interpretation:
- report the number of local tests;
- state the permutation procedure and significance threshold;
- consider a multiple-testing correction such as false-discovery-rate control;
- do not treat unadjusted labels as confirmed clusters;
- compare local results with the global statistic and the chosen spatial weights.

PySAL's `Geary_Local` can return a label for each unit using a selected raw significance threshold. The labels are not automatically adjusted for multiple testing. If you apply an FDR cutoff, apply it to the p-values and clearly distinguish the adjusted result from the estimator's original labels.

## PySAL example

The current PySAL guide uses the following pattern:

```python
from esda import Geary_Local, fdr
from libpysal import graph

# Keep the GeoDataFrame and variable in the same row order.
y = gdf["value"].to_numpy()
w = graph.Graph.build_contiguity(gdf, rook=False).transform("r")

local = Geary_Local(
    connectivity=w,
    labels=True,
    sig=0.05,
    permutations=999,
    seed=12345,
    alternative="two-sided",
).fit(y)

# The FDR function returns a p-value cutoff, not adjusted p-values.
fdr_cutoff = fdr(local.p_sim, alpha=0.05)
passes_fdr = local.p_sim <= fdr_cutoff
```

The example uses Queen contiguity, row-standardised weights and conditional permutations. These are modelling choices. Check the API documentation for the version you install, especially the treatment of islands and the interpretation of the returned labels.

## Explore the calculation

The accompanying notebook uses the same synthetic ring graph as the Local Moran lab. It is not a geographic map; it lets us inspect local differences without introducing polygon geometry or data preparation as extra variables.

The notebook:
- constructs the neighbour graph;
- calculates local Geary values and conditional permutation p-values;
- compares the estimator's raw labels with an FDR-filtered classification;
- plots local values so that clusters and outliers can be inspected;
- lets you change the data while keeping the graph fixed.

- [Interactive Local Geary notebook](../../notebooks/local-geary-lab.ipynb)

## What to report

Record:
- the spatial units, attribute and study area;
- the weights construction, transformation and treatment of islands;
- the Local Geary implementation and software version;
- the number of conditional permutations and random seed;
- the raw and multiple-testing-adjusted significance thresholds;
- how the returned cluster/outlier labels were created;
- the global Geary and Moran results used as context.

## References

- PySAL `esda`. [Local Spatial Autocorrelation with Geary's C](https://pysal.org/esda/stable/user-guide/local_geary.html).
- PySAL `esda`. [Geary_Local API reference](https://pysal.org/esda/stable/generated/esda.Geary_Local.html).
- Anselin, L. (1995). “Local Indicators of Spatial Association—LISA.” *Geographical Analysis*, 27(2), 93–115. [https://doi.org/10.1111/j.1538-4632.1995.tb00338.x](https://doi.org/10.1111/j.1538-4632.1995.tb00338.x).

## What this lesson does not claim

- A small or large local Geary value is not, by itself, a significance result.
- A significant local statistic does not identify a cause.
- Local tests are not independent of one another.
- Local Geary and Local Moran are not interchangeable.
- The best spatial weights matrix depends on the substantive question.

## Change history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-13 | Initial reader-facing research draft with official PySAL workflow and interactive notebook |
