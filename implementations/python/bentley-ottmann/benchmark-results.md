# First benchmark: list status versus all pairs

**Purpose.** This is a small, reproducible diagnostic of the current Python teaching implementation. It is not a general performance claim and does not replace a benchmark suite using real geospatial linework.

## Fixture and method

The fixture contains parallel, non-intersecting horizontal segments. Their start and end x-coordinates are all distinct, and their vertical order never changes. Endpoints are arranged in a seeded, shuffled order so status insertion and removal are not always append/pop operations.

For each input size, the script records:
- wall-clock time for the list-status Bentley–Ottmann prototype;
- the number of pairwise intersection calls made by its neighbour checks;
- wall-clock time for the independent all-pairs oracle;
- the number of pair checks made by that oracle.

Run it from this directory:

```bash
PYTHONPATH=../segment-intersection python benchmark.py
```

## Recorded run

Environment: Python 3.13.5, Linux x86_64. One run in the project execution environment; timings are illustrative and will vary with hardware, interpreter, system load and runtime conditions.

| Segments (n) | Sweep time (s) | Sweep pair checks | All-pairs time (s) | All-pairs checks |
|---:|---:|---:|---:|---:|
| 50 | 0.005983 | 89 | 0.002197 | 1,225 |
| 100 | 0.027106 | 187 | 0.011757 | 4,950 |
| 200 | 0.075193 | 388 | 0.047678 | 19,900 |
| 400 | 0.336961 | 791 | 0.162033 | 79,800 |
| 800 | 1.369394 | 1,582 | 1.138126 | 319,600 |

No intersections were present in these fixtures.

## What the results tell us

The sweep performs roughly two candidate-pair checks per segment in this particular fixture, while the all-pairs method performs exactly:

[
\binom{n}{2}=\frac{n(n-1)}{2}
]

Yet the sweep is not faster in this run. That is not a contradiction. The current sweep stores active segments in a Python list. Searching for a segment, inserting it in order, removing it and finding its position can each take linear time. The pair-check count alone does not measure the cost of maintaining the status.

This is precisely why the implementation README separates the abstract algorithm's balanced-tree complexity from the current list-based code's complexity.

## What this benchmark does not tell us

- It does not establish performance on intersecting, dense, clustered or real-world GIS linework.
- It does not prove asymptotic complexity from five input sizes.
- It does not compare against an optimised geometry library.
- It does not measure memory, allocation costs or arithmetic bit complexity.
- It does not show that the sweep wins for small inputs.

## Next experiment

Implement a status structure with logarithmic insertion, deletion and neighbour lookup while preserving a valid order through crossing events. Run the exact same fixtures and correctness oracle against both implementations. Then add sparse-crossing and dense-crossing fixtures, report repeated-run medians, and keep the current list version as the easier-to-read reference implementation.
