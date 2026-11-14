# Two-step floating catchment area: measuring potential access to services

Stable ID: `SA-OPT-TWO-STEP-FCA` · Draft 0.1 · Source compendium section 6, page 10

## The accessibility question

A service may be nearby but overloaded. Another may have more capacity but be farther away. A simple count of facilities within a radius misses this balance between supply and demand.

The two-step floating catchment area (2SFCA) method estimates potential spatial accessibility by comparing provider supply with the demand inside a catchment, then summing the reachable provider ratios at each population location.

## The two steps

Let:
- $i$ index population locations;
- $j$ index service providers;
- $P_i$ be population or another demand measure at location i;
- $S_j$ be provider supply or capacity at location j;
- $d_{ij}$ be the travel impedance from population i to provider j;
- $d_0$ be the catchment threshold.

**Step 1 — Provider supply-to-demand ratio**

For each provider, sum the population demand inside its catchment and divide provider supply by that demand:

$$
R_j=\frac{S_j}{\sum_{i:d_{ij}\leq d_0}P_i}
$$

**Step 2 — Accessibility at each population location**

For each population location, sum the ratios of all providers reachable within the catchment:

$$
A_i=\sum_{j:d_{ij}\leq d_0}R_j
$$

The result is a relative accessibility score. It is not a probability of being served, a measure of service quality or proof that capacity is sufficient.

## The impedance matrix is a modelling decision

The method does not prescribe how $d_{ij}$ is calculated. It may be:
- straight-line distance;
- road-network travel time;
- transit travel time;
- a generalised travel cost.

Those choices describe different opportunities. A radius on a map is not automatically equivalent to a travel-time catchment.

The [teaching implementation](../../implementations/python/two-step-fca/README.md) takes a matrix with population locations in rows and providers in columns. It uses a binary inclusive threshold: values less than or equal to $d_0$ are inside the catchment. Positive infinity can represent an unreachable pair; NaN and negative impedance are invalid.

## A small example

Two population locations have demand 100 each. Provider A has supply 10 and is reachable from both locations. Provider B has supply 20 and is reachable only from the second.

The provider ratios are:

$$
R_A=\frac{10}{100+100}=0.05,
\qquad
R_B=\frac{20}{100}=0.2.
$$

The accessibility scores are:

$$
A_1=0.05,
\qquad
A_2=0.05+0.2=0.25.
$$

The second location has more potential provider capacity within its catchment under this simplified model.

## Assumptions and limitations

- The binary catchment treats every location inside the threshold equally and every location outside it as unreachable.
- Provider capacity and population demand must have meaningful, documented units.
- Supply and demand should refer to compatible time periods.
- The model does not include provider choice, queueing, service quality, capacity constraints or temporal variation.
- An isolated provider with no demand in its catchment receives ratio zero in the teaching implementation; a population location with no reachable provider receives accessibility zero.
- The model is sensitive to the impedance definition and threshold.

A distance-decay extension is included separately below. Multiple catchments, variable catchment sizes, provider choice and dynamic capacity remain outside this teaching implementation.

## Exercises

1. Change provider B's supply. How does the second population location's score change?
2. Reduce the catchment threshold so provider A is reachable from only one population location.
3. Replace straight-line distances with a road travel-time matrix. What does the score now represent?
4. Give a provider a very large supply value. Does the model account for whether that supply is actually available to every patient?
5. Explain how a distance-decay version would differ from this binary catchment.

## References

- Radke, J. and Mu, L. (2000), [Spatial decompositions, modeling and mapping service regions to predict access to social programs](https://doi.org/10.1080/10824000009480538), *Geographic Information Sciences*, 6(2), 105–112.
- Luo, W. and Wang, F. (2003), [Measures of spatial accessibility to health care in a GIS environment: synthesis and a case study in the Chicago region](https://doi.org/10.1068/b29120), *Environment and Planning B: Planning and Design*, 30(6), 865–884.

**Scope:** binary-catchment 2SFCA with supplied impedance costs; no distance decay, provider choice or dynamic capacity model is included.


## Distance-decay extension: E2SFCA-style weighting

The binary method creates a sharp edge: a provider just inside the threshold contributes fully, while one just outside contributes nothing. Enhanced 2SFCA (E2SFCA) addresses uniform access within the catchment by applying weights to travel-time zones in both calculation steps (Luo and Qi, 2009).

Let $w_{ij}$ be a non-negative, non-increasing impedance weight for the pair of population location $i$ and provider $j$. The weighted provider ratio is:

$$
R_j=\frac{S_j}{\sum_i P_i w_{ij}}
$$

and population accessibility becomes:

$$
A_i=\sum_j R_j w_{ij}.
$$

The teaching implementation uses a piecewise-constant schedule. The analyst supplies strictly increasing band upper bounds $b_1,\ldots,b_K$ and non-increasing weights $w_1,\ldots,w_K$. A pair is assigned to the first band whose upper bound is greater than or equal to its impedance. A pair beyond the final bound receives weight zero. The same weights are applied in both steps.

For example, bounds $[10,20]$ and weights $[1,0.5]$ mean that a cost up to and including 10 receives weight 1; a cost above 10 and up to and including 20 receives weight 0.5; and a cost above 20 receives zero. These are illustrative values, not recommended universal parameters.

### Worked example

For:

$$
D=\begin{bmatrix}5&15\\25&5\end{bmatrix},
\qquad
W=\begin{bmatrix}1&0.5\\0&1\end{bmatrix},
$$

with supply $S=[10,20]$ and demand $P=[100,100]$, weighted demand is $[100,150]$. Therefore:

$$
R=[0.1,0.1333\ldots],
\qquad
A=[0.1667,0.1333\ldots].
$$

### Modelling cautions

- The analyst must justify travel-cost units, band edges and weights for the service and mode being studied.
- Weights are assumptions about impedance, not empirically observed individual choices unless calibrated with suitable data.
- This zonal implementation is not a continuous Gaussian decay model.
- A fixed maximum catchment still excludes all pairs beyond its final band.
- Test multiple plausible schedules and report sensitivity; do not present one schedule as objectively correct.

The [distance-decay implementation](../../implementations/python/two-step-fca/README.md) includes tests and a reproducible worked example.

## References

- Luo, W. and Qi, Y. (2009), [An enhanced two-step floating catchment area (E2SFCA) method for measuring spatial accessibility to primary care physicians](https://doi.org/10.1016/j.healthplace.2009.06.002), *Health & Place*, 15(4), 1100–1107. See also Luo's [2011 erratum](https://doi.org/10.1016/j.healthplace.2010.10.006): the printed Gaussian schedule should be $(1.00, 0.42, 0.03)$, not $(1.00, 0.42, 0.09)$. The erratum notes that the original calculations used 0.09 and were internally consistent with that value; it does not change the illustrative piecewise-constant weights used in this lesson.
