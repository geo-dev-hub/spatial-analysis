import numpy as np
import pytest

from ripley_k import ripley_k


def test_two_point_pattern_counts_ordered_pairs_at_inclusive_radius():
    result = ripley_k([(0.5, 0.5), (1.5, 0.5)], bounds=(0, 2, 0, 2), radii=[0.9, 1.0, 1.1])
    np.testing.assert_allclose(result.k_values, [0, 2, 2])
    np.testing.assert_allclose(result.l_values, [0, np.sqrt(2 / np.pi), np.sqrt(2 / np.pi)])


def test_k_and_l_are_monotone_for_increasing_radii():
    points = [(0, 0), (1, 0), (2, 0), (2, 2)]
    result = ripley_k(points, bounds=(-1, 3, -1, 3), radii=[0.5, 1, 2, 3])
    assert np.all(np.diff(result.k_values) >= 0)
    assert np.all(np.diff(result.l_values) >= 0)


def test_zero_radius_includes_duplicate_event_pairs():
    result = ripley_k([(1, 1), (1, 1)], bounds=(0, 2, 0, 2), radii=[0])
    assert result.k_values[0] == 2


def test_invalid_points_bounds_and_radii_are_rejected():
    with pytest.raises(ValueError, match="at least two"):
        ripley_k([(0, 0)], bounds=(0, 1, 0, 1), radii=[1])
    with pytest.raises(ValueError, match="inside bounds"):
        ripley_k([(0, 0), (2, 2)], bounds=(0, 1, 0, 1), radii=[1])
    with pytest.raises(ValueError, match="positive width"):
        ripley_k([(0, 0), (0, 1)], bounds=(0, 0, 0, 1), radii=[1])
    with pytest.raises(ValueError, match="non-empty"):
        ripley_k([(0, 0), (1, 1)], bounds=(0, 2, 0, 2), radii=[])
    with pytest.raises(ValueError, match="non-negative"):
        ripley_k([(0, 0), (1, 1)], bounds=(0, 2, 0, 2), radii=[-1])
