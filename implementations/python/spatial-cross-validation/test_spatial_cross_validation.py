import numpy as np
import pytest

from spatial_cross_validation import grid_block_ids, spatial_block_folds


def test_grid_blocks_group_points_in_same_cell():
    ids = grid_block_ids([[1, 1], [2, 2], [11, 1]], 10)
    assert ids[0] == ids[1]
    assert ids[0] != ids[2]


def test_rectangular_blocks_and_origin_are_applied():
    ids = grid_block_ids([[100, 200], [104, 207], [110, 200]], (10, 8), (100, 200))
    assert ids[0] == ids[1]
    assert ids[0] != ids[2]


def test_block_ids_are_invariant_to_row_permutation_as_groups():
    points = np.array([[1, 1], [11, 1], [2, 2]])
    a = grid_block_ids(points, 10)
    b = grid_block_ids(points[[2, 0, 1]], 10)
    assert a[0] == a[2]
    assert b[0] == b[1]


def test_folds_keep_whole_blocks_together_and_partition_all_points():
    points = np.array([[1, 1], [2, 2], [11, 1], [12, 2], [21, 1], [22, 2]])
    folds = spatial_block_folds(points, 3, 10, seed=7)
    all_test = np.concatenate([f.test_indices for f in folds])
    np.testing.assert_array_equal(np.sort(all_test), np.arange(len(points)))
    for fold in folds:
        assert not set(fold.train_indices).intersection(fold.test_indices)


def test_fold_assignment_is_reproducible():
    points = np.array([[x, y] for x in range(0, 60, 5) for y in (0, 5)])
    a = spatial_block_folds(points, 3, 10, seed=12)
    b = spatial_block_folds(points, 3, 10, seed=12)
    for fa, fb in zip(a, b):
        np.testing.assert_array_equal(fa.test_indices, fb.test_indices)


def test_buffer_excludes_close_training_points_but_not_test_points():
    points = np.array([[1, 1], [2, 1], [21, 1], [22, 1], [41, 1], [42, 1]])
    folds = spatial_block_folds(points, 3, 10, buffer_distance=5, seed=4)
    for fold in folds:
        assert len(fold.test_indices) > 0
        if len(fold.excluded_indices):
            delta = points[fold.excluded_indices, None, :] - points[None, fold.test_indices, :]
            nearest = np.sqrt(np.min(np.sum(delta * delta, axis=2), axis=1))
            assert np.all(nearest < 5)
        if len(fold.train_indices):
            delta = points[fold.train_indices, None, :] - points[None, fold.test_indices, :]
            nearest = np.sqrt(np.min(np.sum(delta * delta, axis=2), axis=1))
            assert np.all(nearest >= 5)


@pytest.mark.parametrize("coords", [[], [1, 2], [[1, np.nan]], [[1, 2, 3]]])
def test_invalid_coordinates_are_rejected(coords):
    with pytest.raises(ValueError):
        grid_block_ids(coords, 10)


@pytest.mark.parametrize("size", [0, -1, float("nan"), (1, 0), (1, float("inf"))])
def test_invalid_block_size_is_rejected(size):
    with pytest.raises(ValueError):
        grid_block_ids([[0, 0], [1, 1]], size)


def test_invalid_fold_contracts_are_rejected():
    points = [[1, 1], [11, 1], [21, 1]]
    with pytest.raises(ValueError):
        spatial_block_folds(points, 1, 10)
    with pytest.raises(ValueError):
        spatial_block_folds(points, 4, 10)
    with pytest.raises(ValueError):
        spatial_block_folds(points, 2, 10, buffer_distance=-1)
    with pytest.raises(ValueError):
        spatial_block_folds(points, 2, 10, seed=1.5)


def test_too_large_buffer_is_reported():
    points = [[1, 1], [11, 1], [21, 1]]
    with pytest.raises(ValueError, match="buffer removed every"):
        spatial_block_folds(points, 3, 10, buffer_distance=100)
