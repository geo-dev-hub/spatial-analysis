# Intern walkthrough: Strahler order and Shreve magnitude

## 1. Define the network before ordering it

The input is a D8 direction raster plus a boolean stream mask. The stream mask is not inferred here: it is typically derived from a contributing-area or other channel-initiation criterion and then reviewed.

A stream cell must point directly to another stream cell whenever its downstream neighbour is inside the valid raster. This avoids silently calculating an order on a broken network.

## 2. Build the stream graph

Each stream cell is a node. Its D8 direction identifies at most one downstream stream cell. The implementation builds the downstream pointer and counts incoming stream links.

Non-stream cells may contribute to flow accumulation but are not channel tributaries in the ordering calculation.

## 3. Strahler's rule

Headwater links have order one. At a confluence, let $m$ be the largest order among incoming tributaries. The downstream order is:

$$
S_{out}=\begin{cases}
m+1,&\text{if at least two incoming tributaries have order }m,\\
m,&\text{otherwise.}
\end{cases}
$$

A confluence of two first-order streams therefore becomes second order. A second-order and a first-order tributary produce second order, not third.

## 4. Shreve magnitude

Shreve magnitude starts at one for each headwater link and sums at every confluence:

$$
M_{out}=\sum_k M_k
$$

Unlike Strahler order, the magnitude retains the total number of headwater links represented by the tributaries.

## 5. Topological processing

The implementation processes stream cells from upstream to downstream using indegree counts. It tracks the largest incoming Strahler order and how many tributaries share it, while Shreve magnitudes are summed.

If not all stream cells can be processed, a cycle exists and the input is rejected.

## 6. Limits

The result depends on the stream mask, D8 direction model and network topology. A thresholded accumulation raster may create a channel network, but the threshold and resulting connectivity require justification. These topological measures are not discharge or drainage area.
