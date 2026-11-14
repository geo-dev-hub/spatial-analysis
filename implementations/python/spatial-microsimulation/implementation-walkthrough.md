# IPF / raking implementation walkthrough

Given seed weights w and binary control-membership matrix A, fitted margins are Aᵀw. For control j with target tⱼ and current fitted margin mⱼ, update records belonging to that control: wᵢ ← wᵢ × tⱼ / mⱼ. Repeat over controls until the largest relative margin error is within tolerance, or report non-convergence at max_iter.

IPF adjusts weights on the support of the seed microdata. If a household type is absent, raking cannot create it. If targets conflict, successive margins can pull weights in incompatible directions. Structural zeros are preserved, and positive targets with no seed support are rejected. Convergence is not evidence that the seed sample is representative, controls are accurate, or data are private.

Tests cover compatible two-way margins, structural-zero preservation, missing seed support, incompatible margins and invalid inputs. Execute pytest in the package directory before treating them as run evidence.
