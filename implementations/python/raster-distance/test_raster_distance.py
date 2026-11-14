import numpy as np
import pytest

from raster_distance import distance_to_targets


def test_distance_is_zero_at_targets_and_increases_by_cell_spacing():
    targets = np.zeros((5, 5), dtype=bool)
    targets[2, 2] = True
    result = distance_to_targets(targets, cell_size=(10, 20))
    assert result[2, 2] == 0
    assert result[2, 3] == pytest.approx(20)
    assert result[3, 2] == pytest.approx(10)
    assert result[3, 3] == pytest.approx(np.hypot(10, 20))


def test_multiple_targets_use_nearest_euclidean_distance():
    targets = np.zeros((4, 5), dtype=bool)
    targets[0, 0] = True
    targets[3, 4] = True
    result = distance_to_targets(targets)
    assert result[0, 4] == pytest.approx(3)
    assert result[3, 0] == pytest.approx(3)


def test_rectangular_cells_use_anisotropic_sampling():
    targets = np.zeros((3, 3), dtype=bool)
    targets[0, 0] = True
    result = distance_to_targets(targets, cell_size=(2, 5))
    assert result[1, 0] == pytest.approx(2)
    assert result[0, 1] == pytest.approx(5)
    assert result[1, 1] == pytest.approx(np.hypot(2, 5))


@pytest.mark.parametrize("mask", [np.array([]), np.ones((2, 2, 2)), np.zeros((2, 2), dtype=bool)])
def test_invalid_or_target_free_masks_rejected(mask):
    with pytest.raises(ValueError):
        distance_to_targets(mask)


@pytest.mark.parametrize("spacing", [(0, 1), (1, -1), (float("inf"), 1), (1,), (float("nan"), 1)])
def test_invalid_cell_spacing_rejected(spacing):
    targets = np.zeros((2, 2), dtype=bool)
    targets[0, 0] = True
    with pytest.raises(ValueError):
        distance_to_targets(targets, cell_size=spacing)
