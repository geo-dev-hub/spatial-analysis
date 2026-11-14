# ELECTRE I-style outranking relation in Python

This package constructs a crisp pairwise outranking relation using weighted concordance and a range-normalised discordance index. It is a scoped teaching baseline for the first stage of an ELECTRE I-style analysis.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from electre_i import electre_i_relation

    performance = np.array([
        [8, 7, 4],  # candidate A
        [6, 8, 5],  # candidate B
        [5, 4, 7],  # candidate C
    ])
    result = electre_i_relation(
        performance,
        weights=[0.5, 0.3, 0.2],
        directions=["benefit", "benefit", "cost"],
        concordance_threshold=0.6,
        discordance_threshold=0.3,
        alternative_names=["A", "B", "C"],
    )
    print(result.concordance)
    print(result.discordance)
    print(result.outranks)

## What the implementation calculates

For an ordered pair (a, b):

- Concordance is the sum of normalised criterion weights where a is at least as good as b.
- Discordance is the largest disadvantage of a on any criterion where b is better, divided by that criterion's observed range across the alternatives.
- a outranks b when concordance meets the chosen lower threshold and discordance does not exceed the chosen upper threshold.

The relation is reflexive. It may be incomplete or non-transitive. That is an expected property of outranking methods, not necessarily a defect.

## Scope and limitations

This package constructs the pairwise relation only. It does not extract the ELECTRE I kernel/choice set, produce a complete ranking, elicit weights or thresholds, model indifference/preference/veto thresholds, account for criterion interactions or validate stakeholder judgements. The range-normalised discordance index is one explicit teaching convention; record it and the thresholds used. Do not present this package as ELECTRE III, ELECTRE TRI or a complete ELECTRE decision workflow.

See the [ELECTRE method-family lesson](../../../methods/electre-outranking.md) and [intern walkthrough](implementation-walkthrough.md).


## Kernel / choice-set stage

The companion module `electre_i_kernel.py` enumerates every subset satisfying the two graph-kernel conditions for the supplied relation:

1. **Internal stability:** no two distinct selected alternatives outrank one another.
2. **External stability:** every alternative outside the selected set is directly outranked by at least one selected alternative.

```python
from electre_i_kernel import enumerate_electre_kernels

choice = enumerate_electre_kernels(
    result.outranks,
    result.alternative_names,
)
print(choice.kernels)
print("Unique kernel:", choice.is_unique)
```

The function returns all kernels, including multiple kernels, or an empty tuple when no kernel exists. It does not silently remove cycles or invent a unique recommendation. The exhaustive search is exponential and is capped at 20 alternatives by default. This is a small-choice-set teaching implementation, not a large-graph solver.

The kernel is an exploitation step applied to the outranking relation. It is not a complete ranking. If cycles prevent a kernel or produce multiple kernels, inspect the graph and decision assumptions before selecting a documented cycle-reduction procedure.
