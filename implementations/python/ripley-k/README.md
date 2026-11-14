# Ripley's K and L for planar point patterns

Ripley's K summarises how many other events are found within a distance r of a typical event, compared with the point intensity. This implementation provides an uncorrected estimator and a translation edge-corrected estimator for a rectangular planar study window.

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
- Both modes count ordered event pairs and use the documented A/n² denominator.\n- Translation correction weights each pair by A divided by the overlap area of the window and its translated copy.
- Under homogeneous Poisson CSR on the infinite plane, theoretical K(r) = pi*r² and L(r) = r.
- edge_correction is either none or translation. Translation correction is specific to rectangular windows and rejects zero-overlap pairs.\n- No isotropic or border correction, simulation envelopes or formal hypothesis tests are included.
- The implementation stores all unique pair distances and uses O(n²) memory; it is a small-data teaching baseline.
- Isotropic and border corrections, simulation envelopes and formal hypothesis tests are not included.

Read the [canonical lesson](../../../algorithms/statistics/ripley-k.md) and [intern walkthrough](implementation-walkthrough.md).


## Conditional CSR simulation and global deviation test

The companion module `ripley_k_envelope.py` keeps the observed event count fixed, simulates uniform point patterns in the same rectangular window and calculates translation-corrected L curves.

```python
import numpy as np
from ripley_k_envelope import ripley_k_csr_envelope

result = ripley_k_csr_envelope(
    points,
    bounds=(0, 10, 0, 10),
    radii=np.linspace(0.5, 3.0, 26),
    n_simulations=199,
    alpha=0.05,
    seed=2026,
)
print(result.global_p_value)
print(result.pointwise_lower_l, result.pointwise_upper_l)
```

The returned bands are pointwise quantiles, not a simultaneous global envelope. The p-value is calculated separately from a studentised maximum absolute deviation over the selected radii. The null is homogeneous CSR conditional on the observed number of events. The simulation count controls Monte Carlo resolution; the smallest possible p-value is 1/(B+1).

This is a transparent teaching test, not a specialist rank-envelope implementation. It does not adjust for parameter estimation, inhomogeneous intensity, network constraints or other departures from the stated null. See the [canonical lesson](../../../algorithms/statistics/ripley-k.md).
