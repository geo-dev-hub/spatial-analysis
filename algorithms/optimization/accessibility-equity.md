# Accessibility equity: measure who receives access, not only the average

Stable ID: SA-OPT-ACCESS-EQUITY · Draft 0.1 · Source compendium section 6

## The planning question

A location model can reduce total travel cost or increase the number of people inside a service catchment while leaving some communities with very poor access. An average can improve even when the lowest-access group receives little benefit.

Equity analysis asks how accessibility is distributed. It is separate from calculating accessibility and from deciding which distribution is just.

## Start with an accessibility measure

Let a_i >= 0 be an accessibility score for population unit i, and w_i >= 0 the population represented by that unit. The weighted mean is:

$$
\bar a_w=\frac{\sum_i w_i a_i}{\sum_i w_i}.
$$

The score might come from cumulative opportunities, a gravity measure or 2SFCA. State its units and interpretation. Do not apply the conventional Gini coefficient directly to raw travel costs without defining an appropriate non-negative access measure.

## Worked example

For the exercise data (scores 2, 4, 8, 10 and populations 100, 300, 200, 100), the place-weighted mean is 6.0 while the population-weighted mean is approximately 5.71. The place-weighted Gini is approximately 0.292; the population-weighted Gini is approximately 0.257. With a minimum standard of 5, 400 of 700 represented residents (about 57.1%) fall below it. The different Gini values arise because the two calculations describe different distributions.

## Four complementary views

### 1. Lorenz curve and Gini coefficient

Sort units from lowest to highest accessibility. Plot cumulative population share against cumulative accessibility share. The diagonal represents equal distribution.

$$
G=1-\sum_{k=1}^{n}(p_k-p_{k-1})(L_k+L_{k-1}).
$$

Here p_k is cumulative population share and L_k is cumulative accessibility share. A larger Gini indicates more relative inequality. The [Lorenz curve diagram](../../assets/accessibility-lorenz-curve.svg) shows the equality line and a conceptual unequal distribution. If every unit has zero access, the curve is conventionally returned on the diagonal and Gini is zero because all values are equal; this is not a good outcome, so report absolute levels too.

### 2. Lower-tail quantiles

Report population-weighted p10, median and p90. Lower-tail quantiles describe the least-served share rather than allowing high-access places to dominate the story.

### 3. Minimum-standard shortfall

If a defensible minimum accessibility standard t exists, calculate:

$$
S(t)=\frac{\sum_i w_i\,\mathbf{1}(a_i<t)}{\sum_i w_i}.
$$

This is the population share below the declared standard. The standard must be justified by service policy, needs or an explicit scenario.

### 4. Group gaps

For caller-defined groups g, calculate weighted means:

$$
\bar a_g=\frac{\sum_{i\in g}w_i a_i}{\sum_{i\in g}w_i}.
$$

Compare highest and lowest group means using an absolute gap and a ratio. Also inspect within-group distributions.

## A practical workflow

1. Calculate accessibility using a documented destination set, mode, time period, impedance matrix and opportunity measure.
2. Join population weights and group labels using a defensible spatial crosswalk.
3. Check missingness, boundary mismatch, zero-population units and geographic scale.
4. Calculate mean, Lorenz curve, Gini, lower-tail quantiles and threshold shortfall.
5. Compare group distributions and inspect within-group variation.
6. Repeat for alternative network assumptions, thresholds, population estimates and time periods.
7. Compare policy scenarios using total benefits and distributional changes.

The [Python implementation and unit tests](../../implementations/python/accessibility-equity/README.md) provides descriptive diagnostics; the [notebook](../../notebooks/accessibility-equity-lab.ipynb) demonstrates them on synthetic data.

## Equity is not a single number

A lower Gini is not automatically a more just outcome. Inequality can fall because high access is reduced rather than low access improved. A policy may improve the mean while worsening a disadvantaged group's position.

Pereira, Schwanen and Banister review competing theories of transport justice and argue for examining accessibility as a capability, including minimum standards and the distributional effects on disadvantaged groups. The ethical principles, groups, opportunities, thresholds and priorities must be made transparent with affected communities and decision-makers.

## Assumptions and limits

- Accessibility values must be non-negative and comparable.
- Population weights define the population represented by each observation.
- Area averages do not describe every individual resident.
- Group differences are descriptive, not causal.
- Gini and group means do not account for spatial dependence or uncertainty.
- A single index can hide absolute deprivation and within-group inequality.
- Accessibility is not the same as mobility, service quality, affordability, safety or realised participation.
- Results are sensitive to spatial units, data quality, impedance, time of day and opportunity definition.

## Exercise

Work through the [accessibility equity exercise](../../exercises/accessibility-equity.md). Compare weighted and unweighted distributions and explain why they answer different questions.

## References

- Pereira, R. H. M., Schwanen, T., & Banister, D. (2017). [Distributive justice and equity in transportation](https://doi.org/10.1080/01441647.2016.1257660). Transport Reviews, 37(2), 170–191.
- Daskin, M. S. (2013). Network and Discrete Location: Models, Algorithms, and Applications (2nd ed.). Wiley.

Scope: descriptive distributional diagnostics for non-negative accessibility scores; not a normative fairness test, causal model or equity-constrained optimiser.
