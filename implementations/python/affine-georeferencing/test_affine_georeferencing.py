import numpy as np
import pytest

from affine_georeferencing import apply_affine, fit_affine


def test_recovers_known_affine_transform_from_three_controls():
    source = np.array([[0, 0], [1, 0], [0, 1]], dtype=float)
    coefficients = np.array([[5, -2], [2, -1], [3, 4]], dtype=float)
    target = apply_affine(source, coefficients)
    fit = fit_affine(source, target)
    np.testing.assert_allclose(fit.coefficients, coefficients, atol=1e-12)
    np.testing.assert_allclose(fit.residual_vectors, 0, atol=1e-12)
    assert fit.rmse == pytest.approx(0)


def test_overdetermined_fit_reports_residuals():
    source = np.array([[0, 0], [1, 0], [0, 1], [1, 1], [2, 1]], dtype=float)
    coefficients = np.array([[10, 20], [2, 0.5], [-1, 3]], dtype=float)
    target = apply_affine(source, coefficients)
    target[-1] += [0.2, -0.1]
    fit = fit_affine(source, target)
    assert fit.rank == 3
    assert fit.rmse > 0
    assert fit.residual_vectors.shape == target.shape


def test_apply_affine_accepts_multiple_points():
    coeff = np.array([[1, 2], [2, 0], [0, -3]], dtype=float)
    points = np.array([[0, 0], [1, 1]], dtype=float)
    np.testing.assert_allclose(apply_affine(points, coeff), [[1, 2], [3, -1]])


def test_collinear_control_points_are_rejected():
    source = np.array([[0, 0], [1, 1], [2, 2], [3, 3]], dtype=float)
    target = source + 1
    with pytest.raises(ValueError, match="collinear"):
        fit_affine(source, target)


@pytest.mark.parametrize("source,target", [
    ([[0, 0], [1, 0]], [[0, 0], [1, 0]]),
    ([[0, 0], [1, 0], [0, 1]], [[0, 0], [1, 0]]),
    ([[0, 0], [1, 0], [0, np.nan]], [[0, 0], [1, 0], [0, 1]]),
])
def test_invalid_control_points_are_rejected(source, target):
    with pytest.raises(ValueError):
        fit_affine(source, target)


def test_invalid_apply_inputs_are_rejected():
    with pytest.raises(ValueError):
        apply_affine([[1, 2, 3]], np.zeros((3, 2)))
    with pytest.raises(ValueError):
        apply_affine([[1, 2]], np.zeros((2, 2)))
