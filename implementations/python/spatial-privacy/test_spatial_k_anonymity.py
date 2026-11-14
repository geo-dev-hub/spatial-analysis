import numpy as np
import pytest
from spatial_k_anonymity import spatial_k_anonymity


def test_every_published_location_group_has_at_least_k_records():
    x = np.array([0.1, 0.12, 0.14, 0.8, 0.82, 0.84, 0.86, 0.88])
    y = np.array([0.1, 0.12, 0.14, 0.8, 0.82, 0.84, 0.86, 0.88])
    result = spatial_k_anonymity(x, y, 3, max_depth=6)
    assert not np.any(result["suppressed"])
    assert all(group["count"] >= 3 for group in result["groups"])
    assert sum(group["count"] for group in result["groups"]) == len(x)


def test_small_population_is_suppressed():
    result = spatial_k_anonymity([0, 1], [0, 1], 3)
    assert np.all(result["suppressed"])
    assert result["groups"] == []


def test_parent_cell_is_used_when_a_child_would_be_smaller_than_k():
    x = np.array([0.1, 0.11, 0.12, 0.9])
    y = np.array([0.1, 0.11, 0.12, 0.9])
    result = spatial_k_anonymity(x, y, 2, max_depth=8)
    assert len(result["groups"]) == 1
    assert result["groups"][0]["count"] == 4
    assert result["groups"][0]["depth"] == 0


def test_assignments_partition_records_without_overlap():
    x = np.array([0, .01, .02, .8, .81, .82, .83, .84, .85])
    y = np.array([0, .01, .02, .8, .81, .82, .83, .84, .85])
    result = spatial_k_anonymity(x, y, 3)
    ids = result["group_ids"]
    assert np.all(ids >= 0)
    for group in result["groups"]:
        assert np.count_nonzero(ids == group["group_id"]) == group["count"]


def test_max_depth_zero_returns_root_group_when_population_is_large_enough():
    result = spatial_k_anonymity([0, 1, 2], [0, 1, 2], 2, max_depth=0)
    assert len(result["groups"]) == 1
    assert result["groups"][0]["depth"] == 0


@pytest.mark.parametrize("k,depth", [(0, 2), (-1, 2), (1.5, 2), (2, -1), (2, 1.5)])
def test_invalid_parameters_are_rejected(k, depth):
    with pytest.raises(ValueError):
        spatial_k_anonymity([0, 1], [0, 1], k, max_depth=depth)


def test_invalid_coordinate_contract_is_rejected():
    with pytest.raises(ValueError):
        spatial_k_anonymity([0, 1], [0], 1)
    with pytest.raises(ValueError):
        spatial_k_anonymity([0, float("nan")], [0, 1], 1)
