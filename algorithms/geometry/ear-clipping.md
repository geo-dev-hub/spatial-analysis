# Ear clipping: triangulate a simple polygon

A concave polygon can be difficult to process as one large area. Triangulation divides its interior into triangles while preserving the original boundary. This is useful in mesh construction, rendering, finite-element preparation and some spatial-analysis workflows.

Ear clipping is one of the clearest ways to understand the construction.

## What is an ear?

Take three consecutive boundary vertices (a,b,c). They form an *ear at (b)* when the triangle (abc) lies inside the polygon and its diagonal (ac) is a valid interior diagonal. The middle vertex is called the ear tip.

<escape>
~~~text
        b
       / \
      /   \
     a-----c
      candidate ear
~~~
</escape>

The dashed conceptual diagonal (ac) replaces the two boundary edges (ab) and (bc). The triangle is recorded, and (b) is removed from the active ring.

## The orientation test

For three points, use the signed determinant

[
\operatorname{orient}(a,b,c)=
(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x).
]

For a counter-clockwise ring:

- positive: the turn at (b) is convex;
- negative: the turn is reflex;
- zero: the three points are collinear.

The determinant is twice the signed area of triangle (abc). It avoids calculating angles and slopes.

## How clipping proceeds

1. Remove a repeated closing vertex and redundant consecutive duplicates.
2. Remove a collinear middle vertex only when it lies between its neighbours.
3. Reject a zero-area or self-intersecting ring.
4. Normalize the ring to counter-clockwise orientation.
5. Find a convex candidate vertex.
6. Test whether any other active vertex lies inside or on its candidate triangle. If one does, this candidate is not an ear.
7. Record the triangle and remove its middle vertex.
8. Repeat until three vertices remain; those form the final triangle.

Meisters' two-ears theorem establishes that every simple polygon with at least four vertices has at least two non-overlapping ears. This is the existence argument behind repeated clipping.

## A small invariant

A triangulation of a simple polygon with (n) vertices has

[
T=n-2
]

triangles and (n-3) internal diagonals. The count follows directly from clipping: each ear removes one vertex and contributes one triangle; the final three vertices contribute the last triangle.

For a polygon with area (A(P)), the triangle areas should satisfy

[
\sum_{i=1}^{n-2} A(T_i)=A(P).
]

Area agreement is a strong diagnostic, but it does not by itself prove that triangles do not overlap. The ear condition and simple-polygon precondition are essential.

## Follow the clipping decisions\n\n~~~mermaid\nflowchart TD\n    A[Read polygon ring] --> B[Normalize duplicates and collinear points]\n    B --> C[Check area and simple topology]\n    C --> D[Orient ring counter-clockwise]\n    D --> E[Find a convex candidate vertex]\n    E --> F{Any other vertex inside or on triangle?}\n    F -- Yes --> G[Reject this candidate]\n    G --> E\n    F -- No --> H[Record triangle and remove ear tip]\n    H --> I{Three vertices remain?}\n    I -- No --> E\n    I -- Yes --> J[Emit final triangle]\n~~~\n\nThe flow is deliberately sequential. It is easy to trace and test, but it is not the most efficient way to maintain the set of possible ears.\n\n## Complexity

The teaching implementation checks up to (O(n)) candidate vertices at each of (O(n)) clipping steps. Its point-in-triangle check can inspect another (O(n)) vertices, but the implementation uses the convex-vertex filter and simple active-ring scan. The resulting straightforward algorithm is (O(n^2)) worst-case when candidate testing scans only reflex vertices; this package instead scans all remaining vertices, so its conservative bound is **(O(n^3))** in the worst case. This distinction matters: the code prioritizes transparency over an optimized ear queue.

The validation pass for non-adjacent edge intersections is also (O(n^2)). The output and active-ring storage require (O(n)) space.

## Assumptions and limitations

This lesson and package handle one simple polygon ring. They do not handle holes, multipolygons, self-intersections, constrained segments, Delaunay refinement or mesh-quality optimization. Collinear vertices are simplified only under the documented between-neighbours rule. Exact rational predicates avoid floating-point sign ambiguity for decimal input values, but can be slower as coordinate numerators and denominators grow.

A triangulation is not automatically a constrained Delaunay triangulation. If triangle quality, constrained edges or holes matter, select a library and method that explicitly supports those requirements.

## Follow the implementation

- [Python implementation](../../implementations/python/ear-clipping/README.md)
- [Intern walkthrough](../../implementations/python/ear-clipping/implementation-walkthrough.md)
- [Exercise](../../exercises/ear-clipping-triangulation.md)
- [Visual lab](../../notebooks/ear-clipping-lab.ipynb)

## Further reading

- Meisters, G. H. (1975), [*Polygons have ears*](https://www.jstor.org/stable/2319845), The American Mathematical Monthly 82(6), 648–651. The two-ears theorem provides the existence result used by the method.
- Eder, G., Held, M. & Palfrader, P. (2015), *Experiments on Parallel Polygon Triangulation Using Ear Clipping*. The paper describes ear candidates, clipping and the (O(n^2)) baseline, and discusses practical parallel variants.
- Geometric Tools, [*Triangulation by Ear Clipping*](https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf), for a careful presentation of the simple-polygon method and its complexity.
