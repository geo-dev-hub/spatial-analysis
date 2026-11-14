import numpy as np
import pytest
from spatiotemporal_validation import leave_location_and_time_out


def test_test_folds_partition_all_rows_exactly_once():
    locations = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
    times = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    folds = leave_location_and_time_out(locations, times)
    held_out = np.concatenate([fold["test"] for fold in folds])
    assert sorted(held_out.tolist()) == list(range(9))
    assert len(set(held_out.tolist())) == 9


def test_training_excludes_both_held_out_location_and_time():
    locations = ["A", "A", "B", "B", "C", "C"]
    times = [1, 2, 1, 2, 1, 2]
    folds = leave_location_and_time_out(locations, times)
    fold = next(f for f in folds if f["location"] == "A" and f["time"] == 1)
    assert fold["test"].tolist() == [0]
    assert fold["buffer"].tolist() == [1, 2, 4]
    assert fold["train"].tolist() == [3, 5]


def test_only_observed_pairs_create_folds():
    folds = leave_location_and_time_out(["A", "A", "B"], [1, 2, 2])
    assert len(folds) == 3
    assert all(len(fold["test"]) > 0 for fold in folds)


def test_fold_order_follows_first_observed_pair():
    folds = leave_location_and_time_out(["B", "A", "B", "A"], [2, 1, 1, 2])
    assert [(f["location"], f["time"]) for f in folds] == [
        ("B", 2), ("A", 1), ("B", 1), ("A", 2)
    ]


def test_single_location_produces_explicit_empty_training_sets():
    folds = leave_location_and_time_out(["A", "A", "A"], [1, 2, 3])
    assert all(len(f["train"]) == 0 for f in folds)
    assert all(len(f["buffer"]) == 2 for f in folds)


@pytest.mark.parametrize("locations,times", [
    ([], []), (["A"], []), (["A", "B"], ["1"]),
    ([["A"], ["B"]], [1, 2]), (["A", None], [1, 2]),
    (["A", float("nan")], [1, 2]),
])
def test_invalid_inputs_are_rejected(locations, times):
    with pytest.raises(ValueError):
        leave_location_and_time_out(locations, times)
