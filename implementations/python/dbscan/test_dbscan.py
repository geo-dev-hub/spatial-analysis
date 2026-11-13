import numpy as np
import pytest

from dbscan import dbscan


def test_dbscan_finds_two_clusters_and_noise():
    points = [(0, 0), (0.1, 0), (0, 0.1), (5, 5), (5.1, 5), (5, 5.1), (10, 10)]
    labels = dbscan(points, eps=0.2, min_samples=3)
    assert labels == [0, 0, 0, 1, 1, 1, -1]


def test_dbscan_min_samples_includes_the_point_itself():
    points = [(0, 0), (0.1, 0)]
    assert dbscan(points, eps=0.2, min_samples=2) == [0, 0]
    assert dbscan(points, eps=0.2, min_samples=3) == [-1, -1]


def test_dbscan_connects_density_reachable_points():
    points = [(0, 0), (0.1, 0), (0.2, 0), (0.3, 0), (0.4, 0)]
    labels = dbscan(points, eps=0.11, min_samples=2)
    assert labels == [0, 0, 0, 0, 0]


def test_dbscan_returns_noise_when_no_core_points_exist():
    assert dbscan([(0, 0), (2, 2), (4, 4)], eps=0.1, min_samples=2) == [-1, -1, -1]


def test_dbscan_is_deterministic_for_fixed_input_order():
    points = [(0, 0), (0.1, 0), (5, 5), (5.1, 5)]
    assert dbscan(points, eps=0.2, min_samples=2) == dbscan(points, eps=0.2, min_samples=2)


@pytest.mark.parametrize("eps", [0, -1, float("nan"), float("inf")])
def test_dbscan_rejects_invalid_eps(eps):
    with pytest.raises(ValueError, match="eps"):
        dbscan([(0, 0)], eps=eps, min_samples=1)


@pytest.mark.parametrize("min_samples", [0, -1, 1.5, True])
def test_dbscan_rejects_invalid_min_samples(min_samples):
    with pytest.raises(ValueError, match="min_samples"):
        dbscan([(0, 0)], eps=1, min_samples=min_samples)


def test_dbscan_rejects_invalid_coordinates():
    with pytest.raises(ValueError, match="2D"):
        dbscan([1, 2, 3], eps=1, min_samples=1)
    with pytest.raises(ValueError, match="finite"):
        dbscan([[0, 0], [np.nan, 1]], eps=1, min_samples=1)
