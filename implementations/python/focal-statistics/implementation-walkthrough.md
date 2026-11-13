# Intern walkthrough: focal mean with integral images

## 1. Define the neighbourhood

A focal operation calculates a new value at each cell from a local window. Here the window is a centred, odd-sized square. At raster edges it is truncated to the cells that exist; the algorithm does not invent padded values.

## 2. Why an integral image helps

A summed-area table stores cumulative sums. For input raster $x$, define:

$$
I(r,c)=\sum_{i<r,\,j<c}x(i,j)
$$

The sum of a half-open rectangle can then be recovered from four table values:

$$
S=I(r_1,c_1)-I(r_0,c_1)-I(r_1,c_0)+I(r_0,c_0)
$$

That makes each rectangular window sum O(1) after the table has been built.

## 3. Preserve NoData semantics

The implementation builds two integral images:
- one for values, with invalid cells replaced by zero;
- one for the count of valid observations.

For each focal window it calculates both the sum and valid count. The mean is their ratio, provided the count reaches min_count.

This avoids treating NoData as zero. It also lets the reader inspect how many observations contributed to each result.

## 4. Complexity

Building both tables is O(n) for n raster cells. Each cell requires one constant-time rectangle query from each table, so the full focal mean is O(n) time and O(n) memory for a fixed square-window operation.

## 5. Limitations

The method is an unweighted square-window mean. It does not implement Gaussian kernels, arbitrary weights, circular neighbourhoods, zonal statistics, resampling or edge padding. Those methods have different semantics and should be added as separate operations.

## 6. Validate

Tests compare known neighbourhood values, window size one, edge truncation, NoData handling, masks, minimum valid counts and invalid parameter values. For further validation, compare the output with a straightforward nested-loop reference implementation on random small arrays.
