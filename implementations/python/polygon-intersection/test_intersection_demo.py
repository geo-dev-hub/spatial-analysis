import shapely
import pytest
from shapely import Polygon, box

from intersection_demo import polygon_intersection


def test_partial_overlap_has_expected_rectangle_and_area():
    result = polygon_intersection(box(0, 0, 4, 4), box(2, 1, 5, 3))
    expected = box(2, 1, 4, 3)
    assert result.equals(expected)
    assert result.area == pytest.approx(4.0)
    assert result.geom_type == "Polygon"


def test_disjoint_polygons_return_empty_geometry():
    result = polygon_intersection(box(0, 0, 1, 1), box(2, 2, 3, 3))
    assert result.is_empty


def test_containment_returns_inner_polygon():
    outer, inner = box(0, 0, 5, 5), box(1, 1, 2, 2)
    assert polygon_intersection(outer, inner).equals(inner)


def test_shared_edge_returns_line():
    left, right = box(0, 0, 1, 1), box(1, 0, 2, 1)
    result = polygon_intersection(left, right)
    assert result.geom_type == "LineString"
    assert result.length == pytest.approx(1.0)


def test_shared_vertex_returns_point():
    lower_left, upper_right = box(0, 0, 1, 1), box(1, 1, 2, 2)
    result = polygon_intersection(lower_left, upper_right)
    assert result.geom_type == "Point"
    assert tuple(result.coords[0]) == (1.0, 1.0)


def test_hole_is_respected():
    donut = Polygon(
        shell=[(0, 0), (5, 0), (5, 5), (0, 5), (0, 0)],
        holes=[[(1, 1), (4, 1), (4, 4), (1, 4), (1, 1)]],
    )
    result = polygon_intersection(donut, box(0, 0, 5, 5))
    assert result.equals(donut)
    assert result.area == pytest.approx(16.0)


def test_intersection_is_commutative():
    a, b = box(0, 0, 4, 4), box(2, 1, 5, 3)
    assert polygon_intersection(a, b).equals(polygon_intersection(b, a))


def test_invalid_geometry_is_rejected_explicitly():
    bow_tie = Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)])
    assert not shapely.is_valid(bow_tie)
    with pytest.raises(ValueError, match="must be valid"):
        polygon_intersection(bow_tie, box(0, 0, 2, 2))


def test_none_is_rejected_explicitly():
    with pytest.raises(TypeError, match="not None"):
        polygon_intersection(None, box(0, 0, 1, 1))
