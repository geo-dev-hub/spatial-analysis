# NNDM LOO implementation walkthrough

## Why ordinary LOO can be misleading

In clustered samples, each held-out observation may remain very close to another training observation. A prediction map may instead contain locations much farther from any sample. If prediction error changes with distance to the nearest training point, ordinary LOO can then represent easier prediction conditions than the map faces.

## Algorithm

1. Compute prediction-to-training nearest-neighbour distances and their empirical CDF.
2. Create one LOO analysis set per training observation.
3. Compute the current held-out-to-analysis nearest-neighbour distance in every fold.
4. Select the smallest current distance r and its nearest analysis point k.
5. Trial-remove k from that fold. Accept only if the modified CV ECDF at r remains greater than or equal to the prediction ECDF at r.
6. Continue in increasing current-distance order while r is within autocorrelation range phi and the minimum training fraction has not been reached.

The procedure is greedy. Each accepted removal makes one fold's held-out prediction harder by increasing its nearest distance to the retained training set. It does not remove the held-out point itself from other folds.

## Interpreting phi

The autocorrelation range limits the distances at which matching is considered necessary. If phi is zero, the method reduces to ordinary LOO. If the target prediction region is far beyond all training points, the procedure tends toward buffered LOO with radius phi, subject to the minimum-training safeguard.

## Complexity and scope

The implementation uses pairwise Euclidean distances and recomputes nearest neighbours across folds. It is intentionally transparent and suitable for small teaching datasets, not large operational data. It does not implement geographic distances, prediction-domain polygon sampling or automatic phi estimation. Check retained training sizes and the distance ECDFs before fitting models.
