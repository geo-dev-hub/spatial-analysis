# Section 5 — Remote sensing, SAR, LiDAR, photogrammetry

- **Original source section:** 5
- **Source pages:** 7–9
- **Source transcription:** [pages 6–10](../../source-inventory/pages-06-10.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

The source spans raw imagery correction, spectral transforms, classification, hyperspectral analysis, radar, point clouds, photogrammetry and biophysical retrieval. These methods operate at different stages of a sensor-to-product workflow; do not collapse them into one generic “remote sensing algorithm” category.

## Preprocessing and correction

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Atmospheric: dark object subtraction, 6S, MODTRAN, FLAASH, Sen2Cor, ocean color atmospheric correction | Atmospheric correction methods / models / software | 7 | Captured; names not individually verified |
| Topographic and BRDF: C-correction, SCS+C, Minnaert, Ross-Li, BRDF normalization | Topographic correction / reflectance modelling | 7 | Captured; names not individually verified |
| Relative normalization: IR-MAD, pseudo-invariant features, histogram matching, empirical line calibration | Radiometric normalisation / calibration methods | 7 | Captured; names not individually verified |
| Cloud and shadow masking: Fmask, s2cloudless, CloudSEN12-style models; sensor harmonization (HLS) | Masking algorithms / model families / harmonisation products | 8 | Captured; names not individually verified |
| Mosaicking, seamline detection (Voronoi, graph cut), color balancing, orthorectification, co-registration | Image assembly / seamline algorithms / geometric correction | 8 | Captured; names not individually verified |
| Fusion: pan-sharpening (Brovey, IHS, Gram-Schmidt, PCA, wavelet, CNN), spatiotemporal fusion, Bayesian and Kalman fusion, sub-pixel and super-resolution mapping | Image fusion methods / statistical methods / neural approaches | 8 | Captured; names not individually verified |

## Indices and transforms

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Vegetation and soil: NDVI, EVI, SAVI, NDRE, NDMI, LSWI, tasseled cap (Kauth-Thomas) | Spectral indices / transforms | 8 | Captured; names not individually verified |
| Water, burn, snow, urban: NDWI, MNDWI, AWEI, NBR, dNBR, NDSI, NDBI | Spectral indices | 8 | Captured; names not individually verified |
| Transforms: PCA, minimum noise fraction (MNF), Fourier, wavelet, Hough, Radon | Statistical and signal transforms | 8 | Captured; names not individually verified |
| Texture and edges: GLCM, Gabor, Sobel, Canny, mathematical morphology, SIFT, SURF | Texture measures / filters / feature detectors and descriptors | 8 | Captured; names not individually verified |
| Thresholding: Otsu, adaptive; Stumpf bathymetry; OC4 chlorophyll | Thresholding methods / retrieval algorithms | 8 | Captured; names not individually verified |
| Compositing: best-pixel, medoid, maximum NDVI | Image compositing rules | 8 | Captured; names not individually verified |

## Classification and segmentation

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Pixel-based: maximum likelihood, SVM, random forest, XGBoost, LightGBM, stacked generalization, k-means, ISODATA | Classification models / ensemble methods / clustering | 8 | Captured; names not individually verified |
| Segmentation: watershed, SLIC superpixels, mean shift, region growing, multiresolution segmentation, graph cuts, MRF and CRF, active contours, level sets | Segmentation algorithms / optimisation and probabilistic models | 8 | Captured; names not individually verified |
| Object-based image analysis (OBIA) | Analysis workflow / method family | 8 | Captured; names not individually verified |
| Time-series classification: TempCNN, Transformer, InceptionTime, TimeMatch, DTW, TWDTW | Time-series models / matching methods | 8 | Captured; names not individually verified |
| Change detection: differencing, CVA, post-classification, IR-MAD, Siamese networks, ChangeFormer | Change-detection methods / model families | 8 | Captured; names not individually verified |
| Fractional cover: spectral mixture analysis, regression trees, vegetation continuous fields | Spectral unmixing / regression / derived products | 8 | Captured; names not individually verified |

## Hyperspectral

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Endmember extraction (N-FINDR, PPI, VCA), unmixing (FCLS, sparse, nonlinear, deep) | Endmember extraction / spectral unmixing methods | 8 | Captured; names not individually verified |
| Anomaly and target detection: RX, Kernel RX, matched filter, CEM, ACE, subspace methods | Detection algorithms / statistical methods | 8 | Captured; names not individually verified |
| Spectral angle mapper, spectral information divergence, band selection, continuum removal, absorption feature analysis, red-edge position | Spectral similarity measures / feature selection / spectral analysis | 8 | Captured; names not individually verified |

## SAR and InSAR

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Speckle filtering, polarimetric decomposition (H/A/alpha, Freeman-Durden, Yamaguchi), CFAR detection, SAR-to-optical translation | Filtering / decomposition methods / detection / translation models | 8 | Captured; names not individually verified |
| InSAR: PS-InSAR, SBAS, SqueeSAR, distributed scatterers, phase unwrapping (SNAPHU, minimum cost flow), coherence change detection, offset tracking, tomographic SAR, autofocus | Interferometric processing workflows / algorithms / software | 9 | Captured; names not individually verified |

## LiDAR and point clouds

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Ground filtering: CSF, progressive morphological; ICP registration; RANSAC shape fitting | Point-cloud filtering / registration / model fitting | 9 | Captured; names not individually verified |
| Tree segmentation (local maxima, watershed, Dalponte), canopy height models, crown delineation | Segmentation methods / derived surface models | 9 | Captured; names not individually verified |
| Classification, voxelization, strip adjustment, GEDI waveform processing, ICESat-2 ground photon classification | Point-cloud processing / sensor-specific workflows | 9 | Captured; names not individually verified |
| Deep point networks: PointNet, PointNet++, KPConv, Point Transformer, RandLA-Net, MinkowskiNet | Neural network architectures for point clouds | 9 | Captured; names not individually verified |

## Photogrammetry and 3D

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Structure from Motion (COLMAP), bundle adjustment, aerial triangulation, GCP and IMU-aided adjustment, direct georeferencing | Photogrammetric workflows / optimisation / software | 9 | Captured; names not individually verified |
| Dense matching: SGM, PatchMatch, multi-view stereo; RPC sensor models; satellite stereo DSM; DSM, DTM and nDSM derivation | Stereo matching algorithms / sensor models / surface products | 9 | Captured; names not individually verified |
| Lens calibration (Brown-Conrady), boresight calibration, orthomosaic generation, mesh texturing | Calibration methods / production workflows | 9 | Captured; names not individually verified |
| Surface reconstruction: Poisson, marching cubes, mesh simplification, 3D alpha shapes, NeRF, 3D Gaussian splatting | Surface reconstruction / mesh algorithms / neural representations | 9 | Captured; names not individually verified |

## Biophysical and geophysical retrieval

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Evapotranspiration and energy balance: SEBAL, METRIC, SEBS, ALEXI, Penman-Monteith, Hargreaves; land surface temperature (split-window, temperature-emissivity separation) | Energy-balance models / evapotranspiration and temperature retrieval | 9 | Captured; names not individually verified |
| Productivity and structure: light-use efficiency GPP, biomass allometry, LAI and fAPAR retrieval, soil moisture retrieval, albedo | Biophysical retrieval methods / allometric models / products | 9 | Captured; names not individually verified |
| Water and atmosphere: Case 2 water quality inversion, aerosol retrieval (dark target, MAIAC), DOAS trace gases, cloud property retrieval | Inversion and retrieval methods | 9 | Captured; names not individually verified |
| Cryosphere and ocean: sea ice concentration (NASA Team, Bootstrap), ice motion, glacier velocity, DEM differencing, eddy detection (Okubo-Weiss), SST fronts, altimetry processing | Retrieval / motion estimation / ocean analysis methods | 9 | Captured; names not individually verified |
| Thermal and fire: thermal anomaly and volcanic hotspot detection, active fire detection, burned area (MCD64A1) | Detection algorithms / products | 9 | Captured; names not individually verified |

## Decisions for the next pass

1. Keep sensor correction, feature extraction, classification, change detection and retrieval as distinct stages.
2. Record sensor, band configuration, spatial and temporal resolution, atmospheric assumptions and preprocessing.
3. Distinguish an algorithm from a named software package, product, dataset or model architecture.
4. Verify recent neural architectures and product names against original papers and maintainer sources.
5. Include conventional baselines and independent validation when evaluating learned methods.
