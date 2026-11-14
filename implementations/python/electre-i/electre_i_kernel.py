"""Exact kernel enumeration for a small ELECTRE I outranking graph.

An edge a -> b means that alternative a outranks alternative b.
A kernel is an internally stable (independent) set that externally
stabilises the relation: every alternative outside the set is outranked
by at least one member of the set.

This exhaustive implementation is deliberately limited to small choice
sets. It reports every kernel rather than silently resolving cycles.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence

import numpy as np
from numpy.typing import ArrayLike


@dataclass(frozen=True)
class KernelEnumeration:
    """All kernels found, expressed as alternative-name tuples."""

    kernels: tuple[tuple[str, ...], ...]

    @property
    def has_kernel(self) -> bool:
        return bool(self.kernels)

    @property
    def is_unique(self) -> bool:
        return len(self.kernels) == 1


def enumerate_electre_kernels(
    outranks: ArrayLike,
    alternative_names: Sequence[str] | None = None,
    *,
    max_alternatives: int = 20,
) -> KernelEnumeration:
    """Enumerate all independent, externally stable subsets.

    outranks[a, b] means alternative a outranks alternative b.
    The diagonal is ignored. A candidate kernel must satisfy:

    1. Internal stability: no two distinct members outrank one another.
    2. External stability: every alternative outside the kernel is
       outranked directly by at least one member of the kernel.

    The search is exhaustive (O(2**n * n) in this straightforward
    bit-mask implementation), so the default limit is 20 alternatives.
    Multiple kernels and the absence of a kernel are both returned
    explicitly; cycles are not automatically reduced.
    """
    raw = np.asarray(outranks)
    if raw.ndim != 2 or raw.shape[0] != raw.shape[1] or raw.shape[0] < 1:
        raise ValueError("outranks must be a square matrix with at least one alternative")
    if raw.dtype.kind not in "bui":
        raise ValueError("outranks must contain boolean or integer 0/1 values")
    if np.any((raw != 0) & (raw != 1)):
        raise ValueError("outranks must contain only boolean or integer 0/1 values")

    relation = raw.astype(bool, copy=True)
    n = relation.shape[0]
    if not isinstance(max_alternatives, int) or max_alternatives < 1:
        raise ValueError("max_alternatives must be a positive integer")
    if n > max_alternatives:
        raise ValueError(
            f"exact enumeration is limited to {max_alternatives} alternatives; got {n}"
        )

    if alternative_names is None:
        names = tuple(f"A{i + 1}" for i in range(n))
    else:
        names = tuple(alternative_names)
        if len(names) != n or any(not isinstance(name, str) or not name for name in names):
            raise ValueError("alternative_names must contain one non-empty string per alternative")
        if len(set(names)) != n:
            raise ValueError("alternative_names must be unique")

    np.fill_diagonal(relation, False)
    outgoing = []
    incoming = [0] * n
    for i in range(n):
        mask = 0
        for j in range(n):
            if relation[i, j]:
                mask |= 1 << j
                incoming[j] |= 1 << i
        outgoing.append(mask)

    kernels = []
    for selected in range(1, 1 << n):
        # Internal stability: no directed edge between distinct members.
        independent = True
        remaining = selected
        while remaining:
            bit = remaining & -remaining
            i = bit.bit_length() - 1
            if outgoing[i] & (selected ^ bit):
                independent = False
                break
            remaining ^= bit
        if not independent:
            continue

        # External stability: each excluded vertex has an incoming edge
        # from at least one selected vertex.
        outside = ((1 << n) - 1) ^ selected
        dominated = True
        while outside:
            bit = outside & -outside
            j = bit.bit_length() - 1
            if not (incoming[j] & selected):
                dominated = False
                break
            outside ^= bit
        if dominated:
            kernels.append(tuple(names[i] for i in range(n) if selected & (1 << i)))

    return KernelEnumeration(tuple(kernels))
