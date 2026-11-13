import pytest

from simplification import douglas_peucker, visvalingam_whyatt


def test_douglas_peucker_preserves_endpoints_and_removes_near_line_points():
    line = [(0, 0), (1, 0.1), (2, -0.1), (3, 0)]
    result = douglas_peucker(line, 0.2)
    assert result == [line[0], line[-1]]


def test_douglas_peucker_retains_peak_above_tolerance():
    line = [(0, 0), (1, 2), (2, 0)]
    assert douglas_peucker(line, 1) == line


def test_douglas_peucker_uses_distance_to_finite_segment():
    line = [(0, 0), (3, 0), (1, 0)]
    assert douglas_peucker(line, 0) == [line[0], line[-1]]


def test_douglas_peucker_handles_duplicate_endpoints():
    line = [(0, 0), (1, 1), (0, 0)]
    result = douglas_peucker(line, 0)
    assert result[0] == line[0] and result[-1] == line[-1]


def test_visvalingam_preserves_endpoints_and_removes_small_area_vertex():
    line = [(0, 0), (1, 0.1), (2, 0), (3, 0)]
    result = visvalingam_whyatt(line, 0.2)
    assert result[0] == line[0] and result[-1] == line[-1]
    assert len(result) < len(line)


def test_visvalingam_threshold_zero_keeps_non_collinear_points():
    line = [(0, 0), (1, 1), (2, 0)]
    assert visvalingam_whyatt(line, 0) == line


def test_visvalingam_collinear_points_can_be_removed_at_zero():
    line = [(0, 0), (1, 0), (2, 0), (3, 0)]
    assert visvalingam_whyatt(line, 0) == [line[0], line[-1]]


@pytest.mark.parametrize("function,kwargs", [
    (douglas_peucker, {"tolerance": -1}),
    (visvalingam_whyatt, {"area_threshold": -1}),
])
def test_negative_threshold_rejected(function, kwargs):
    with pytest.raises(ValueError):
        function([(0, 0), (1, 1)], **kwargs)


def test_non_finite_coordinate_rejected():
    with pytest.raises(ValueError):
        douglas_peucker([(0, 0), (1, float("nan"))], 1)
