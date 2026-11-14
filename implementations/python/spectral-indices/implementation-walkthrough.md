# Intern walkthrough: calculating NDVI from reflectance arrays

## 1. Start with the sensor values

NDVI uses near-infrared and red reflectance. It is not safe to assume that raw digital numbers from two bands are directly comparable. Confirm scale factors, offsets, calibration, atmospheric correction and NoData encoding for the product.

## 2. Apply the formula

$$
NDVI=\frac{NIR-Red}{NIR+Red}
$$

The numerator compares the two bands. The denominator normalises the difference by their sum. If the denominator is zero, the index is undefined.

## 3. Carry validity through the calculation

The implementation converts inputs to float64 and builds a validity mask from finite values, an optional caller-supplied mask and an optional NoData sentinel. Pixels that fail these checks or have a zero denominator remain NaN.

The function does not silently clip values. A result outside the familiar -1 to 1 interval may indicate unusual inputs, negative corrected reflectance or a processing problem. Diagnose the source rather than forcing the output into a preferred range.

## 4. Keep interpretation modest

NDVI is a spectral contrast index. It can be useful for vegetation monitoring, but it is affected by canopy structure, soil background, atmosphere, sensor characteristics, illumination, season and saturation in dense vegetation. It is not a direct biomass or health measurement.

## 5. Validate before mapping

Tests check known values, zero denominators, non-finite inputs, NoData, explicit masks and shape mismatches. A production workflow should additionally record the sensor, product level, scale factors, acquisition date, QA mask and processing history.
