# Two-step floating catchment area accessibility

The two-step floating catchment area (2SFCA) method estimates spatial accessibility by comparing service supply with population demand inside a travel catchment.

This implementation uses a binary catchment: a provider and population location are connected when their supplied impedance is less than or equal to a maximum threshold. It does not apply distance decay.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from two_step_fca import two_step_fca

# Rows are population locations; columns are service providers.
travel_costs = [[1, 4], [2, 1]]
provider_supply = [10, 20]       # e.g. service capacity units
population = [100, 100]
ratios, accessibility = two_step_fca(
    travel_costs, provider_supply, population, max_cost=2
)
print(ratios, accessibility)
~~~

## Contract and limits

- The impedance matrix has one row per population location and one column per provider.
- Supply and demand must use documented, compatible units.
- Positive infinity may represent an unreachable population-provider pair; NaN and negative impedance are rejected.
- The catchment includes costs less than or equal to max_cost.
- A provider with no demand inside its catchment receives a ratio of zero.
- A population location with no reachable provider receives accessibility zero.
- The baseline function uses a binary catchment. A separate distance-decay function is also provided; neither version models provider choice, queueing, capacity constraints or temporal variation.
- Results depend on the impedance model and threshold. Euclidean distance, road travel time and transit travel time produce different accessibility measures.

Read the [canonical lesson](../../../algorithms/optimization/two-step-fca.md) and [intern walkthrough](implementation-walkthrough.md).


## Distance-decay extension (E2SFCA-style)

Use \`two_step_fca_distance_decay\` when all population-provider pairs inside the maximum catchment should not be treated as equally accessible. Supply increasing band upper bounds and non-increasing weights; the same piecewise-constant weight function is applied in both steps.

~~~python
from two_step_fca import two_step_fca_distance_decay

ratios, accessibility = two_step_fca_distance_decay(
    [[5, 15], [25, 5]],
    [10, 20],
    [100, 100],
    band_upper_bounds=[10, 20],
    band_weights=[1.0, 0.5],
)
~~~

A cost exactly on a band upper bound belongs to that band. Costs above the final bound receive zero weight. The implementation does not choose the bands or weights for the analyst: document their units, rationale and sensitivity. This is a zonal distance-decay implementation, not a continuous Gaussian decay function.

The extension follows the two-stage weighting principle described by Luo and Qi (2009). See the canonical lesson and intern walkthrough for the equations and modelling cautions.
