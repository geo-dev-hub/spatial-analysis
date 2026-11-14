import numpy as np
import pytest
from werner_deconvolution import werner_deconvolution_windows, werner_thin_dike_profile


def test_forward_model_and_window_solver_recover_known_thin_dike():
    x = np.linspace(-5, 5, 21)
    expected = {"x0": 0.7, "depth": 2.4, "amplitude_a": 10.0, "amplitude_b": -3.0}
    anomaly = werner_thin_dike_profile(x, **expected)
    result = werner_deconvolution_windows(x, anomaly, window_size=7)
    assert result["solutions"]
    solution = min(result["solutions"], key=lambda item: abs(item["x0"] - expected["x0"]))
    for key, value in expected.items():
        assert solution[key] == pytest.approx(value, rel=1e-8, abs=1e-8)
    assert solution["profile_rmse"] < 1e-10


def test_coordinate_translation_and_scaling_preserve_physical_solution():
    x = np.linspace(1000, 1100, 31)
    expected = {"x0": 1042.0, "depth": 12.0, "amplitude_a": 4.0, "amplitude_b": 2.0}
    anomaly = werner_thin_dike_profile(x, **expected)
    result = werner_deconvolution_windows(x, anomaly, window_size=9)
    solution = min(result["solutions"], key=lambda item: abs(item["x0"] - expected["x0"]))
    for key, value in expected.items():
        assert solution[key] == pytest.approx(value, rel=1e-7, abs=1e-7)


def test_rank_deficient_constant_profile_is_rejected():
    result = werner_deconvolution_windows(np.arange(8.0), np.zeros(8), window_size=7)
    assert result["solutions"] == []
    assert result["rejected_windows"]


def test_step_controls_window_starts():
    result = werner_deconvolution_windows(
        np.arange(12.0),
        werner_thin_dike_profile(np.arange(12.0), x0=5, depth=2, amplitude_a=3, amplitude_b=1),
        window_size=7,
        step=2,
    )
    assert [s["start"] for s in result["solutions"]] == [0, 2, 4]


def test_invalid_profiles_and_controls_are_rejected():
    with pytest.raises(ValueError):
        werner_deconvolution_windows([0, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        werner_deconvolution_windows([0, 1, 1, 2], [1, 2, 3, 4])
    with pytest.raises(ValueError):
        werner_deconvolution_windows(np.arange(5), np.arange(5), window_size=3)
    with pytest.raises(ValueError):
        werner_deconvolution_windows(np.arange(5), np.arange(5), step=0)
    with pytest.raises(ValueError):
        werner_thin_dike_profile([0, 1], x0=0, depth=0, amplitude_a=1, amplitude_b=1)
