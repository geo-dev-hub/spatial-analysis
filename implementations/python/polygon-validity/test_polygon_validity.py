import pytest
from shapely.geometry import MultiPolygon, Polygon

from polygon_validity import inspect_polygon, repair_polygon_explicitly


def test_valid_polygon_is_reported_without_change():
    polygon = Polygon([(0, 0), (4, 0), (4, 4), (0, 4)])
    before = polygon.wkt
    report = inspect_polygon(polygon)
    assert report.geometry_type == "Polygon"
    assert report.is_valid
    assert report.reason == "Valid Geometry"
    assert report.area == 16
    assert report.component_count == 1
    assert polygon.wkt == before


def test_bow_tie_is_flagged_as_invalid():
    polygon = Polygon([(0, 0), (4, 4), (0, 4), (4, 0), (0, 0)])
    report = inspect_polygon(polygon)
    assert not report.is_valid
    assert "Self-intersection" in report.reason
    assert report.area >= 0


def test_hole_outside_shell_is_flagged():
    polygon = Polygon(
        shell=[(0, 0), (4, 0), (4, 4), (0, 4)],
        holes=[[(6, 6), (7, 6), (7, 7), (6, 7)]],
    )
    assert not inspect_polygon(polygon).is_valid


def test_overlapping_multipolygon_components_are_flagged():
    first = Polygon([(0, 0), (3, 0), (3, 3), (0, 3)])
    second = Polygon([(2, 2), (5, 2), (5, 5), (2, 5)])
    report = inspect_polygon(MultiPolygon([first, second]))
    assert not report.is_valid
    assert report.component_count == 2


def test_explicit_repair_returns_valid_geometry_and_preserves_source():
    polygon = Polygon([(0, 0), (4, 4), (0, 4), (4, 0), (0, 0)])
    original_wkt = polygon.wkt
    repaired = repair_polygon_explicitly(polygon)
    assert polygon.wkt == original_wkt
    assert not inspect_polygon(polygon).is_valid
    assert inspect_polygon(repaired).is_valid
    assert repaired.geom_type in {"MultiPolygon", "GeometryCollection"}


def test_empty_polygon_is_reported():
    report = inspect_polygon(Polygon())
    assert report.is_valid
    assert report.area == 0
    assert report.component_count == 0


def test_rejects_non_polygon_geometry():
    from shapely.geometry import LineString

    with pytest.raises(TypeError):
        inspect_polygon(LineString([(0, 0), (1, 1)]))
    with pytest.raises(TypeError):
        repair_polygon_explicitly(LineString([(0, 0), (1, 1)]))
