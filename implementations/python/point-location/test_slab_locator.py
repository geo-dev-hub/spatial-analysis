import pytest

from slab_locator import BOUNDARY, SlabPointLocator


def rect(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]


def test_locates_inside_outside_and_boundary():
    locator = SlabPointLocator({"park": [rect(0, 0, 4, 4)]})
    assert locator.locate(2, 2) == "park"
    assert locator.locate(5, 2) is None
    assert locator.locate(2, 0) == BOUNDARY


def test_adjacent_faces_are_distinguished_on_either_side_of_shared_edge():
    locator = SlabPointLocator({
        "west": [rect(0, 0, 2, 2)],
        "east": [rect(2, 0, 4, 2)],
    })
    assert locator.locate(1, 1) == "west"
    assert locator.locate(3, 1) == "east"
    assert locator.locate(2, 1) == BOUNDARY


def test_hole_is_outside_face():
    shell = rect(0, 0, 6, 6)
    hole = rect(2, 2, 4, 4)
    locator = SlabPointLocator({"parcel": [shell, hole]})
    assert locator.locate(1, 1) == "parcel"
    assert locator.locate(3, 3) is None


def test_vertex_and_vertical_edge_queries_use_event_line_policy():
    locator = SlabPointLocator({"face": [rect(0, 0, 3, 3)]})
    assert locator.locate(0, 1) == BOUNDARY
    assert locator.locate(0, 0) == BOUNDARY
    assert locator.locate(0, 4) is None


def test_queries_outside_x_extent_are_outside():
    locator = SlabPointLocator({"face": [rect(0, 0, 3, 3)]})
    assert locator.locate(-1, 1) is None
    assert locator.locate(4, 1) is None


def test_invalid_open_ring_rejected():
    with pytest.raises(ValueError):
        SlabPointLocator({"bad": [[(0, 0), (1, 0), (1, 1), (0, 1)]]})


def test_non_finite_query_rejected():
    locator = SlabPointLocator({"face": [rect(0, 0, 3, 3)]})
    with pytest.raises(ValueError):
        locator.locate(float("nan"), 1)


def test_overlapping_polygons_rejected():
    with pytest.raises(ValueError):
        SlabPointLocator({
            "a": [rect(0, 0, 3, 3)],
            "b": [rect(2, 2, 4, 4)],
        })
