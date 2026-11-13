# Clark–Evans nearest-neighbour index

The Clark–Evans index compares the observed mean nearest-neighbour distance in a planar point pattern with the expected mean distance under a homogeneous Poisson (complete spatial randomness) reference process.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from clark_evans import clark_evans_index

result = clark_evans_index(
    [(0.5, 0.5), (1.5, 0.5), (1.5, 1.5)],
    bounds=(0, 2, 0, 2),
)
print(result.ratio)
~~~

## Interpretation

- R < 1: nearest neighbours are closer than the homogeneous Poisson expectation (a clustering tendency).
- R approximately 1: mean nearest-neighbour spacing is near the reference expectation.
- R > 1: nearest neighbours are farther apart than the reference expectation (a regularity tendency).

## Contract and limitations

- Coordinates must be planar, projected and expressed in consistent linear units.
- The study window is a rectangle `(x_min, x_max, y_min, y_max)` containing all points.
- At least two points are required.
- The expected distance uses the infinite-plane homogeneous Poisson approximation: 1 / (2 sqrt(lambda)), where lambda = n / window_area.
- No edge correction is applied. Boundary effects can inflate observed nearest-neighbour distances.
- The result is a descriptive index, not a p-value or significance test.
- The implementation uses a chunked brute-force distance calculation: O(n²) time and O(chunk_size × n) temporary memory.

Read the [canonical lesson](../../../algorithms/statistics/clark-evans.md) and [intern walkthrough](implementation-walkthrough.md).