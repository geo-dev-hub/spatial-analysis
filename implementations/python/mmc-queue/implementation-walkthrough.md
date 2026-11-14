# Intern walkthrough: the M/M/c queue

## 1. Translate the service operation

M/M/c describes one queue feeding c identical servers. The first M means Markovian (Poisson) arrivals; the second M means exponential service times; c is the number of parallel servers.

## 2. Keep units consistent

If arrivals are measured per hour, service rates must also be per hour. The service rate is per server, so total nominal capacity is c times mu. Do not pass a facility-wide service rate as though it were a per-server rate.

## 3. Check stability first

The queue has a finite steady-state solution only when lambda is less than c times mu. The implementation rejects an unstable queue. This is not a numerical inconvenience: when long-run arrival demand meets or exceeds long-run service capacity, the queue cannot settle into a stationary distribution.

## 4. Read the Erlang-C calculation

The solver calculates offered load, utilisation, the empty-system probability and the probability that an arrival finds all servers busy. It then obtains expected waiting time from the spare service capacity.

## 5. Apply Little's law

The package reports expected queue and system lengths using L=lambda W. These are average counts under the steady-state assumptions, not a prediction of the exact queue at a particular minute.

## 6. Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Then execute `notebooks/mmc-queue-lab.ipynb`. Change arrival rate, service rate and server count. Keep all rates in one time unit.

## 7. Challenge the assumptions

A real facility may have lunch peaks, appointments, priority classes, different staff skills, no-shows, abandonment and correlated arrivals. Compare the assumptions with observed data before using the model to make staffing decisions. Validate predicted waits against held-out periods.
