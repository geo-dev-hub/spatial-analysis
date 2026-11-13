# Masked autoencoding for geospatial imagery

Masked autoencoding (MAE) is a self-supervised pretraining approach: hide part of an input, encode what remains, and train a decoder to reconstruct the missing content. Unlike contrastive learning, the learning signal comes from reconstruction rather than explicitly comparing positive and negative pairs.

## The basic design

An image is divided into a sequence of patches. Let X contain L patch tokens. A masking procedure selects a visible subset V and a masked subset M:

\[
X=V\cup M,\qquad V\cap M=\varnothing.
\]

The encoder processes only visible patches. A lightweight decoder receives encoded visible patches and learned mask tokens, restores the original sequence order, and predicts the masked input. A simple pixel reconstruction objective is:

\[
\mathcal L_{\mathrm{MAE}}=
\frac{1}{|M|}\sum_{i\in M}\|\hat x_i-x_i\|_2^2.
\]

The loss is evaluated on masked patches in the original MAE formulation. Normalisation, target representation and loss details vary between implementations and model families.

## Why mask a large fraction?

The original vision MAE work showed that high masking ratios can create a useful reconstruction task while reducing encoder computation because the encoder sees only visible tokens. A 75% mask ratio is a common reference point from that work, not a universal optimum for geospatial data.

The companion implementation teaches only the random patch-selection and sequence-restoration mechanics. It does not implement a transformer, decoder, reconstruction target, optimiser or trained model.

## What changes for Earth observation?

Satellite imagery carries information absent from ordinary RGB image assumptions:

- **Spectral structure:** bands have physical meanings and sensor-specific response functions. Treating all channels as interchangeable RGB can discard useful information.
- **Temporal structure:** observations are irregularly sampled and may represent different seasons, phenological stages, cloud conditions or acquisition geometries.
- **Spatial scale:** the same pixel dimensions can represent very different ground areas. Record ground sample distance and footprint.
- **Missingness:** clouds, shadows, sensor gaps and quality masks are structured missing data, not always random corruption.
- **Geographic dependence:** overlapping tiles and nearby scenes can leak across train/test partitions.

SatMAE extends masked autoencoding to temporal and multispectral satellite imagery using temporal embeddings and spectral positional encodings. Its paper studies independent and consistent masking strategies for temporal observations. Scale-MAE explicitly models known spatial scale and multiscale reconstruction. These are distinct designs, not merely different model names.

## Masking choices are scientific assumptions

Ask:
1. Are patches masked independently across time or consistently at the same locations?
2. Are spectral bands grouped or treated as separate tokens?
3. Does the mask preserve enough context for the intended reconstruction task?
4. Are cloud and quality masks respected?
5. Does the target require preserving absolute radiometry, spatial texture, temporal change or cross-sensor relationships?
6. Could the model reconstruct a masked region from near-duplicate overlapping tiles in the same training batch?

The right answer depends on the downstream task. Do not copy a masking ratio or augmentation policy without testing its implications.

## Evaluation

A decreasing reconstruction loss is not evidence that an encoder is useful for mapping. Evaluate frozen representations with linear probes, k-nearest-neighbour classification, retrieval or clustering, then compare fine-tuning under a controlled label budget. Hold out geography, time and, where relevant, sensors or spatial resolutions. Compare against random initialisation, supervised and simpler self-supervised baselines.

## Practical implementation

- [Random patch masking and restoration baseline](../implementations/python/masked-autoencoding/README.md)
- [Step-by-step intern walkthrough](../implementations/python/masked-autoencoding/implementation-walkthrough.md)
- [GeoAI foundations path](../learning-paths/geoai-foundations.md)
- [Spatial cross-validation](spatial-cross-validation.md)

## References

- He, K. et al. (2022). Masked Autoencoders Are Scalable Vision Learners. *Proceedings of CVPR*, 16000–16009. https://arxiv.org/abs/2111.06377
- Cong, Y. et al. (2022). SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery. *NeurIPS 2022*. https://proceedings.neurips.cc/paper_files/paper/2022/hash/01c561df365429f33fcd7a7faa44c985-Abstract-Conference.html
- Reed, C. J. et al. (2023). Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning. *ICCV 2023*. https://openaccess.thecvf.com/content/ICCV2023/papers/Reed_Scale-MAE_A_Scale-Aware_Masked_Autoencoder_for_Multiscale_Geospatial_Representation_Learning_ICCV_2023_paper.pdf

The references support the described research directions. The repository's NumPy example is not a reproduction of any of these trained models.
