# Building-based population disaggregation walkthrough

For each source zone z, let B(z) be its eligible residential buildings. For building b, define a supplied allocation weight

w_b = floor_area_b × occupancy_factor_b.

The allocated population is

P_b = P_z × w_b / Σ_{j∈B(z)} w_j.

This construction conserves the known source-zone total. Non-residential buildings are excluded through the residential mask. An explicit uniform fallback is available only when the caller chooses it for a positive zone with eligible buildings but zero total weight.

## Assumptions and limits

Building-to-zone assignments, floor areas and occupancy factors are inputs, not inferred facts. Floor area is only a proxy for residential capacity; it does not capture vacancy, household size, mixed use, informal occupancy or within-building vertical distribution. The output is a modelled allocation, not observed population. Validate the inputs and compare against independent building or microcensus data before operational use.
