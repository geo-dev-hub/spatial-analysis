# Geometry foundations: how points, lines and areas relate

<small>Four connected lessons · Start with a map question · Work through the examples in Python</small>

A point falls inside a boundary. Two lines cross. Two areas overlap. A whole network of lines has thousands of crossings.

These sound like separate tasks, but they build on a small set of geometric ideas. This path takes you from one location to a collection of intersecting segments.

You can follow the sequence or jump to the lesson that answers your immediate question. The [interactive geometry foundations lab](../notebooks/geometry-foundations-lab.ipynb) lets you move a point, change a segment and adjust polygon overlap in one place.

## Before you begin

You should be comfortable with:
- reading an x,y coordinate pair;
- understanding a line segment as two endpoints;
- recognising a polygon as a closed boundary.

You do not need advanced mathematics or prior experience with computational geometry. Each lesson introduces the ideas it needs.

## Follow the four lessons

### 1. Is the point inside the area?

[Point in polygon](../algorithms/geometry/point-in-polygon.md)

Start with a familiar map question: does this location fall inside a park, service area or administrative boundary?

You will learn:
- the difference between inside, outside and boundary;
- how ray crossing counts intersections;
- why vertex and edge cases need deliberate handling;
- how winding number offers a related way to describe the interior.

**Try it:** move a point around a square, then test a concave polygon. Run the [Python example](../implementations/python/point-in-polygon/README.md).

### 2. Do these two lines meet?

[Segment intersection](../algorithms/geometry/segment-intersection.md)

Now look at the boundaries themselves. Given two line segments, determine whether they are separate, meet at one point or overlap along part of their length.

You will learn:
- the orientation test and signed area;
- how to detect a proper crossing;
- why endpoint touches and collinear overlaps are separate cases;
- how exact integer predicates and rational coordinates help in a restricted teaching implementation.

**Try it:** change the endpoints and predict the result before running the [Python example](../implementations/python/segment-intersection/README.md).

### 3. What part of two areas do they share?

[Polygon intersection](../algorithms/geometry/polygon-intersection.md)

Use the ideas from point location and segment intersection to understand a full geometry overlay. The output may be an area, a line, a point or an empty geometry.

You will learn:
- the difference between an intersection predicate and an intersection operation;
- how noding turns crossings into explicit vertices;
- how a geometry engine selects and assembles the shared result;
- why precision, invalid inputs and dimensional collapse matter.

**Try it:** run the [Shapely example](../implementations/python/polygon-intersection/README.md), then change the rectangles so they overlap, touch or separate.

### 4. How do we find every crossing in a large set?

[Bentley–Ottmann](../algorithms/geometry/bentley-ottmann.md)

The pairwise test works for two segments. But if you have thousands, checking every pair can waste a lot of work. The sweep-line algorithm keeps track of active segments and tests only newly adjacent pairs under its stated assumptions.

You will learn:
- how an event queue and sweep status work together;
- why intersecting segments become neighbours before they cross;
- how the status order changes at an event;
- why degeneracies and data-structure choices affect real implementations.

**Try it:** follow the [step-by-step implementation walkthrough](../implementations/python/bentley-ottmann/implementation-walkthrough.md), run both implementations and compare them with the all-pairs oracle.

## Continue into polygon geometry

The four foundations above lead into a second set of practical questions: is the boundary valid, how should one polygon be clipped by another, and how do we combine or subtract whole areas?

1. [Check polygon validity](../algorithms/geometry/polygon-validity.md), then inspect the [Shapely validity workflow](../implementations/python/polygon-validity/README.md). Treat repair as an explicit modelling decision.
2. [Understand polygon clipping](../algorithms/geometry/polygon-clipping.md), then run the [convex Sutherland–Hodgman teaching implementation](../implementations/python/polygon-clipping/README.md). Its deliberate convex-input limit is part of the lesson.
3. [Study polygon overlay](../algorithms/geometry/overlay-operations.md), run the [four-operation Shapely/GEOS package](../implementations/python/polygon-overlay/README.md), and explore the [visual overlay lab](../notebooks/polygon-overlay-lab.ipynb).

This continuation distinguishes a narrow algorithm implementation (convex clipping) from a library-backed general overlay workflow. It also reinforces a key habit: inspect the geometry type and validity of every result rather than assuming that polygon inputs always produce polygon outputs.

A related construction problem is the [convex hull](../algorithms/geometry/convex-hull.md): find the smallest convex boundary containing a set of points. Run the [Graham scan implementation](../implementations/python/convex-hull/README.md) and explore its [visual lab](../notebooks/convex-hull-lab.ipynb) to see how interior and collinear points are handled.

The [Voronoi and Delaunay lesson](../algorithms/geometry/voronoi-delaunay.md) then connects nearest-site regions to triangulations. Explore both structures in the [visual tessellation lab](../notebooks/voronoi-delaunay-lab.ipynb) and inspect the [SciPy/Qhull implementation](../implementations/python/voronoi-delaunay/README.md).

## What connects the lessons?

- Point-in-polygon asks where a point sits relative to a boundary.
- Segment intersection asks how two boundary pieces meet.
- Polygon intersection uses those relationships to construct a shared geometry.
- Bentley–Ottmann scales the search for segment crossings across a set of segments.

The path ends with a useful distinction: knowing how to test one pair is not the same as finding every intersecting pair efficiently.

## Check what you can now explain

1. Why should a point on a polygon edge not be silently treated as an ordinary inside point?
2. What does the sign of an orientation determinant tell you?
3. Why can the intersection of two polygons be a line or point rather than an area?
4. Why does Bentley–Ottmann test neighbouring segments instead of every pair?
5. Which assumptions would you need to check before using the teaching implementation on real GIS data?

If you can explain those answers and reproduce the examples, you have a solid first foundation. The next part of the Core GIS collection will extend these ideas into spatial indexes, proximity queries and network analysis.

## Continue into robust geometry and point location

Once you can recognise intersections, two deeper questions follow: how do we make an arrangement reliable on a fixed precision grid, and how can we locate a point quickly in a subdivision with many faces?

- [Snap rounding](../algorithms/geometry/snap-rounding.md) explains hot pixels and why intersections must be found before grid rounding. Run the [visual snap-rounding lab](../notebooks/snap-rounding-noder-lab.ipynb) and inspect the [exact-arithmetic teaching noder](../implementations/python/snap-rounding-noder/README.md).
- [Planar point location](../algorithms/geometry/point-location.md) compares static slab decomposition with randomized trapezoidal maps. Use the [point-location lab](../notebooks/point-location-lab.ipynb) for the implemented slab model, then complete the [randomized trapezoidal-map exercise](../exercises/randomized-trapezoidal-map.md) to trace the more advanced construction.

These are follow-on topics, not prerequisites for the four-lesson foundation. The snap-rounding package is a transparent teaching baseline; the randomized trapezoidal-map exercise is conceptual and does not claim a complete implementation.

## Triangulate a polygon

A simple polygon can be divided into triangles by repeatedly removing an ear. Read the [ear-clipping lesson](../algorithms/geometry/ear-clipping.md), run the [Python teaching implementation](../implementations/python/ear-clipping/README.md), and explore the [visual triangulation lab](../notebooks/ear-clipping-lab.ipynb). This extension assumes one simple ring; holes and constrained Delaunay refinement are separate topics.

## Partition into convex pieces

After triangulating a simple polygon, ask whether adjacent triangles can be merged without introducing a reflex corner. The [convex decomposition lesson](../algorithms/geometry/convex-decomposition.md) compares this approach with optimal dynamic programming and tolerance-based approximate decomposition. Complete the [convex decomposition exercise](../exercises/convex-decomposition.md) before attempting the Hertel–Mehlhorn merge implementation.
