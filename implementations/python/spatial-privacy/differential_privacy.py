"""User-level differential privacy for bounded spatial cell contributions."""
from __future__ import annotations
from collections import defaultdict
import numpy as np


def private_spatial_counts(records, cells, epsilon, *, max_cells_per_person=1, rng=None):
    """Release noisy cell counts with a user-level Laplace mechanism.

    records is an iterable of (person_id, cell_id) pairs. Each person's
    contributions are deduplicated and deterministically capped to at most k
    distinct cells. Under add/remove-one-person adjacency, vector L1
    sensitivity is k and independent Laplace noise has scale k/epsilon.

    The returned object contains only cell IDs, noisy counts and mechanism
    metadata; identifiers are not returned. This is a single release and
    does not provide a privacy accountant for repeated queries.
    """
    eps=float(epsilon)
    if not np.isfinite(eps) or eps<=0:
        raise ValueError("epsilon must be finite and positive")
    if not isinstance(max_cells_per_person,int) or max_cells_per_person<1:
        raise ValueError("max_cells_per_person must be a positive integer")
    ordered_cells=list(dict.fromkeys(cells))
    if not ordered_cells:
        raise ValueError("cells must be non-empty")
    known=set(ordered_cells)
    contributions=defaultdict(set)
    for record in records:
        if len(record)!=2:
            raise ValueError("each record must be (person_id, cell_id)")
        person,cell=record
        if cell not in known:
            raise ValueError("record references a cell outside the release domain")
        contributions[person].add(cell)
    true_counts={cell:0 for cell in ordered_cells}
    for person,person_cells in contributions.items():
        # Stable cap independent of input row ordering.
        for cell in sorted(person_cells,key=lambda value:(type(value).__name__,str(value)))[:max_cells_per_person]:
            true_counts[cell]+=1
    generator=np.random.default_rng(rng)
    sensitivity=float(max_cells_per_person)
    scale=sensitivity/eps
    noisy={cell:float(true_counts[cell]+generator.laplace(0.0,scale)) for cell in ordered_cells}
    return {"noisy_counts":noisy,"epsilon":eps,
            "max_cells_per_person":max_cells_per_person,
            "l1_sensitivity":sensitivity,"noise_scale":scale,
            "adjacency":"add_remove_one_person"}
