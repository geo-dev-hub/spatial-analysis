import numpy as np
import pytest

from priority_flood import priority_flood


def test_fills_single_cell_bowl_to_lowest_boundary_spill():
    dem = np.array([[5, 5, 5], [5, 1, 5], [5, 5, 5]], dtype=float)
    filled, depth = priority_flood(dem)
    assert filled[1, 1] == 5
    assert depth[1, 1] == 4
    assert np.all(depth[[0, -1], :] == 0)


def test_preserves_dem_that_already_drains_to_boundary():
    dem = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]], dtype=float)
    filled, depth = priority_flood(dem)
    np.testing.assert_allclose(filled, dem)
    np.testing.assert_allclose(depth, 0)


def test_fills_depression_to_its_spill_level_not_global_maximum():
    dem = np.array([
        [9, 9, 9, 9, 7],
        [9, 8, 8, 8, 7],
        [9, 8, 2, 7, 7],
        [9, 8, 8, 8, 7],
        [9, 9, 9, 9, 7],
    ], dtype=float)
    filled, depth = priority_flood(dem)
    assert filled[2, 2] == 7
    assert depth[2, 2] == 5
    assert filled[2, 3] == 7


def test_nodata_cells_remain_nan_and_adjacent_valid_cells_are_seeds():
    dem = np.array([
        [5, 5, 5, 5, 5],
        [5, 1, 1, 1, 5],
        [5, 1, -9999, 1, 5],
        [5, 1, 1, 1, 5],
        [5, 5, 5, 5, 5],
    ], dtype=float)
    filled, depth = priority_flood(dem, nodata=-9999)
    assert np.isnan(filled[2, 2])
    assert np.isnan(depth[2, 2])
    # Cells adjacent to the NoData hole are treated as outlets by contract.
    assert filled[1, 2] == 1


def test_valid_mask_excludes_cells_and_checks_shape():
    dem = np.array([[5, 5, 5], [5, 1, 5], [5, 5, 5]], dtype=float)
    mask = np.ones_like(dem, dtype=bool)
    mask[1, 1] = False
    filled, depth = priority_flood(dem, valid_mask=mask)
    assert np.isnan(filled[1, 1]) and np.isnan(depth[1, 1])
    with pytest.raises(ValueError, match="valid_mask"):
        priority_flood(dem, valid_mask=np.ones((2, 2)))


def test_rejects_empty_or_all_invalid_dem():
    with pytest.raises(ValueError, match="2D"):
        priority_flood([])
    with pytest.raises(ValueError, match="at least one valid"):
        priority_flood([[np.nan]])
