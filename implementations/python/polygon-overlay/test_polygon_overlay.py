import pytest
from shapely.geometry import LineString, MultiPolygon, Polygon
from polygon_overlay import describe_result, overlay

A = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
B = Polygon([(2, -1), (5, -1), (5, 2), (2, 2)])


@pytest.mark.parametrize(("operation", "expected"), [
    ("intersection", 4.0), ("union", 17.0),
    ("difference", 8.0), ("symmetric_difference", 13.0),
])
def test_rectangle_overlay_areas(operation, expected):
    result = overlay(A, B, operation)
    assert result.is_valid
    assert result.area == pytest.approx(expected)


def test_union_intersection_area_identity():
    assert overlay(A, B, "union").area + overlay(A, B, "intersection").area == pytest.approx(A.area + B.area)


def test_difference_intersection_area_identity():
    assert overlay(A, B, "difference").area + overlay(A, B, "intersection").area == pytest.approx(A.area)


def test_disjoint_union_is_multipart():
    distant = Polygon([(10, 10), (12, 10), (12, 12), (10, 12)])
    result = overlay(A, distant, "union")
    assert isinstance(result, MultiPolygon) and len(result.geoms) == 2


def test_disjoint_intersection_is_empty():
    distant = Polygon([(10, 10), (12, 10), (12, 12), (10, 12)])
    assert overlay(A, distant, "intersection").is_empty


def test_containment_difference_creates_hole():
    inner = Polygon([(1, 1), (3, 1), (3, 2), (1, 2)])
    result = overlay(A, inner, "difference")
    assert len(result.interiors) == 1
    assert result.area == pytest.approx(10.0)


def test_edge_touch_intersection_is_line():
    adjacent = Polygon([(4, 0), (6, 0), (6, 3), (4, 3)])
    result = overlay(A, adjacent, "intersection")
    assert isinstance(result, LineString)
    assert result.length == pytest.approx(3.0) and result.area == 0


def test_point_touch_intersection_is_point():
    touching = Polygon([(4, 3), (6, 3), (6, 5), (4, 5)])
    result = overlay(A, touching, "intersection")
    assert result.geom_type == "Point" and result.area == 0


def test_polygon_hole_is_preserved():
    donut = Polygon([(0, 0), (6, 0), (6, 6), (0, 6)],
                    holes=[[(2, 2), (4, 2), (4, 4), (2, 4)]])
    clip = Polygon([(1, 1), (5, 1), (5, 5), (1, 5)])
    result = overlay(donut, clip, "intersection")
    assert result.area == pytest.approx(12.0) and result.is_valid


def test_multipolygon_input_is_supported():
    parts = MultiPolygon([
        Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
        Polygon([(3, 0), (4, 0), (4, 1), (3, 1)]),
    ])
    clip = Polygon([(-1, -1), (5, -1), (5, 2), (-1, 2)])
    assert overlay(parts, clip, "intersection").area == pytest.approx(2.0)


def test_invalid_polygon_is_rejected():
    bow_tie = Polygon([(0, 0), (2, 2), (0, 2), (2, 0)])
    with pytest.raises(ValueError, match="invalid"):
        overlay(bow_tie, A, "intersection")


def test_non_polygonal_input_is_rejected():
    with pytest.raises(TypeError, match="Polygon or MultiPolygon"):
        overlay(A.boundary, B, "intersection")


def test_unknown_operation_is_rejected():
    with pytest.raises(ValueError, match="operation must be"):
        overlay(A, B, "xor")


@pytest.mark.parametrize("grid", [-1, float("nan"), float("inf")])
def test_invalid_precision_grid_is_rejected(grid):
    with pytest.raises(ValueError, match="finite non-negative"):
        overlay(A, B, "intersection", grid_size=grid)


def test_fixed_precision_grid_is_applied():
    result = overlay(A, B, "intersection", grid_size=0.5)
    assert result.is_valid and result.area == pytest.approx(4.0)


def test_result_description_reports_actual_dimension():
    line = overlay(A, Polygon([(4, 0), (6, 0), (6, 3), (4, 3)]), "intersection")
    report = describe_result(line)
    assert report["geometry_type"] == "LineString"
    assert report["area"] == 0.0 and report["is_valid"] is True
