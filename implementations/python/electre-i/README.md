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
