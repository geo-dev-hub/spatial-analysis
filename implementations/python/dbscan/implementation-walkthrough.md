# Intern walkthrough: DBSCAN

## 1. Define density, not a fixed number of clusters

DBSCAN does not ask for k clusters. It uses a neighbourhood radius eps and a minimum point count min_samples. A point is a core point when at least min_samples observations—including itself—fall within eps.

A point may be a border point if it lies within the neighbourhood of a core point but does not have enough neighbours to be core itself. Points that are not density-reachable from any core point are noise.

## 2. Build neighbourhoods

The teaching implementation computes the pairwise Euclidean distance matrix and records every point within eps of each point. This makes the neighbourhood definition explicit, but uses O(n²) time and memory.

## 3. Expand a cluster

Visit points in input order. If an unvisited point is not core, mark it as noise for now. If it is core, start a new cluster and expand through its neighbours. When a newly reached point is itself core, add its neighbours to the expansion queue.

A point first marked as noise may later be reached from a core point and become a border member. The implementation handles this case.

## 4. Understand deterministic ambiguity

A border point can be reachable from two different clusters without connecting their core components. Standard DBSCAN implementations may assign it according to traversal order. This implementation resolves the ambiguity by expanding clusters in input order. That policy is documented and tested for reproducibility.

## 5. Choose parameters as part of the analysis

eps uses coordinate units. A geographic longitude/latitude coordinate system does not provide a uniform Euclidean distance. The choice of eps and min_samples changes what counts as dense, so justify them using the data, scale and analytical question.

## 6. Know what this implementation is not

The pairwise distance matrix is intended for small examples. Large datasets need a spatial index or a library implementation. HDBSCAN and OPTICS address different density structures and are not implemented here.
