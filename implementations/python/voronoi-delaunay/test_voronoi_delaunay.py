import numpy as np
import pytest
from scipy.spatial import QhullError

from voronoi_delaunay import build_tessellations


def test_three_non_collinear_sites_produce_one_delaunay_triangle():
    result = build_tessellations([(0, 0), (2, 0), (0, 2)])
    assert result.delaunay.simplices.shape == (1, 3)
    assert result.voronoi.vertices.shape == (1, 2)


def test_square_produces_two_triangles_and_one_voronoi_vertex():
    result = build_tessellations([(0, 0), (2, 0), (2, 2), (0, 2)])
    assert result.delaunay.simplices.shape == (2, 3)
    assert result.voronoi.vertices.shape == (1, 2)


def test_interior_site_is_included_in_triangulation():
    result = build_tessellations([(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)])
    used = set(result.delaunay.simplices.ravel().tolist())
    assert used == set(range(5))


def test_voronoi_vertex_is_equidistant_from_at_least_three_sites():
    points = [(0, 0), (2, 0), (0, 2)]
    result = build_tessellations(points)
    vertex = result.voronoi.vertices[0]
    distances = np.linalg.norm(result.points - vertex, axis=1)
    assert np.max(distances) - np.min(distances) < 1e-10


def test_delaunay_triangles_obey_empty_circumcircle_property():
    points = np.array([(0, 0), (4, 0), (4, 4), (0, 4), (2, 1), (1, 3)], dtype=float)
    result = build_tessellations(points)
    for simplex in result.delaunay.simplices:
        a, b, c = result.points[simplex]
        matrix = 2 * np.array([b - a, c - a])
        rhs = np.array([b @ b - a @ a, c @ c - a @ a])
        centre = np.linalg.solve(matrix, rhs)
        radius2 = np.sum((centre - a) ** 2)
        distances2 = np.sum((result.points - centre) ** 2, axis=1)
        outside = np.ones(len(points), dtype=bool)
        outside[simplex] = False
        assert np.all(distances2[outside] >= radius2 - 1e-9)


def test_duplicate_sites_are_rejected():
    with pytest.raises(ValueError, match="duplicate"):
        build_tessellations([(0, 0), (1, 0), (0, 1), (0, 0)])


def test_collinear_sites_are_rejected():
    with pytest.raises(ValueError, match="collinear"):
        build_tessellations([(0, 0), (1, 1), (2, 2), (3, 3)])


def test_too_few_sites_are_rejected():
    with pytest.raises(ValueError, match="at least three"):
        build_tessellations([(0, 0), (1, 0)])


def test_wrong_coordinate_shape_is_rejected():
    with pytest.raises(ValueError, match="n-by-2"):
        build_tessellations([(0, 0, 0), (1, 0, 0), (0, 1, 0)])


def test_non_finite_sites_are_rejected():
    with pytest.raises(ValueError, match="finite"):
        build_tessellations([(0, 0), (1, 0), (0, float("nan"))])


def test_returned_site_array_is_read_only():
    result = build_tessellations([(0, 0), (1, 0), (0, 1)])
    with pytest.raises(ValueError):
        result.points[0, 0] = 99
