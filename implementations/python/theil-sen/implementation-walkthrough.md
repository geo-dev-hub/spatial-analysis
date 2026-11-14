# Intern walkthrough: Theil–Sen

1. Enumerate every pair \((i,j)\) with \(i<j\) and \(t_i\ne t_j\).
2. Compute the pairwise slope \((y_j-y_i)/(t_j-t_i)\).
3. Take the median of the slopes. A median limits the influence of a small
   number of extreme pairwise slopes.
4. Estimate the intercept as the median residual offset
   \(y_i-\hat\beta_1t_i\).

The estimator uses elapsed time, not observation index. This matters for
irregularly sampled satellite composites or sensor records. The O(n²)
implementation is intentionally transparent, not a large-data algorithm.

Robustness to outliers does not remove autocorrelation, seasonality, serially
dependent errors or structural breaks. The point estimate is not a significance
test. Use an inference procedure whose assumptions match the sampling process.
