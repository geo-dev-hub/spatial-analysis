# Coverage-aware polygon simplification

This package demonstrates shared-edge-aware simplification for a valid polygon
coverage using Shapely's `coverage_simplify` operation (GEOS 3.12+).

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from shapely.geometry import Polygon
from coverage_simplification import simplify_coverage

left = Polygon([(0, 0), (5, 0), (5, 10), (0, 10)])
right = Polygon([(5, 0), (10, 0), (10, 10), (5, 10)])
result = simplify_coverage([left, right], tolerance=0.25)
```

## Contract and limits

- Inputs must form a valid, edge-matched polygon coverage.
- Tolerance uses the input coordinate units; use an appropriate projected CRS.
- The result is checked again as a valid coverage.
- This is a GEOS-backed wrapper, not a from-scratch generalisation algorithm.
- It does not repair invalid input coverages, infer missing shared edges, or
  guarantee that a chosen tolerance is cartographically appropriate.
- Coverage simplification preserves shared-edge consistency; it is distinct
  from independently simplifying each polygon with a per-feature topology flag.

See the canonical algorithm dossier and walkthrough before using it on data.
