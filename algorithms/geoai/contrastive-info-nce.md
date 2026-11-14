# Contrastive representation learning with NT-Xent

Stable ID: SA-GEOAI-CONTRASTIVE-NTXENT · Draft 0.1 · Source compendium section 8, page 15

## Why contrastive learning?

Self-supervised contrastive learning trains an encoder to bring two views of the same underlying sample closer in representation space while separating them from other samples in the batch. It can create reusable embeddings when labelled geospatial data are scarce, but the quality of the representation depends on the definition of a positive pair, the augmentation policy and the negative set.

This lesson implements the symmetric normalized temperature-scaled cross-entropy (NT-Xent) objective as a NumPy baseline. It does not implement a full neural network or claim to reproduce a particular remote-sensing foundation model.

## Positive pairs and normalized embeddings

For each source sample, construct two views and encode them as zᵢ and zᵢ′. Normalize:

$$\hat z=\frac{z}{\|z\|_2}$$

The similarity is cosine similarity divided by temperature τ:

$$s_{ij}=\frac{\hat z_i^T\hat z_j}{\tau}$$

The paired view is the positive; all other non-self examples in the concatenated batch are negatives.

## NT-Xent objective

For anchor i with positive index p(i):

$$\ell_i=-\log\frac{\exp(s_{i,p(i)})}{\sum_{k\ne i}\exp(s_{ik})}$$

The symmetric batch loss averages the objective over both augmented views:

$$\mathcal L=\frac{1}{2B}\sum_{i=1}^{2B}\ell_i$$

A numerically stable implementation subtracts the maximum logit before exponentiation.

## Geospatial positive-pair design

Positive pairs must reflect the invariances desired by the downstream task. Examples include two spatial crops of the same scene, two radiometric views of the same acquisition, or carefully selected cross-sensor observations. But none is universally valid:

- Rotation and reflection may destroy orientation information needed for roads, solar geometry or directional processes.
- Spectral jitter must respect sensor response, band meaning and physical reflectance ranges.
- Temporal augmentation must not leak future observations into forecasting or change-detection tasks.
- Nearby or overlapping tiles can leak across train/test partitions and inflate evaluation.
- Two different places with similar land cover are not automatically positive pairs; the target invariance must be justified.

## Limitations

The [Python baseline](../../implementations/python/info-nce/README.md) contains only the loss. It does not implement an encoder, projection head, data augmentation, optimizer, distributed negative gathering, memory bank, model evaluation or a foundation model. Batch composition affects the negative set and therefore the objective. A complete study needs an explicit data split, geographic leakage analysis, sensor and temporal metadata, baselines and downstream evaluation.

## Exercises

1. Calculate the loss for two orthogonal paired views by hand.
2. Change temperature. How does the softmax distribution sharpen?
3. Construct false negatives by placing two similar adjacent tiles in the same batch.
4. Propose augmentations for a land-cover task and a road-orientation task. Why should they differ?
5. Explain why random tile splitting can leak geographic context.
6. Compare contrastive learning with masked reconstruction and self-distillation.

## References

- Chen, T. et al. (2020), *A Simple Framework for Contrastive Learning of Visual Representations*, Proceedings of ICML.
- He, K. et al. (2020), *Momentum Contrast for Unsupervised Visual Representation Learning*, Proceedings of CVPR.

**Scope:** symmetric NT-Xent loss for paired embedding batches; no model architecture, data pipeline, training loop or benchmark reproduction.
