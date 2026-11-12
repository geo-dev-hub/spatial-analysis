# Spatial autocorrelation and hotspots: do nearby places have similar values?

**Status:** First complete version. Six core methods are available with worked examples and interactive notebooks; the supplementary Global Getis-Ord G lesson explains the global-to-local hotspot family.

## What this path helps you answer

You have a value for each area on a map: rent, population density, travel time, tree cover or another continuous measurement.

Are similar values found near one another? Are neighbouring areas unusually different? And how much of the answer depends on how we define “near”?

This path introduces two ways to measure the overall pattern. They use the same spatial relationships but look at similarity differently.

## Before you begin

It helps to be comfortable with:
- a mean and deviations from the mean;
- squared differences and sums;
- a matrix as a way of recording relationships;
- the idea that a map can be represented as a set of connected spatial units.

You do not need to know spatial statistics already. The lessons introduce the key terms as they are needed.

## Follow the path

### 1. Decide what counts as a neighbour

Start with the [spatial weights matrix lesson](../methods/spatial-weights-matrix.md) and its [interactive notebook](../notebooks/spatial-weights-lab.ipynb). It turns a map into a set of relationships.

Understand:
- Queen and Rook contiguity;
- distance bands and nearest neighbours;
- binary and row-standardised weights;
- islands and disconnected units;
- why the order of observations must match the order used by the weights.

The two lessons below revisit these ideas. Do not treat the weights as a neutral setting: they are part of the question you are asking.

### 2. Global Moran's I: compare deviations from the mean

[Read Global Moran's I](../algorithms/statistics/global-morans-i.md) and work through the [interactive notebook](../notebooks/global-morans-i-lab.ipynb).

Moran's I compares each area's deviation from the overall mean with the deviations of its neighbours. It gives one summary of global spatial autocorrelation.

Focus on:
- why the expected value under the randomisation null is slightly below zero for finite $n$;
- how the weights matrix affects the result;
- why the global statistic does not locate individual clusters;
- how a permutation reference distribution differs from the observed statistic.

### 3. Geary's C: compare neighbouring values directly

[Read Geary's C](../algorithms/statistics/gearys-c.md) and work through the [interactive notebook](../notebooks/gearys-c-lab.ipynb).

Geary's C uses squared differences between neighbouring values. It is therefore especially responsive to local contrasts between connected areas.

Focus on:
- why its null expectation is one;
- why values below one indicate positive spatial autocorrelation;
- why values above one indicate negative spatial autocorrelation;
- how its perspective complements Moran's I.

### 4. Compare the two methods on the same data

Use exactly the same spatial units, variable and weights matrix for both statistics.

Write down:
1. what Moran's I says about the overall relationship;
2. what Geary's C says about neighbouring differences;
3. whether the two point in the same direction;
4. whether changing the weights changes either conclusion;
5. what neither global statistic tells you about the location of clusters.

Do not compare the raw numerical values directly. The statistics have different formulas and different null expectations.

## 5. Find the places behind the global pattern

[Read Local Moran's I](../algorithms/statistics/local-morans-i.md) and use its [interactive notebook](../notebooks/local-morans-i-lab.ipynb).

This moves from one global summary to a statistic for each spatial unit. Learn the four quadrants (High–High, Low–Low, High–Low and Low–High), conditional permutations and the multiple-testing problem. A quadrant label alone is not evidence of significance.

## 6. Find local differences between neighbours

[Read Local Geary](../algorithms/statistics/local-geary.md) *(supplementary companion method)* and use its [interactive notebook](../notebooks/local-geary-lab.ipynb).

Local Geary compares a unit directly with its neighbours through squared differences. It complements Local Moran: one emphasizes local pairwise contrast, while the other uses the focal value and the neighbourhood lag relative to the overall mean.

## 7. Test for an overall concentration of positive values

[Read Global Getis-Ord G](../algorithms/statistics/global-getis-ord-g.md) and use its [interactive notebook](../notebooks/global-getis-ord-g-lab.ipynb).

This is a supplementary companion method added to explain the global-to-local Getis-Ord family. It tests whether high or low positive values are concentrated overall; it does not locate the areas responsible.

## 8. Find concentrations of high and low values

[Read Getis-Ord Gi*](../algorithms/statistics/getis-ord-gi-star.md) and use its [interactive notebook](../notebooks/getis-ord-gi-star-lab.ipynb).

Gi* answers a different question from Local Moran: it looks for unusually high or low concentrations in a neighbourhood, including the focal unit. It does not classify high-low or low-high outliers. Pay close attention to binary weights, the self-inclusion rule and the requirement for positive values.

## Bring the methods together

Use one dataset and the same spatial units wherever the methods allow. Choose the method that matches the question.

| Your question | Start with |
|---|---|
| Are similar values near one another overall? | Global Moran's I |
| How different are neighbouring values overall? | Global Geary's C |
| Where are High–High and Low–Low clusters, and where are spatial outliers? | Local Moran's I |
| Which locations have neighbours with especially similar or dissimilar values? | Local Geary |
| Are positive values concentrated across the whole study area? | Global Getis-Ord G |
| Where are local concentrations of high or low positive values? | Getis-Ord Gi* |

### Final exercise

Prepare a short spatial-autocorrelation report:

1. State the question and why it matters.
2. Describe the spatial units, attribute and study area.
3. Build and justify a weights matrix. Record its transformation and any islands.
4. Calculate the global statistic that matches your question.
5. If location-specific patterns matter, choose an appropriate local statistic.
6. Run permutation inference and state the null, alternative, number of permutations and seed.
7. Apply and report a multiple-testing procedure for the local tests.
8. Explain what the results show, what they do not show and how changing the weights might affect the conclusion.

### You are ready to move on when you can explain

- the difference between global and local statistics;
- why a statistic and its p-value answer different questions;
- how the weights matrix changes the question being asked;
- why local tests need a multiple-testing strategy;
- why Moran, Geary and Getis-Ord methods are complementary rather than interchangeable.

## Beyond this first path

Further extensions include spatial correlograms, point-pattern analysis, spatial regression, bivariate and multivariate local statistics, local join counts and spatial heteroskedasticity. Each needs its own question, assumptions, inference procedure and worked example. They will be added after those details are checked.

## References

- PySAL `esda`: [Global Moran's I](https://pysal.org/esda/stable/user-guide/global_morans_i.html).
- PySAL `esda`: [Global Geary's C](https://pysal.org/esda/stable/user-guide/geary.html).
- PySAL `esda`: [User guide](https://pysal.org/esda/stable/user-guide/index.html).
