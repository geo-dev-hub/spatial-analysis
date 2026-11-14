# DBSCAN: finding clusters by density

Stable ID: `SA-STAT-DBSCAN` · Draft 0.1 · Source compendium section 2, page 3

## The question

A point dataset may contain dense groups, sparse transitions and isolated observations. DBSCAN (Density-Based Spatial Clustering of Applications with Noise) identifies clusters as connected regions of sufficient point density and labels observations outside those regions as noise.

Unlike k-means, DBSCAN does not require the number of clusters in advance and can find non-convex clusters. Its results depend strongly on the neighbourhood radius and minimum point count.

## The two parameters

- $\varepsilon$ (`eps`) is the maximum distance for two observations to be neighbours.
- `min_samples` is the number of observations in an eps-neighbourhood required for a point to be core. The point itself counts.

A core point has at least min_samples neighbours. A border point lies within the neighbourhood of a core point but is not itself core. A noise point is not density-reachable from any core point.

## How cluster expansion works

1. Visit an unvisited point.
2. If it is not core, mark it as noise provisionally.
3. If it is core, create a cluster and add its neighbours to an expansion queue.
4. Visit queued points. A provisional noise point reached from a cluster becomes a border point in that cluster.
5. If a reached point is core, add its neighbours to the queue.
6. Continue until the density-connected region has been expanded, then start the next cluster.

The same cluster can have an irregular shape because connectivity is defined by chains of core neighbourhoods, not by distance to a centroid.

## A small density picture

~~~text
Cluster A                 Cluster B            Noise
  • • •                     • • •                •
 • • • •                   • • •
  • •                       • • •
~~~

The picture illustrates the idea only; eps and min_samples determine the actual classification.

## Distance and coordinate system

The [teaching implementation](../../implementations/python/dbscan/README.md) uses Euclidean distance between 2D coordinates. Use a suitable projected CRS and document the units. For global or regional data, choose an appropriate geodesic or projected metric rather than applying planar Euclidean distance to longitude/latitude degrees.

The implementation builds all pairwise distances, so it requires O(n²) time and memory. A spatially indexed implementation is more appropriate for larger datasets.

## Border-point ambiguity

A border point can be within eps of core points belonging to two different clusters, even though the two core components are not connected. Implementations may assign that border point according to traversal order. The teaching implementation uses input order and documents this deterministic tie policy.

## Parameter selection and interpretation

A common exploratory aid is a sorted k-distance plot, but it does not choose a universally correct eps. Examine the spatial scale, sampling design, coordinate units and domain meaning. Clusters in an unevenly sampled dataset can reflect observation effort rather than a meaningful process.

DBSCAN is not HDBSCAN or OPTICS. Those methods use different density concepts and should have separate lessons.

## Exercises

1. Draw three dense groups and a few isolated points. Predict the cluster labels before running the implementation.
2. Increase eps. When do separate clusters merge?
3. Increase min_samples. Which points cease to be core?
4. Create a border point that is reachable from two clusters. Observe the input-order tie policy.
5. Explain why a cluster can have a non-convex shape.
6. Describe how spatial sampling bias could create a misleading cluster.

## References

- Ester, M., Kriegel, H.-P., Sander, J. and Xu, X. (1996), [A density-based algorithm for discovering clusters in large spatial databases with noise](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf), Proceedings of KDD-96, 226–231.
- [scikit-learn DBSCAN documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html).

**Scope:** Euclidean DBSCAN for small planar point sets; no spatial index, variable-density model or geodesic metric is included.
