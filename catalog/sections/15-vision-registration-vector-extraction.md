# Section 15 — Additions: vision backbones, registration, vector extraction, hydrology ML

- **Original source section:** 15
- **Source pages:** 31–33
- **Source transcription:** [pages 31–35](../../source-inventory/pages-31-35.md)
- **Review state:** intake extracted; names are explicitly described by the source as representative and from memory
- **Current canonical records:** none yet

**Source caution:** the compendium says model and method names in this section are representative and from memory. Verify current names, papers, code, datasets and licences before citation.

## Vision backbones, promptable and open-vocabulary tools

| Source entry | Kind to review | Source page |
|---|---|---:|
| Backbones: SegFormer, HRNet, Mask DINO, Video Swin, TimeSformer, ViViT, VideoMAE for satellite image time series, Perceiver IO, MLP-Mixer, ConvMixer | Vision and video model architectures | 31 |
| Promptable segmentation: SAM variants (SAM-HQ, MobileSAM, EfficientSAM), Grounded-SAM, CLIPSeg | Promptable and open-vocabulary segmentation systems | 31 |
| Open-vocabulary detection and grounding: Grounding DINO, OWL-ViT, Florence-2, remote sensing adaptations (LAE-DINO, OpenRSD) | Detection and grounding architectures / adaptations | 31 |
| Monocular depth and height estimation: Depth Anything-style models adapted to overhead imagery | Depth and height estimation models | 31 |

## Hyperspectral deep learning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Classification: 3D-CNN, HybridSN, SSRN, SpectralFormer, spectral-spatial transformers, graph convolution on superpixels | Hyperspectral classification architectures | 31 |
| Unmixing autoencoders: EndNet, DAEN, uDAS-style models; physically constrained unmixing networks | Spectral unmixing models | 31 |
| Denoising and super-resolution: low-rank and tensor-based denoising, HSI-DeNet, hyperspectral-multispectral fusion networks | Denoising and fusion methods | 31 |
| Complex-valued CNNs for polarimetric SAR, PolSAR classification networks | Complex-valued neural architectures / radar classification | 31 |

## Point cloud deep learning, registration and building reconstruction

| Source entry | Kind to review | Source page |
|---|---|---:|
| Self-supervised and large backbones: Point-BERT, Point-MAE, PointMLP, PointNeXt, SPVCNN, Cylinder3D, Point Transformer V3, Sonata | Point-cloud representation and segmentation architectures | 31 |
| Aerial LiDAR segmentation benchmarks: DALES, SensatUrban, Toronto-3D | Benchmark datasets | 31 |
| Registration: point-to-plane ICP, generalized ICP, NDT, colored ICP, FPFH with RANSAC, TEASER++, deep registration (DCP, PointNetLK, GeoTransformer) | Point-cloud registration algorithms | 31 |
| Building reconstruction: PolyFit, City3D, 2.5D dual contouring, roof plane segmentation (RANSAC, region growing), LoD2 generation, implicit surfaces (DeepSDF, occupancy networks) | Building reconstruction / geometric fitting / neural representations | 31 |

## Image matching and multimodal registration

| Source entry | Kind to review | Source page |
|---|---|---:|
| Classical features: SIFT, ORB, AKAZE; phase correlation, ECC, mutual information registration | Feature detection and image registration methods | 31 |
| Learned matching: SuperPoint with SuperGlue or LightGlue, LoFTR, DKM, RoMa, multimodal matchers (MINIMA) | Learned feature matching and registration architectures | 31 |
| Optical-SAR matching: RIFT, HOPC, CFOG, OS-SIFT, deep cross-modal descriptors | Cross-modal matching methods | 31 |
| Dense optical flow and sub-pixel displacement: COSI-Corr-style correlation, deep flow for glacier and landslide motion | Displacement estimation / optical flow workflows | 32 |

## Road, building and polygon extraction

| Source entry | Kind to review | Source page |
|---|---|---:|
| Road graph extraction: Sat2Graph, RNGDet, iCurb, RoadTracer, lane graph inference | Road and network extraction architectures | 32 |
| Polygon and frame-field methods: PolyRNN, Pix2Poly, frame field learning, HiSup, P2PFormer | Polygon and boundary extraction models | 32 |
| Evaluation: APLS, TOPO, junction F1, boundary IoU, polygon similarity and vertex-based metrics | Geospatial extraction evaluation metrics | 32 |
| Map inference from GPS traces: kernel density methods, trace merging, clustering-based, incremental, deep map generation (DeepMG, kharita) | Map inference and road-network reconstruction workflows | 32 |

## Bayesian spatial clustering and partition models

| Source entry | Kind to review | Source page |
|---|---|---:|
| Potts-model priors, Voronoi tessellation priors, product partition models, spatial Dirichlet process mixtures | Bayesian spatial clustering and partition models | 32 |
| Bayesian cluster detection (BaySTDetect), spatially varying finite mixtures, reversible-jump MCMC for change in partition | Bayesian cluster detection / mixture and partition inference | 32 |
| Bayesian spatial change-point models and boundary detection | Bayesian spatial change-point and boundary models | 32 |

## Hydrology machine learning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Streamflow LSTMs, CAMELS-based training, regional models for ungauged basins, transformer and graph-based flood forecasting | Hydrological forecasting architectures / datasets and regionalisation | 32 |
| Differentiable hydrology: HBV-style differentiable models, differentiable parameter learning, neural ODEs for catchments | Differentiable process models / parameter learning | 32 |
| Operational flood forecasting pipelines, hybrid process-ML models, data assimilation with learned correctors | Forecasting systems / hybrid modelling and assimilation | 32 |
| Ocean surrogates and ocean forecasting models, learned wave and surge emulators | Ocean emulation and forecasting models | 32 |

## Image geolocation

| Source entry | Kind to review | Source page |
|---|---|---:|
| Cell classification over S2 or H3 cells with hierarchical heads, contrastive image-location training, retrieval plus refinement (PIGEON, G3, StreetCLIP) | Image geolocation / retrieval and classification models | 32 |
| Evaluation with distance-threshold accuracy, geographic bias audits, adversarial robustness and privacy risk analysis | Geolocation evaluation / fairness and privacy assessment | 32 |

## Onboard and edge intelligence

| Source entry | Kind to review | Source page |
|---|---|---:|
| Onboard cloud screening (CloudScout-style), low-power CNN accelerators for satellites, event-triggered downlink | Onboard inference / hardware and data-transfer workflows | 32 |
| Model update strategies for in-orbit inference, quantized models for UAV payloads | Model deployment and update methods | 32 |

## Renewable energy forecasting

| Source entry | Kind to review | Source page |
|---|---|---:|
| Solar nowcasting from satellite imagery and sky cameras, irradiance forecasting, PV power estimation | Solar nowcasting and energy prediction methods | 33 |
| Wind power forecasting with graph neural networks, spatiotemporal ensembles, probabilistic forecasting for grid operations | Wind forecasting architectures / probabilistic prediction | 33 |

## Decisions for the next pass

1. Verify every model name and release before citation.
2. Distinguish a benchmark dataset from a model architecture and an evaluation metric.
3. Report registration accuracy, geometric consistency and spatial distribution of control points.
4. Evaluate extracted road and building geometry topologically, not only by pixel overlap.
5. For hydrology ML, record basin splits, temporal splits, climate regimes and process-model baselines.
