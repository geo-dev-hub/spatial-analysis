# Intern walkthrough: D8 flow direction

## 1. Start with the elevation grid

Each cell stores an elevation. D8 examines the eight adjacent cells around a valid cell. Row indices increase southward and column indices increase eastward in this teaching convention.

## 2. Calculate slope to each neighbour

For a candidate neighbour at row/column offset $(\Delta r,\Delta c)$:

$$
s=\frac{z_0-z_1}{\sqrt{(\Delta r\,s_r)^2+(\Delta c\,s_c)^2}}
$$

where $s_r$ and $s_c$ are row and column cell spacing. Only strictly positive slopes are eligible.

## 3. Choose the steepest descent

The neighbour with the largest positive slope receives the flow. The code maps directions to the ESRI power-of-two codes and uses a fixed iteration order to resolve equal slopes reproducibly.

## 4. Handle cells without a lower neighbour

A valid cell with no lower valid neighbour receives code 0. This can represent a flat or a pit in this simple implementation. Invalid or NoData cells receive -1 and are not considered as neighbours.

## 5. Understand what is not solved

Real DEM conditioning often needs explicit flat resolution, depression filling or breaching, and treatment of artefacts. This implementation does none of those. It also does not calculate flow accumulation, stream extraction or watershed boundaries.

## 6. Check the units

Horizontal cell spacing and elevation values must use compatible units for slope comparisons. If horizontal coordinates are metres and elevations are feet, convert before running the algorithm. Document the DEM CRS, vertical datum and NoData policy.
