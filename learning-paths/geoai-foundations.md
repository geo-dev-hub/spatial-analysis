# GeoAI foundations: from spatial data to reusable representations

**Status:** First self-supervised objective lesson published. This is a learning path, not a catalogue of verified foundation-model claims.

## 1. Begin with the data, not the model name

Before choosing an encoder, define:
- the spatial unit (pixel, patch, scene, point, object or region);
- the sensors and band semantics;
- acquisition dates, temporal windows and spatial resolution;
- the coordinate system and spatial coverage;
- NoData, cloud, quality and uncertainty masks;
- geographic train/validation/test separation.

For spatial imagery, random tile splitting can leak near-duplicate or overlapping scenes across partitions. Split by geography, time, acquisition or another defensible grouping before fitting a model.

## 2. Learn a self-supervised objective

Read [Contrastive representation learning with NT-Xent](../algorithms/geoai/contrastive-info-nce.md) and run the [InfoNCE notebook](../notebooks/contrastive-info-nce-lab.ipynb). The NumPy implementation explains paired views, cosine similarity, temperature and the batch negative set.

This is a loss-function baseline only. It is not a trained encoder, remote-sensing foundation model or benchmark reproduction.

## 3. Design geospatial positive pairs carefully

An augmentation is valid only when it preserves the information the downstream task needs. Rotations may be useful for some land-cover tasks but harmful when orientation is meaningful, such as road direction or solar geometry. Spectral perturbations must respect sensor response and band semantics. Temporal augmentations must not leak future information into forecasting or change-detection tasks.

Write down the invariance you want the model to learn before selecting augmentations.

## 4. Evaluate representations beyond the pretraining loss

A lower pretraining loss is not proof of useful spatial representations. Evaluate on held-out geography and time using downstream tasks such as:
- linear probing;
- fine-tuning with limited labels;
- retrieval and nearest-neighbour search;
- transfer across regions, sensors and seasons;
- robustness to cloud, missing bands and distribution shift.

Compare against simple baselines and report the split design, spatial leakage checks, class balance and uncertainty.

## 5. Expand the learning sequence

The source inventory includes masked autoencoding, contrastive learning, self-distillation, image-text alignment, multi-sensor pretraining, temporal encoders, parameter-efficient adaptation, segmentation, detection, change detection, geolocalization, vision-language models and agentic GIS workflows. Each family needs a separate, verified lesson and implementation scope. Model names and benchmark claims must be checked against original papers, official model cards and maintained project documentation before publication.

## Exercises

1. Define a positive pair for a multispectral land-cover task.
2. Give an example where rotation augmentation would destroy useful information.
3. Design a spatially separated test split for a regional mapping task.
4. Explain why overlapping satellite tiles can leak across random train/test splits.
5. Compare contrastive learning with masked reconstruction and self-distillation.
6. Design a downstream evaluation that tests transfer to a new region and sensor.
