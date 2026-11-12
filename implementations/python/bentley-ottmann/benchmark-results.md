# Benchmark: list status, treap status and all pairs

**Purpose.** This is a small, reproducible diagnostic of two teaching implementations. It is not a general performance claim and does not replace a benchmark suite using real geospatial linework.

## Fixture and method

The fixture contains parallel, non-intersecting horizontal segments. Their start and end x-coordinates are all distinct, and their vertical order never changes. Endpoints are arranged in a seeded, shuffled order so status insertion and removal are not always append/pop operations.

For each input size, the script records:
- wall-clock time for the list-status Bentley–Ottmann prototype;
- candidate-pair intersection calls made by its neighbour checks;
- wall-clock time for the implicit-treap status implementation;
- candidate-pair intersection calls made by its neighbour checks;
- wall-clock time and pair-check count for the independent all-pairs oracle.

Run it from this directory:

```bash
PYTHONPATH=../segment-intersection python benchmark.py
```

## Recorded run

Environment: Python 3.13.5, Linux x86_64. One run in the project execution environment; timings are illustrative and will vary with hardware, interpreter, system load and runtime conditions.

| Segments (n) | List sweep (s) | List pair checks | Treap sweep (s) | Treap pair checks | All pairs (s) | All-pairs checks |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 0.008062 | 89 | 0.003797 | 89 | 0.002657 | 1,225 |
| 100 | 0.028391 | 187 | 0.005507 | 187 | 0.009397 | 4,950 |
| 200 | 0.094201 | 388 | 0.011005 | 388 | 0.043529 | 19,900 |
| 400 | 0.361982 | 791 | 0.030568 | 791 | 0.209361 | 79,800 |
| 800 | 1.487701 | 1,582 | 0.078506 | 1,582 | 0.728933 | 319,600 |

No intersections were present in these fixtures. Both sweep implementations produced the same empty result as the all-pairs oracle.

## What the results tell us

Both sweep versions perform roughly two candidate-pair checks per segment in this particular fixture. The all-pairs method performs exactly:

[
\binom{n}{2}=\frac{n(n-1)}{2}
]

The list version becomes slower as status operations become more expensive. The treap version is faster in this run because insertion, removal, rank and adjacent swaps operate on a balanced sequence tree rather than shifting or scanning a Python list.

The treap uses independently randomized priorities. Its height and operation costs are **expected** logarithmic, not a deterministic worst-case guarantee. The classical bound is therefore an expected bound for this implementation under the stated assumptions, not an AVL/red-black worst-case guarantee.

## What this benchmark does not tell us

- It does not establish performance on intersecting, dense, clustered or real-world GIS linework.
- It does not prove asymptotic complexity from five input sizes.
- It does not compare against an optimised geometry library.
- It does not measure memory, allocation costs or arithmetic bit complexity.
- It does not show that a sweep wins for every small input.

## Next experiment

Add sparse-crossing and dense-crossing fixtures, repeat each measurement and report medians. Then benchmark a carefully selected, redistributable line dataset with independently verified expected results. Keep the list version as a readable reference and the treap version as the faster balanced-status teaching implementation.
