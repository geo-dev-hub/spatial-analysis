# Population diversity and multigroup segregation

Diversity and segregation are related but different questions. A population can be diverse overall while groups are distributed very unevenly between areal units. These statistics depend on the group classification, unit system, denominators and boundary choices.

## Shannon entropy

For category proportions p_i,

\[
H=-\sum_i p_i\log p_i.
\]

Zero proportions contribute zero. Higher values indicate greater diversity, with the maximum determined by the number of categories.

## Simpson concentration

\[
D=\sum_i p_i^2,\qquad G=1-D.
\]

D is the probability that two independent draws from the same distribution belong to the same category; Gini–Simpson diversity is its complement.

## Reardon–Firebaugh multigroup entropy index

Let x_ik be the count of group k in areal unit i, X_i the unit total, t_k the group total and T the grand total. Overall entropy is

\[
E=-\sum_k \frac{t_k}{T}\log\frac{t_k}{T},
\]

and the population-weighted mean within-unit entropy is

\[
\bar E=\sum_i\frac{X_i}{T}\left[-\sum_k\frac{x_{ik}}{X_i}\log\frac{x_{ik}}{X_i}\right].
\]

The multigroup entropy index is

\[
H=\frac{E-\bar E}{E}.
\]

It is zero when every unit has the overall composition and one under complete separation (when E>0). This is an areal-unit segregation measure; it does not encode distance between units.

## Exposure and isolation

The group exposure probability is

\[
P^*_{ij}=\sum_k\left(\frac{x_{ik}}{X_i}\right)\left(\frac{x_{jk}}{t_k}\right).
\]

The diagonal gives isolation probabilities. The implementation uses areal-unit composition and does not add distance or adjacency weights.

## Runnable implementation

- [Python implementation](../implementations/python/population-diversity/README.md)
- [Tests](../implementations/python/population-diversity/test_population_diversity.py)
- [Intern walkthrough](../implementations/python/population-diversity/implementation-walkthrough.md)
- [Synthetic lab](../notebooks/population-diversity-segregation-lab.ipynb)

## Reference

Reardon, S. F., and Firebaugh, G. (2002). Measures of multigroup segregation. *Sociological Methodology*, 32(1), 33–67. https://doi.org/10.1111/1467-9531.00110

**Limit:** these measures are sensitive to areal-unit definitions and group aggregation. The exposure matrix here is not a distance-weighted spatial interaction measure.
