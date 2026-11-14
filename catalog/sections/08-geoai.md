# Section 8 — GeoAI and geospatial foundation models

- **Original source section:** 8
- **Source pages:** 14–18
- **Source transcription:** [pages 11–15](../../source-inventory/pages-11-15.md) and [pages 16–20](../../source-inventory/pages-16-20.md)
- **Review state:** source entries extracted into this index; names and claims not yet individually verified
- **Current canonical records:** [Masked autoencoding](../../methods/masked-autoencoding.md) (scoped objective and masking mechanics); [Contrastive representation learning with NT-Xent](../../algorithms/geoai/contrastive-info-nce.md) (scoped objective lesson); [spatial cross-validation](../../methods/spatial-cross-validation.md) (validation foundation shared with Section 10). Neither record is a foundation-model catalogue.

The source explicitly says that model names are representative examples, not an exhaustive or verified catalogue. The first canonical record is a general contrastive objective lesson; it does not verify or reproduce any named geospatial foundation model. Preserve that warning. This section changes quickly: model names, benchmark results, datasets and deployment claims must be checked against original papers, official model cards and maintained project documentation before publication.

## First implemented learning records\n\nThe [GeoAI foundations learning path](../../learning-paths/geoai-foundations.md) begins with paired-view contrastive learning and NT-Xent. It makes spatial split leakage and geospatial augmentation assumptions explicit.\n\n## Spatial validity and evaluation foundation

The source identifies spatial block cross-validation, leave-location-out evaluation and autocorrelation-aware sampling as central GeoAI validity concerns. Start with the [spatial cross-validation lesson](../../methods/spatial-cross-validation.md) and its tested [Python implementation](../../implementations/python/spatial-cross-validation/README.md). It is a compact point-data teaching splitter, not a complete validation framework or a scientifically selected block design.

## Pretraining objectives

A first masked-autoencoding lesson now explains the encoder-visible/decoder-masked sequence and connects the general MAE idea to satellite-specific temporal, spectral and scale-aware adaptations. Its NumPy package demonstrates masking and inverse sequence restoration only; it does not train or reproduce MAE, SatMAE or Scale-MAE.

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Masked autoencoding: MAE, SatMAE (temporal and spectral grouping), Scale-MAE (GSD-aware encoding), SelectiveMAE, S2MAE, SpectralGPT (3D masking) | Self-supervised pretraining objectives / model families | 15  Not checked — intake only |
| Contrastive and self-distillation: SimCLR, MoCo, DINO, DINOv2, DINOv3, iBOT, BYOL, Barlow Twins, VICReg, SeCo, SSL4EO, CROMA, JEPA-style latent prediction | Self-supervised learning methods / model families | 15  Not checked — intake only |
| Image-text and image-location alignment: RemoteCLIP, GeoRSCLIP, SkyCLIP, SatCLIP, GeoCLIP, CSP | Cross-modal representation learning models | 15  Not checked — intake only |
| Multi-sensor and cross-modal masking: Galileo, DOFA, SkySense, Copernicus-FM, TerraMind, AnySat, Panopticon | Multimodal and multisensor model families | 15  Not checked — intake only |
| Embedding fields: AlphaEarth Foundations, Clay, TESSERA; pixel-timeseries models: Presto, Galileo, TiMo | Geospatial embedding models / time-series model families | 15  Not checked — intake only |
| Supervised and multi-task pretraining: SatlasPretrain, MTP, GFM-style continual pretraining, distillation | Pretraining workflows / multi-task learning / model compression | 15  Not checked — intake only |
| Weak supervision from land cover maps, OSM and geotagged text; deduplicated and stratified global tile sampling | Weak-supervision sources / data sampling and curation procedures | 15  Not checked — intake only |

## Architectures and encodings

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Backbones: ViT, Swin, hierarchical ViT, ConvNeXt, Mamba and state-space models (RS-Mamba, Samba), Perceiver-style encoders, mixture-of-experts | Neural architecture families | 15  Not checked — intake only |
| Prithvi-EO temporal ViT with 3D patch embeddings; U-TAE, L-TAE, PSE-TAE temporal attention | Remote-sensing model architectures / temporal attention | 15  Not checked — intake only |
| Channel and spectral handling: ChannelViT, hypernetwork-generated weights (DOFA), wavelength conditioning (FiLM, cross-attention), spectral-band tokens | Multispectral and hyperspectral encoding approaches | 15  Not checked — intake only |
| Positional encodings: 2D sin-cos, learned, RoPE, ALiBi, relative; GSD-aware; day-of-year and date embeddings | Positional and temporal encoding methods | 15  Not checked — intake only |
| Decoders and heads: UNet-style, UPerNet, ViTDet feature pyramids, linear and MLP probes | Decoder architectures / prediction heads / probing methods | 15  Not checked — intake only |
| Token handling for large scenes: windowed attention, token merging, token pruning, dynamic resolution, register tokens | Attention and token-efficiency methods | 15  Not checked — intake only |

## Adaptation and efficiency

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| LoRA, adapters (GeoAdapter), prompt tuning, visual prompt tuning, in-context learning, PEFT | Parameter-efficient adaptation methods | 15  Not checked — intake only |
| Few-shot and zero-shot, meta-learning (prototypical networks, MAML), open-set recognition, model merging, task arithmetic, continual learning | Transfer and adaptation settings / meta-learning / model composition | 16  Not checked — intake only |
| Compression: pruning, quantization-aware training, distillation to small students, on-board satellite inference, edge and UAV deployment | Model compression / deployment approaches | 16  Not checked — intake only |
| Training systems: mixed precision, gradient checkpointing, FSDP, DeepSpeed, flash attention, AdamW, LARS, layer-wise learning-rate decay, EMA teachers | Training infrastructure / optimisation methods | 16  Not checked — intake only |
| Tooling: TorchGeo, Terratorch, tiled and sliding-window inference with Gaussian blending, vector databases and embedding caches | Software libraries / inference workflows / retrieval infrastructure | 16  Not checked — intake only |

## Downstream tasks

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Segmentation: UNet, DeepLab, Mask2Former, UPerNet, SAM and SAM 2 adaptations (RSPrompter, SAMGeo) | Segmentation architectures / geospatial adaptations | 16  Not checked — intake only |
| Detection: Oriented R-CNN, RoI Transformer, ReDet, DETR variants, YOLO | Object detection architectures | 16  Not checked — intake only |
| Change detection: Siamese networks, ChangeFormer, BIT, SNUNet | Change-detection architectures and methods | 16  Not checked — intake only |
| Mapping tasks: cloud masking, flood and burn-scar mapping, crop type mapping, canopy height regression, building and road extraction (D-LinkNet, HRNet, RoadTracer), vectorization (PolyWorld, HiSup), field boundaries, monocular height and depth | Application tasks / model families / vector extraction methods | 16  Not checked — intake only |
| Super-resolution and generative: SRGAN, diffusion, DiffusionSat, CycleGAN, Pix2Pix, VAEs, VQGAN, cloud removal, sensor translation, synthetic data generation | Generative models / image translation and enhancement | 16  Not checked — intake only |
| Open-vocabulary and referring segmentation (SegEarth-OV) | Open-vocabulary segmentation model family | 16  Not checked — intake only |
| HD map construction and BEV perception: MapTR, VectorMapNet, BEVFormer | Mapping and bird's-eye-view perception architectures | 16  Not checked — intake only |
| Visual place recognition and geolocalization: NetVLAD, MixVPR, CosPlace, SALAD, PlaNet, StreetCLIP, G3, cross-view matching | Place-recognition / geolocalisation methods | 16  Not checked — intake only |

## Vision-language and agentic GeoAI

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Remote sensing VLMs: GeoChat, EarthGPT, LHRS-Bot, SkyEyeGPT, RSGPT, VHM, TEOChat, EarthDial; RemoteSAM, GeoSAM | Vision-language model families / segmentation systems | 16  Not checked — intake only |
| Captioning, VQA, visual grounding, reasoning benchmarks, chain-of-thought VLMs, reinforcement learning (GRPO-style) for geo-VLMs | Tasks / evaluation / reasoning and training methods | 16  Not checked — intake only |
| LLM agents: text-to-SQL and text-to-GIS (LLM-Geo, GeoAgent, GeoGPT), PyQGIS and GeoPandas code generation, tool-calling, MCP-based agents, GeoRAG, dense retrieval over layers and metadata | Agent workflows / code-generation / retrieval-augmented systems | 16  Not checked — intake only |
| Geographic knowledge probing (GeoLLM), LLM geolocation, geocoding with language models, toponym resolution, spatial reasoning and mental map prompting, vision-language navigation | Geographic reasoning / geocoding / navigation tasks | 16  Not checked — intake only |

## Location encoders and representation learning

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Space2Vec, Sphere2Vec, Theory, Grid, wrap and RBF encoders; spherical harmonics and Spherical Fourier Features; SINR for species ranges | Coordinate and location encodings / spatial representation methods | 17  Not checked — intake only |
| Multi-scale sinusoidal and random Fourier features, hyperbolic (Poincaré) embeddings | Representation and embedding methods | 17  Not checked — intake only |
| Tile2Vec, Place2Vec, Urban2Vec, Geo2Vec, H3 and geohash token embeddings | Spatial and place representation models / spatial indexing encodings | 17  Not checked — intake only |
| Graph embeddings: Node2Vec, DeepWalk, LINE, TransE and RotatE on geographic knowledge graphs | Graph representation learning methods | 17  Not checked — intake only |

## Spatiotemporal and Earth-system deep learning

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Graph models: GCN, GAT, GraphSAGE, TGN, spatiotemporal GCNs, GNN-based kriging (KCN, IGNNK, SATCN) | Graph neural networks / spatiotemporal models / kriging models | 17  Not checked — intake only |
| Sequence and field models: ConvLSTM, PredRNN, SimVP, Earthformer, neural ODEs, neural fields, implicit neural representations, neural point processes (Neural Hawkes) | Sequence models / dynamical systems / neural representations and point processes | 17  Not checked — intake only |
| Weather and climate: FourCastNet, Pangu-Weather, GraphCast, GenCast, FuXi, FengWu, Aurora, ClimaX, Prithvi WxC, NeuralGCM, NowcastNet, DGMR, MetNet | Weather and climate model architectures | 17  Not checked — intake only |
| Neural operators and physics-informed: FNO, DeepONet, PINNs; diffusion and flow-matching downscaling (CorrDiff); world models and Earth-system emulators | Neural operators / physics-informed learning / generative downscaling | 17  Not checked — intake only |
| 3D and equivariant: spherical CNNs, DeepSphere, icosahedral and HEALPix convolutions, equivariant message passing, 3D Gaussian splatting | Spherical and equivariant architectures / 3D representations | 17  Not checked — intake only |

## Spatial ML and hybrid statistics

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Geographically weighted random forest, RFsp, spatial stacking, kriging plus ML residuals, spatial KNN, GNNWR, GWNN, deep kriging, deep GP, neural Gaussian processes, Spatial Lag Neural Networks, TabPFN on spatial features | Spatial machine-learning methods / hybrid statistical models | 17  Not checked — intake only |
| Spatial feature engineering: buffer statistics, distance to features, lag features | Feature-engineering procedures | 17  Not checked — intake only |
| Weak-label methods: positive-unlabeled learning, one-class SVM, noisy-label learning, semi-supervised (FixMatch), active learning | Weak and semi-supervised learning methods | 17  Not checked — intake only |
| Physics-guided hybrids: LSTM plus process models in hydrology and crop modeling | Hybrid process and machine-learning models | 17  Not checked — intake only |

## Losses, augmentation, evaluation

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Losses: Dice, Tversky, focal, Lovász-softmax, class-balanced cross-entropy, boundary and distance-transform loss, clDice, Huber, quantile and pinball | Loss functions | 17  Not checked — intake only |
| Augmentation: rotation, flip, scale jitter, CutMix, mosaic, copy-paste, spectral jitter, band dropout, cloud and shadow simulation, test-time augmentation | Data augmentation / inference-time procedures | 17  Not checked — intake only |
| Metrics: OA, F1, IoU and mIoU, Dice, kappa, mAP with rotated IoU, boundary F-score, panoptic quality, RMSE, MAE, R², NSE, KGE, CRPS, ECE | Evaluation metrics | 17  Not checked — intake only |
| Embedding quality: linear probing, k-NN, retrieval recall@k, clustering NMI | Representation evaluation methods | 17  Not checked — intake only |
| Benchmarks: GEO-Bench, PANGAEA, Satlas, fMoW, BigEarthNet, EuroSAT | Benchmark suites / datasets | 17  Not checked — intake only |

## Spatial validity, uncertainty and interpretability

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Spatial block cross-validation, leave-location-out, autocorrelation-aware sampling and loss | Spatial validation and sampling procedures | 18  Not checked — intake only |
| Domain adaptation (DANN, CORAL), test-time adaptation, covariate shift correction, importance weighting, out-of-distribution detection, area of applicability | Domain adaptation / robustness and applicability diagnostics | 18  Not checked — intake only |
| Uncertainty: MC dropout, deep ensembles, conformal prediction, evidential deep learning, Bayesian neural networks, SWAG, Laplace approximation, temperature scaling | Predictive uncertainty and calibration methods | 18  Not checked — intake only |
| Explainability: SHAP, GeoShapley, LIME, Grad-CAM, integrated gradients, attention rollout, TCAV, probing, spatial partial dependence, ALE, counterfactuals | Explainability and interpretability methods | 18  Not checked — intake only |
| Fairness: geographic generalization gaps, spatial fairness metrics, coverage audits for training data, label scarcity in the Global South | Fairness evaluation / data coverage audits | 18  Not checked — intake only |
| Federated and privacy-preserving training; scaling laws for Earth observation models | Privacy-preserving learning / scaling analysis | 18  Not checked — intake only |

## Decisions for the next pass

1. Verify each model name, paper, release date, licence, dataset and benchmark before treating it as a fact.
2. Separate architecture, pretraining objective, downstream task, training recipe, software and benchmark.
3. Report geographic and temporal generalisation, not only random tile splits.
4. Compare foundation models with transparent baselines and task-specific models.
5. Record sensor, spatial resolution, temporal coverage, training data provenance and inference constraints.
6. Keep the source warning visible: this is a representative intake list, not a verified ranking or exhaustive catalogue.
