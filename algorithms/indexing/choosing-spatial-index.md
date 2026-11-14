# Choosing a spatial index: match the structure to the question

A spatial index is not a faster version of every spatial operation. It is a data structure that makes particular queries cheaper by organising data so that parts of the search can be ruled out.

The right choice depends on four things:

1. **What is stored?** Points, extended geometries, raster-like regions or high-dimensional vectors.
2. **What is queried?** Window intersection, exact geometry predicate, nearest neighbour, k-nearest neighbours or a join.
3. **How does the data change?** Immutable snapshot, frequent insertion, deletion or periodic rebuild.
4. **Which metric and coordinate model apply?** Planar Euclidean, geodesic or another distance function.

## Start with the query, not the index name

~~~mermaid
flowchart TD
    A["What are you indexing?"]
    B{"Extended geometries?"}
    C["R-tree / STRtree"]
    D{"2D point data?"}
    E{"Main query is nearest neighbour?"}
    F["k-d tree"]
    G["Point-region quadtree"]
    H["Choose a structure for the data model and metric; benchmark candidates"]
    I["Apply exact predicates after envelope filtering"]
    A --> B
    B -- Yes --> C --> I
    B -- No --> D
    D -- No --> H
    D -- Yes --> E
    E -- Yes --> F
    E -- No --> G
~~~

This is a starting guide, not a complete taxonomy. A workload may need more than one index, and production libraries may use hybrid strategies internally.

## Compare the structures in this collection

| Structure | What it organises | Good starting query | Update model in the teaching example | Main caution |
|---|---|---|---|---|
| STR-packed R-tree | 2D bounding boxes of objects | Rectangle/window candidates | Immutable after bulk loading | Candidate boxes are not the exact geometry |
| Shapely STRtree | Envelopes of Shapely geometries | Spatial query and optional exact predicate | Query-only, rebuild to change contents | Tree results and predicate semantics are version-specific |
| Point-region quadtree | 2D points assigned to spatial cells | Rectangular point-window query | Insertions within a fixed root; no deletion | Root extent, depth and duplicate points need explicit rules |
| k-d tree | Points split by coordinate axes | Exact low-dimensional nearest neighbour | Static after construction | Worst-case search can approach a scan; high dimensions weaken pruning |

The teaching implementations deliberately have different contracts. Do not compare their timings as if they performed the same task.

## R-tree: index extended objects by their envelopes

An R-tree stores minimum bounding rectangles (MBRs) that enclose geometries. It is a natural first choice when the objects are polygons, lines or other extended features and the query is about spatial overlap.

The index first returns envelope candidates. A candidate may still fail the exact geometry predicate, especially for concave or multipart geometries with large empty spaces inside their bounding boxes.

Read the [STR-packed R-tree lesson](str-packed-rtree.md), run its [Python implementation](../../implementations/python/str-packed-rtree/README.md), and compare it with the [filter-and-refine spatial join](../query-processing/filter-refine-spatial-join.md).

## Point-region quadtree: partition the plane

A point-region quadtree divides a fixed 2D extent into four cells recursively. It is useful when point data and rectangular window queries are central, and when a spatial partition is a helpful way to organise the workload.

Its behaviour depends on the root extent, bucket capacity, split-line convention, maximum depth and distribution of points. Coincident points cannot be separated by repeated subdivision, so stopping rules are essential.

Read the [quadtree lesson](quadtree.md) and reproduce the [bucket PR quadtree implementation](../../implementations/python/quadtree/README.md).

## k-d tree: prune nearest-neighbour searches

A k-d tree recursively partitions point coordinates along one axis at a time. For low-dimensional Euclidean nearest-neighbour queries, the split planes provide lower bounds that can help prune branches.

The method is not a universal nearest-neighbour accelerator. High-dimensional data, poor distributions or weak bounds can make many branches relevant. The metric used by the query must agree with the lower-bound calculation.

Read the [k-d tree lesson](kd-tree-nearest-neighbour.md) and reproduce the [2D teaching implementation](../../implementations/python/kd-tree/README.md).

## The coordinate model is part of the index

A tree built on longitude and latitude degrees is indexing a coordinate plane, not equal-distance ground space. Degrees of longitude vary in ground length by latitude, and Euclidean distance in degrees is not geodesic distance.

Before indexing, decide whether the task is local planar analysis or global geographic analysis. For local work, choose a suitable projected CRS and record its units. For global work, use a distance-aware method or a spatial representation whose query bounds are valid for the intended metric.

Do not reuse Euclidean k-d tree pruning bounds for geodesic distance without proving that the bounds remain valid.

## A fair comparison protocol

A meaningful index benchmark must hold the query problem constant.

1. **Define one dataset.** Record point/geometry counts, coordinate extent, distribution, dimensionality and geometry complexity.
2. **Define one exact answer.** Use the same boundary policy, predicate, distance metric and tie policy for every candidate.
3. **Build the same query workload.** Include small and large windows, clustered regions, edge-touching cases and queries outside dense areas.
4. **Measure build and query separately.** Include rebuild cost for static indexes and update cost for mutable ones.
5. **Count work as well as time.** Record nodes visited, candidates returned, exact predicates evaluated and memory use where possible.
6. **Check every result.** Compare against a brute-force oracle on deterministic samples and adversarial edge cases.
7. **Repeat.** Report hardware, software versions, warm-up, repetitions and distributions rather than one timing.

A query result that is fast but incomplete is not a successful index.

## Practical selection checklist

Before choosing, write down:

- object type and dimensionality;
- query type and exact predicate;
- coordinate reference system and distance metric;
- update frequency and rebuild tolerance;
- expected data distribution and scale;
- boundary and tie semantics;
- memory constraints;
- required exactness or permitted approximation;
- validation oracle and benchmark workload.

If those details are unknown, start with a brute-force implementation. It is often the clearest correctness oracle and may be fast enough for small data.

## Reproduce the collection

- [STR-packed R-tree](../../implementations/python/str-packed-rtree/README.md)
- [Filter-and-refine spatial join](../../implementations/python/spatial-join/README.md)
- [Point-region quadtree](../../implementations/python/quadtree/README.md)
- [k-d tree nearest neighbour](../../implementations/python/kd-tree/README.md)

## References

- Guttman, A. (1984), [R-trees: A dynamic index structure for spatial searching](https://doi.org/10.1145/602259.602266), for the R-tree family.
- Leutenegger, S. T., Edgington, J. M. and Lopez, M. A. (1997), [STR: A simple and efficient algorithm for R-tree packing](https://doi.org/10.1109/ICDE.1997.582015), for Sort-Tile-Recursive bulk loading.
- Samet, H. (1984), [The quadtree and related hierarchical data structures](https://doi.org/10.1145/356924.356930), for quadtree families.
- Bentley, J. L. (1975), [Multidimensional binary search trees used for associative searching](https://doi.org/10.1145/361002.361007), for k-d trees.
- [Shapely STRtree documentation](https://shapely.readthedocs.io/en/stable/strtree.html), for the maintained Python geometry-index interface.

**Evidence state:** the data-structure descriptions are linked to foundational papers and maintained implementation documentation. The selection guidance is workload-oriented; it is not a claim that one structure dominates another.
