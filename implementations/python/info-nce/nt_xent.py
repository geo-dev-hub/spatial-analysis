"""NumPy implementation of the symmetric NT-Xent contrastive objective."""
from __future__ import annotations
import numpy as np

def nt_xent_loss(view_a, view_b, *, temperature: float=0.1) -> float:
    """Compute symmetric NT-Xent loss for paired batches of embeddings.

    Each row in view_a is the positive partner of the same row in view_b.
    All other rows in the concatenated 2B batch are negatives, except self.
    Embeddings are L2-normalized before cosine similarity.
    """
    a=np.asarray(view_a,dtype=float)
    b=np.asarray(view_b,dtype=float)
    if a.ndim!=2 or b.ndim!=2 or a.shape!=b.shape or a.shape[0]<2 or a.shape[1]<1:
        raise ValueError("views must be aligned 2D arrays with at least two pairs")
    if not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError("embeddings must be finite")
    if not np.isfinite(temperature) or temperature<=0:
        raise ValueError("temperature must be finite and positive")
    joined=np.concatenate([a,b],axis=0)
    norms=np.linalg.norm(joined,axis=1,keepdims=True)
    if (norms==0).any():
        raise ValueError("embedding vectors must have non-zero norm")
    normalized=joined/norms
    logits=(normalized@normalized.T)/temperature
    np.fill_diagonal(logits,-np.inf)
    batch=a.shape[0]
    positive=np.concatenate([np.arange(batch,2*batch),np.arange(batch)])
    row_max=np.max(logits,axis=1,keepdims=True)
    log_denominator=row_max[:,0]+np.log(np.exp(logits-row_max).sum(axis=1))
    positive_logits=logits[np.arange(2*batch),positive]
    return float(np.mean(log_denominator-positive_logits))
