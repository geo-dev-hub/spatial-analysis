import pytest
from ais_gap_detection import detect_ais_gaps, haversine_distance_nm


def test_haversine_known_one_degree_equatorial_distance():
    assert haversine_distance_nm(0, 0, 1, 0) == pytest.approx(60.04, rel=0.002)


def test_long_reporting_gap_is_flagged():
    result = detect_ais_gaps(["v1", "v1"], [0, 3600], [0, 0.1], [0, 0])
    assert len(result) == 1
    assert result[0]["flags"] == ("long_reporting_gap",)
    assert result[0]["from_index"] == 0 and result[0]["to_index"] == 1


def test_implausible_speed_is_flagged_even_for_short_interval():
    result = detect_ais_gaps(["v1", "v1"], [0, 60], [0, 1], [0, 0],
                             max_gap_seconds=1800, max_speed_knots=60)
    assert result[0]["flags"] == ("implausible_implied_speed",)


def test_both_independent_conditions_can_be_flagged():
    result = detect_ais_gaps(["v1", "v1"], [0, 7200], [0, 2], [0, 0],
                             max_gap_seconds=1800, max_speed_knots=60)
    assert result[0]["flags"] == ("long_reporting_gap", "implausible_implied_speed")


def test_vessels_are_grouped_and_each_track_sorted_stably():
    result = detect_ais_gaps(
        ["a", "b", "a", "b"], [3600, 0, 0, 3600],
        [0.1, 10, 0, 10.1], [0, 0, 0, 0], max_gap_seconds=1800
    )
    assert [item["vessel_id"] for item in result] == ["a", "b"]
    assert result[0]["from_index"] == 2 and result[0]["to_index"] == 0


def test_normal_track_returns_no_findings():
    assert detect_ais_gaps(["a", "a"], [0, 600], [0, 0.01], [0, 0]) == []


@pytest.mark.parametrize("kwargs", [
    {"max_gap_seconds": 0}, {"max_speed_knots": float("inf")},
    {"max_gap_seconds": -1}, {"max_speed_knots": 0},
])
def test_invalid_thresholds_rejected(kwargs):
    with pytest.raises(ValueError):
        detect_ais_gaps(["a", "a"], [0, 1], [0, 0], [0, 0], **kwargs)


def test_duplicate_timestamp_rejected_within_vessel():
    with pytest.raises(ValueError, match="timestamps"):
        detect_ais_gaps(["a", "a"], [1, 1], [0, 1], [0, 0])


def test_invalid_coordinates_and_lengths_rejected():
    with pytest.raises(ValueError):
        detect_ais_gaps(["a", "a"], [0, 1], [0, 181], [0, 0])
    with pytest.raises(ValueError):
        detect_ais_gaps(["a", "a"], [0, 1], [0], [0, 0])


def test_different_vessels_are_never_connected():
    assert detect_ais_gaps(["a", "b"], [0, 99999], [0, 100], [0, 0]) == []
