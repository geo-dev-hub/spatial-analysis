# Intern walkthrough: NT-Xent contrastive loss

## 1. Build positive pairs

A batch contains two views of each underlying sample. For geospatial imagery, views might be two crops or augmentations of the same tile, acquisition or location. The positive-pair definition is a modelling decision: two different dates or sensors are not automatically positive unless the task says they should share a representation.

## 2. Normalize embeddings

For embedding z, L2 normalization is:

$$\hat z=\frac{z}{\|z\|_2}$$

The dot product of normalized vectors is cosine similarity.

## 3. Scale similarities by temperature

For embeddings i and j:

$$s_{ij}=\frac{\hat z_i^T\hat z_j}{\tau}$$

A lower temperature sharpens the softmax distribution. It changes gradient concentration and should be selected and validated rather than treated as a cosmetic setting.

## 4. Identify the positive and negatives

Concatenate the two views into a batch of size 2B. For each anchor, its paired view is the positive; every other non-self embedding in the batch is a negative.

The per-anchor loss is:

$$\ell_i=-\log\frac{\exp(s_{i,p(i)})}{\sum_{k\ne i}\exp(s_{ik})}$$

The final loss averages over all 2B anchors. The implementation uses a stable log-sum-exp calculation to avoid overflow.

## 5. Geospatial augmentation cautions

Augmentations must preserve the semantics the model is expected to learn. Rotations and flips may be invalid when orientation matters; spectral perturbations must respect sensor bands and physical reflectance; temporal crops must not leak future information into past prediction tasks. Spatially adjacent or overlapping tiles should not be split across train and test without an explicit leakage analysis.

## 6. What is not implemented

This package contains only the objective. It does not include a neural encoder, projection head, image augmentations, optimizer, distributed all-gather, memory bank or evaluation protocol. A production geospatial representation-learning study needs all of those choices documented and tested.
