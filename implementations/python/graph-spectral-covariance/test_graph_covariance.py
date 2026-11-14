import numpy as np
import pytest

from graph_covariance import (
    covariance_diagnostics,
    graph_heat_covariance,
    graph_laplacian,
    graph_spectral_covariance,
)


def path_adjacency():
    return np.array([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], dtype=float)


def test_path_graph_laplacian_is_correct():
    expected = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 1]], dtype=float)
    np.testing.assert_allclose(graph_laplacian(path_adjacency()), expected)


def test_laplacian_is_symmetric_positive_semidefinite():
    L = graph_laplacian(path_adjacency())
    assert np.allclose(L, L.T)
    assert np.linalg.eigvalsh(L).min() >= -1e-12


def test_nonnegative_spectral_variances_generate_psd_covariance():
    K = graph_spectral_covariance(path_adjacency(), [2, 1, 0.5, 0.1])
    result = covariance_diagnostics(K)
    assert result["symmetric"]
    assert result["positive_semidefinite_within_tolerance"]


def test_zero_spectral_variance_gives_low_rank_covariance():
    K = graph_spectral_covariance(path_adjacency(), [2, 0, 0, 0])
    assert np.linalg.matrix_rank(K, tol=1e-10) == 1


def test_heat_covariance_is_psd_and_time_changes_smoothing():
    A = path_adjacency()
    K0 = graph_heat_covariance(A, diffusion_time=0)
    K1 = graph_heat_covariance(A, diffusion_time=0.5)
    K2 = graph_heat_covariance(A, diffusion_time=2)
    np.testing.assert_allclose(K0, np.eye(4), atol=1e-12)
    assert covariance_diagnostics(K1)["positive_semidefinite_within_tolerance"]
    assert np.linalg.norm(K2 - np.diag(np.diag(K2))) > np.linalg.norm(K1 - np.diag(np.diag(K1)))


def test_isolated_vertex_is_supported():
    A = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=float)
    K = graph_heat_covariance(A, diffusion_time=1)
    assert covariance_diagnostics(K)["positive_semidefinite_within_tolerance"]


@pytest.mark.parametrize("bad", [
    [[0, 1], [0, 0]], [[0, -1], [-1, 0]], [[1, 1], [1, 0]],
    [[0, np.nan], [np.nan, 0]], [[0, 1, 0], [1, 0, 0]],
])
def test_invalid_adjacency_is_rejected(bad):
    with pytest.raises(ValueError):
        graph_laplacian(bad)


@pytest.mark.parametrize("bad", [[1], [-1, 2, 3, 4], [1, np.nan, 1, 1], [[1, 2, 3, 4]]])
def test_invalid_spectral_variances_are_rejected(bad):
    with pytest.raises(ValueError):
        graph_spectral_covariance(path_adjacency(), bad)


@pytest.mark.parametrize("time", [-1, np.nan, np.inf])
def test_invalid_diffusion_time_is_rejected(time):
    with pytest.raises(ValueError):
        graph_heat_covariance(path_adjacency(), diffusion_time=time)


def test_invalid_variance_scale_is_rejected():
    with pytest.raises(ValueError):
        graph_heat_covariance(path_adjacency(), diffusion_time=1, variance_scale=0)


def test_diagnostics_reject_invalid_matrix_and_tolerance():
    with pytest.raises(ValueError):
        covariance_diagnostics([[1, np.nan]])
    with pytest.raises(ValueError):
        covariance_diagnostics([[1]], tolerance=-1)
