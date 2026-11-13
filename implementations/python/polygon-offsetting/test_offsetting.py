import pytest
from shapely.geometry import Polygon

from offsetting import offset_polygon


SQUARE = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])


def test_positive_offset_increases_area():
    result = offset_polygon(SQUARE, 1)
    assert result.is_valid
    assert result.area > SQUARE.area


def test_negative_offset_decreases_area():
    result = offset_polygon(SQUARE, -1)
    assert result.is_valid
    assert result.area < SQUARE.area


def test_large_negative_offset_can_collapse_to_empty():
    result = offset_polygon(SQUARE, -6)
    assert result.is_empty


def test_join_styles_return_valid_geometry():
    for style in ("round", "mitre", "bevel"):
        assert offset_polygon(SQUARE, 1, join_style=style).is_valid


def test_invalid_polygon_rejected():
    bowtie = Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)])
    with pytest.raises(ValueError):
        offset_polygon(bowtie, 1)


def test_non_polygon_rejected():
    from shapely.geometry import LineString
    with pytest.raises(TypeError):
        offset_polygon(LineString([(0, 0), (1, 1)]), 1)


def test_invalid_parameters_rejected():
    with pytest.raises(ValueError):
        offset_polygon(SQUARE, float("nan"))
    with pytest.raises(ValueError):
        offset_polygon(SQUARE, 1, join_style="square")
    with pytest.raises(ValueError):
        offset_polygon(SQUARE, 1, quad_segs=0)
