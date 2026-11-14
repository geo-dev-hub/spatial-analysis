# Theil–Sen robust trend estimator

A dependency-free teaching implementation of the Theil–Sen point estimator.

For every pair with distinct times, calculate the slope
\[
m_{ij}=\frac{y_j-y_i}{t_j-t_i}.
\]
The estimate is the median of these slopes. The intercept is the median of
\(y_i-\hat m t_i\). Actual numeric time coordinates are used, so irregular
sampling intervals are respected.

Run `python -m pip install -r requirements.txt` and
`python -m pytest -q`.

The implementation is O(n²) in pair generation and stores all pairwise slopes.
It returns a point estimate only. It does not provide a confidence interval,
correct for serial correlation, remove seasonality, or distinguish a smooth
trend from a step change. For large series, use a specialised selection
algorithm or a vetted scientific library and document its exact variant.
