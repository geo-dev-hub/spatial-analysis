# Intern walkthrough: MMD and energy distance

Two-sample testing asks whether samples X and Y plausibly come from the same distribution. A spatial application must first define the feature representation, sampling unit and null hypothesis.

## Maximum mean discrepancy
For a kernel k, squared MMD compares within-sample similarity with cross-sample similarity. The unbiased U-statistic removes diagonal self-similarities:
MMD² = mean_{i≠j} k(x_i,x_j) + mean_{i≠j} k(y_i,y_j) - 2 mean_{i,j} k(x_i,y_j).
The Gaussian RBF kernel is exp(-||x-y||²/(2σ²)). Bandwidth changes the scale of differences the test can detect. The unbiased estimate may be negative in finite samples.

## Energy distance
The energy statistic is 2 E||X-Y|| - E||X-X'|| - E||Y-Y'||, estimated with off-diagonal within-sample distances. It detects distributional differences under suitable finite-moment conditions.

## Permutation inference
The implementation pools observations, permutes row labels and recomputes MMD. The plus-one p-value correction avoids zero p-values. This is valid only under exchangeability. Spatial autocorrelation violates naive row exchangeability; use spatial blocks, clusters or a model-based null and justify the design before interpreting a p-value.
