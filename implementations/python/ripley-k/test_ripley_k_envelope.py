import numpy as np
import pytest

from ripley_k_envelope import ripley_k_csr_envelope


POINTS = [(1, 1), (2, 1), (3, 2), (5, 4), (7, 8), (8, 2)]


def test_envelope_returns_pointwise_bands_and_global_test():
    result = ripley_k_csr_envelope(
        POINTS, bounds=(0, 10, 0, 10), radii=np.linspace(0.5, 4, 8),
        n_simulations=39, seed=12,
    )
    assert result.simulated_l_values.shape == (39, 8)
    assert result.pointwise_lower_l.shape == (8,)
    assert result.pointwise_upper_l.shape == (8,)
    assert result.simulated_global_statistics.shape == (39,)
    assert 0 < result.global_p_value <= 1
    assert np.all(result.pointwise_lower_l <= result.pointwise_upper_l)


def test_simulation_is_reproducible_for_a_fixed_seed():
    kwargs = dict(bounds=(0, 10, 0, 10), radii=[0.5, 1, 2, 3],
                  n_simulations=29, seed=2026)
    a = ripley_k_csr_envelope(POINTS, **kwargs)
    b = ripley_k_csr_envelope(POINTS, **kwargs)
    np.testing.assert_allclose(a.simulated_l_values, b.simulated_l_values)
    assert a.global_p_value == b.global_p_value


def test_p_value_has_monte_carlo_resolution():
    result = ripley_k_csr_envelope(
        POINTS, bounds=(0, 10, 0, 10), radii=[1, 2, 3],
        n_simulations=19, seed=4,
    )
    assert result.global_p_value >= 1 / 20
    assert result.global_p_value <= 1


def test_invalid_simulation_count_alpha_and_bounds_are_rejected():
    with pytest.raises(ValueError, match="n_simulations"):
        ripley_k_csr_envelope(POINTS, bounds=(0, 10, 0, 10), radii=[1], n_simulations=0)
    with pytest.raises(ValueError, match="alpha"):
        ripley_k_csr_envelope(POINTS, bounds=(0, 10, 0, 10), radii=[1], alpha=1)
    with pytest.raises(ValueError, match="positive width"):
        ripley_k_csr_envelope(POINTS, bounds=(0, 0, 0, 10), radii=[1])


def test_zero_variance_radius_only_input_is_rejected():
    with pytest.raises(ValueError, match="no variable"):
        ripley_k_csr_envelope(
            [(1, 1), (2, 2)], bounds=(0, 10, 0, 10), radii=[0],
            n_simulations=9, seed=1,
        )
