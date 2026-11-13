import pytest
from shapely.geometry import Polygon
from shapely import coverage_is_valid

from coverage_simplification import simplify_coverage


def adjacent_coverage():
    # The shared boundary is deliberately wavy and represented by the same
    # coordinate sequence in opposite directions by the two polygons.
    shared = [(5, 0), (5.2, 2), (4.8, 4), (5.1, 6), (5, 8)]
    left = Polygon([(0, 0), *shared, (0, 8), (0, 0)])
    right = Polygon([*reversed(shared), (10, 8), (10, 0), (5, 0)])
    return [left, right]


def test_simplification_keeps_coverage_valid():
    source = adjacent_coverage()
    result = simplify_coverage(source, 0.5)
    assert len(result) == 2
    assert coverage_is_valid(result)


def test_simplification_preserves_total_covered_area_reasonably():
    source = adjacent_coverage()
    result = simplify_coverage(source, 0.25)
    assert sum(g.area for g in result) == pytest.approx(
        sum(g.area for g in source), abs=1.0
    )


def test_overlapping_polygons_are_rejected():
    source = [Polygon([(0, 0), (3, 0), (3, 3), (0, 3)]),
              Polygon([(2, 2), (4, 2), (4, 4), (2, 4)])]
    with pytest.raises(ValueError, match="valid, edge-matched"):
        simplify_coverage(source, 0.2)


@pytest.mark.parametrize("tolerance", [-1, float("nan"), float("inf")])
def test_invalid_tolerance_is_rejected(tolerance):
    with pytest.raises(ValueError, match="tolerance"):
        simplify_coverage(adjacent_coverage(), tolerance)


def test_empty_input_returns_empty_list():
    assert simplify_coverage([], 1.0) == []
