# Section 11 — Additions: GeoAI, GeoFMs and computer vision

- **Original source section:** 11
- **Source pages:** 23–24
- **Source transcription:** [pages 21–25](../../source-inventory/pages-21-25.md)
- **Review state:** intake extracted; names are explicitly described by the source as representative and not verified against current releases
- **Current canonical records:** none yet

**Source caution:** this section says its model names are representative and not verified against current releases. Keep that warning attached to every downstream research task. Verify model existence, exact naming, publication, release date, code and dataset licences before citation.

## More GeoFM families and pretraining recipes

| Source entry | Kind to review | Source page |
|---|---|---:|
| Optical and multispectral: Prithvi-EO-2.0, SatMAE++, RingMo, RVSA, SatViT, USat, SMARTIES, DeCUR, FoMo, THOR, RoMA, SkySense++ | Foundation-model and pretraining families | 23 |
| Multimodal and multi-sensor: OmniSat, MMEarth (pretext tasks from auxiliary geographic data), SSL4EO-S12, DOFA-CLIP, Hydra-style multi-head pretraining | Multimodal model families / datasets / pretraining approaches | 23 |
| Time-series and temporal: EarthPT, TESSERA, Presto, SITS-Former, pixel-wise transformers for satellite image time series | Time-series model families | 23 |
| Mamba and linear-attention variants for hyperspectral and large-scene encoders (HyperSIGMA, Samba) | Efficient neural architectures | 23 |
| Pretraining datasets: SSL4EO-S12, MMEarth, Satlas, fMoW, BigEarthNet, SEN12MS, Major TOM, GeoPile | Pretraining datasets / data collections | 23 |

## Detection, tracking and counting

| Source entry | Kind to review | Source page |
|---|---|---:|
| Oriented detection: Gliding Vertex, S2A-Net, R3Det, LSKNet, Oriented RepPoints, ReDet | Oriented object detection architectures | 23 |
| Small-object detection and slicing: SAHI, tile-based inference, multi-scale feature fusion | Detection workflow / inference and feature-fusion methods | 23 |
| Video and tracking: SORT, DeepSORT, ByteTrack, satellite video object tracking, vehicle counting, crowd density estimation | Object tracking algorithms / counting and density estimation | 23 |
| Instance, panoptic and keypoint tasks: Mask R-CNN, Mask2Former, panoptic FPN, building roof keypoints, centerline and road graph extraction | Instance and panoptic segmentation / keypoint and graph extraction | 23 |

## Vision-language and multimodal additions

| Source entry | Kind to review | Source page |
|---|---|---:|
| Remote sensing VLMs: SkySenseGPT, GeoPixel, GeoGround, EarthMind, GeoLLaVA-style models; image-text corpora such as RS5M | Vision-language models / image-text datasets | 23 |
| Pixel-level grounding, change captioning, multi-temporal VQA, visual question answering over multispectral and SAR inputs | Multimodal tasks / evaluation tasks | 23 |
| Multimodal LLM agents that call segmentation and detection models as tools | Agent architectures / tool-use workflows | 23 |

## Neural combinatorial optimization and reinforcement learning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Attention models and POMO for TSP and VRP, GNN-based heuristics, learned neighborhood search | Neural combinatorial optimisation / learned heuristics | 24 |
| Reinforcement learning for traffic signal control (max pressure baselines, DQN, PPO), ride-hailing dispatch, spatial crowdsourcing assignment, ambulance relocation | Reinforcement-learning applications / dispatch and allocation problems | 24 |
| Learned routing and ETA models: GNN-based travel time, transformer-based route recommendation | Learned routing and travel-time models | 24 |

## Generative and probabilistic models for Earth observation

| Source entry | Kind to review | Source page |
|---|---|---:|
| Diffusion for cloud removal, super-resolution, gap filling, and controllable synthetic scene generation | Generative image models / restoration and synthesis tasks | 24 |
| Flow matching and consistency models for fast generation; latent diffusion in learned EO tokenizers | Generative modelling methods / representation tokenizers | 24 |
| Probabilistic forecasting heads: mixture density networks, normalizing flows, quantile regression networks | Probabilistic prediction methods | 24 |

## Benchmarks and datasets (representative)

| Source entry | Kind to review | Source page |
|---|---|---:|
| Segmentation and land cover: LoveDA, iSAID, Open-Earth-Map, SpaceNet, FLAIR, Sen1Floods11, HLS Burn Scars, So2Sat LCZ42, DynamicEarthNet | Benchmark datasets | 24 |
| Detection: DOTA, DIOR, xView, FAIR1M | Object-detection datasets | 24 |
| Multi-task GeoFM evaluation: PANGAEA, GEO-Bench, Copernicus-Bench | Evaluation suites / benchmark datasets | 24 |
| Weather and climate: WeatherBench 2, SEVIR, ClimateBench, ERA5-based training sets | Weather and climate datasets / benchmarks | 24 |

## Operational GeoAI engineering

| Source entry | Kind to review | Source page |
|---|---|---:|
| Data curation: tile deduplication, label noise audits, class-balanced geographic sampling, region-stratified splits | Dataset quality and sampling procedures | 24 |
| MLOps for imagery: dataset versioning, STAC-driven training pipelines, monitoring for temporal drift and sensor change | ML operations / data and model monitoring workflows | 24 |
| Human-in-the-loop mapping: active learning loops, interactive segmentation with SAM, quality scoring and review queues | Human-in-the-loop annotation and quality workflows | 24 |
| Evaluation under distribution shift: cross-continent splits, seasonal shift tests, sensor-swap tests, calibration drift checks | Geographic and temporal generalisation evaluation | 24 |

## Decisions for the next pass

1. Treat every model and dataset name as an unverified lead until checked.
2. Record original papers, release dates, model cards, code repositories, dataset terms and licence changes.
3. Distinguish a benchmark dataset from a benchmark protocol and from a model leaderboard.
4. Compare learned routing and allocation with established optimisation baselines.
5. Do not present this source list as a current ranking or complete inventory.
