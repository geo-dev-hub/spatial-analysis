## Rasterisation algorithms — Python teaching implementation

This standard-library package implements DDA, all-octant Bresenham, Xiaolin Wu anti-aliased lines, supercover traversal and even-odd scanline polygon fill.

Run from this directory with `python -m unittest -v`.

Inputs use `(x, y)` grid coordinates and outputs use `(column, row)`. No CRS transform is applied: transform world coordinates to pixel coordinates using the raster affine transform before calling these routines. Bresenham and supercover require integer endpoints. Polygon fill supports one simple ring, samples cell centres and does not implement holes, multipolygons, self-intersections or fractional-area coverage. Wu values are display intensities, not area fractions.

The tests cover all-octant traversal and reversal, integer input validation, degenerate DDA, corner-touch supercover, bounded Wu intensities, square/triangle filling and invalid rings. This is a teaching baseline, not a replacement for GDAL, Rasterio, GEOS or a production scan converter. Further work should add an independent segment-cell oracle and rotated/sheared affine-grid tests.
