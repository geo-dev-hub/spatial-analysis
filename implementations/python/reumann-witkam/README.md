# Reumann-Witkam line simplification

A pure-Python teaching implementation of the Reumann-Witkam strip method for ordered planar polylines.

## Run

~~~bash
python -m pytest -q
~~~

## Example

~~~python
from simplify import reumann_witkam
line = [(0, 0), (1, 0.05), (2, -0.03), (3, 0)]
print(reumann_witkam(line, tolerance=0.1))
~~~

## Algorithm

1. Anchor a strip on the first two vertices.
2. Scan forward while each vertex remains within the perpendicular-distance tolerance of the baseline.
3. When a vertex exits the strip, retain the preceding vertex.
4. Start a new strip at that retained vertex, using the exiting vertex as the look-ahead point.
5. Preserve the final input vertex.

This implementation measures distance to the infinite baseline line. Coordinates must be planar and tolerance must use the same units. Project longitude/latitude data to a suitable local coordinate system first.

## Scope and limitations

This is a transparent teaching implementation, not a topology-preserving coverage simplifier. It does not guarantee preservation of shared polygon boundaries or network connectivity. Published and software variants may differ in strip and endpoint choices; do not assume their outputs are interchangeable.

The tests cover straight lines, strip exits, short lines, zero tolerance, duplicate vertices and invalid numerical inputs.
