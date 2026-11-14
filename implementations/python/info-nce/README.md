# Contrastive learning: symmetric NT-Xent loss

This package implements the normalized temperature-scaled cross-entropy (NT-Xent) objective for paired batches of embeddings. It is a small NumPy loss-function baseline, not a complete self-supervised training system.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Inputs are aligned arrays with shape (batch, embedding_dimension), with at least two positive pairs.
- Row i in view A is paired with row i in view B.
- Embeddings are L2-normalized; cosine similarities are divided by a positive temperature.
- The other 2B−2 samples in the batch are negatives for each anchor.
- The loss is symmetric across both views and uses a numerically stable log-sum-exp calculation.
- Zero vectors, non-finite embeddings and invalid temperatures are rejected.
- No encoder, augmentation pipeline, optimizer, distributed negative gathering, memory bank or training loop is included.

Read the [canonical lesson](../../../algorithms/geoai/contrastive-info-nce.md) and [intern walkthrough](implementation-walkthrough.md).
