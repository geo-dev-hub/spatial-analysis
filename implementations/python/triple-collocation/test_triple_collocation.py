import numpy as np
import pytest

from triple_collocation import triple_collocation


def test_recovers_noise_variances_with_large_independent_sample():
    rng = np.random.default_rng(41)
    truth = rng.normal(size=120_000)
    expected = (0.04**2, 0.07**2, 0.05**2)
    products = (
        0.2 + 1.0 * truth + rng.normal(0, 0.04, truth.size),
        -0.4 + 1.5 * truth + rng.normal(0, 0.07, truth.size),
        1.1 + 0.8 * truth + rng.normal(0, 0.05, truth.size),
    )
    result = triple_collocation(*products)
    assert result.n_observations == truth.size
    assert result.error_variances == pytest.approx(expected, abs=2e-4)


def test_uses_one_common_complete_case_sample():
    x = np.array([1., 2., 3., 4., np.nan, 6.])
    y = np.array([2., 4., 6., 8., 10., 12.])
    z = np.array([3., 5., 7., 9., 11., np.inf])
    result = triple_collocation(x, y, z)
    assert result.n_observations == 4


def test_negative_estimates_are_not_clipped():
    rng = np.random.default_rng(7)
    target_covariance = np.array([
        [1.0, 0.5, 0.5],
        [0.5, 1.0, 0.1],
        [0.5, 0.1, 1.0],
    ])
    sample = rng.multivariate_normal(np.zeros(3), target_covariance, size=20_000)
    result = triple_collocation(sample[:, 0], sample[:, 1], sample[:, 2])
    assert result.error_variances[0] < 0


def test_rejects_unequal_lengths():
    with pytest.raises(ValueError, match="same number"):
        triple_collocation(np.arange(4), np.arange(3), np.arange(4))


def test_rejects_non_vector_input():
    with pytest.raises(ValueError, match="one-dimensional"):
        triple_collocation(np.ones((2, 2)), np.ones(4), np.ones(4))


def test_rejects_too_few_complete_rows():
    with pytest.raises(ValueError, match="At least three"):
        triple_collocation([1, np.nan], [2, 3], [4, 5])


def test_rejects_zero_cross_covariance():
    x = np.array([-1., 1., -1., 1., -1., 1.])
    y = np.array([-1., -1., 1., 1., -1., -1.])
    z = np.array([1., -1., -1., 1., 1., -1.])
    with pytest.raises(ValueError, match="cross-covariance"):
        triple_collocation(x, y, z)


def test_rejects_invalid_tolerance():
    with pytest.raises(ValueError, match="finite and positive"):
        triple_collocation([1, 2, 3], [2, 4, 6], [3, 6, 9],
                           denominator_tolerance=0)
