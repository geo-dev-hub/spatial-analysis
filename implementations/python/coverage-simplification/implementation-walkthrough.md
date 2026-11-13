# Intern walkthrough: coverage-aware polygon simplification

## The problem

Two adjacent administrative polygons share one boundary. If each polygon is
simplified independently, the two versions of that boundary can diverge.
The map can acquire a gap or overlap even when each individual polygon remains
valid.

## Step 1 — Define a coverage

A polygon coverage is a set of polygonal faces with non-overlapping interiors
and exactly edge-matched shared boundaries. This is a stronger contract than
“a list of valid polygons”.

## Step 2 — Validate before simplifying

The wrapper calls `coverage_is_valid`. It rejects overlapping or mismatched
input rather than silently pretending that a repair has happened.

## Step 3 — Simplify shared edges consistently

GEOS coverage simplification processes the coverage so adjacent faces retain
the same simplified shared boundary. The `simplify_boundary` option controls
whether the outer boundary is simplified as well.

## Step 4 — Validate the output

The wrapper checks coverage validity again. This is a guardrail, not proof that
the result is fit for a legal boundary, a cadastral dataset or a particular map
scale.

## Step 5 — Test the contract

The tests include a deliberately wavy shared edge, overlapping invalid input,
invalid tolerances and an empty input. Extend them with holes, multipart
coverage members, narrow corridors and boundaries with many short segments.

## Step 6 — Compare with per-feature simplification

Run ordinary polygon simplification independently on the two faces. Inspect
the shared boundary. Explain why per-feature topology preservation does not
necessarily preserve topology between features.

## Further work

Investigate coverage gap detection, gap-width policies, shared-arc data models,
and cartographic generalisation methods that preserve network and semantic
constraints. Record the GEOS and Shapely versions used in any published result.
