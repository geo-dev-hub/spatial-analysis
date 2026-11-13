# Ripley's K and L for planar point patterns

Ripley's K summarises how many other events are found within a distance r of a typical event, compared with the point intensity. This implementation calculates a simple uncorrected estimator for a rectangular planar study window.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from ripley_k import ripley_k

result = ripley_k(
    [(0.5, 0.5), (1.5, 0.5), (1.5, 1.5)],
    bounds=(0, 2, 0, 2),
    radii=[0.25, 0.5, 1.0],
)
print(result.k_values, result.l_values)
~~~

## Contract and limitations

- Coordinates are planar, projected and expressed in consistent linear units.
- Bounds are a rectangular study window containing all events.
- At least two points and one or more finite non-negative radii are required.
- The estimator counts ordered event pairs and applies the uncorrected factor A/n².
- Under homogeneous Poisson CSR on the infinite plane, theoretical K(r) = pi*r² and L(r) = r.
- No edge correction is applied. This uncorrected estimator is biased near finite-window boundaries and must not be treated as an inferential test.
- The implementation stores all unique pair distances and uses O(n²) memory; it is a small-data teaching baseline.
- Translation, isotropic and border corrections, simulation envelopes and formal hypothesis tests are not included.

Read the [canonical lesson](../../../algorithms/statistics/ripley-k.md) and [intern walkthrough](implementation-walkthrough.md).
