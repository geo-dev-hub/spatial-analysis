# Exercise: from an outranking graph to an ELECTRE I kernel

This exercise follows the pairwise relation lesson. It does not turn ELECTRE I into a total ranking.

## Part A — Read the direction of an edge

An edge A → B means that A outranks B under the selected concordance/discordance rule. The row is the potential outranker; the column is the alternative being outranked.

Use the relation:

| | A | B | C |
|---|---:|---:|---:|
| A | 0 | 1 | 0 |
| B | 0 | 0 | 1 |
| C | 0 | 0 | 0 |

1. Draw the directed graph.
2. Which alternatives are directly outranked by A?
3. Does A directly outrank C?
4. Why is the set {A, C} internally stable?

## Part B — Check the two kernel conditions

A kernel K must satisfy both conditions:

- **Internal stability:** no two distinct alternatives in K outrank one another.
- **External stability:** every alternative outside K is directly outranked by at least one alternative in K.

1. Test K = {A}.
2. Test K = {A, C}.
3. Test K = {B}.
4. Explain why external stability is a direct-edge condition, not reachability through a path.

## Part C — Run the implementation

Run `implementations/python/electre-i/test_electre_i_kernel.py` and the companion notebook.

1. Change the relation to a directed three-cycle.
2. Observe that no kernel exists for that graph.
3. Change it to mutual outranking between A and B.
4. Observe that more than one kernel may exist.
5. Explain why the software reports all kernels rather than choosing one arbitrarily.

## Part D — Decision interpretation

1. Why is a kernel not a complete ranking?
2. What should a decision analyst report when there are multiple kernels?
3. What should happen when no kernel exists?
4. Why should cycles be investigated before applying a cycle-reduction procedure?
5. Which parts of the result depend on the selected concordance and discordance thresholds?

The exact enumeration is exponential and intentionally limited to small candidate sets. Do not use it as a large-scale graph algorithm. The kernel is an exploitation step applied after the outranking relation has been constructed; it cannot repair poor criterion definitions, weights, thresholds or data.
