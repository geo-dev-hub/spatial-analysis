# Convex hulls: find the outside boundary of a point set

A convex hull answers a simple question: what is the smallest convex shape that contains every point in this collection?

Imagine stretching a tight rubber band around a set of nails on a board. The band touches the outermost nails. Those contact points form the convex hull. Points inside the band do not affect its boundary.

## The geometric idea

A set is convex when the straight line segment between any two points in the set stays entirely inside it.

For a finite point set P, its convex hull is the smallest convex set containing P:

$$
\operatorname{CH}(P)=
\bigcap\{C\mid P\subseteq C,\ C\text{ is convex}\}
$$

For a non-degenerate planar point set, the hull boundary is a convex polygon. Depending on the input, the result may instead be empty, one point or a line segment.

## Why it matters

A convex hull is a useful geometric summary. It can support:

- a coarse extent around a collection of facilities or observations;
- collision and separation reasoning;
- spatial clustering and shape descriptors;
- preprocessing for other geometric algorithms;
- approximate envelopes for visualisation and analysis.

It is not a substitute for the original geometry. A hull fills concavities and can include large areas that contain no input points.

## The orientation test

For three points O, A and B, calculate the signed 2D cross product:

$$
\operatorname{cross}(O,A,B)
=(A_x-O_x)(B_y-O_y)-(A_y-O_y)(B_x-O_x)
$$

- Positive: A to B makes a counter-clockwise turn around O.
- Negative: the turn is clockwise.
- Zero: the three points are collinear.

This predicate is the central decision in Graham scan. As the algorithm walks around the sorted points, a clockwise turn means the previous candidate cannot remain on the convex boundary.

## Graham scan

Graham scan builds the hull in two broad phases:

1. Sort points by their polar angle around a pivot.
2. Scan that order, maintaining a stack of the boundary vertices.

The pivot is commonly the point with the lowest y-coordinate, breaking ties by lowest x-coordinate. It is guaranteed to be a hull vertex.

~~~mermaid
flowchart TD
    A["Input points"] --> B["Remove duplicate coordinates"]
    B --> C["Choose lowest-then-leftmost pivot"]
    C --> D["Sort remaining points by polar angle"]
    D --> E["Keep farthest point on each pivot ray"]
    E --> F["Process points in sorted order"]
    F --> G{"Does the last turn go left?"}
    G -- "No: clockwise or collinear" --> H["Pop middle stack point"]
    H --> G
    G -- "Yes" --> I["Push new point"]
    I --> J{"More points?"}
    J -- Yes --> F
    J -- No --> K["Return counter-clockwise hull"]
~~~

The stack is the key idea: every time a point is popped, it is no longer part of the current outer boundary. Each sorted point is pushed once and popped at most once.

### Same-angle points

Several points may lie on the same ray from the pivot. Only the farthest one can be an extreme hull vertex. A stable implementation must define how it orders and collapses these points.

### Collinear boundary points

Some applications want every input point along the hull boundary. Others want only the extreme vertices. The teaching implementation in this repository uses the second policy: intermediate collinear boundary points are omitted. State this choice because it changes the output vertex sequence.

## Complexity

The polar sort takes (O(n\log n)). The stack scan is (O(n)), because each point is pushed once and popped at most once. The total time is therefore:

$$
T(n)=O(n\log n)
$$

The result stores at most n vertices, so auxiliary storage is (O(n)).

## Numerical robustness

The cross product is a floating-point predicate in the teaching implementation. When points are nearly collinear, rounding can change the sign and therefore change which point is popped.

For high-assurance computational geometry, use exact or adaptive-precision orientation predicates. Do not assume that a small epsilon is a universal repair: the appropriate tolerance depends on coordinate scale and the intended geometry model.

## Convex hull is not concave hull

A convex hull always produces a convex envelope. It may cover large empty spaces between separated clusters. A concave hull attempts to follow the shape of the data more closely, but there is no single universal concave-hull definition; methods such as alpha shapes introduce additional parameters and modelling choices.

Do not use the terms interchangeably.

## Other convex-hull algorithms

The source compendium also names Jarvis march (gift wrapping) and Quickhull. They solve the same broad problem using different strategies and trade-offs. This repository's runnable example is Graham scan; it does not claim to implement those alternatives.

## Try it

1. Add a point strictly inside the hull. Does the hull change?
2. Add a point outside one edge. Which vertices are replaced?
3. Add several points along one hull edge. Which ones remain under the stated collinearity policy?
4. Make all points collinear. What should the hull contain?
5. Scale the coordinates by a large factor. Does the mathematical hull change?
6. Construct almost-collinear triples. Why might floating-point predicates become unreliable?

## Reproduce the teaching example

The [Graham scan implementation](../../implementations/python/convex-hull/README.md) is dependency-free and includes tests for duplicates, collinear points, degenerate inputs, orientation and non-finite coordinates. Follow the [step-by-step walkthrough](../../implementations/python/convex-hull/implementation-walkthrough.md) and explore the [visual convex hull lab](../../notebooks/convex-hull-lab.ipynb).

## References

- Graham, R. L. (1972), [An efficient algorithm for determining the convex hull of a finite planar set](https://doi.org/10.1016/0020-0190(72)90045-2), Information Processing Letters.
- Preparata, F. P. and Shamos, M. I. (1985), *Computational Geometry: An Introduction*, Springer, for foundational geometric algorithms.
- [CGAL 2D convex hull documentation](https://doc.cgal.org/latest/Convex_hull_2/index.html), for robust computational geometry implementations and traits.

**Evidence state:** the Graham scan description and asymptotic bound are grounded in the original paper and standard computational geometry references. The repository implementation is a deliberately small floating-point teaching version, not an exact-predicate geometry kernel.
