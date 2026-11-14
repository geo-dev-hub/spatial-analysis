# Section 5 — Remote sensing, SAR, LiDAR, photogrammetry

- **Original source section:** 5
- **Source pages:** 7–9
- **Source transcription:** [pages 6–10](../../source-inventory/pages-06-10.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** [Normalised Difference Vegetation Index (NDVI)](../../algorithms/remote-sensing/ndvi.md) (first audited spectral index; remaining entries are still unverified)

The source spans raw imagery correction, spectral transforms, classification, hyperspectral analysis, radar, point clouds, photogrammetry and biophysical retrieval. These methods operate at different stages of a sensor-to-product workflow; do not collapse them into one generic “remote sensing algorithm” category.

## First audited index

The [NDVI lesson](../../algorithms/remote-sensing/ndvi.md) defines the normalised red/NIR contrast and explains reflectance preprocessing, quality masks and interpretation limits. A tested NumPy implementation preserves invalid pixels, with an interactive lab. Other indices, calibration workflows, classification, SAR, LiDAR and photogrammetry remain open.

## Preprocessing and correction

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Atmospheric: dark object subtraction, 6S, MODTRAN, FLAASH, Sen2Cor, ocean color atmospheric correction | Atmospheric correction methods / models / software | 7 | Not checked — intake only |
| Topographic and BRDF: C-correction, SCS+C, Minnaert, Ross-Li, BRDF normalization | Topographic correction / reflectance modelling | 7 | Not checked — intake only |
| Relative normalization: IR-MAD, pseudo-invariant features, histogram matching, empirical line calibration | Radiometric normalisation / calibration methods | 7 | Not checked — intake only |
| Cloud and shadow masking: Fmask, s2cloudless, CloudSEN12-style models; sensor harmonization (HLS) | Masking algorithms / model families / harmonisation products | 8 | Not checked — intake only |
| Mosaicking, seamline detection (Voronoi, graph cut), color balancing, orthorectification, co-registration | Image assembly / seamline algorithms / geometric correction | 8 | Not checked — intake only |
| Fusion: pan-sharpening (Brovey, IHS, Gram-Schmidt, PCA, wavelet, CNN), spatiotemporal fusion, Bayesian and Kalman fusion, sub-pixel and super-resolution mapping | Image fusion methods / statistical methods / neural approaches | 8 | Not checked — intake only |

## Indices and transforms

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Vegetation and soil: NDVI, EVI, SAVI, NDRE, NDMI, LSWI, tasseled cap (Kauth-Thomas) | Spectral indices / transforms | 8 | Not checked — intake only |
| Water, burn, snow, urban: NDWI, MNDWI, AWEI, NBR, dNBR, NDSI, NDBI | Spectral indices | 8 | Not checked — intake only |
| Transforms: PCA, minimum noise fraction (MNF), Fourier, wavelet, Hough, Radon | Statistical and signal transforms | 8 | Not checked — intake only |
| Texture and edges: GLCM, Gabor, Sobel, Canny, mathematical morphology, SIFT, SURF | Texture measures / filters / feature detectors and descriptors | 8 | Not checked — intake only |
| Thresholding: Otsu, adaptive; Stumpf bathymetry; OC4 chlorophyll | Thresholding methods / retrieval algorithms | 8 | Not checked — intake only |
| Compositing: best-pixel, medoid, maximum NDVI | Image compositing rules | 8 | Not checked — intake only |

## Classification and segmentation

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Pixel-based: maximum likelihood, SVM, random forest, XGBoost, LightGBM, stacked generalization, k-means, ISODATA | Classification models / ensemble methods / clustering | 8 | Not checked — intake only |
| Segmentation: watershed, SLIC superpixels, mean shift, region growing, multiresolution segmentation, graph cuts, MRF and CRF, active contours, level sets | Segmentation algorithms / optimisation and probabilistic models | 8 | Not checked — intake only |
| Object-based image analysis (OBIA) | Analysis workflow / method family | 8 | Not checked — intake only |
| Time-series classification: TempCNN, Transformer, InceptionTime, TimeMatch, DTW, TWDTW | Time-series models / matching methods | 8 | Not checked — intake only |
| Change detection: differencing, CVA, post-classification, IR-MAD, Siamese networks, ChangeFormer | Change-detection methods / model families | 8 | Not checked — intake only |
| Fractional cover: spectral mixture analysis, regression trees, vegetation continuous fields | Spectral unmixing / regression / derived products | 8 | Not checked — intake only |

## Hyperspectral

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Endmember extraction (N-FINDR, PPI, VCA), unmixing (FCLS, sparse, nonlinear, deep) | Endmember extraction / spectral unmixing methods | 8 | Not checked — intake only |
| Anomaly and target detection: RX, Kernel RX, matched filter, CEM, ACE, subspace methods | Detection algorithms / statistical methods | 8 | Not checked — intake only |
| Spectral angle mapper, spectral information divergence, band selection, continuum removal, absorption feature analysis, red-edge position | Spectral similarity measures / feature selection / spectral analysis | 8 | Not checked — intake only |

## SAR and InSAR

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Speckle filtering, polarimetric decomposition (H/A/alpha, Freeman-Durden, Yamaguchi), CFAR detection, SAR-to-optical translation | Filtering / decomposition methods / detection / translation models | 8 | Not checked — intake only |
| InSAR: PS-InSAR, SBAS, SqueeSAR, distributed scatterers, phase unwrapping (SNAPHU, minimum cost flow), coherence change detection, offset tracking, tomographic SAR, autofocus | Interferometric processing workflows / algorithms / software | 9 | Not checked — intake only |

## LiDAR and point clouds

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Ground filtering: CSF, progressive morphological; ICP registration; RANSAC shape fitting | Point-cloud filtering / registration / model fitting | 9 | Not checked — intake only |
| Tree segmentation (local maxima, watershed, Dalponte), canopy height models, crown delineation | Segmentation methods / derived surface models | 9 | Not checked — intake only |
| Classification, voxelization, strip adjustment, GEDI waveform processing, ICESat-2 ground photon classification | Point-cloud processing / sensor-specific workflows | 9 | Not checked — intake only |
| Deep point networks: PointNet, PointNet++, KPConv, Point Transformer, RandLA-Net, MinkowskiNet | Neural network architectures for point clouds | 9 | Not checked — intake only |

## Photogrammetry and 3D

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Structure from Motion (COLMAP), bundle adjustment, aerial triangulation, GCP and IMU-aided adjustment, direct georeferencing | Photogrammetric workflows / optimisation / software | 9 | Not checked — intake only |
| Dense matching: SGM, PatchMatch, multi-view stereo; RPC sensor models; satellite stereo DSM; DSM, DTM and nDSM derivation | Stereo matching algorithms / sensor models / surface products | 9 | Not checked — intake only |
| Lens calibration (Brown-Conrady), boresight calibration, orthomosaic generation, mesh texturing | Calibration methods / production workflows | 9 | Not checked — intake only |
| Surface reconstruction: Poisson, marching cubes, mesh simplification, 3D alpha shapes, NeRF, 3D Gaussian splatting | Surface reconstruction / mesh algorithms / neural representations | 9 | Not checked — intake only |

## Biophysical and geophysical retrieval

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Evapotranspiration and energy balance: SEBAL, METRIC, SEBS, ALEXI, Penman-Monteith, Hargreaves; land surface temperature (split-window, temperature-emissivity separation) | Energy-balance models / evapotranspiration and temperature retrieval | 9 | Not checked — intake only |
| Productivity and structure: light-use efficiency GPP, biomass allometry, LAI and fAPAR retrieval, soil moisture retrieval, albedo | Biophysical retrieval methods / allometric models / products | 9 | Not checked — intake only |
| Water and atmosphere: Case 2 water quality inversion, aerosol retrieval (dark target, MAIAC), DOAS trace gases, cloud property retrieval | Inversion and retrieval methods | 9 | Not checked — intake only |
| Cryosphere and ocean: sea ice concentration (NASA Team, Bootstrap), ice motion, glacier velocity, DEM differencing, eddy detection (Okubo-Weiss), SST fronts, altimetry processing | Retrieval / motion estimation / ocean analysis methods | 9 | Not checked — intake only |
| Thermal and fire: thermal anomaly and volcanic hotspot detection, active fire detection, burned area (MCD64A1) | Detection algorithms / products | 9 | Not checked — intake only |

## Decisions for the next pass

1. Keep sensor correction, feature extraction, classification, change detection and retrieval as distinct stages.
2. Record sensor, band configuration, spatial and temporal resolution, atmospheric assumptions and preprocessing.
3. Distinguish an algorithm from a named software package, product, dataset or model architecture.
4. Verify recent neural architectures and product names against original papers and maintainer sources.
5. Include conventional baselines and independent validation when evaluating learned methods.
