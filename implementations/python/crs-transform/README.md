# Coordinate transformation with explicit x/y axis order

This package wraps PROJ through pyproj to transform point coordinates between declared coordinate reference systems.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Input is a non-empty N×2 array.
- Source and target CRS may be EPSG identifiers, WKT or other pyproj-supported user inputs.
- always_xy is enabled: geographic coordinates are longitude, latitude; projected coordinates are easting, northing.
- Output coordinates use the target CRS units.
- Non-finite inputs or outputs and invalid transformations are rejected.
- The wrapper transforms points only; it does not reproject raster grids, geometries or datasets.

## Important limitations

A coordinate transformation is not merely a change of units. It can involve datum transformations, grid-shift files, area-of-use restrictions and coordinate epochs. The selected operation may depend on installed PROJ data and available transformation grids. This teaching wrapper does not expose operation selection, vertical transformations, dynamic reference frames, epoch metadata or accuracy budgets. Production work must record the full CRS definitions, selected operation, PROJ version and required grids.

Read the [canonical lesson](../../../algorithms/geodesy/crs-transformation.md) and [intern walkthrough](implementation-walkthrough.md).
