# How the Global Geary's C reference implementation works

This walkthrough follows `geary_c.py` from input validation to the final statistic. It mirrors the mathematical definition so a reader can trace each term in the formula to the code.

## 1. Validate the weights

`_validated_weights()` checks the matrix dimensions, finite values, non-negative weights and zero diagonal.

The implementation permits an asymmetric matrix. Whether asymmetry is appropriate depends on how the spatial relationships were defined; report that choice.

## 2. Validate the observations

`gearys_c()` requires at least two observations. It converts the values to floats and rejects non-finite values.

The number of observations must match the number of rows and columns in the weights matrix.

## 3. Calculate the total weight

```python
s0 = sum(sum(row) for row in w)
```

This is:

$$
S_0 = \sum_i\sum_j w_{ij}
$$

A zero total means there are no positive spatial links, so the statistic cannot be calculated.

## 4. Calculate the overall mean and total variation

The mean is:

```python
mean = sum(x) / n
```

The denominator of Geary's C is the total squared deviation from that mean:

```python
denominator = sum((value - mean) ** 2 for value in x)
```

If all values are identical, the denominator is zero and Geary's C is undefined.

## 5. Compare neighbouring values directly

The numerator adds the squared difference for every weighted pair:

```python
numerator = sum(
    w[i][j] * (x[i] - x[j]) ** 2
    for i in range(n)
    for j in range(n)
)
```

Unlike Moran's I, this does not multiply centred deviations. It measures how different connected values are from one another.

## 6. Apply the formula

The final expression is:

```python
return ((n - 1) / (2 * s0)) * (numerator / denominator)
```

In mathematical form:

$$
C = \frac{n-1}{2S_0}
\frac{\sum_i\sum_j w_{ij}(x_i-x_j)^2}
{\sum_i(x_i-\bar{x})^2}
$$

The factor (2S_0) accounts for the sum of weighted pairwise differences in the standard definition.

## 7. Why the tests include permutations

For the four-unit symmetric chain, the tests enumerate all possible assignments of the values and check the mean of the resulting Geary statistics. This checks a mathematical property of the statistic under that specific symmetric graph.

It is not a general significance test. The implementation itself does not calculate a p-value or permutation reference distribution.

## 8. What the implementation does not do

It does not:
- construct neighbours from geometry;
- check the suitability of the weights matrix;
- align IDs with a spatial table;
- handle missing values;
- calculate analytical or permutation inference.

Use the [canonical Geary's C lesson](../../../algorithms/statistics/gearys-c.md) and the [interactive notebook](../../../notebooks/gearys-c-lab.ipynb) for the full interpretation and inference discussion.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
