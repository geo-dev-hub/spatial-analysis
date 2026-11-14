import numpy as np
import pytest
from gaussian_plume_inversion import gaussian_column_kernel, invert_gaussian_plume


def grid():
    return np.meshgrid(np.linspace(-500, 2500, 61), np.linspace(-900, 900, 37))


def test_kernel_is_zero_upwind_and_positive_downwind():
    x, y = grid()
    kernel = gaussian_column_kernel(x, y, 0, 0, 5, 30, 0.08)
    assert np.all(kernel[x <= 0] == 0)
    assert np.all(kernel[x > 0] > 0)


def test_inversion_recovers_emission_and_background_without_noise():
    x, y = grid()
    kernel = gaussian_column_kernel(x, y, 0, 0, 6, 25, 0.06)
    observed = 125 * kernel + 0.002
    result = invert_gaussian_plume(observed, x, y, source_x=0, source_y=0,
                                   wind_speed_m_s=6, sigma_y0_m=25, dispersion_growth=0.06)
    assert result["emission_rate_kg_s"] == pytest.approx(125, rel=1e-7)
    assert result["background_kg_m2"] == pytest.approx(0.002, rel=1e-7)
    assert result["rms_residual_kg_m2"] < 1e-10


def test_nonnegative_emission_when_no_plume_is_present():
    x, y = grid()
    result = invert_gaussian_plume(np.full(x.shape, 0.003), x, y, source_x=0, source_y=0,
                                   wind_speed_m_s=5, sigma_y0_m=20, dispersion_growth=0.05)
    assert result["emission_rate_kg_s"] >= 0
    assert result["emission_rate_kg_s"] == pytest.approx(0, abs=1e-8)
    assert result["background_kg_m2"] == pytest.approx(0.003)


def test_inversion_handles_small_measurement_noise():
    x, y = grid()
    rng = np.random.default_rng(19)
    kernel = gaussian_column_kernel(x, y, 0, 0, 5, 35, 0.07)
    observed = 80 * kernel + 0.001 + rng.normal(0, 1e-6, x.shape)
    result = invert_gaussian_plume(observed, x, y, source_x=0, source_y=0,
                                   wind_speed_m_s=5, sigma_y0_m=35, dispersion_growth=0.07)
    assert result["emission_rate_kg_s"] == pytest.approx(80, rel=0.03)
    assert result["background_kg_m2"] == pytest.approx(0.001, abs=2e-6)


@pytest.mark.parametrize("wind,sigma,growth", [(0, 20, .1), (5, 0, .1), (5, 20, -.1)])
def test_kernel_rejects_invalid_physics(wind, sigma, growth):
    x, y = grid()
    with pytest.raises(ValueError):
        gaussian_column_kernel(x, y, 0, 0, wind, sigma, growth)


def test_inversion_rejects_shape_mismatch_and_nonfinite_values():
    x, y = grid()
    with pytest.raises(ValueError):
        invert_gaussian_plume(np.ones((2, 2)), x, y, source_x=0, source_y=0,
                              wind_speed_m_s=5, sigma_y0_m=20, dispersion_growth=.1)
    bad = np.ones_like(x)
    bad[0, 0] = np.nan
    with pytest.raises(ValueError):
        invert_gaussian_plume(bad, x, y, source_x=0, source_y=0,
                              wind_speed_m_s=5, sigma_y0_m=20, dispersion_growth=.1)
