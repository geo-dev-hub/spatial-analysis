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
- This baseline uses a binary catchment and does not include distance decay, competition outside the catchment, capacity constraints or temporal variation.
- Results depend on the impedance model and threshold. Euclidean distance, road travel time and transit travel time produce different accessibility measures.

Read the [canonical lesson](../../../algorithms/optimization/two-step-fca.md) and [intern walkthrough](implementation-walkthrough.md).
