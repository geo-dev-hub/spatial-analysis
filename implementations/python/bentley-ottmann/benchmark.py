"""Reproducible microbenchmark: list-status sweep versus all-pairs oracle.

Run from this directory:
    PYTHONPATH=../segment-intersection python benchmark.py

The fixture contains parallel, non-intersecting segments with distinct endpoint
x-coordinates. It isolates event/status overhead and candidate-pair reduction;
it is not a representative GIS workload or a proof of asymptotic performance.
"""
from __future__ import annotations

import random
import time

import bentley_ottmann as sweep
from bentley_ottmann import Segment, bentley_ottmann
from segment_intersection import segment_intersection


def make_fixture(n: int, seed: int = 20261113) -> list[Segment]:
    rng = random.Random(seed + n)
    end_order = list(range(n))
    rng.shuffle(end_order)
    # Parallel horizontal segments never intersect. Start and end x values are
    # all distinct, and endpoint heights are distinct.
    return [Segment(i, (i, 10 * i), (2 * n + end_order[i], 10 * i)) for i in range(n)]


def all_pairs(segments: list[Segment]) -> tuple[int, int]:
    checks = 0
    hits = 0
    for i, first in enumerate(segments):
        for second in segments[i + 1 :]:
            checks += 1
            if segment_intersection(first.a, first.b, second.a, second.b).kind != "none":
                hits += 1
    return checks, hits


def timed(fn):
    start = time.perf_counter()
    result = fn()
    return time.perf_counter() - start, result


def main() -> None:
    print("n,sweep_seconds,sweep_pair_checks,brute_seconds,brute_pair_checks,hits")
    for n in (50, 100, 200, 400, 800):
        segments = make_fixture(n)
        original = sweep.segment_intersection
        sweep_checks = 0

        def counted(a, b, c, d):
            nonlocal sweep_checks
            sweep_checks += 1
            return original(a, b, c, d)

        sweep.segment_intersection = counted
        try:
            sweep_seconds, sweep_result = timed(lambda: bentley_ottmann(segments))
        finally:
            sweep.segment_intersection = original
        brute_seconds, (brute_checks, brute_hits) = timed(lambda: all_pairs(segments))
        if sweep_result or brute_hits:
            raise AssertionError("Parallel benchmark fixture unexpectedly intersected")
        if sweep_checks > brute_checks:
            raise AssertionError("Sweep performed more pair checks than brute force")
        print(f"{n},{sweep_seconds:.6f},{sweep_checks},{brute_seconds:.6f},{brute_checks},{brute_hits}")


if __name__ == "__main__":
    main()
