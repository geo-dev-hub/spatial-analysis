"""Reproducible microbenchmark: list/treap sweeps versus all-pairs oracle.

Run from this directory:
    PYTHONPATH=../segment-intersection python benchmark.py

The fixture contains parallel, non-intersecting segments with distinct endpoint
x-coordinates. It isolates event/status overhead and candidate-pair reduction;
it is not a representative GIS workload or a proof of asymptotic performance.
"""
from __future__ import annotations

import random
import time

import bentley_ottmann as list_impl
import bentley_ottmann_treap as treap_impl
from bentley_ottmann import Segment, bentley_ottmann
from bentley_ottmann_treap import bentley_ottmann_treap
from segment_intersection import segment_intersection


def make_fixture(n: int, seed: int = 20261113) -> list[Segment]:
    rng = random.Random(seed + n)
    end_order = list(range(n))
    rng.shuffle(end_order)
    return [Segment(i, (i, 10 * i), (2 * n + end_order[i], 10 * i)) for i in range(n)]


def all_pairs(segments: list[Segment]) -> tuple[int, int]:
    checks = hits = 0
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
    print("n,list_seconds,list_pair_checks,treap_seconds,treap_pair_checks,brute_seconds,brute_pair_checks,hits")
    for n in (50, 100, 200, 400, 800):
        segments = make_fixture(n)

        original_pair = list_impl.segment_intersection
        list_checks = 0
        def count_list(a, b, c, d):
            nonlocal list_checks
            list_checks += 1
            return original_pair(a, b, c, d)
        list_impl.segment_intersection = count_list
        try:
            list_seconds, list_result = timed(lambda: bentley_ottmann(segments))
        finally:
            list_impl.segment_intersection = original_pair

        original_intersection = treap_impl._intersection
        treap_checks = 0
        def count_treap(a, b):
            nonlocal treap_checks
            treap_checks += 1
            return original_intersection(a, b)
        treap_impl._intersection = count_treap
        try:
            treap_seconds, treap_result = timed(lambda: bentley_ottmann_treap(segments))
        finally:
            treap_impl._intersection = original_intersection

        brute_seconds, (brute_checks, brute_hits) = timed(lambda: all_pairs(segments))
        if list_result != treap_result or list_result or brute_hits:
            raise AssertionError("Benchmark implementations disagree or fixture unexpectedly intersected")
        if list_checks > brute_checks or treap_checks > brute_checks:
            raise AssertionError("A sweep performed more pair checks than brute force")
        print(f"{n},{list_seconds:.6f},{list_checks},{treap_seconds:.6f},{treap_checks},{brute_seconds:.6f},{brute_checks},{brute_hits}")


if __name__ == "__main__":
    main()
