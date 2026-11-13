# Section 13 — Additions: GeoFM workflows, urban and mobility foundation models, geo-LLMs

- **Original source section:** 13
- **Source pages:** 26–28
- **Source transcription:** [pages 26–30](../../source-inventory/pages-26-30.md)
- **Review state:** intake extracted; names are explicitly described by the source as representative and from memory
- **Current canonical records:** none yet

**Source caution:** the compendium says model names in this section are representative and from memory. Treat each as a research lead, not a verified model catalogue. Confirm papers, model cards, code, release dates, datasets and licence terms before citation.

## Using GeoFMs: embedding-based workflows

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Similarity search and few-shot mapping: query-by-example over embedding indexes, prototype-based land cover from a handful of labels | Retrieval and few-shot classification workflows | 27 | Captured; names not individually verified |
| Linear and k-NN probes on annual embedding fields; unsupervised clustering of embeddings for land cover discovery | Representation evaluation / clustering workflows | 27 | Captured; names not individually verified |
| Change detection by embedding differencing, anomaly detection in embedding space, temporal trajectory analysis of embeddings | Embedding-based change and anomaly analysis | 27 | Captured; names not individually verified |
| Retrieval at scale: approximate nearest neighbor search (HNSW, IVF-PQ) with spatial and temporal metadata filters | Approximate vector retrieval / spatial-temporal query methods | 27 | Captured; names not individually verified |
| Evaluation protocols: frozen versus full fine-tune, label-efficiency curves, cross-sensor transfer, resolution generalization, spectral generalization, cross-region splits | Model evaluation protocols | 27 | Captured; names not individually verified |

## Physics-informed and simulation-based GeoAI

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Hybrid radiative transfer plus deep learning: PROSAIL and SCOPE-driven pretraining, neural network inversion, Gaussian process emulators of RTMs | Physical model and machine-learning hybrids / emulation | 27 | Captured; names not individually verified |
| Simulation-based inference and amortized Bayesian inference for retrieval problems | Simulation-based and Bayesian inference methods | 27 | Captured; names not individually verified |
| Physics-guided losses and constraints: mass conservation, energy balance, monotonicity constraints in hydrology and climate emulators | Physics-informed learning constraints | 27 | Captured; names not individually verified |
| Differentiable simulators and differentiable hydrology (differentiable parameter learning) | Differentiable simulation / parameter estimation | 27 | Captured; names not individually verified |

## Multimodal inputs beyond imagery

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| LiDAR, GEDI and ICESat-2 fused with optical and SAR; street view; POIs; building footprints; road graphs; soundscapes | Multisensor and multimodal data fusion | 27 | Captured; names not individually verified |
| Mobility and social data as modalities: CDR, GPS traces, check-ins, transit smart card data | Mobility and social-data integration | 27 | Captured; names not individually verified |
| Text and knowledge graph conditioning for place understanding, geographic hierarchies as inductive bias | Language and knowledge-graph conditioning / representation methods | 27 | Captured; names not individually verified |

## Urban and spatiotemporal foundation models

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Urban vision-language: UrbanCLIP, UrbanVLP, region embedding models, street-view and satellite fusion for socioeconomic prediction | Urban vision-language models / multimodal prediction | 27 | Captured; names not individually verified |
| Spatiotemporal and traffic foundation models: UniST, UrbanGPT, OpenCity, UrbanDiT, STFM-style universal forecasters | Spatiotemporal and traffic model families | 27 | Captured; names not individually verified |
| Trajectory foundation models: TrajFM, UniTraj, trajectory tokenizers, mobility LLMs for next-location and mode prediction | Trajectory representation and prediction models | 27 | Captured; names not individually verified |
| General time-series foundation models applied to spatial sensors: TimesFM, Chronos, Moirai, Lag-Llama, with spatial adapters | Time-series foundation models / spatial adaptation workflows | 27 | Captured; names not individually verified |
| Hypergraph and heterogeneous graph neural networks for urban knowledge graphs, region and POI embeddings (HGI, ReMVC) | Graph architectures / urban representation learning | 28 | Captured; names not individually verified |

## Geospatial LLMs and agents

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Domain LLMs: GeoGalactica, K2, GeoGPT, GeoLLM, map-aware instruction-tuned models | Domain language model families | 28 | Captured; names not individually verified |
| Map understanding: map VQA, map reading, georeferenced map OCR, chart and cartographic style question answering | Map understanding tasks / multimodal evaluation | 28 | Captured; names not individually verified |
| Tool-use evaluation: GeoLLM-Engine, GeoBenchX, GIS Copilot-style agents, spatial reasoning benchmarks (SpatialEval, GeoQA) | Agent evaluation / benchmark suites | 28 | Captured; names not individually verified |
| Pipelines: natural language to spatial SQL, to PyQGIS, to GeoPandas or GDAL, with validation, execution sandboxes and self-repair loops | Natural-language interfaces / agent workflows / execution safeguards | 28 | Captured; names not individually verified |
| Retrieval and grounding: GeoRAG over STAC catalogs, metadata-aware retrieval, OSM tag reasoning, gazetteer-augmented generation | Retrieval-augmented generation / geographic grounding | 28 | Captured; names not individually verified |

## Data-centric GeoAI

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Label refinement from coarse land cover and OSM, noisy-label correction, confident learning for segmentation | Label quality and refinement methods | 28 | Captured; names not individually verified |
| Synthetic data: physically based rendering, procedural cities, domain randomization, diffusion-generated training tiles | Synthetic data generation / simulation | 28 | Captured; names not individually verified |
| Dataset distillation and core-set selection for imagery, geographic diversity sampling, long-tail class handling | Dataset selection and curation methods | 28 | Captured; names not individually verified |
| Annotation tooling: SAM-assisted labeling, superpixel scribbles, interactive segmentation, consensus labeling across annotators | Annotation workflows / interactive segmentation | 28 | Captured; names not individually verified |

## Scaling and efficiency

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Neural scaling laws for EO pretraining (data, parameters, compute), compute-optimal budgets, data pruning | Scaling analysis / compute allocation / data selection | 28 | Captured; names not individually verified |
| Efficient attention: windowed, linear, state-space, FlashAttention; resolution-adaptive patching; token dropping | Efficient neural computation methods | 28 | Captured; names not individually verified |
| Mixed-resolution inference: coarse-to-fine cascades, region-of-interest zoom, gigapixel streaming | Large-scene inference workflows | 28 | Captured; names not individually verified |

## Decisions for the next pass

1. Keep the source's memory-based warning visible until every model and tool is checked.
2. Separate a workflow pattern from the specific foundation model used in it.
3. Record embedding model, index type, metadata filters and geographic validation splits for retrieval examples.
4. Evaluate multimodal models against modality-specific baselines and missing-modality cases.
5. Document execution sandboxes, SQL validation and data permissions for agent workflows.
