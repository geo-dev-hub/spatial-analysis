import pytest
from polygon_clipping import clip_convex_polygon, signed_area

SUBJECT = [(0, 0), (6, 0), (6, 4), (0, 4)]
WINDOW = [(2, -1), (5, -1), (5, 5), (2, 5)]


def test_overlap_has_expected_vertices_and_area():
    result = clip_convex_polygon(SUBJECT, WINDOW)
    assert result == [(2.0, 0.0), (5.0, 0.0), (5.0, 4.0), (2.0, 4.0)]
    assert signed_area(result) == pytest.approx(12.0)


def test_clockwise_inputs_are_normalized():
    result = clip_convex_polygon(SUBJECT[::-1], WINDOW[::-1])
    assert signed_area(result) == pytest.approx(12.0)


def test_containment_returns_inner_polygon():
    inner = [(1, 1), (2, 1), (2, 2), (1, 2)]
    assert signed_area(clip_convex_polygon(inner, SUBJECT)) == pytest.approx(1.0)


def test_disjoint_polygons_return_empty():
    distant = [(10, 10), (12, 10), (12, 12), (10, 12)]
    assert clip_convex_polygon(SUBJECT, distant) == []


def test_shared_edge_only_contact_returns_empty():
    adjacent = [(6, 0), (8, 0), (8, 4), (6, 4)]
    assert clip_convex_polygon(SUBJECT, adjacent) == []


def test_point_only_contact_returns_empty():
    touching = [(6, 4), (8, 4), (8, 6), (6, 6)]
    assert clip_convex_polygon(SUBJECT, touching) == []


def test_concave_input_is_rejected():
    concave = [(0, 0), (4, 0), (2, 1), (4, 4), (0, 4)]
    with pytest.raises(ValueError, match="convex"):
        clip_convex_polygon(concave, WINDOW)


def test_zero_area_input_is_rejected():
    with pytest.raises(ValueError, match="non-zero area"):
        clip_convex_polygon([(0, 0), (1, 1), (2, 2)], WINDOW)


def test_negative_epsilon_is_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        clip_convex_polygon(SUBJECT, WINDOW, epsilon=-1)
