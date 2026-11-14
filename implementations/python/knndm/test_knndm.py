import numpy as np
import pytest
from knndm import knndm_cv

def test_returns_complete_disjoint_folds_and_diagnostics():
    rng = np.random.default_rng(4)
    train = rng.uniform(0, 100, size=(45, 2))
    pred = rng.uniform(0, 100, size=(250, 2))
    result = knndm_cv(train, pred, n_splits=5, random_state=12)
    held = np.concatenate([f["test"] for f in result["folds"]])
    assert sorted(held.tolist()) == list(range(len(train)))
    for fold in result["folds"]:
        assert len(np.intersect1d(fold["train"], fold["test"])) == 0
        assert len(fold["train"]) + len(fold["test"]) == len(train)
    assert np.isfinite(result["wasserstein_w"])
    assert len(result["cv_nearest_distances"]) == len(train)
    assert len(result["prediction_nearest_distances"]) == len(pred)

def test_clustered_design_produces_candidate_scores_when_detected():
    rng = np.random.default_rng(9)
    centers = np.array([[0, 0], [100, 0], [0, 100], [100, 100]])
    train = np.vstack([c + rng.normal(0, 2, size=(15, 2)) for c in centers])
    pred = rng.uniform(-20, 120, size=(300, 2))
    result = knndm_cv(train, pred, n_splits=4, random_state=3, candidate_count=8)
    assert result["branch"] in {"knndm_cluster_search", "random_kfold_no_clustering_detected"}
    if result["branch"] == "knndm_cluster_search":
        assert result["candidates"]
        assert result["selected_q"] is not None

@pytest.mark.parametrize("train,pred", [
    (np.ones((2, 2)), np.ones((3, 2))),
    (np.ones((3, 2)), np.ones((2, 2))),
    (np.array([[0, 0], [1, 1], [np.nan, 2]]), np.ones((3, 2))),
])
def test_rejects_invalid_points(train, pred):
    with pytest.raises(ValueError):
        knndm_cv(train, pred)

def test_rejects_invalid_parameters():
    points = np.arange(20, dtype=float).reshape(10, 2)
    with pytest.raises(ValueError):
        knndm_cv(points, points, n_splits=1)
    with pytest.raises(ValueError):
        knndm_cv(points, points, max_fold_fraction=0)
