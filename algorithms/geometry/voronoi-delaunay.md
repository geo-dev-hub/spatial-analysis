# Voronoi diagrams and Delaunay triangulations: two views of the same sites

A collection of points can describe two different but closely connected structures:

- A **Voronoi diagram** divides the plane into regions according to the nearest site.
- A **Delaunay triangulation** connects sites into triangles whose circumcircles contain no other site in their interior.

These are geometric duals. Understanding one makes the other easier to reason about.

## The nearest-site question

Suppose each point represents a facility, service location or observation. For any location x, which site is closest?

For a site p_i, its Voronoi region is:

$$
V(p_i)=\{x\in\mathbb{R}^2:
\|x-p_i\|\leq\|x-p_j\|\quad\forall j\}
$$

Every point in that region is at least as close to p_i as to any other site. The boundary between two regions lies on the perpendicular bisector of their two sites.

A Voronoi diagram is the collection of all these regions and their shared boundaries.

## The Delaunay view

The Delaunay triangulation connects two sites when their Voronoi regions share an edge. A Voronoi vertex is equidistant from three or more sites; those sites define a Delaunay face.

For a non-degenerate triangle, the defining property is the **empty circumcircle**: no other site lies strictly inside its circumcircle.

~~~mermaid
flowchart TD
    A["Start with a set of sites"]
    B["Construct nearest-site Voronoi regions"]
    C["Find pairs of regions sharing an edge"]
    D["Connect their generating sites"]
    E["Delaunay graph"]
    F["Triangulate polygonal faces where required"]
    A --> B --> C --> D --> E --> F
~~~

The duality is structural, not a visual coincidence. Voronoi vertices correspond to Delaunay faces, and Voronoi edges correspond to Delaunay edges. In a non-degenerate general-position set, the Delaunay faces are triangles. When four or more sites are cocircular, a Voronoi vertex can have degree greater than three and the Delaunay face may require a choice of diagonals to form a triangulation.

## Where these structures are useful

- **Nearest-facility analysis:** identify the nearest site and understand how its service territory changes.
- **Proximity and adjacency:** identify neighbouring sites without comparing every pair directly.
- **Spatial partitioning:** construct regions around monitoring stations, service facilities or sample points.
- **Mesh generation:** build triangulations used in finite-element and numerical workflows.
- **Movement and visibility:** support geometric reasoning in robotics, navigation and computational geometry.

A Voronoi cell is not automatically a realistic service area. It assumes nearest-site assignment under a chosen distance metric and does not account for roads, barriers, capacity, travel time or demand.

## Fortune's sweep-line algorithm

Fortune's algorithm constructs the Voronoi diagram of point sites using a plane sweep. The sweep maintains a **beach line**: a sequence of parabolic arcs that separates the already processed part of the diagram from the unprocessed part.

Two event families change the beach line:

1. **Site events:** the sweep reaches a new site. A new parabolic arc is inserted and an existing arc is split.
2. **Circle events:** an arc disappears as the sweep reaches the lowest point of a circle through three neighbouring sites. This identifies a Voronoi vertex and changes the beach-line adjacency.

A priority queue orders upcoming events. A balanced search structure maintains the beach line. Fortune's original point-site algorithm has (O(n\log n)) worst-case time and (O(n)) space under its stated model.

~~~mermaid
flowchart TD
    A["Sort sites and initialise event queue"]
    B["Take next event"]
    C{"Site or circle event?"}
    D["Insert site arc into beach line"]
    E["Remove disappearing arc"]
    F["Create Voronoi vertex and edges"]
    G["Update neighbouring circle events"]
    H{"More valid events?"}
    I["Finish diagram and handle unbounded edges"]
    A --> B --> C
    C -- Site --> D --> G
    C -- Circle --> E --> F --> G
    G --> H
    H -- Yes --> B
    H -- No --> I
~~~

This is a conceptual event flow, not a complete implementation specification. A production Fortune implementation must manage invalidated events, simultaneous events, cocircular sites, beach-line ordering and numerical robustness.

## Other construction approaches

Voronoi and Delaunay structures can be built through several algorithm families:

| Family | Core idea | Important qualification |
|---|---|---|
| Fortune sweep | Sweep the plane while maintaining the beach line and event queue | Efficient but subtle event and degeneracy handling |
| Divide and conquer | Build structures for subsets and merge them | Merge topology and degeneracies require careful handling |
| Incremental insertion | Insert sites one at a time and update the affected neighbourhood | Point order and point-location strategy affect performance |
| Bowyer–Watson | Remove triangles whose circumcircles contain the inserted site, then retriangulate the cavity | Circumcircle predicates and cavity boundary handling are numerically sensitive |
| Local edge flipping | Start from a triangulation and flip edges until the local Delaunay condition holds | Requires a valid initial triangulation and termination rules |

The repository's runnable package uses SciPy/Qhull. It does **not** implement Fortune's sweep or Bowyer–Watson. That distinction is explicit so a library call is not mistaken for an implementation of a named algorithm.

## Degeneracies and modelling choices

- **Duplicate sites:** two identical coordinates do not define distinct nearest-site regions.
- **Collinear sites:** the intended two-dimensional triangulation degenerates.
- **Cocircular sites:** more than one Delaunay diagonal may be valid.
- **Nearly collinear or cocircular sites:** floating-point predicates can change topology.
- **Unbounded Voronoi cells:** outer regions extend infinitely. A plotting extent is only a display window, not a mathematical boundary.
- **Metric choice:** Euclidean distance in longitude/latitude degrees is not geodesic ground distance.

State the coordinate system, distance metric, duplicate policy, degeneracy policy and software version before interpreting the output.

## Reproduce the visual example

The repository includes a [validated SciPy/Qhull wrapper](../../implementations/python/voronoi-delaunay/README.md), with an [intern walkthrough](../../implementations/python/voronoi-delaunay/implementation-walkthrough.md) and a [visual notebook](../../notebooks/voronoi-delaunay-lab.ipynb). The tests check the Voronoi equidistance property and the Delaunay empty-circumcircle property. They do not claim to verify Fortune's algorithm.

## Try it

1. Add a site near the centre. Which Voronoi regions shrink or expand?
2. Move a site outside the current point set. Which Delaunay triangles change?
3. Place four sites on a circle. Why can either diagonal be valid?
4. Create duplicate and collinear sites. Which input rules should reject them?
5. Explain why a Voronoi nearest-site partition is not the same as a road-network service area.

## References

- Fortune, S. (1987), [A sweepline algorithm for Voronoi diagrams](https://doi.org/10.1007/BF01840357), Algorithmica 2, 153–174.
- Aurenhammer, F. (1991), [Voronoi diagrams—a survey of a fundamental geometric data structure](https://doi.org/10.1145/116873.116880), ACM Computing Surveys 23(3), 345–405.
- [SciPy Voronoi documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Voronoi.html) and [Delaunay documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html), for the library-backed example.
- [Qhull documentation](http://www.qhull.org/), for the underlying convex-hull and tessellation library.

**Evidence state:** Fortune's algorithm and complexity are grounded in the original paper; the family overview and Voronoi properties are supported by Aurenhammer's survey. The runnable implementation delegates to SciPy/Qhull and does not claim those papers' algorithms are implemented in this repository.
