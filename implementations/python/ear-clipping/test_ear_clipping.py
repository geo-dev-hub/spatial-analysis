import pytest
from ear_clipping import triangulate, triangle_area, polygon_area, orient


def area_sum(triangles):
    return sum((triangle_area(t) for t in triangles), start=0)


def test_convex_quadrilateral_has_two_triangles_and_preserves_area():
    ring = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = triangulate(ring)
    assert len(result) == 2
    assert area_sum(result) == polygon_area(ring) == 12


def test_concave_polygon_is_triangulated():
    ring = [(0, 0), (5, 0), (5, 4), (3, 2), (0, 4)]
    result = triangulate(ring)
    assert len(result) == len(ring) - 2
    assert area_sum(result) == polygon_area(ring)


def test_clockwise_input_returns_ccw_triangles():
    result = triangulate([(0, 4), (5, 4), (5, 0), (0, 0)])
    assert len(result) == 2
    assert all(orient(*triangle) > 0 for triangle in result)


def test_repeated_closing_vertex_and_collinear_middle_are_normalized():
    ring = [(0, 0), (2, 0), (4, 0), (4, 4), (0, 4), (0, 0)]
    result = triangulate(ring)
    assert len(result) == 2
    assert area_sum(result) == 16


def test_decimal_coordinates_use_exact_decimal_predicates():
    ring = [(0.1, 0.1), (2.1, 0.1), (2.1, 1.1), (0.1, 1.1)]
    assert area_sum(triangulate(ring)) == polygon_area(ring)


def test_bow_tie_is_rejected():
    with pytest.raises(ValueError, match="not a simple polygon"):
        triangulate([(0, 0), (3, 3), (0, 3), (3, 0)])


def test_degenerate_ring_is_rejected():
    with pytest.raises(ValueError):
        triangulate([(0, 0), (1, 1), (2, 2)])


def test_too_few_vertices_is_rejected():
    with pytest.raises(ValueError):
        triangulate([(0, 0), (1, 0)])


def test_non_finite_coordinate_is_rejected():
    with pytest.raises(ValueError, match="finite"):
        triangulate([(0, 0), (1, 0), (float("nan"), 1)])
