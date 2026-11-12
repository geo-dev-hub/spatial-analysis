# How the Global Moran's I reference implementation works

This walkthrough follows `moran_i.py` from validation to the final statistic. It is a deliberately small dense-matrix implementation: the aim is to make the formula visible, not to replace a spatial statistics library.

## 1. Validate the weights matrix

`_validated_weights()` checks that the matrix:
- has one row per observation;
- is square;
- contains finite, non-negative weights;
- has a zero diagonal.

The function copies values into a regular Python list of lists. It does not decide whether the matrix represents a defensible neighbourhood definition. That remains an analysis decision.

## 2. Row-standardise when that is the chosen model

`row_standardize()` divides every nonzero row by its row sum.

An isolated row remains all zeros. The function does not invent neighbours or silently remove an island.

Row standardisation is a transformation of the model. It is not a mandatory preparation step for every Moran analysis.

## 3. Validate the observed values

`morans_i()` requires at least two observations and converts values to floats. It rejects NaN and infinite values.

The number of values must match the dimensions of the weights matrix.

## 4. Calculate the total weight

The implementation calculates:

```python
s0 = sum(sum(row) for row in w)
```

This is (S_0=\sum_i\sum_j w_{ij}). A matrix with no positive weights cannot define a spatial association statistic, so it is rejected.

## 5. Centre the values

The overall mean is calculated and subtracted from every value:

```python
mean = sum(x) / n
z = [value - mean for value in x]
```

The centred values show how far each observation is above or below the study-wide mean.

## 6. Calculate numerator and denominator

The numerator is the weighted cross-product of centred neighbouring values:

```python
numerator = sum(
    w[i][j] * z[i] * z[j]
    for i in range(n)
    for j in range(n)
)
```

The denominator is the total squared deviation from the mean:

```python
denominator = sum(value * value for value in z)
```

A constant variable has a zero denominator, so Moran's I is undefined and the implementation raises an error.

## 7. Apply the formula

The final calculation is:

```python
return (n / s0) * (numerator / denominator)
```

This is the global Moran's I formula:

$$
I = \frac{n}{S_0}
\frac{\sum_i\sum_j w_{ij}z_i z_j}
{\sum_i z_i^2}
$$

## 8. What the implementation deliberately does not do

It does not:
- construct neighbours from polygons or points;
- check that the matrix is symmetric;
- align spatial IDs with a GeoDataFrame;
- handle missing observations;
- calculate analytical significance;
- run a permutation test.

Those tasks require additional assumptions and are covered in the [canonical lesson](../../../algorithms/statistics/global-morans-i.md) and the [interactive notebook](../../../notebooks/global-morans-i-lab.ipynb).

## 9. How the tests help

The tests check the hand-calculated chain examples, positive and negative association, row standardisation, invariance under translation and positive scaling, isolated rows and invalid inputs.

The test suite verifies the implementation of the statistic. It does not validate a real-world weights matrix or the assumptions of a statistical test.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
