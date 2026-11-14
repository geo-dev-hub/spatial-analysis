# Walkthrough: user-level Laplace noise for spatial counts

Let the query return a vector of counts, one per cell. Under add/remove-one-person adjacency, changing one person's record can alter at most k distinct cell counts by one when each person is capped at k cells. Therefore the vector query has L1 sensitivity

\[\Delta_1 q = k.\]

The Laplace mechanism releases

\[\widetilde q_j=q_j+\eta_j,\qquad \eta_j\sim\operatorname{Laplace}(0,k/\epsilon).\]

This provides epsilon-DP for the stated adjacency relation and bounded contribution rule. The implementation deduplicates each person's cells and applies a deterministic cap before counting. It returns the noise scale and sensitivity so the mechanism is auditable.

The cap is part of the privacy definition, not a harmless implementation detail. A different contribution policy or adjacency relation changes sensitivity. Releasing the same data repeatedly with fresh noise consumes additional privacy budget; this function intentionally does not claim to account for composition. The mechanism also does not hide the existence of a public cell domain, nor does it solve secure identity linkage, data minimisation or governance.

## Tests

Tests cover deterministic seeded noise, sensitivity/noise scale, deduplication, contribution capping, order invariance and invalid inputs. They do not prove a privacy guarantee by empirical testing; the guarantee follows from the sensitivity argument and Laplace mechanism under the documented assumptions.
