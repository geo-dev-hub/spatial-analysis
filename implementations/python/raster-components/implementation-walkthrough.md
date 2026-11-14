# Intern walkthrough: connected components in a raster

## 1. Define foreground and valid cells

The input foreground mask identifies cells of interest. A separate valid mask can exclude NoData or otherwise unavailable cells. Excluded cells are barriers; background cells are not part of any component.

## 2. Choose connectivity

With 4-connectivity, only edge-sharing orthogonal neighbours connect. With 8-connectivity, diagonal neighbours also connect. A pair of diagonally touching pixels therefore forms two components under 4-connectivity and one under 8-connectivity.

This is a modelling choice. It changes component count, size and topology.

## 3. Breadth-first traversal

Scan cells in row-major order. When an unlabelled foreground cell is found, assign the next positive label and start a queue. Repeatedly remove a cell and visit its unlabelled valid foreground neighbours. Every discovered cell is labelled once.

The size counter increments as cells leave the queue. When the queue empties, that component is complete and the scan continues.

## 4. Complexity and deterministic labels

Each raster cell is inspected a constant number of times, so time is O(RC) for R rows and C columns. The label raster is O(RC); the queue can hold O(RC) cells in the largest component.

Labels are deterministic because the outer scan is row-major and neighbour offsets have a fixed order. The numeric label itself is not a meaningful class or rank; it is simply a component identifier.

## 5. Validation

Tests cover multiple components, diagonal connectivity, invalid barriers, background-only masks and input validation. The result is not a vector polygonization and does not solve cross-tile label reconciliation for distributed rasters.
