import math

import pytest

from interpolation import (
    exponential_semivariogram,
    idw_predict,
    ordinary_kriging_predict,
)


SAMPLES = [(0, 0, 10), (10, 0, 20), (0, 10, 30), (10, 10, 40)]


def test_idw_exact_sample_returns_observed_value():
    assert idw_predict(SAMPLES, [(0, 0)]) == [10.0]


def test_idw_equal_distance_uses_arithmetic_mean():
    assert idw_predict([(0, 0, 2), (2, 0, 6)], [(1, 0)]) == [4.0]


def test_idw_power_changes_relative_influence():
    samples = [(0, 0, 0), (10, 0, 10)]
    low = idw_predict(samples, [(2, 0)], power=1)[0]
    high = idw_predict(samples, [(2, 0)], power=3)[0]
    assert high < low


def test_idw_radius_and_max_neighbours_are_applied():
    samples = [(0, 0, 1), (1, 0, 3), (10, 0, 100)]
    assert idw_predict(samples, [(0, 0.1)], radius=2, max_neighbors=1) == [1.0]
    assert idw_predict(samples, [(20, 0)], radius=2) == [None]


def test_idw_rejects_invalid_parameters():
    with pytest.raises(ValueError, match="power"):
        idw_predict(SAMPLES, [(1, 1)], power=0)
    with pytest.raises(ValueError, match="radius"):
        idw_predict(SAMPLES, [(1, 1)], radius=0)
    with pytest.raises(ValueError, match="max_neighbors"):
        idw_predict(SAMPLES, [(1, 1)], max_neighbors=0)


def test_idw_rejects_duplicate_coordinates_and_non_finite_values():
    with pytest.raises(ValueError, match="unique"):
        idw_predict([(0, 0, 1), (0, 0, 2)], [(1, 1)])
    with pytest.raises(ValueError, match="finite"):
        idw_predict([(0, 0, math.nan)], [(1, 1)])


def test_semivariogram_has_zero_at_origin_and_increases():
    assert exponential_semivariogram(0, partial_sill=5, range_scale=10) == 0
    assert 0 < exponential_semivariogram(5, partial_sill=5, range_scale=10) < 5


def test_ordinary_kriging_weights_are_unbiased_and_variance_nonnegative():
    result = ordinary_kriging_predict(
        SAMPLES, [(5, 5)], partial_sill=100, range_scale=8
    )[0]
    estimate, variance = result
    assert estimate == pytest.approx(25)
    assert variance >= 0


def test_ordinary_kriging_reproduces_a_sample_location():
    estimate, variance = ordinary_kriging_predict(
        SAMPLES, [(0, 0)], partial_sill=100, range_scale=8
    )[0]
    assert estimate == pytest.approx(10)
    assert variance == pytest.approx(0, abs=1e-9)


def test_ordinary_kriging_rejects_singular_duplicate_samples():
    with pytest.raises(ValueError, match="unique"):
        ordinary_kriging_predict(
            [(0, 0, 1), (0, 0, 2)], [(1, 1)], partial_sill=1, range_scale=1
        )


def test_ordinary_kriging_rejects_bad_model_and_too_few_samples():
    with pytest.raises(ValueError, match="partial_sill"):
        ordinary_kriging_predict(SAMPLES, [(1, 1)], partial_sill=0, range_scale=1)
    with pytest.raises(ValueError, match="at least two"):
        ordinary_kriging_predict([(0, 0, 1)], [(1, 1)], partial_sill=1, range_scale=1)


def test_ordinary_kriging_handles_distinct_collinear_samples():
    samples = [(0, 0, 1), (1, 0, 2), (2, 0, 3), (3, 0, 4)]
    # The exponential model should remain solvable for distinct collinear points.
    result = ordinary_kriging_predict(samples, [(1.5, 1)], partial_sill=1, range_scale=2)
    assert math.isfinite(result[0][0])
    assert result[0][1] >= 0
