# Section 15 — Additions: vision backbones, registration, vector extraction, hydrology ML

- **Original source section:** 15
- **Source pages:** 31–33
- **Source transcription:** [pages 31–35](../../source-inventory/pages-31-35.md)
- **Review state:** intake extracted; names are explicitly described by the source as representative and from memory
- **Current canonical records:** none yet

**Source caution:** the compendium says model and method names in this section are representative and from memory. Verify current names, papers, code, datasets and licences before citation.

## Vision backbones, promptable and open-vocabulary tools

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Backbones: SegFormer, HRNet, Mask DINO, Video Swin, TimeSformer, ViViT, VideoMAE for satellite image time series, Perceiver IO, MLP-Mixer, ConvMixer | Vision and video model architectures | 31  Not checked — intake only |
| Promptable segmentation: SAM variants (SAM-HQ, MobileSAM, EfficientSAM), Grounded-SAM, CLIPSeg | Promptable and open-vocabulary segmentation systems | 31  Not checked — intake only |
| Open-vocabulary detection and grounding: Grounding DINO, OWL-ViT, Florence-2, remote sensing adaptations (LAE-DINO, OpenRSD) | Detection and grounding architectures / adaptations | 31  Not checked — intake only |
| Monocular depth and height estimation: Depth Anything-style models adapted to overhead imagery | Depth and height estimation models | 31  Not checked — intake only |

## Hyperspectral deep learning

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Classification: 3D-CNN, HybridSN, SSRN, SpectralFormer, spectral-spatial transformers, graph convolution on superpixels | Hyperspectral classification architectures | 31  Not checked — intake only |
| Unmixing autoencoders: EndNet, DAEN, uDAS-style models; physically constrained unmixing networks | Spectral unmixing models | 31  Not checked — intake only |
| Denoising and super-resolution: low-rank and tensor-based denoising, HSI-DeNet, hyperspectral-multispectral fusion networks | Denoising and fusion methods | 31  Not checked — intake only |
| Complex-valued CNNs for polarimetric SAR, PolSAR classification networks | Complex-valued neural architectures / radar classification | 31  Not checked — intake only |

## Point cloud deep learning, registration and building reconstruction

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Self-supervised and large backbones: Point-BERT, Point-MAE, PointMLP, PointNeXt, SPVCNN, Cylinder3D, Point Transformer V3, Sonata | Point-cloud representation and segmentation architectures | 31  Not checked — intake only |
| Aerial LiDAR segmentation benchmarks: DALES, SensatUrban, Toronto-3D | Benchmark datasets | 31  Not checked — intake only |
| Registration: point-to-plane ICP, generalized ICP, NDT, colored ICP, FPFH with RANSAC, TEASER++, deep registration (DCP, PointNetLK, GeoTransformer) | Point-cloud registration algorithms | 31  Not checked — intake only |
| Building reconstruction: PolyFit, City3D, 2.5D dual contouring, roof plane segmentation (RANSAC, region growing), LoD2 generation, implicit surfaces (DeepSDF, occupancy networks) | Building reconstruction / geometric fitting / neural representations | 31  Not checked — intake only |

## Image matching and multimodal registration

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Classical features: SIFT, ORB, AKAZE; phase correlation, ECC, mutual information registration | Feature detection and image registration methods | 31  Not checked — intake only |
| Learned matching: SuperPoint with SuperGlue or LightGlue, LoFTR, DKM, RoMa, multimodal matchers (MINIMA) | Learned feature matching and registration architectures | 31  Not checked — intake only |
| Optical-SAR matching: RIFT, HOPC, CFOG, OS-SIFT, deep cross-modal descriptors | Cross-modal matching methods | 31  Not checked — intake only |
| Dense optical flow and sub-pixel displacement: COSI-Corr-style correlation, deep flow for glacier and landslide motion | Displacement estimation / optical flow workflows | 32  Not checked — intake only |

## Road, building and polygon extraction

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Road graph extraction: Sat2Graph, RNGDet, iCurb, RoadTracer, lane graph inference | Road and network extraction architectures | 32  Not checked — intake only |
| Polygon and frame-field methods: PolyRNN, Pix2Poly, frame field learning, HiSup, P2PFormer | Polygon and boundary extraction models | 32  Not checked — intake only |
| Evaluation: APLS, TOPO, junction F1, boundary IoU, polygon similarity and vertex-based metrics | Geospatial extraction evaluation metrics | 32  Not checked — intake only |
| Map inference from GPS traces: kernel density methods, trace merging, clustering-based, incremental, deep map generation (DeepMG, kharita) | Map inference and road-network reconstruction workflows | 32  Not checked — intake only |

## Bayesian spatial clustering and partition models

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Potts-model priors, Voronoi tessellation priors, product partition models, spatial Dirichlet process mixtures | Bayesian spatial clustering and partition models | 32  Not checked — intake only |
| Bayesian cluster detection (BaySTDetect), spatially varying finite mixtures, reversible-jump MCMC for change in partition | Bayesian cluster detection / mixture and partition inference | 32  Not checked — intake only |
| Bayesian spatial change-point models and boundary detection | Bayesian spatial change-point and boundary models | 32  Not checked — intake only |

## Hydrology machine learning

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Streamflow LSTMs, CAMELS-based training, regional models for ungauged basins, transformer and graph-based flood forecasting | Hydrological forecasting architectures / datasets and regionalisation | 32  Not checked — intake only |
| Differentiable hydrology: HBV-style differentiable models, differentiable parameter learning, neural ODEs for catchments | Differentiable process models / parameter learning | 32  Not checked — intake only |
| Operational flood forecasting pipelines, hybrid process-ML models, data assimilation with learned correctors | Forecasting systems / hybrid modelling and assimilation | 32  Not checked — intake only |
| Ocean surrogates and ocean forecasting models, learned wave and surge emulators | Ocean emulation and forecasting models | 32  Not checked — intake only |

## Image geolocation

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Cell classification over S2 or H3 cells with hierarchical heads, contrastive image-location training, retrieval plus refinement (PIGEON, G3, StreetCLIP) | Image geolocation / retrieval and classification models | 32  Not checked — intake only |
| Evaluation with distance-threshold accuracy, geographic bias audits, adversarial robustness and privacy risk analysis | Geolocation evaluation / fairness and privacy assessment | 32  Not checked — intake only |

## Onboard and edge intelligence

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Onboard cloud screening (CloudScout-style), low-power CNN accelerators for satellites, event-triggered downlink | Onboard inference / hardware and data-transfer workflows | 32  Not checked — intake only |
| Model update strategies for in-orbit inference, quantized models for UAV payloads | Model deployment and update methods | 32  Not checked — intake only |

## Renewable energy forecasting

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Solar nowcasting from satellite imagery and sky cameras, irradiance forecasting, PV power estimation | Solar nowcasting and energy prediction methods | 33  Not checked — intake only |
| Wind power forecasting with graph neural networks, spatiotemporal ensembles, probabilistic forecasting for grid operations | Wind forecasting architectures / probabilistic prediction | 33  Not checked — intake only |

## Decisions for the next pass

1. Verify every model name and release before citation.
2. Distinguish a benchmark dataset from a model architecture and an evaluation metric.
3. Report registration accuracy, geometric consistency and spatial distribution of control points.
4. Evaluate extracted road and building geometry topologically, not only by pixel overlap.
5. For hydrology ML, record basin splits, temporal splits, climate regimes and process-model baselines.
