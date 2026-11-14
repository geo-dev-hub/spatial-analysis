import numpy as np
import pytest

from point_pattern_kde import gaussian_kde


def test_single_point_density_matches_gaussian_kernel_at_grid_centre():
    density, xs, ys = gaussian_kde(
        [(0.5, 0.5)],
        bounds=(0, 1, 0, 1),
        grid_shape=(1, 1),
        bandwidth=1.0,
    )
    assert xs.tolist() == [0.5]
    assert ys.tolist() == [0.5]
    assert density[0, 0] == pytest.approx(1 / (2 * np.pi))


def test_single_point_surface_is_symmetric_around_event():
    density, _, _ = gaussian_kde(
        [(1, 1)],
        bounds=(0, 2, 0, 2),
        grid_shape=(2, 2),
        bandwidth=0.5,
    )
    assert density[0, 0] == pytest.approx(density[0, 1])
    assert density[0, 0] == pytest.approx(density[1, 0])
    assert density[0, 0] == pytest.approx(density[1, 1])


def test_weights_scale_the_intensity_linearly():
    base, _, _ = gaussian_kde(
        [(0.5, 0.5)], bounds=(0, 1, 0, 1), grid_shape=(1, 1), bandwidth=1
    )
    weighted, _, _ = gaussian_kde(
        [(0.5, 0.5)], bounds=(0, 1, 0, 1), grid_shape=(1, 1), bandwidth=1,
        weights=[3],
    )
    assert weighted[0, 0] == pytest.approx(3 * base[0, 0])


def test_chunk_size_does_not_change_results():
    points = [(1, 1), (2, 2), (3, 1)]
    a, _, _ = gaussian_kde(points, bounds=(0, 4, 0, 4), grid_shape=(8, 8), bandwidth=0.8, chunk_size=3)
    b, _, _ = gaussian_kde(points, bounds=(0, 4, 0, 4), grid_shape=(8, 8), bandwidth=0.8, chunk_size=1000)
    np.testing.assert_allclose(a, b)


def test_bounds_must_contain_events():
    with pytest.raises(ValueError, match="inside bounds"):
        gaussian_kde([(2, 2)], bounds=(0, 1, 0, 1), bandwidth=1)


@pytest.mark.parametrize("bandwidth", [0, -1, float("inf"), float("nan"), "wide"])
def test_invalid_bandwidth_is_rejected(bandwidth):
    with pytest.raises(ValueError, match="bandwidth"):
        gaussian_kde([(0.5, 0.5)], bounds=(0, 1, 0, 1), bandwidth=bandwidth)


def test_invalid_event_shape_and_nonfinite_coordinates_are_rejected():
    with pytest.raises(ValueError, match="shape"):
        gaussian_kde([1, 2], bounds=(0, 1, 0, 1), bandwidth=1)
    with pytest.raises(ValueError, match="finite"):
        gaussian_kde([(float("nan"), 0.5)], bounds=(0, 1, 0, 1), bandwidth=1)


def test_invalid_weights_and_grid_shape_are_rejected():
    with pytest.raises(ValueError, match="weights"):
        gaussian_kde([(0.5, 0.5)], bounds=(0, 1, 0, 1), bandwidth=1, weights=[1, 2])
    with pytest.raises(ValueError, match="weights"):
        gaussian_kde([(0.5, 0.5)], bounds=(0, 1, 0, 1), bandwidth=1, weights=[-1])
    with pytest.raises(ValueError, match="grid_shape"):
        gaussian_kde([(0.5, 0.5)], bounds=(0, 1, 0, 1), bandwidth=1, grid_shape=(0, 1))
