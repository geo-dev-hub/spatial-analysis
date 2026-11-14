# How the empirical semivariogram implementation works

## 1. Validate the observations

The function checks that there are at least two locations, one value per location, consistent coordinate dimensions and finite coordinates and values.

## 2. Validate the lag bins

The caller supplies strictly increasing distance edges. Each bin includes its left edge and excludes its right edge, except that the final bin includes its right edge. This convention makes assignment deterministic and is documented rather than hidden.

## 3. Visit each unique pair once

The nested loops use $i<j$, so each unordered pair is included once. The Euclidean distance is calculated from the coordinate vectors.

## 4. Assign the pair to a lag class

A pair contributes only when its separation falls within the requested range. The function places it into the matching bin and accumulates the squared difference between the two observed values.

## 5. Calculate the Matheron estimate

For a bin containing $N$ pairs:

$$
\widehat{\gamma}(h)=\frac{1}{2N}\sum_{(i,j)}(z_i-z_j)^2.
$$

The code divides the sum of squared differences by twice the number of pairs. It returns the bin midpoint as the representative lag and preserves empty bins with a missing semivariance.

## 6. What the tests check

Tests compare results with a hand calculation, check the final-bin convention, preserve empty bins, and verify invariance to coordinate translation and value translation. They also check that scaling all values by two scales semivariance by four.

## 7. What this implementation does not do

It does not fit a theoretical semivariogram, estimate the nugget/sill/range, account for directional anisotropy, use robust estimators, handle spatial trends or select the lag bins automatically.
