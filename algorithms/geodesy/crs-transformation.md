# Coordinate transformation and CRS axis order

Stable ID: SA-GEODESY-CRS-TRANSFORMATION · Draft 0.1 · Source compendium section 9, page 18

## A coordinate is not just two numbers

A coordinate pair only has spatial meaning when its coordinate reference system (CRS) is known. Geographic coordinates use angular units such as degrees. Projected coordinates use linear units such as metres or feet. Assigning a new CRS label to existing numbers is not a coordinate transformation.

A CRS describes a reference system and its relationship to the Earth. A coordinate operation maps coordinates from one CRS to another, potentially involving a projection, datum transformation, grid shift or other operation.

## Axis order

Some CRS definitions specify latitude before longitude. Many GIS workflows use a conventional x/y order. The [Python baseline](../../implementations/python/crs-transform/README.md) uses pyproj with always_xy enabled:
- geographic input: longitude, latitude;
- projected input: easting, northing.

This convention is explicit in the wrapper and tests. It should not be assumed for every library or API.

## Example: geographic to Web Mercator

For a point at longitude λ and latitude φ, spherical Mercator coordinates are:

$$x=R\lambda$$

$$y=R\ln\left(\tan\left(\frac{\pi}{4}+\frac{\phi}{2}\right)\right)$$

where angles are in radians and R is the chosen sphere radius. Web Mercator is widely used for web maps, but it is not an equal-area projection and its scale distortion increases toward the poles. It is not suitable for every measurement.

The code example uses PROJ rather than reimplementing projection formulas, so it can also use the datum and operation machinery provided by the installed geospatial library.

## Datum transformations and operation selection

A transformation may require grid-shift files, a specific reference-frame realization, coordinate epoch or vertical datum. PROJ may choose among available operations based on installed resources and area of use. Reproducible high-accuracy work must record the CRS definitions, chosen operation, software version, grid files and expected accuracy.

## Tests and limitations

The implementation tests a known geographic-to-Web-Mercator coordinate, an equator point in UTM zone 32N, round-trip conversion and explicit x/y order.

It transforms point arrays only. It does not reproject rasters or geometries, select a high-accuracy operation manually, apply dynamic reference-frame epochs or transform vertical coordinates.

## Exercises

1. Transform longitude 0°, latitude 0° to Web Mercator. Why is the result the projected origin?
2. Transform longitude 9°, latitude 0° into UTM zone 32N. Why is the easting 500,000 m?
3. Swap longitude and latitude. Why can the result still be numerically valid but geographically wrong?
4. Explain why Web Mercator is unsuitable for measuring area at high latitudes.
5. List the metadata needed to reproduce a high-accuracy datum transformation.

## References

- Snyder, J. P. (1987), *Map Projections—A Working Manual*, USGS Professional Paper 1395.
- PROJ documentation, *Coordinate operations and transformations*.
- EPSG Geodetic Parameter Dataset, CRS definitions and coordinate operation metadata.

**Scope:** point transformation between declared CRSs with explicit traditional x/y axis order; no raster warp, geometry reprojection or dynamic/vertical datum workflow.
