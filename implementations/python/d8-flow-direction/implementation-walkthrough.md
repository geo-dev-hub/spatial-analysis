# How the D8 teaching implementation works

## 1. Validate the elevation grid

The input must contain at least one cell, have the same number of columns in every row and contain finite elevations or `None` for NoData. Cell width and height must be finite and positive.

## 2. Define the eight directions

The implementation stores row and column offsets alongside the ESRI-style direction code. Rows increase downward; columns increase to the right. The order is fixed so exact ties have deterministic behaviour.

## 3. Measure the path length

For an offset of $\Delta r$ rows and $\Delta c$ columns:

$$
d=\sqrt{(\Delta c\,w)^2+(\Delta r\,h)^2},
$$

where $w$ is cell width and $h$ is cell height.

## 4. Compare downslope gradients

For each valid neighbour, the code calculates

$$
g=\frac{z_c-z_n}{d}.
$$

Only positive gradients are eligible. The largest positive value wins. If no valid neighbour is lower, the result is 0.

## 5. Return the direction code

The code associated with the winning offset is written to the output grid. NoData cells remain `None`.

## 6. Why this is not a complete hydrology tool

Real DEM workflows need decisions about depression conditioning, flats, NoData boundaries, edge flow, tie handling and the appropriate flow model. This implementation exposes one local D8 rule so the learner can inspect it. It should not be used as a production watershed workflow.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
