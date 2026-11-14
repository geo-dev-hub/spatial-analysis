"""Teaching implementation of k-fold nearest-neighbour distance matching CV."""
from __future__ import annotations
import numpy as np
from scipy.spatial.distance import cdist
from scipy.stats import ks_2samp, wasserstein_distance
from sklearn.cluster import KMeans
from sklearn.model_selection import KFold

def _points(values, name):
    a = np.asarray(values, dtype=float)
    if a.ndim != 2 or a.shape[0] < 3 or a.shape[1] < 1 or not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be a finite 2D array with at least three rows")
    return a

def _nnd(query, reference):
    return cdist(query, reference).min(axis=1)

def _q_values(n, k, count):
    if count < 2:
        raise ValueError("candidate_count must be at least 2")
    return sorted(set(np.clip(np.rint(np.geomspace(k, n, count)).astype(int), k, n)))

def _merge(labels, centers, k, n):
    _, inverse = np.unique(labels, return_inverse=True)
    sizes = np.bincount(inverse)
    centered = centers - centers.mean(axis=0)
    if centers.shape[1] == 1:
        axis = np.array([1.0])
    else:
        _, _, vh = np.linalg.svd(centered, full_matrices=False)
        axis = vh[0]
    order = np.argsort(centers @ axis, kind="stable")
    large = [c for c in order if sizes[c] > n / k]
    if len(large) > k:
        return None
    fold_sizes = np.zeros(k, dtype=int)
    cluster_fold = np.full(len(sizes), -1, dtype=int)
    for fold, cluster in enumerate(large):
        cluster_fold[cluster] = fold
        fold_sizes[fold] += sizes[cluster]
    rotation = 0
    for cluster in [c for c in order if cluster_fold[c] < 0]:
        tied = np.flatnonzero(fold_sizes == fold_sizes.min())
        fold = int(tied[rotation % len(tied)])
        rotation += 1
        cluster_fold[cluster] = fold
        fold_sizes[fold] += sizes[cluster]
    return cluster_fold[inverse]

def knndm_cv(training_points, prediction_points, *, n_splits=5,
             candidate_count=100, max_fold_fraction=1.0, alpha=0.05,
             random_state=0, n_init=10):
    """Return kNNDM folds and diagnostics for projected Euclidean coordinates.

    This is a bounded KMeans implementation of the 2024 kNNDM method. It is
    not the original NNDM leave-one-out algorithm. Coordinates must share a
    suitable projected CRS and units. Prediction points should represent the
    actual model domain. Returned fold indices are zero-based.
    """
    train = _points(training_points, "training_points")
    pred = _points(prediction_points, "prediction_points")
    n = len(train)
    if not isinstance(n_splits, (int, np.integer)) or not 2 <= n_splits <= n:
        raise ValueError("n_splits must be between 2 and the number of training points")
    if not 0 < float(max_fold_fraction) <= 1 or not 0 < float(alpha) < 1:
        raise ValueError("max_fold_fraction must be in (0,1] and alpha in (0,1)")
    pairwise = cdist(train, train)
    np.fill_diagonal(pairwise, np.inf)
    training_nnd = pairwise.min(axis=1)
    prediction_nnd = _nnd(pred, train)
    ks = ks_2samp(training_nnd, prediction_nnd, alternative="greater", method="auto")
    candidates, selected_q = [], None
    if ks.pvalue >= alpha:
        labels = np.empty(n, dtype=int)
        for fold, (_, test) in enumerate(KFold(n_splits=n_splits, shuffle=True,
                                               random_state=random_state).split(train)):
            labels[test] = fold
        branch = "random_kfold_no_clustering_detected"
    else:
        branch = "knndm_cluster_search"
        labels = None
        for q in _q_values(n, n_splits, candidate_count):
            model = KMeans(n_clusters=q, random_state=random_state, n_init=n_init)
            cluster_labels = model.fit_predict(train)
            merged = _merge(cluster_labels, model.cluster_centers_, n_splits, n)
            if merged is None:
                continue
            sizes = np.bincount(merged, minlength=n_splits)
            if sizes.max() / n > max_fold_fraction:
                continue
            cv_nnd = np.empty(n, dtype=float)
            feasible = True
            for fold in range(n_splits):
                test = np.flatnonzero(merged == fold)
                fit = np.flatnonzero(merged != fold)
                if not len(test) or not len(fit):
                    feasible = False
                    break
                cv_nnd[test] = _nnd(train[test], train[fit])
            if not feasible:
                continue
            score = float(wasserstein_distance(cv_nnd, prediction_nnd))
            candidates.append({"q": int(q), "wasserstein_w": score,
                               "fold_sizes": sizes.tolist()})
            if labels is None or score < min(c["wasserstein_w"] for c in candidates[:-1]):
                labels, selected_q = merged, int(q)
        if labels is None:
            raise ValueError("no feasible candidate; relax max_fold_fraction or reduce n_splits")
    folds, cv_nnd = [], np.empty(n, dtype=float)
    for fold in range(n_splits):
        test = np.flatnonzero(labels == fold)
        fit = np.flatnonzero(labels != fold)
        if not len(test) or not len(fit):
            raise ValueError("empty train or test fold")
        cv_nnd[test] = _nnd(train[test], train[fit])
        folds.append({"fold": fold, "train": fit, "test": test})
    return {"folds": folds, "branch": branch, "selected_q": selected_q,
            "wasserstein_w": float(wasserstein_distance(cv_nnd, prediction_nnd)),
            "ks_statistic": float(ks.statistic), "ks_pvalue": float(ks.pvalue),
            "training_nearest_distances": training_nnd,
            "cv_nearest_distances": cv_nnd,
            "prediction_nearest_distances": prediction_nnd,
            "candidates": candidates}
