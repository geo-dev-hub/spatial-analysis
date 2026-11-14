# Exercise: service capacity and queueing

## Learning goal

Understand how arrival demand, per-server service rates and server count combine to determine waiting in a simple steady-state queue.

## Starter material

Use the [M/M/c implementation](../implementations/python/mmc-queue/README.md) and [visual lab](../notebooks/mmc-queue-lab.ipynb). No external dataset is required.

## Tasks

1. Calculate utilisation for 8 arrivals per hour, 5 services per hour per server and two servers.
2. Compare c=1, c=2 and c=3. Record probability of waiting, expected queue wait and expected number waiting.
3. Increase arrivals from 8 to 9.5 per hour while holding service capacity fixed. Explain the change in waiting time.
4. Use Little's law to verify both expected queue length and expected system length.
5. Identify a real service setting where exponential service times are implausible.
6. Explain why a queue model does not replace a travel-time accessibility model.
7. Propose a data collection plan that would let an analyst test the Poisson-arrival and exponential-service assumptions.

## What to submit

A parameter table, a plot or table of wait versus arrival rate, a short explanation of stability, and a limitations note naming at least three assumptions that may fail in practice.

## Check your work

Rates must share a time unit. Service rate is per server. The queue is stable only when lambda is strictly less than c times mu. Expected system time includes both queue wait and service time. The model describes a long-run average, not a guarantee for an individual customer.
