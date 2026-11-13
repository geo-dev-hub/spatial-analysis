# Section 15 — Additions: vision backbones, registration, vector extraction, hydrology ML

- **Original source section:** 15
- **Source pages:** 31–33
- **Source transcription:** [pages 31–35](../../source-inventory/pages-31-35.md)
- **Review state:** intake extracted; names are explicitly described by the source as representative and from memory
- **Current canonical records:** none yet

**Source caution:** the compendium says model and method names in this section are representative and from memory. Verify current names, papers, code, datasets and licences before citation.

## Vision backbones, promptable and open-vocabulary tools

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Backbones: SegFormer, HRNet, Mask DINO, Video Swin, TimeSformer, ViViT, VideoMAE for satellite image time series, Perceiver IO, MLP-Mixer, ConvMixer | Vision and video model architectures | 31 | Captured; names not individually verified |
| Promptable segmentation: SAM variants (SAM-HQ, MobileSAM, EfficientSAM), Grounded-SAM, CLIPSeg | Promptable and open-vocabulary segmentation systems | 31 | Captured; names not individually verified |
| Open-vocabulary detection and grounding: Grounding DINO, OWL-ViT, Florence-2, remote sensing adaptations (LAE-DINO, OpenRSD) | Detection and grounding architectures / adaptations | 31 | Captured; names not individually verified |
| Monocular depth and height estimation: Depth Anything-style models adapted to overhead imagery | Depth and height estimation models | 31 | Captured; names not individually verified |

## Hyperspectral deep learning

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Classification: 3D-CNN, HybridSN, SSRN, SpectralFormer, spectral-spatial transformers, graph convolution on superpixels | Hyperspectral classification architectures | 31 | Captured; names not individually verified |
| Unmixing autoencoders: EndNet, DAEN, uDAS-style models; physically constrained unmixing networks | Spectral unmixing models | 31 | Captured; names not individually verified |
| Denoising and super-resolution: low-rank and tensor-based denoising, HSI-DeNet, hyperspectral-multispectral fusion networks | Denoising and fusion methods | 31 | Captured; names not individually verified |
| Complex-valued CNNs for polarimetric SAR, PolSAR classification networks | Complex-valued neural architectures / radar classification | 31 | Captured; names not individually verified |

## Point cloud deep learning, registration and building reconstruction

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Self-supervised and large backbones: Point-BERT, Point-MAE, PointMLP, PointNeXt, SPVCNN, Cylinder3D, Point Transformer V3, Sonata | Point-cloud representation and segmentation architectures | 31 | Captured; names not individually verified |
| Aerial LiDAR segmentation benchmarks: DALES, SensatUrban, Toronto-3D | Benchmark datasets | 31 | Captured; names not individually verified |
| Registration: point-to-plane ICP, generalized ICP, NDT, colored ICP, FPFH with RANSAC, TEASER++, deep registration (DCP, PointNetLK, GeoTransformer) | Point-cloud registration algorithms | 31 | Captured; names not individually verified |
| Building reconstruction: PolyFit, City3D, 2.5D dual contouring, roof plane segmentation (RANSAC, region growing), LoD2 generation, implicit surfaces (DeepSDF, occupancy networks) | Building reconstruction / geometric fitting / neural representations | 31 | Captured; names not individually verified |

## Image matching and multimodal registration

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Classical features: SIFT, ORB, AKAZE; phase correlation, ECC, mutual information registration | Feature detection and image registration methods | 31 | Captured; names not individually verified |
| Learned matching: SuperPoint with SuperGlue or LightGlue, LoFTR, DKM, RoMa, multimodal matchers (MINIMA) | Learned feature matching and registration architectures | 31 | Captured; names not individually verified |
| Optical-SAR matching: RIFT, HOPC, CFOG, OS-SIFT, deep cross-modal descriptors | Cross-modal matching methods | 31 | Captured; names not individually verified |
| Dense optical flow and sub-pixel displacement: COSI-Corr-style correlation, deep flow for glacier and landslide motion | Displacement estimation / optical flow workflows | 32 | Captured; names not individually verified |

## Road, building and polygon extraction

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Road graph extraction: Sat2Graph, RNGDet, iCurb, RoadTracer, lane graph inference | Road and network extraction architectures | 32 | Captured; names not individually verified |
| Polygon and frame-field methods: PolyRNN, Pix2Poly, frame field learning, HiSup, P2PFormer | Polygon and boundary extraction models | 32 | Captured; names not individually verified |
| Evaluation: APLS, TOPO, junction F1, boundary IoU, polygon similarity and vertex-based metrics | Geospatial extraction evaluation metrics | 32 | Captured; names not individually verified |
| Map inference from GPS traces: kernel density methods, trace merging, clustering-based, incremental, deep map generation (DeepMG, kharita) | Map inference and road-network reconstruction workflows | 32 | Captured; names not individually verified |

## Bayesian spatial clustering and partition models

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Potts-model priors, Voronoi tessellation priors, product partition models, spatial Dirichlet process mixtures | Bayesian spatial clustering and partition models | 32 | Captured; names not individually verified |
| Bayesian cluster detection (BaySTDetect), spatially varying finite mixtures, reversible-jump MCMC for change in partition | Bayesian cluster detection / mixture and partition inference | 32 | Captured; names not individually verified |
| Bayesian spatial change-point models and boundary detection | Bayesian spatial change-point and boundary models | 32 | Captured; names not individually verified |

## Hydrology machine learning

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Streamflow LSTMs, CAMELS-based training, regional models for ungauged basins, transformer and graph-based flood forecasting | Hydrological forecasting architectures / datasets and regionalisation | 32 | Captured; names not individually verified |
| Differentiable hydrology: HBV-style differentiable models, differentiable parameter learning, neural ODEs for catchments | Differentiable process models / parameter learning | 32 | Captured; names not individually verified |
| Operational flood forecasting pipelines, hybrid process-ML models, data assimilation with learned correctors | Forecasting systems / hybrid modelling and assimilation | 32 | Captured; names not individually verified |
| Ocean surrogates and ocean forecasting models, learned wave and surge emulators | Ocean emulation and forecasting models | 32 | Captured; names not individually verified |

## Image geolocation

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Cell classification over S2 or H3 cells with hierarchical heads, contrastive image-location training, retrieval plus refinement (PIGEON, G3, StreetCLIP) | Image geolocation / retrieval and classification models | 32 | Captured; names not individually verified |
| Evaluation with distance-threshold accuracy, geographic bias audits, adversarial robustness and privacy risk analysis | Geolocation evaluation / fairness and privacy assessment | 32 | Captured; names not individually verified |

## Onboard and edge intelligence

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Onboard cloud screening (CloudScout-style), low-power CNN accelerators for satellites, event-triggered downlink | Onboard inference / hardware and data-transfer workflows | 32 | Captured; names not individually verified |
| Model update strategies for in-orbit inference, quantized models for UAV payloads | Model deployment and update methods | 32 | Captured; names not individually verified |

## Renewable energy forecasting

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Solar nowcasting from satellite imagery and sky cameras, irradiance forecasting, PV power estimation | Solar nowcasting and energy prediction methods | 33 | Captured; names not individually verified |
| Wind power forecasting with graph neural networks, spatiotemporal ensembles, probabilistic forecasting for grid operations | Wind forecasting architectures / probabilistic prediction | 33 | Captured; names not individually verified |

## Decisions for the next pass

1. Verify every model name and release before citation.
2. Distinguish a benchmark dataset from a model architecture and an evaluation metric.
3. Report registration accuracy, geometric consistency and spatial distribution of control points.
4. Evaluate extracted road and building geometry topologically, not only by pixel overlap.
5. For hydrology ML, record basin splits, temporal splits, climate regimes and process-model baselines.
