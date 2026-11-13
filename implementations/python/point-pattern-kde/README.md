# Planar Gaussian kernel density estimation for point patterns

Kernel density estimation (KDE) turns a set of event locations into a continuous intensity surface. This package evaluates a fixed-bandwidth, isotropic Gaussian kernel on a regular grid.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from point_pattern_kde import gaussian_kde

points = [(2, 3), (2.2, 3.1), (7, 8)]
density, x_centres, y_centres = gaussian_kde(
    points,
    bounds=(0, 10, 0, 10),
    grid_shape=(100, 100),
    bandwidth=0.8,
)
~~~

## Contract and limitations

- Coordinates are planar and must use a suitable projected coordinate system with consistent linear units.
- Bounds are (xmin, xmax, ymin, ymax) and must contain all event locations.
- Grid shape is (rows, columns); returned x and y arrays contain cell-centre coordinates.
- The Gaussian kernel is isotropic with one fixed bandwidth.
- Optional non-negative event weights change the estimated intensity units accordingly.
- The output is intensity per square map unit, not a count per raster cell.
- No edge correction is applied. Estimates near the study-window boundary can be biased downward because part of the kernel lies outside the observation window.
- This is a direct O(nm) evaluation for n events and m grid cells; it is a transparent small/medium-data teaching baseline, not an indexed large-data KDE.
- Adaptive bandwidths, cross-validation, network KDE and formal point-process inference are not included.

Read the [canonical lesson](../../../algorithms/statistics/point-pattern-kde.md) and [intern walkthrough](implementation-walkthrough.md).
