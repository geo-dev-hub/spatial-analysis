# Strahler order and Shreve magnitude for a D8 stream raster

Stream ordering describes the branching structure of a mapped channel network. This package calculates two common measures on an explicitly supplied stream mask and D8 direction raster:

- **Strahler order:** headwater streams are order 1. At a confluence, the order increases by one only when at least two incoming tributaries share the maximum order.
- **Shreve magnitude:** headwater streams have magnitude 1; downstream magnitude is the sum of incoming tributary magnitudes.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract and limitations

- Direction codes follow ESRI D8: E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128, terminal=0, invalid=-1.
- The stream mask is a boolean raster with the same shape as the direction grid.
- A stream cell that flows to another valid cell must flow directly to another stream cell. A disconnected stream mask is rejected.
- Flow from a non-stream cell into a stream cell does not count as a stream tributary.
- Stream cells that drain beyond the raster or into NoData are terminal for this network.
- Cycles in the stream subgraph are rejected.
- Non-stream cells have order/magnitude 0; invalid cells have -1.
- These are topological network measures, not channel discharge, drainage area or a substitute for checking the extracted network.

Read the [canonical lesson](../../../algorithms/raster/stream-order.md) and [intern walkthrough](implementation-walkthrough.md).
