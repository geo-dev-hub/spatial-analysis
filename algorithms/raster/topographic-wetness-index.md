# Topographic wetness index from specific catchment area and slope

Stable ID: SA-RASTER-TOPGRAPHIC-WETNESS-INDEX · Draft 0.1 · Source compendium section 4, page 7

## What the index represents

The topographic wetness index (TWI), also called the compound topographic index, is a terrain-derived indicator of potential water accumulation. It combines specific catchment area with local slope:

$$\mathrm{TWI}=\ln\left(\frac{a}{\tan\beta}\right)$$

where a is specific catchment area (contributing area per unit contour width, conventionally expressed in metres) and β is local slope angle.

Large specific catchment area and gentle slopes tend to produce larger index values. The index is a relative terrain indicator, not a direct measurement of soil moisture, groundwater level or saturation.

## Inputs matter

The [Python function](../../implementations/python/terrain-derivatives/README.md) accepts specific catchment area and slope in degrees. The catchment-area input must be positive and in metres. Convert other length units before calculating the index; changing units changes the numeric value inside the logarithm.

The method does not derive specific catchment area from flow accumulation. That conversion requires a declared flow-routing model, cell geometry and contour-width convention. It also does not calculate slope: use a documented DEM derivative method and align its units and NoData policy.

## Flat terrain

When β approaches zero, tan(β) approaches zero and the index tends to infinity. Flat areas therefore require an explicit treatment. This implementation replaces slopes below a declared positive floor (default 0.1°) with that floor before evaluating the logarithm. The floor is a modelling parameter and should be reported.

## Limitations

- TWI is an index, not a physically complete hydrological model.
- It does not represent soil depth, hydraulic conductivity, rainfall, vegetation, drainage infrastructure or transient water flow.
- It is sensitive to DEM resolution, depression treatment, flat resolution, flow-routing method and specific-area calculation.
- Different GIS packages may use different slope estimators, area conventions and flat handling.
- Do not compare numeric TWI values without aligning units and processing conventions.

## Exercises

1. Calculate TWI for a specific area of 10 m and slope of 30°.
2. Hold slope constant and increase specific catchment area. Explain the change.
3. Hold area constant and decrease slope toward zero. Why does the index increase?
4. Change the slope floor and report the effect on flat cells.
5. Explain why TWI is not a soil-moisture observation.

## References

- Beven, K. J. and Kirkby, M. J. (1979), *A physically based, variable contributing area model of basin hydrology*, Hydrological Sciences Bulletin, 24(1), 43–69.
- Moore, I. D., Grayson, R. B. and Ladson, A. R. (1991), *Digital terrain modelling: a review of hydrological, geomorphological, and biological applications*, Hydrological Processes, 5(1), 3–30.

**Scope:** index calculation from supplied specific catchment area and slope; no flow routing, area derivation or physical soil-moisture model.
