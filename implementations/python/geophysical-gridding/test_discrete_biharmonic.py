import numpy as np
import pytest
from discrete_biharmonic import discrete_biharmonic_grid


def test_reproduces_affine_plane_from_fixed_perimeter():
    x, y = np.meshgrid(np.arange(6.0), np.arange(5.0))
    plane = 3.0 + 2.0 * x - 4.0 * y
    values = plane.copy()
    values[1:-1, 1:-1] = np.nan
    result = discrete_biharmonic_grid(values)
    np.testing.assert_allclose(result, plane, atol=1e-10)


def test_single_missing_node_solves_spacing_weighted_laplacian():
    values = np.array([[0.0, 2.0, 0.0],
                       [4.0, np.nan, 8.0],
                       [0.0, 6.0, 0.0]])
    result = discrete_biharmonic_grid(values, dx=2.0, dy=1.0)
    expected = ((4.0 + 8.0) / 4.0 + (2.0 + 6.0)) / (2.0 / 4.0 + 2.0)
    assert result[1, 1] == pytest.approx(expected)


def test_finite_interior_observations_are_preserved():
    values = np.full((5, 5), np.nan)
    values[0, :] = values[-1, :] = 0
    values[:, 0] = values[:, -1] = 0
    values[2, 2] = 10
    result = discrete_biharmonic_grid(values)
    assert result[2, 2] == 10
    assert np.all(np.isfinite(result))


def test_complete_grid_is_returned_without_change():
    values = np.arange(16.0).reshape(4, 4)
    np.testing.assert_array_equal(discrete_biharmonic_grid(values), values)


@pytest.mark.parametrize("values,kwargs", [
    (np.ones(5), {}),
    (np.ones((2, 3)), {}),
    (np.array([[np.nan, 1, 1], [1, 1, 1], [1, 1, 1]]), {}),
    (np.array([[1, 1, 1], [1, np.inf, 1], [1, 1, 1]]), {}),
    (np.ones((3, 3)), {"dx": 0}),
    (np.ones((3, 3)), {"dy": float("nan")}),
])
def test_invalid_grid_contract_is_rejected(values, kwargs):
    with pytest.raises(ValueError):
        discrete_biharmonic_grid(values, **kwargs)
