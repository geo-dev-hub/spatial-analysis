# Quadtrees: divide space into smaller regions

A quadtree is a family of hierarchical data structures built around recursive subdivision. In two dimensions, a region is divided into four child regions; in three dimensions, an octree divides a volume into eight. The name describes the branching pattern, not one single data structure or one universal rule for storing objects.

This lesson focuses on the spatial-indexing idea: use a hierarchy of regions to narrow down the parts of space that a query needs to inspect.

## Start with a map question

Suppose a city map contains many points: bus stops, trees, address locations or sensor readings. A query asks which points fall inside a rectangular window.

A brute-force scan checks every point. A point-region quadtree can instead subdivide the study region into four quadrants and recursively subdivide crowded quadrants. A window query can skip cells that do not intersect the query window.

## The basic subdivision

Let the root cell cover a rectangular extent. For a square cell with bounds x_min, y_min, x_max, y_max, the midpoint is:

$$
x_m = \frac{x_{min}+x_{max}}{2}, \qquad
y_m = \frac{y_{min}+y_{max}}{2}
$$

The four child cells are formed by combining the lower and upper halves of each axis:

- southwest: [x_min,x_m] × [y_min,y_m];
- southeast: [x_m,x_max] × [y_min,y_m];
- northwest: [x_min,x_m] × [y_m,y_max];
- northeast: [x_m,x_max] × [y_m,y_max].

A practical implementation must define how points exactly on a dividing line are assigned. Use a consistent half-open interval convention or another explicit tie-breaking rule so that a point is stored once, not duplicated or lost.

## A point-region quadtree

A common point-region (PR) quadtree stores points in leaf cells. A leaf may hold up to a chosen bucket capacity. When inserting a point would exceed that capacity, the cell is split into four children and its points are redistributed.

The splitting rule needs a stopping condition. If several points have identical coordinates, or are too close to distinguish at the chosen precision, repeated subdivision may never separate them. Implementations therefore need a maximum depth, minimum cell size, duplicate-coordinate policy or a combination of these.

A PR quadtree is not the same as a region quadtree. A region quadtree represents a raster-like or block-structured region by subdividing cells until each cell satisfies a homogeneity condition. A point quadtree, a PR quadtree, a region quadtree and a quadtree used for line-segment indexing have different data models and algorithms.

## Querying a rectangular window

For a query rectangle Q and a node cell C:

1. If C does not intersect Q, skip the entire subtree.
2. If C intersects Q and is internal, visit its children.
3. If C intersects Q and is a leaf, test its stored points against Q.
4. Return points satisfying the exact query predicate.

The hierarchy is useful because an entire region can be rejected with one cell-intersection test. The query still needs an exact point-in-window test at the leaves.

## Visualising the subdivision

~~~mermaid
flowchart TD
    A["Root extent"]
    B["Split into four quadrants"]
    C["Inspect point count in each cell"]
    D{"Cell exceeds capacity?"}
    E["Keep points in leaf"]
    F["Split cell and redistribute"]
    G["Repeat until stopping rule"]
    A --> B --> C --> D
    D -- No --> E
    D -- Yes --> F --> G
~~~

This illustrates a bucket PR quadtree. Region quadtrees use a different split criterion, such as whether a cell contains a mixture of foreground and background pixels.

## What affects performance?

A quadtree's depth depends on the spatial distribution, bucket capacity, root extent and stopping rule. A query visits only cells intersecting its window, but a large query or highly clustered data may visit much of the tree.

It is misleading to promise logarithmic query time for every quadtree. A balanced-looking subdivision does not imply that every workload visits only logarithmically many nodes. State the data model and workload before making complexity claims.

## Compare it with an R-tree

| Question | Point-region quadtree | R-tree / packed R-tree |
|---|---|---|
| What is partitioned? | The space itself | Bounding rectangles of stored objects |
| Basic node shape | Four spatial child cells | Variable number of child entries |
| Natural data model | Points or cells/regions, depending on variant | Spatial objects represented by bounding rectangles |
| Query pruning | Skip cells outside query | Skip node MBRs outside query |
| Common issue | Deep subdivision in clustered or coincident data | Overlapping MBRs and weak selectivity |
| Updates | Variant-dependent; insertion is natural in many PR trees | Dynamic R-trees support updates; packed STR trees are static |

Neither structure is universally better. Choose based on whether the data are points, extended geometries, raster-like regions or a changing collection, and on the operations that matter.

## Geospatial coordinate considerations

A quadtree subdivides a coordinate space. If the coordinates are longitude and latitude, equal numeric subdivisions do not correspond to equal ground distances or equal-area cells. For local planar work, a suitable projected CRS may be appropriate. For global indexing, use a spatial model designed for the globe rather than assuming a flat square grid is geographically uniform.

The root extent is also part of the index contract. Define what happens to points outside it: reject them, expand/rebuild the root, or maintain an overflow structure.

## Try it

Create a point set with:
- points spread uniformly across the root;
- a dense cluster in one quadrant;
- several duplicate coordinates;
- points exactly on quadrant boundaries.

Build a bucket PR quadtree and compare its window-query results with a brute-force scan.

Record:
1. node count and maximum depth;
2. number of cells visited by each query;
3. number of point candidates tested;
4. exact result count;
5. behaviour at split lines and duplicate coordinates.

Repeat with different bucket capacities and root extents. Explain why the results can change even though the correct query answer must not.

## References

- Samet, H. (1984), [The quadtree and related hierarchical data structures](https://doi.org/10.1145/356924.356930), ACM Computing Surveys. A foundational survey of quadtree families and applications.
- Samet, H., Rosenfeld, A., Shaffer, C. A. and Webber, R. E. (1984), [A geographic information system using quadtrees](https://doi.org/10.1016/0031-3203(84)90018-9), Pattern Recognition.
- Aref, W. G. and Samet, H. (1997), [Efficient window block retrieval in quadtree-based spatial databases](https://www.cs.umd.edu/~hjs/pubs/geoinformatica97.pdf), GeoInformatica.
- Samet, H. (1991), [Hierarchical data structures for spatial databases](https://www.cs.umd.edu/~hjs/pubs/Sametgisundkartographie91.pdf), for a broader comparison of spatial hierarchical structures.

**Evidence state:** the family distinction and GIS uses are grounded in Samet's survey and GIS papers. This lesson's insertion/query description is specifically a bucket point-region quadtree teaching model; do not generalise its rules to every quadtree variant.
