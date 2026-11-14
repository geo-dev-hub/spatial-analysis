# Accessibility distribution and equity diagnostics

This package measures how a supplied accessibility surface is distributed across people or groups. It complements an accessibility calculation such as [2SFCA](../../../algorithms/optimization/two-step-fca.md).

## Quick start

~~~python
from equity_diagnostics import accessibility_summary, group_accessibility_summary, group_mean_gap
access = [0.2, 0.5, 0.8, 1.0]       # dimensionless opportunity scores
population = [100, 200, 150, 50]   # residents represented by each row
groups = ["outer", "outer", "inner", "inner"]

print(accessibility_summary(access, population, minimum_threshold=0.6))
by_group = group_accessibility_summary(access, groups, population)
print(group_mean_gap(by_group))
~~~

## What is measured?

For non-negative accessibility values a_i and population weights w_i:

\[
\bar a_w=\frac{\sum_i w_i a_i}{\sum_i w_i}.
\]

The weighted Lorenz curve sorts observations from lowest to highest access and plots cumulative population share against cumulative accessibility share. The weighted Gini coefficient is one minus twice the area under that curve:

\[
G=1-\sum_{k=1}^{n}(p_k-p_{k-1})(L_k+L_{k-1}).
\]

The curve includes (0, 0). A perfectly equal distribution follows the 45-degree line. If all values are zero, the implementation returns the Lorenz curve on the diagonal and defines Gini as zero because there is no variation; this does not mean access is adequate.

Weighted p10, median and p90 describe the lower, middle and upper parts of the population distribution. For a declared minimum standard t, the population share below it is:

\[
S(t)=\frac{\sum_i w_i\,\mathbf{1}(a_i<t)}{\sum_i w_i}.
\]

Group summaries and the max-minus-min group mean gap provide a first comparison, not a complete account of within-group inequality.

## Input contract and limitations

- Values are finite, non-negative accessibility scores, not raw travel costs. Define the access measure and units first.
- Weights represent the population exposed to each observation, not arbitrary model importance.
- Arrays must have equal lengths; weights must be non-negative with positive total.
- Zero-weight observations are ignored.
- Groups are caller-supplied labels; this code does not infer identities or choose priority groups.
- Gini measures relative inequality, not whether everyone has sufficient access. Report absolute levels and lower-tail statistics too.
- Area-level scores do not describe every resident. Avoid ecological inference.
- Equal access scores do not imply equal opportunity: needs, affordability, opening hours, safety, disability access and service quality can differ.
- Results depend on geography, denominator, impedance, destinations, time period and spatial aggregation.
- Group gaps are descriptive, not causal. This package does not model uncertainty or spatial dependence.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

See the [canonical lesson](../../../algorithms/optimization/accessibility-equity.md), [intern walkthrough](implementation-walkthrough.md) and [exercise](../../../exercises/accessibility-equity.md).
