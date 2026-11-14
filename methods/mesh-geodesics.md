# Geodesics on triangle meshes: exact wavefronts and fast marching

A geodesic is a shortest path constrained to a surface. On a flat plane, the shortest path between two points is a straight segment. On a curved or folded surface, the shortest path may bend in 3D while remaining on the surface.

This lesson focuses on triangulated surfaces. It distinguishes exact polyhedral geodesics from numerical approximations to the Eikonal equation, and it explains why ordinary shortest paths on the mesh edge graph solve a different problem.

## 1. Three different distance problems

Let a triangle mesh represent a piecewise-flat surface M, and let s and t be points on that surface.

1. **Edge-graph distance:** paths may travel only along mesh edges. Dijkstra's algorithm gives the exact shortest path in this graph.
2. **Polyhedral surface geodesic:** paths may cross triangle interiors. The path is straight when unfolded across adjacent faces, except at vertices where the geodesic may pass through a saddle-type configuration.
3. **Weighted travel-time geodesic:** movement has spatially varying speed or cost. The path minimizes travel time or accumulated cost, not necessarily Euclidean surface length.

The edge graph is a constrained subset of all surface paths. Its shortest route is therefore generally longer than or equal to the true continuous surface geodesic.

## 2. What makes a path geodesic?

On a smooth surface, a geodesic has zero geodesic curvature: locally, it does not turn within the tangent plane. On a polyhedral surface, unfold the adjacent triangles into one plane. A shortest path crossing an ordinary edge continues as a straight line in this unfolded neighbourhood.

A useful local test is to unfold the two faces sharing an edge into the same plane. If the path bends at the shared edge after unfolding, it can usually be shortened locally. This is the surface analogue of the straight-line shortest-path principle.

At a mesh vertex, the geometry is different. The total incident angle may be less than, equal to or greater than 2π. A shortest path can pass through a vertex only under the appropriate local angular condition; algorithms must account for vertex events rather than assume every path crosses edges in generic positions.

## 3. Exact polyhedral methods: MMP and Chen–Han

### Mitchell–Mount–Papadimitriou (MMP)

The MMP method uses a continuous-Dijkstra viewpoint. Instead of assigning a single distance to each mesh vertex, it propagates wavefront information across edges as windows. Each window represents a family of shortest paths whose distance function can be expressed relative to a source image in an unfolded sequence of faces.

When a window reaches another edge, the algorithm computes the portion of that edge visible to the propagated shortest paths and creates successor windows. Competing windows are pruned when one is dominated by another. The resulting subdivision supports distance queries and path back-tracing.

For a polyhedral surface with n edges, the published MMP result gives O(n² log n) preprocessing time and O(n²) space. After preprocessing, point location in the subdivision supports distance queries; path reconstruction additionally depends on the number of faces crossed. These are theoretical bounds for the stated algorithm and model, not a promise about every software implementation.

### Chen–Han

Chen and Han proposed a different exact approach to shortest paths on a possibly nonconvex polyhedron. Their 1990 conference paper describes O(n²) time and Θ(n) space for the source-based computation and its inward layout. The algorithm differs from the conventional continuous-Dijkstra propagation strategy.

Do not conflate the Chen–Han method with MMP merely because both compute exact polyhedral surface paths. Their data structures, propagation strategy, complexity statements and implementation details differ.

### What “exact” means here

“Exact” describes the geometric problem and algorithmic formulation: the method seeks the shortest path on the piecewise-flat polyhedral surface rather than the shortest path constrained to mesh edges. A floating-point implementation can still incur numerical error. Robust predicates, window comparisons, degeneracies and path reconstruction remain engineering concerns.

## 4. Fast marching on triangulated domains

Fast marching solves an Eikonal-type equation using an upwind numerical scheme and an ordered front propagation. For isotropic unit-speed propagation, the arrival-time field T satisfies

$$
\lVert\nabla T(x)\rVert=1,
$$

with T=0 at the source. For spatial speed F(x)>0,

$$
\lVert\nabla T(x)\rVert=\frac{1}{F(x)}.
$$

The method maintains accepted, trial and far states. It repeatedly accepts the trial point with the smallest arrival time and updates its neighbours using a causal upwind discretisation. A priority queue gives the familiar O(M log M) complexity for M mesh samples in the standard setting.

Kimmel and Sethian extended fast marching to triangulated domains and used it to compute geodesic distances and extract paths on triangulated manifolds. This is a numerical approximation: the answer depends on mesh quality, discretisation and update scheme. It should not be described as the same exact algorithm as MMP.

A path can be recovered by descending the computed arrival-time field from the destination toward the source. Gradient tracing requires interpolation and careful handling of flat regions, saddle points and numerical noise.

## 5. Comparison

| Method | Path domain | Character | Strength | Main limitation |
|---|---|---|---|---|
| Dijkstra on mesh edges | Mesh edges only | Exact graph optimum | Simple, reliable baseline | Can overestimate continuous surface distance |
| MMP | Triangle interiors and edges | Exact polyhedral geodesic algorithm | Continuous shortest paths and query structures | Complex windows, events and robust implementation |
| Chen–Han | Triangle interiors and edges | Exact polyhedral geodesic algorithm | Alternative exact source-based construction | Complex data structures; verify the precise variant |
| Fast marching on triangles | Triangulated domain | Numerical Eikonal solution | Distance fields and weighted travel-time models | Discretisation error and mesh sensitivity |

For a quick baseline, implement edge-graph Dijkstra and label it honestly. For exact surface distance, use a validated polyhedral-geodesic implementation or implement a published exact method with extensive geometric tests. For large distance fields, weighted propagation and approximate paths, fast marching may be more appropriate.

## 6. Mesh and coordinate requirements

- **Metric geometry:** coordinates must use a meaningful Euclidean metric. A longitude/latitude mesh in degrees is not a uniform metric surface.
- **Surface topology:** validate triangle indices, manifoldness assumptions, duplicate vertices, degenerate faces, orientation and disconnected components.
- **Nonconvex surfaces:** the surface may fold in 3D; shortest paths are constrained to the surface, not the volume.
- **Boundary conditions:** open boundaries, holes and disconnected components change reachability.
- **Intrinsic versus extrinsic distance:** intrinsic geodesic distance follows the surface. Euclidean 3D chord distance cuts through the volume and is a different quantity.
- **Mesh resolution:** a refined approximation to a smooth surface can improve a numerical model, but refinement alone does not remove all geometric or discretisation error.

## 7. Verification experiments

A useful test suite should include:

1. A single flat triangle: the geodesic is the straight segment in the face.
2. Two coplanar triangles: crossing their shared edge must preserve a straight unfolded path.
3. A folded two-triangle hinge: compare edge-graph distance with the unfolded continuous geodesic.
4. A tetrahedron: compare known symmetric cases and check vertex-event handling.
5. A cylinder-like triangulated surface: compare paths that wrap around versus cut through the ambient space.
6. A nonconvex polyhedron: ensure paths remain on the surface.
7. Disconnected components and holes: unreachable destinations must be reported explicitly.
8. Degenerate or near-degenerate triangles: reject or robustly handle invalid input.
9. Mesh refinement: measure convergence of the numerical fast-marching result against a trusted reference.
10. Weighted speed field: verify that arrival times change in the expected direction when speed is increased or decreased.

For every result, report the surface model, units, mesh statistics, algorithm, exact/approximate status, tolerances and path reconstruction method. Compare intrinsic path length against the 3D length of the returned polyline, not only its projected map length.

## 8. Practical GIS and spatial-computing applications

- Shortest paths over terrain meshes and triangulated elevation surfaces.
- Surface distance on anatomical, engineering or cultural-heritage meshes.
- Texture and parameterisation workflows that need intrinsic distances.
- Geodesic buffers and distance fields on a surface.
- Travel-time modelling where speed varies across a surface.
- Robotics and inspection on curved structures.

A terrain raster and a triangle mesh are not interchangeable. Raster cost-distance methods operate on cell neighbourhoods and their chosen movement graph; mesh geodesics operate on a piecewise-flat surface. Choose the representation that matches the physical movement model.

## Further reading

- Mitchell, J. S. B., Mount, D. M. and Papadimitriou, C. H. (1987), “The Discrete Geodesic Problem,” *SIAM Journal on Computing*, 16(4), 647–668. [DOI 10.1137/0216045](https://doi.org/10.1137/0216045). The paper develops the continuous-Dijkstra exact polyhedral-surface method and reports O(n² log n) time and O(n²) space.
- Chen, J. and Han, Y. (1990), “Shortest Paths on a Polyhedron, Part I: Computing Shortest Paths,” *Proceedings of the Sixth Annual Symposium on Computational Geometry*, DOI [10.1145/98524.98601](https://doi.org/10.1145/98524.98601). An alternative exact method for possibly nonconvex polyhedra.
- Kimmel, R. and Sethian, J. A. (1998), “Computing Geodesic Paths on Manifolds,” *Proceedings of the National Academy of Sciences*, 95(15), 8431–8435. [DOI 10.1073/pnas.95.15.8431](https://doi.org/10.1073/pnas.95.15.8431). Extends fast marching to triangulated domains.
- Sethian, J. A. (1999), “Fast Marching Methods,” *SIAM Review*, 41(2), 199–235, DOI [10.1137/S0036144598347059](https://doi.org/10.1137/S0036144598347059), for the Eikonal and upwind framework.

## Scope

This is a research-backed method guide, not an implementation. It deliberately separates exact polyhedral algorithms from graph approximations and numerical fast marching. A future implementation should begin with a clearly named baseline, validated mesh input, reference geometries and independent distance/path tests before claiming exactness.
