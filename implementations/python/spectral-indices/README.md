# Normalised Difference Vegetation Index (NDVI)

This package calculates NDVI from near-infrared (NIR) and red reflectance arrays:

$$
NDVI=\frac{NIR-Red}{NIR+Red}.
$$

The function preserves undefined pixels as NaN, supports an explicit NoData value and validity mask, and does not clip outputs to a presumed physical range.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
import numpy as np
from spectral_indices import ndvi

nir = np.array([[0.62, 0.48], [0.20, 0.15]])
red = np.array([[0.12, 0.16], [0.18, 0.15]])
index = ndvi(nir, red)
~~~

## Important input contract

- Inputs are same-shaped arrays of comparable reflectance values, not raw digital numbers from unrelated bands.
- Apply the sensor-specific calibration and atmospheric correction appropriate to the product before interpreting the index.
- Pixels with non-finite inputs, an explicit NoData value, a false validity mask or a zero denominator become NaN.
- Negative reflectance values are not silently clipped; inspect upstream processing and interpret the result carefully.
- NDVI is a spectral index, not a direct measurement of biomass, species, health or productivity.

Read the [canonical lesson](../../../algorithms/remote-sensing/ndvi.md) and [intern walkthrough](implementation-walkthrough.md).
