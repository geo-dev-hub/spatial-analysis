# Implementation walkthrough: Voronoi and Delaunay with SciPy

## 1. Start with sites

A site is a point that generates a region in a Voronoi diagram. Given sites p_1,...,p_n, the Voronoi region of p_i contains all locations at least as close to p_i as to any other site:

$$
V(p_i)=\{x\in\mathbb{R}^2:
\|x-p_i\|\leq\|x-p_j\|\text{ for all }j\}
$$

The boundaries between regions are perpendicular bisectors of pairs of sites.

## 2. Understand the dual structure

The Delaunay triangulation connects two sites when their Voronoi regions share an edge. A Voronoi vertex is equidistant from three or more sites; the corresponding sites form a Delaunay face.

For a non-degenerate triangle, the Delaunay condition is the empty-circumcircle property: no other site lies inside its circumcircle.

## 3. Validate the input before calling Qhull

The wrapper checks:
1. the coordinate array has exactly two columns;
2. at least three sites are supplied;
3. all coordinates are finite;
4. duplicate coordinates are absent;
5. the points span a two-dimensional plane.

The last check rejects a collinear set, for which a two-dimensional triangulation is not defined in the intended way.

## 4. Delegate construction explicitly

The implementation calls SciPy's Voronoi and Delaunay constructors. SciPy uses Qhull for these computational geometry structures. The package is therefore a checked library workflow, not a reimplementation of Fortune's sweep-line or Bowyer–Watson's incremental triangulation.

This distinction matters in teaching: the lesson explains the underlying ideas, while the package demonstrates a maintained implementation interface.

## 5. Inspect the output

- Voronoi vertices are the finite meeting points of three or more Voronoi boundaries.
- Voronoi regions can be unbounded; their infinite rays are part of the mathematical diagram.
- Delaunay simplices contain indices into the original site array.
- The chosen diagonal for cocircular sites is not unique, so tests should check valid triangulation properties rather than one arbitrary diagonal.

## 6. Reproduce the checks

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python tessellation_demo.py
~~~

The tests verify triangle counts for simple cases, use of interior sites, equal distances from a Voronoi vertex, the Delaunay empty-circumcircle property, invalid input rejection and read-only site coordinates.

## 7. Coordinate model

The algorithms here use planar Euclidean distance. Do not construct a citywide or global tessellation directly from longitude and latitude degrees and interpret it as a uniform ground-distance partition. Choose an appropriate projected coordinate system for local work or a suitable spherical/geodesic model for global work.

## 8. Numerical limits

The wrapper does not alter Qhull's degeneracy policy. Nearly collinear, duplicate or cocircular configurations can require special handling. For reproducible work, record SciPy/Qhull versions and inspect the exact input and output. For robust production geometry, select a library and precision model whose guarantees match the application.
