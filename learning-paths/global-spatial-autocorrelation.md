# Global spatial autocorrelation: do nearby places have similar values?

**Status:** First two global methods are available. Local statistics and the wider inference sequence are still being added.

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

Start with the idea of a spatial weights matrix. It turns a map into a set of relationships.

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
- why the expected value under the randomisation null is slightly below zero for finite (n);
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

## 4. Find the places behind the global pattern

[Read Local Moran's I](../algorithms/statistics/local-morans-i.md) and use its [interactive notebook](../notebooks/local-morans-i-lab.ipynb).

This moves from one global summary to a statistic for each spatial unit. Learn the four quadrants (High–High, Low–Low, High–Low and Low–High), conditional permutations and the multiple-testing problem. A quadrant label alone is not evidence of significance.

## What comes next

The next lessons in this path will cover:
- local Geary and local contrasts;
- Getis-Ord statistics for local and global concentrations;
- multiple testing and false-discovery-rate correction;
- spatial correlograms and how association changes with distance.

These methods are not interchangeable. Each needs its own question, assumptions, inference procedure and worked example. They will be added here after those details are checked.

## References

- PySAL `esda`: [Global Moran's I](https://pysal.org/esda/stable/user-guide/global_morans_i.html).
- PySAL `esda`: [Global Geary's C](https://pysal.org/esda/stable/user-guide/geary.html).
- PySAL `esda`: [User guide](https://pysal.org/esda/stable/user-guide/index.html).
