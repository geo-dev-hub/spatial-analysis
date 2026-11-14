# Queueing at a service facility: the M/M/c model

Stable ID: `SA-QUE-MM-C` · Draft 0.1 · Location-science and service operations

## The planning question

A clinic, service desk, charging station or transit counter may be close enough to reach but still impose long waits. Queueing theory connects the rate at which customers arrive with the rate at which servers can complete service.

The M/M/c model is a deliberately idealized starting point for one facility with c identical parallel servers and one shared first-come, first-served queue.

## Model assumptions

- Arrivals follow a stationary Poisson process with rate \(\lambda\).
- Service times are independent and exponentially distributed, with rate \(\mu\) per server.
- There are \(c\) identical servers working in parallel.
- Customers join one FCFS queue; no priority classes, balking, reneging or finite queue limit.
- The calling population is effectively infinite and the system is in steady state.
- Arrival and service rates use the same time unit.

The stability condition is:

\[
\lambda < c\mu.
\]

Utilisation per unit of total service capacity is:

\[
\rho=\frac{\lambda}{c\mu}.
\]

A value of \(\rho\) near one means little spare capacity remains. It does not mean the queue will always be short.

## Erlang-C waiting probability

Let the offered load be \(a=\lambda/\mu\). The probability that an arriving customer must wait is:

\[
P(W_q>0)=
\frac{\dfrac{a^c}{c!(1-\rho)}}
{\displaystyle\sum_{n=0}^{c-1}\frac{a^n}{n!}
+\dfrac{a^c}{c!(1-\rho)}}.
\]

The expected queue wait is:

\[
W_q=\frac{P(W_q>0)}{c\mu-\lambda}.
\]

Expected time in the system includes service time:

\[
W=W_q+\frac{1}{\mu}.
\]

By Little's law:

\[
L_q=\lambda W_q,
\qquad
L=\lambda W.
\]

Here \(L_q\) is the expected number waiting and \(L\) is the expected number in the whole system, including those in service.

## Worked example

Suppose arrivals average 8 people per hour, each server completes 5 people per hour, and there are two identical servers.

\[
\rho=\frac{8}{2\times5}=0.8.
\]

The facility is stable, but utilisation is already high. The notebook calculates Erlang-C waiting probability, expected queue length and expected time in the system. Adding a server can reduce waiting, but the model does not decide whether the staffing cost is justified.

## Reproducible implementation

The [Python package](../../implementations/python/mmc-queue/README.md) computes the steady-state metrics using the Erlang-C expression. It rejects unstable systems rather than returning misleading finite waiting times. Tests check the M/M/1 closed form, monotonic response to extra servers, Little's law and invalid inputs.

## What this model cannot tell you

The M/M/c model is not automatically a realistic description of every facility. It does not represent:
- time-varying arrivals, appointment schedules or correlated surges;
- different service-time distributions or server skills;
- priority classes, abandonment, balking or finite waiting space;
- spatially distributed queues, multiple facilities or customer choice;
- service quality, clinical outcomes or equity by itself.

For a real service plan, estimate arrival and service rates from appropriately sampled operational data, test the distributional assumptions, examine peak periods and validate predicted waits against observed queues. Do not use a daily average arrival rate to hide a severe peak-hour queue.

## Exercises

1. Calculate the result for 8 arrivals per hour, 5 services per hour per server and c=2.
2. Increase c from 2 to 3 while keeping rates fixed. Compare waiting probability and expected wait.
3. Increase arrivals toward total service capacity. Explain why waiting time rises nonlinearly.
4. Use Little's law to independently verify the expected queue and system lengths.
5. Give two reasons a clinic's arrival process might not be Poisson.
6. Explain why the M/M/c result cannot be interpreted as a measure of geographic accessibility or equitable service.

## References

- Erlang, A. K. (1917), “Solution of some problems in the theory of probabilities of significance in automatic telephone exchanges,” *The Post Office Electrical Engineers' Journal*, 10, 189–197.
- Gross, D., Shortle, J. F., Thompson, J. M. and Harris, C. M. (2008), *Fundamentals of Queueing Theory*, 4th ed., Wiley.

**Scope:** one stationary M/M/c queue with homogeneous exponential service, FCFS discipline, infinite queue capacity and stable steady state. No spatial choice, priorities, finite capacity or time-varying arrivals.
