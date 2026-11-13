# Turn-aware and time-dependent routing baselines

This package adds two road-network modelling examples beyond a node-only
shortest-path graph.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Turn-aware shortest path

Edges are explicit records: `(edge_id, tail, head, cost)`. The search state is
the incoming edge, so a transition can be prohibited or assigned a turn
penalty. This is the basic reason a turn-restricted road router often needs an
edge-based graph rather than one state per intersection.

## Time-dependent earliest arrival

The time-dependent function receives an edge ID and the actual departure time
from that edge. It returns the travel duration. The search returns an absolute
arrival time, not an elapsed duration.

The label-setting algorithm requires FIFO edge-arrival functions: leaving later
must not result in arriving earlier on the same edge. The code validates that
travel times are finite and non-negative, but it cannot prove FIFO for an
arbitrary Python callable. The caller must document and test that contract.

## Limits

These are small teaching baselines. They do not parse GTFS, model waiting
choices or service calendars, support multimodal transfers, infer turn
restrictions from source data, or provide production-grade network snapping
and route geometry.
