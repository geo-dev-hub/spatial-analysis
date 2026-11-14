# M/M/c queue metrics

A small, dependency-free implementation of the steady-state M/M/c queue for one FCFS queue feeding c identical parallel servers.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from mmc_queue import mmc_metrics

metrics = mmc_metrics(arrival_rate=8, service_rate=5, servers=2)
print(metrics["utilisation"])
print(metrics["expected_wait"])
print(metrics["expected_system_time"])
```

Rates must use the same time unit. The service rate is per server. An unstable queue (arrival rate greater than or equal to total service capacity) raises a ValueError.

## Returned metrics

- `utilisation`: arrival rate divided by total service capacity.
- `probability_wait`: Erlang-C probability that an arrival must wait.
- `expected_queue_length`: expected number waiting.
- `expected_system_length`: expected number waiting or in service.
- `expected_wait`: expected time waiting before service.
- `expected_system_time`: expected wait plus mean service time.

The model assumes Poisson arrivals, exponential service, identical servers, FCFS, an infinite queue and steady state. It is not a simulation and does not represent time-varying demand, priorities, abandonment, spatial choice or equity.

See the [canonical lesson](../../../algorithms/optimization/mmc-queue.md), [intern walkthrough](implementation-walkthrough.md), [exercise](../../../exercises/mmc-queue.md) and [visual lab](../../../notebooks/mmc-queue-lab.ipynb).
