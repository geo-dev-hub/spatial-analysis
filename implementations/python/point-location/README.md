# Static slab point locator

This package implements a restricted static point-location structure for a set of valid, pairwise interior-disjoint polygon faces with linear ring boundaries.

It returns:
- the face identifier when a query lies inside one polygon face;
- None for the outside/unbounded face;
- BOUNDARY when the query lies on a represented boundary.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from slab_locator import SlabPointLocator

faces = {
    "west": [[(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)]],
    "east": [[(2, 0), (4, 0), (4, 2), (2, 2), (2, 0)]],
}
locator = SlabPointLocator(faces)
print(locator.locate(1, 1))
print(locator.locate(3, 1))
print(locator.locate(2, 1))
~~~

## Complexity and limitations

The straightforward preprocessing stores an edge event in every x-slab it crosses, so storage and construction can be O(n²) in the worst case. A query uses binary search over x-events and the slab's preordered edge groups, giving O(log n) comparisons for points strictly inside a slab. Queries on x-event lines use a boundary-aware fallback scan.

This is not Seidel's randomized trapezoidal map and does not implement its expected bounds. It assumes non-crossing polygon boundaries and pairwise interior-disjoint faces. The input ring structure and polygon topology must be valid; this package does not validate arbitrary planar arrangements. It is a teaching implementation of a static slab locator.
