import numpy as np
import pytest

from clark_evans import clark_evans_index


def test_two_point_pattern_matches_poisson_expected_distance_formula():
    result = clark_evans_index([(0.5, 0.5), (1.5, 0.5)], bounds=(0, 2, 0, 2))
    assert result.observed_mean_distance == pytest.approx(1)
    assert result.expected_mean_distance == pytest.approx(1 / (2 * np.sqrt(0.5)))
    assert result.ratio == pytest.approx(np.sqrt(2))
    np.testing.assert_allclose(result.nearest_neighbour_distances, [1, 1])


def test_duplicate_events_have_zero_nearest_neighbour_distance():
    result = clark_evans_index([(1, 1), (1, 1)], bounds=(0, 2, 0, 2))
    assert result.observed_mean_distance == 0
    assert result.ratio == 0


def test_chunk_size_does_not_change_nearest_neighbour_result():
    points = [(0, 0), (1, 0), (3, 0), (3, 2), (8, 8)]
    a = clark_evans_index(points, bounds=(-1, 9, -1, 9), chunk_size=1)
    b = clark_evans_index(points, bounds=(-1, 9, -1, 9), chunk_size=100)
    assert a.ratio == pytest.approx(b.ratio)
    np.testing.assert_allclose(a.nearest_neighbour_distances, b.nearest_neighbour_distances)


def test_invalid_points_and_window_are_rejected():
    with pytest.raises(ValueError, match="at least two"):
        clark_evans_index([(0, 0)], bounds=(0, 1, 0, 1))
    with pytest.raises(ValueError, match="finite"):
        clark_evans_index([(0, 0), (float("nan"), 1)], bounds=(0, 1, 0, 1))
    with pytest.raises(ValueError, match="inside bounds"):
        clark_evans_index([(0, 0), (2, 2)], bounds=(0, 1, 0, 1))
    with pytest.raises(ValueError, match="positive width"):
        clark_evans_index([(0, 0), (0, 1)], bounds=(0, 0, 0, 1))


def test_invalid_chunk_size_is_rejected():
    with pytest.raises(ValueError, match="chunk_size"):
        clark_evans_index([(0, 0), (1, 1)], bounds=(0, 2, 0, 2), chunk_size=0)
