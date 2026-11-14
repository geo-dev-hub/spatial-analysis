# Voronoi diagrams and Delaunay triangulations with SciPy

This package validates a planar 2D site set and asks SciPy/Qhull to construct both the Voronoi diagram and Delaunay triangulation. It is a library-backed workflow, not a from-scratch Fortune or Bowyer–Watson implementation.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python tessellation_demo.py
~~~

## Input contract

- At least three unique, finite 2D points are required.
- The sites must not all be collinear.
- Coordinates are interpreted in a planar Cartesian space.
- Duplicate sites are rejected before calling Qhull.
- Qhull errors for unresolved degeneracies are allowed to propagate. The wrapper does not silently joggle or perturb input coordinates.
- The returned coordinate array is read-only; SciPy's Voronoi and Delaunay objects are returned for inspection.

## What you get

- A Voronoi diagram: each region contains the locations closer to its generating site than to any other site.
- A Delaunay triangulation: sites are connected so that each triangle's circumcircle contains no other site in its interior, under the usual non-degenerate planar definition.
- A shared set of site coordinates used by both structures.

The two structures are geometric duals: a Delaunay edge corresponds to two Voronoi regions that share a boundary.

## Example

~~~python
from voronoi_delaunay import build_tessellations

sites = [(0, 0), (4, 0), (4, 3), (0, 3), (2, 1)]
result = build_tessellations(sites)
print(result.delaunay.simplices)
print(result.voronoi.vertices)
~~~

## Limits

- This wrapper delegates to Qhull through SciPy. It does not implement Fortune's sweep-line algorithm, Bowyer–Watson insertion, exact predicates or robust degeneracy resolution.
- Voronoi cells may be unbounded. A plotting window is not a geometric boundary of the true cell.
- Cocircular sites can admit more than one valid Delaunay diagonal. Do not assert one arbitrary diagonal unless the tie policy is explicitly fixed.
- The planar Euclidean model is not a geodesic construction for longitude/latitude.

## Read next

- [Voronoi and Delaunay lesson](../../../algorithms/geometry/voronoi-delaunay.md)
- [Implementation walkthrough](implementation-walkthrough.md)
- [Visual lab](../../../notebooks/voronoi-delaunay-lab.ipynb)
