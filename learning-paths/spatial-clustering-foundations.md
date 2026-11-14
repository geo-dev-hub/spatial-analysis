# Spatial clustering: finding groups without drawing boundaries first

**Status:** First density-clustering lesson published; the wider clustering and point-pattern path is still being developed.

## The question

A set of observations may contain dense groups, isolated points and irregularly shaped clusters. How can we identify groups without deciding the number of clusters in advance?

## Before you begin

It helps to understand:
- points and Euclidean distance;
- a neighbourhood radius;
- the difference between a dense region and an isolated observation;
- why sampling density can affect the result.

## Follow the path

### 1. Understand core, border and noise points

Read [DBSCAN](../algorithms/statistics/dbscan.md). The method uses eps and min_samples to define density-connected clusters.

### 2. Run the clustering lab

Open the [DBSCAN notebook](../notebooks/dbscan-clustering-lab.ipynb). Change eps and min_samples and inspect how cluster membership and noise labels change.

### 3. Think about scale and sampling

eps uses the coordinate units of the data. A cluster can reflect the observation process rather than a real-world phenomenon. Check the sampling design, coordinate system and density variation before interpreting a result.

### 4. Compare other density methods

HDBSCAN and OPTICS address different density structures. Do not treat them as interchangeable parameterisations of DBSCAN.

## Exercises

1. Make two clusters merge by increasing eps.
2. Raise min_samples until a small cluster becomes noise.
3. Create a border point that is reachable from two clusters and explain the tie policy.
4. Compare DBSCAN with k-means on a non-convex point pattern.
5. Explain how an uneven sampling design could create a misleading cluster.

## What comes next

The wider source section includes point-pattern summary functions, Poisson and Cox processes, Ripley's K, spatial scan statistics, kernel density estimation, hierarchical and density clustering, regionalisation, spatial regression and econometrics. Each requires a separate model and inference discussion.
