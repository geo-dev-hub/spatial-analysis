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

Enhanced 2SFCA variants introduce distance decay, multiple catchments or other refinements. They should be documented as distinct variants rather than silently added to the binary baseline.

## Exercises

1. Change provider B's supply. How does the second population location's score change?
2. Reduce the catchment threshold so provider A is reachable from only one population location.
3. Replace straight-line distances with a road travel-time matrix. What does the score now represent?
4. Give a provider a very large supply value. Does the model account for whether that supply is actually available to every patient?
5. Explain how a distance-decay version would differ from this binary catchment.

## References

- Radke, J. and Mu, L. (2000), [Spatial decomposition, modeling and mapping service regions to predict access to social programs](https://doi.org/10.1080/136588100240976), *Geographical Analysis*, 32(2), 105–129.
- Luo, W. and Wang, F. (2003), [Measures of spatial accessibility to health care in a GIS environment: synthesis and a case study in the Chicago region](https://doi.org/10.1016/S0038-0121(02)00032-8), *Environment and Planning B*, 30(6), 865–884.

**Scope:** binary-catchment 2SFCA with supplied impedance costs; no distance decay, provider choice or dynamic capacity model is included.
