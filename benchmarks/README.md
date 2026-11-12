# Compare methods carefully

Benchmarks help answer a practical question: how does an implementation behave on a stated workload?

A result is only useful when readers can understand how it was produced. Every benchmark in this repository should include:

- the question being tested;
- the implementations and exact versions;
- the machine and runtime environment;
- input size and shape, including spatial characteristics;
- coordinate system, units and precision policy where relevant;
- parameters, random seed and warm-up procedure;
- the measurement method and number of repetitions;
- raw or reproducible output;
- limitations and what the result does **not** establish.

## Start with the existing experiment

[The Bentley–Ottmann benchmark](../implementations/python/bentley-ottmann/benchmark-results.md) compares a list-based sweep, a treap-based sweep and an all-pairs oracle on seeded, non-intersecting segment fixtures.

It is a controlled teaching experiment. It is not a universal performance ranking and does not represent the full range of GIS workloads.

## How to add a benchmark

1. Link it to a canonical method record.
2. State the hypothesis before running it.
3. Keep fixture generation deterministic and publish the seed.
4. Separate algorithmic operation counts from elapsed time.
5. Run enough repetitions to show variability.
6. Include correctness checks; a fast wrong answer is not an improvement.
7. Record the command needed to reproduce the result.
8. Explain the workload's limits.

## Interpret results with care

- Do not compare timings from different machines as if they were controlled.
- Do not generalise from one dataset shape or size.
- Do not hide setup, preprocessing or I/O costs if they matter to the real task.
- Distinguish expected, average, amortised and worst-case bounds.
- Keep raw measurements alongside summaries whenever practical.
