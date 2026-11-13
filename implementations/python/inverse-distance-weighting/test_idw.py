import math
import pytest
from idw import predict


def test_matches_hand_calculated_example():
    assert predict([(0,), (2,), (4,)], [10, 20, 40], (1,)) == pytest.approx(310 / 19)


def test_exact_observation_returns_its_value():
    assert predict([(0, 0), (2, 0)], [12, 30], (2, 0)) == 30


def test_coincident_observations_are_averaged():
    assert predict([(0, 0), (0, 0)], [10, 14], (0, 0)) == 12


def test_larger_power_increases_nearest_observation_influence():
    args = ([(0,), (2,), (5,)], [0, 10, 100], (1,))
    assert predict(*args, power=4) < predict(*args, power=1)


def test_max_neighbors_limits_contributors():
    assert predict([(0,), (2,), (4,)], [10, 20, 40], (1,), max_neighbors=2) == pytest.approx(15)


def test_radius_excludes_distant_observations():
    assert predict([(0,), (2,), (10,)], [10, 20, 100], (1,), radius=2) == pytest.approx(15)


def test_empty_radius_is_rejected():
    with pytest.raises(ValueError, match="no observations"):
        predict([(0,), (10,)], [10, 20], (5,), radius=1)


@pytest.mark.parametrize("power", [0, -1, float("nan"), float("inf")])
def test_invalid_power_is_rejected(power):
    with pytest.raises(ValueError, match="power"):
        predict([(0,)], [1], (2,), power=power)


@pytest.mark.parametrize("neighbors", [0, -1, 1.5, True])
def test_invalid_neighbor_count_is_rejected(neighbors):
    with pytest.raises(ValueError, match="max_neighbors"):
        predict([(0,)], [1], (2,), max_neighbors=neighbors)


def test_invalid_radius_is_rejected():
    with pytest.raises(ValueError, match="radius"):
        predict([(0,)], [1], (2,), radius=0)


def test_mismatched_observations_are_rejected():
    with pytest.raises(ValueError, match="same length"):
        predict([(0,), (1,)], [3], (0.5,))


def test_inconsistent_dimensions_are_rejected():
    with pytest.raises(ValueError, match="same dimension"):
        predict([(0, 1), (2,)], [3, 4], (1, 1))


def test_target_dimension_is_checked():
    with pytest.raises(ValueError, match="target dimension"):
        predict([(0, 1)], [3], (1,))


def test_non_finite_input_is_rejected():
    with pytest.raises(ValueError, match="finite"):
        predict([(0,), (math.nan,)], [3, 4], (1,))


def test_constant_values_are_preserved():
    assert predict([(0,), (2,), (4,)], [7, 7, 7], (1,)) == pytest.approx(7)


def test_prediction_is_bounded_by_contributing_values():
    estimate = predict([(0,), (2,), (4,)], [10, 20, 40], (1,))
    assert 10 <= estimate <= 40


def test_translation_of_coordinates_does_not_change_prediction():
    a = predict([(0, 0), (2, 0), (0, 2)], [10, 20, 30], (1, 1))
    b = predict([(100, 50), (102, 50), (100, 52)], [10, 20, 30], (101, 51))
    assert b == pytest.approx(a)
