import pytest
from semivariogram import experimental_semivariogram


def test_matheron_values_match_hand_calculation():
    result = experimental_semivariogram([(0,), (1,), (2,), (3,)], [1, 2, 4, 7], [0.5, 1.5, 2.5, 3.5])
    assert [row["semivariance"] for row in result] == pytest.approx([14 / 6, 8.5, 18])
    assert [row["pairs"] for row in result] == [3, 2, 1]


def test_empty_bins_are_preserved():
    result = experimental_semivariogram([(0,), (1,)], [2, 4], [0, 0.5, 1.5, 2.5])
    assert result[0]["semivariance"] is None
    assert result[1]["semivariance"] == pytest.approx(2)
    assert result[2]["semivariance"] is None


def test_last_bin_includes_its_right_edge():
    result = experimental_semivariogram([(0,), (2,)], [1, 5], [0, 1, 2])
    assert result[-1]["pairs"] == 1
    assert result[-1]["semivariance"] == pytest.approx(8)


def test_translation_of_coordinates_does_not_change_result():
    a = experimental_semivariogram([(0,), (1,), (2,)], [1, 2, 4], [0, 1.5, 2.5])
    b = experimental_semivariogram([(100,), (101,), (102,)], [1, 2, 4], [0, 1.5, 2.5])
    assert a == b


def test_values_are_shift_invariant():
    a = experimental_semivariogram([(0,), (1,), (2,)], [1, 2, 4], [0, 1.5, 2.5])
    b = experimental_semivariogram([(0,), (1,), (2,)], [11, 12, 14], [0, 1.5, 2.5])
    assert [r["semivariance"] for r in a] == pytest.approx([r["semivariance"] for r in b])


def test_value_scaling_scales_semivariance_quadratically():
    a = experimental_semivariogram([(0,), (1,), (2,)], [1, 2, 4], [0, 1.5, 2.5])
    b = experimental_semivariogram([(0,), (1,), (2,)], [2, 4, 8], [0, 1.5, 2.5])
    assert [r["semivariance"] for r in b] == pytest.approx([4 * r["semivariance"] for r in a])


def test_too_few_points_are_rejected():
    with pytest.raises(ValueError, match="at least two"):
        experimental_semivariogram([(0,)], [1], [0, 1])


def test_misaligned_values_are_rejected():
    with pytest.raises(ValueError, match="same length"):
        experimental_semivariogram([(0,), (1,)], [1], [0, 1])


def test_non_monotonic_edges_are_rejected():
    with pytest.raises(ValueError, match="strictly increasing"):
        experimental_semivariogram([(0,), (1,)], [1, 2], [0, 2, 1])


def test_negative_edges_are_rejected():
    with pytest.raises(ValueError, match="cannot be negative"):
        experimental_semivariogram([(0,), (1,)], [1, 2], [-1, 1])


def test_non_finite_values_are_rejected():
    with pytest.raises(ValueError, match="finite"):
        experimental_semivariogram([(0,), (1,)], [1, float("nan")], [0, 1])


def test_inconsistent_dimensions_are_rejected():
    with pytest.raises(ValueError, match="same dimension"):
        experimental_semivariogram([(0, 1), (2,)], [1, 2], [0, 3])
