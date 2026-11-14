# Intern walkthrough: ensemble CRPS and rank histograms

For an ensemble x_1,...,x_m and observation y, the empirical-distribution continuous ranked probability score is

CRPS = (1/m) sum_i |x_i-y| - (1/(2m^2)) sum_i sum_j |x_i-x_j|.

The first term measures ensemble-member distance from the observation. The second corrects for ensemble spread. The score is non-negative and lower is better. This is the empirical ensemble score; fair-sample corrections are a different estimator and are not silently substituted.

A rank histogram has m+1 bins. Count how many ensemble members are below the observation. With no ties, increment that rank. If the observation ties k ensemble members, there are k+1 admissible insertion ranks; this implementation spreads one case equally across those ranks. This is the expected histogram under random tie-breaking, but deterministic and reproducible.

A U-shaped histogram can indicate under-dispersion, a dome can indicate over-dispersion, and slopes can indicate bias, but sample size, dependence, nonstationarity and stratification matter. These diagnostics are not stand-alone proof of calibration.
