# Normalised Difference Vegetation Index (NDVI)

Stable ID: `SA-RS-NDVI` · Draft 0.1 · Source compendium section 5, page 8

## What it measures

NDVI is a spectral index formed from near-infrared and red reflectance. It expresses their normalised difference and is commonly used as a vegetation-sensitive indicator.

$$
NDVI=\frac{NIR-Red}{NIR+Red}
$$

The numerator captures the contrast between near-infrared and red reflectance. The denominator scales the contrast by their sum. The index is undefined when that sum is zero.

## A visual intuition

Healthy green vegetation often absorbs strongly in the red part of the spectrum and reflects more strongly in the near-infrared. The contrast can therefore produce a higher NDVI than many bare-soil or built surfaces.

This is a tendency, not a universal classification rule. Soil background, canopy density, water, atmosphere, illumination, phenology and sensor characteristics all affect the observed value.

## Do not skip preprocessing

Before calculating NDVI, establish:
- which sensor and product level supplied the bands;
- the correct red and NIR band identifiers;
- scale factors and offsets;
- whether the values are surface reflectance, top-of-atmosphere reflectance or raw digital numbers;
- cloud, cloud-shadow, snow and other quality masks;
- the NoData convention and any saturation flags.

Do not combine uncalibrated band values or compare products with incompatible processing histories without a documented harmonisation step.

## Validity and numerical behaviour

If $NIR+Red=0$, NDVI is undefined. Non-finite inputs and pixels excluded by the quality mask should remain invalid rather than becoming plausible-looking zeros.

The [teaching implementation](../../implementations/python/spectral-indices/README.md) returns NaN for undefined or masked pixels. It does not clip values to [-1,1]. If values fall outside that interval, inspect the inputs and correction workflow before deciding how to handle them.

## Interpretation limits

NDVI is not a direct measurement of biomass, species composition, crop yield, plant health or productivity. Dense vegetation can lead to saturation; soil and atmospheric effects can influence sparse vegetation; and different sensors or seasons can produce different distributions.

Use field observations, suitable reference data and a study-specific validation design when making substantive claims.

## Exercises

1. Calculate NDVI for $NIR=0.6$ and $Red=0.2$.
2. What happens when both bands are zero? Why should that pixel not be assigned an index of zero?
3. Compare a high-NDVI pixel from a dense canopy with one from sparse vegetation. Why is the index not a direct biomass estimate?
4. Inspect the product scale factors and quality flags for a satellite product you use.
5. Explain why a cloud mask should be applied before interpreting an NDVI map.

## References

- Rouse, J. W., Jr., Haas, R. H., Schell, J. A., Deering, D. W. and Harlan, J. C. (1974, November), *Monitoring the vernal advancement and retrogradation (green wave effect) of natural vegetation*. Type III final report for September 1972–November 1974, Texas A&M University Remote Sensing Center, prepared for NASA Goddard Space Flight Center; NASA-CR-144661 (RSC-1978-4). [NASA NTRS record](https://ntrs.nasa.gov/citations/19750020419).
- [USGS Landsat Normalized Difference Vegetation Index](https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index).
- [NASA Earth Observatory: Measuring Vegetation (NDVI & EVI)](https://earthobservatory.nasa.gov/features/MeasuringVegetation).

**Scope:** the NDVI formula, input validity and interpretation; not a complete vegetation-index or remote-sensing preprocessing guide.
