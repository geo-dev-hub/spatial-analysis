"""Steady-state M/M/c queue metrics for a single FCFS service facility.

Assumptions: Poisson arrivals, independent exponential service times,
identical parallel servers, infinite calling population and queue capacity,
and a stable steady state (arrival_rate < servers * service_rate).
"""
from __future__ import annotations

from math import factorial, isfinite


def mmc_metrics(arrival_rate: float, service_rate: float, servers: int) -> dict[str, float]:
    """Return standard M/M/c steady-state metrics.

    Rates must use the same time unit. service_rate is the rate of one server.
    Returns utilisation, probability an arrival waits, expected queue length,
    expected system length, expected queue wait, and expected system time.
    """
    if not isfinite(arrival_rate) or arrival_rate <= 0:
        raise ValueError("arrival_rate must be finite and positive")
    if not isfinite(service_rate) or service_rate <= 0:
        raise ValueError("service_rate must be finite and positive")
    if not isinstance(servers, int) or isinstance(servers, bool) or servers < 1:
        raise ValueError("servers must be a positive integer")
    capacity = servers * service_rate
    if arrival_rate >= capacity:
        raise ValueError("queue is unstable: arrival_rate must be less than total service capacity")

    offered_load = arrival_rate / service_rate
    utilisation = arrival_rate / capacity
    partial_sum = sum(offered_load**n / factorial(n) for n in range(servers))
    tail = (offered_load**servers / factorial(servers)) / (1.0 - utilisation)
    p_zero = 1.0 / (partial_sum + tail)
    probability_wait = tail * p_zero

    wait_in_queue = probability_wait / (capacity - arrival_rate)
    time_in_system = wait_in_queue + 1.0 / service_rate
    queue_length = arrival_rate * wait_in_queue
    system_length = arrival_rate * time_in_system

    return {
        "utilisation": utilisation,
        "probability_wait": probability_wait,
        "expected_queue_length": queue_length,
        "expected_system_length": system_length,
        "expected_wait": wait_in_queue,
        "expected_system_time": time_in_system,
    }
