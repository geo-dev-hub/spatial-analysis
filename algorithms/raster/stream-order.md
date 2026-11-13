# Stream ordering: Strahler order and Shreve magnitude

Stable ID: `SA-RASTER-STREAM-ORDER` · Draft 0.1 · Source compendium section 4, page 7

## Why assign stream order?

A drainage network is not just a collection of lines. Its branching structure can be summarised to compare network hierarchy and complexity. Two common measures are Strahler order and Shreve magnitude.

Both require a stream network with known connectivity and direction. This lesson uses a D8 direction raster plus an explicit stream mask; it does not choose a channel-initiation threshold.

## Strahler order

Headwater streams have order one. At a confluence, let $m$ be the highest order among incoming tributaries. Increase the order only if at least two incoming tributaries have that same maximum order:

$$
S_{out}=\begin{cases}
m+1,&\text{if two or more tributaries have order }m,\\
m,&\text{otherwise.}
\end{cases}
$$

Thus, two first-order tributaries produce a second-order downstream link. A first-order tributary joining a second-order link leaves the downstream order at two.

## Shreve magnitude

Shreve magnitude assigns one to each headwater link and sums magnitudes at confluences:

$$
M_{out}=\sum_k M_k
$$

The magnitude counts the headwater contributions represented by a downstream link. It is not stream discharge.

## Network representation and implementation

The [teaching implementation](../../implementations/python/stream-order/README.md) takes an explicit stream mask and D8 direction grid. A stream cell must flow directly to another stream cell if its next cell is valid and inside the raster; otherwise the mask is rejected as disconnected. Non-stream cells are not counted as stream tributaries.

The stream graph is processed in topological order. Cycles are rejected. Non-stream cells receive zero and invalid cells receive -1 in the output arrays.

## Important modelling choices

- Stream initiation may be based on an accumulation threshold, mapped hydrography or another criterion. The choice changes the network.
- A D8 network sends flow along one cell-to-cell link. Multiple-flow-direction routing needs a different network representation.
- Stream order depends on topology and network pruning; it is not a direct physical measure of channel size or discharge.
- The implementation does not extract channels, calculate drainage density, estimate discharge or correct an inconsistent stream mask.

## Exercises

1. Draw two first-order tributaries meeting. Calculate Strahler order and Shreve magnitude downstream.
2. Add a first-order tributary to a second-order stream. Compare the two measures.
3. Compare two second-order tributaries joining.
4. Change the channel-initiation threshold. How does the stream network and its order change?
5. Explain why stream order is not a substitute for discharge or drainage area.

## References

- Strahler, A. N. (1957), *Quantitative analysis of watershed geomorphology*, Transactions, American Geophysical Union, 38(6), 913–920.
- Shreve, R. L. (1966), *Statistical law of stream numbers*, Journal of Geology, 74(1), 17–37.

**Scope:** Strahler order and Shreve magnitude on a connected, acyclic D8 stream mask; channel extraction and alternative flow-routing models are not included.
