import numpy as np
import pytest
from marine_heatwave_detection import detect_events


def call(temp, *, threshold=10, climatology=8, **kwargs):
    temp = np.asarray(temp, dtype=float)
    return detect_events(temp, np.full(temp.size, threshold),
                         np.full(temp.size, climatology), **kwargs)


def test_detects_five_day_event_and_metrics():
    event, = call([8, 11, 12, 13, 12, 11, 8])
    assert (event.start_index, event.end_index) == (1, 5)
    assert event.duration_days == event.exceedance_days == 5
    assert event.mean_intensity == pytest.approx(3.8)
    assert event.maximum_intensity == pytest.approx(5)
    assert event.cumulative_intensity == pytest.approx(19)


def test_shorter_than_minimum_is_not_an_event():
    assert call([11, 12, 13, 8], minimum_duration=5) == []


def test_joins_two_qualifying_runs_across_two_cool_days():
    events = call([11, 11, 11, 11, 11, 8, 9, 11, 11, 11, 11, 11])
    assert len(events) == 1
    assert events[0].duration_days == 12
    assert events[0].exceedance_days == 10


def test_does_not_join_across_too_long_gap():
    assert len(call([11]*5 + [8, 8, 8] + [11]*5)) == 2


def test_missing_day_breaks_event_and_cannot_be_joined():
    values = np.array([11]*5 + [np.nan, 8] + [11]*5, dtype=float)
    assert len(call(values)) == 2


def test_nonfinite_threshold_breaks_event():
    temp = np.array([11]*10, dtype=float)
    threshold = np.full(10, 10.0)
    threshold[5] = np.nan
    assert len(detect_events(temp, threshold, np.full(10, 8.0))) == 2


def test_rejects_shape_and_length_mismatch():
    with pytest.raises(ValueError, match="1D"):
        detect_events(np.ones((2, 2)), np.ones(4), np.ones(4))
    with pytest.raises(ValueError, match="same length"):
        detect_events(np.ones(4), np.ones(3), np.ones(4))


def test_rejects_invalid_duration_and_gap():
    with pytest.raises(ValueError, match="positive integer"):
        call([11]*5, minimum_duration=0)
    with pytest.raises(ValueError, match="non-negative integer"):
        call([11]*5, maximum_gap=-1)
