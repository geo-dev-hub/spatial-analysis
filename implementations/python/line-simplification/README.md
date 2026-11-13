# Line simplification implementation

This package contains dependency-light teaching implementations of:
- Douglas–Peucker for open polylines, using maximum point-to-segment distance;
- Visvalingam–Whyatt for open polylines, using iterative effective triangle area.

## Run

From this directory:

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from simplification import douglas_peucker, visvalingam_whyatt

line = [(0, 0), (1, 0.2), (2, 0), (3, 1), (4, 0)]
print(douglas_peucker(line, tolerance=0.25))
print(visvalingam_whyatt(line, area_threshold=0.2))
~~~

The Douglas–Peucker tolerance is in coordinate units. The Visvalingam–Whyatt threshold is in squared coordinate units. Both inputs are assumed to be planar 2D coordinate sequences.

## Limits

These are open-line teaching implementations. They do not preserve topology across polygon coverages, simplify rings with shared-arc coordination, implement Wang–Müller, or perform snap rounding. The worst-case Douglas–Peucker runtime can be quadratic; this simple iterative implementation prioritises clarity over advanced acceleration.
