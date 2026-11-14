# Remote sensing indices: what do spectral bands tell us?

**Status:** First spectral-index lesson published; the wider remote-sensing path is still being developed.

## The question

Satellite sensors measure reflected energy in different wavelength ranges. A spectral index combines selected bands to highlight a contrast that may be useful for a particular question.

## Before you begin

It helps to understand:
- the difference between a spectral band and a map layer;
- reflectance versus raw digital numbers;
- arrays, NoData and quality masks;
- why acquisition date and sensor matter.

## Follow the path

### 1. Understand NDVI

Read [Normalised Difference Vegetation Index](../algorithms/remote-sensing/ndvi.md) and run the [NDVI lab](../notebooks/ndvi-lab.ipynb).

The formula is simple. The preprocessing and interpretation are not. Check band mapping, scale factors, product level, atmospheric correction and quality flags before interpreting the output.

### 2. Preserve invalid pixels

Inspect how zero denominators, NoData values, non-finite inputs and quality masks are represented. Do not turn invalid measurements into plausible-looking zeros.

### 3. Interpret cautiously

NDVI is vegetation-sensitive, but it is not a direct measurement of biomass, crop yield or plant health. Consider soil background, canopy density, atmosphere, phenology and sensor characteristics.

## Exercises

1. Calculate NDVI for a few pairs of NIR and red reflectance values.
2. Explain why the index is undefined when the denominator is zero.
3. Compare two products from different sensors. What would need to be harmonised?
4. Design a cloud and shadow masking step and explain its effect on the valid-pixel footprint.
5. Identify field observations or reference data that could support the interpretation you want to make.

## What comes next

The wider source section includes atmospheric and topographic correction, BRDF normalisation, cloud masking, other vegetation/water/burn/snow indices, spectral transforms, classification, change detection, hyperspectral unmixing, SAR/InSAR, LiDAR and photogrammetry. These need separate, sensor-aware lessons.
