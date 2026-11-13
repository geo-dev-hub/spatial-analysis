import numpy as np
import pytest

from stream_order import stream_order


def test_two_first_order_streams_form_second_order_confluence():
    directions = np.array([
        [-1, 4, -1],
        [-1, 1, -1],
        [-1, 64, -1],
    ])
    mask = directions != -1
    order, magnitude = stream_order(directions, mask)
    assert order[0, 1] == 1
    assert order[2, 1] == 1
    assert order[1, 1] == 2
    assert magnitude[1, 1] == 2


def test_unequal_order_confluence_keeps_maximum_strahler_order():
    # Two first-order tributaries form order two; that stream meets one
    # first-order tributary, so the downstream order remains two.
    directions = np.array([
        [-1, -1, 4, -1, -1],
        [-1, 1, 1, 1, 0],
        [-1, -1, -1, 64, -1],
    ])
    mask = directions != -1
    order, magnitude = stream_order(directions, mask)
    assert order[1, 2] == 2
    assert order[1, 3] == 2
    assert magnitude[1, 3] == 3


def test_two_equal_second_order_tributaries_create_third_order():
    # Two separate pairs of headwaters form second-order tributaries,
    # which then meet at a third-order confluence.
    directions = np.array([
        [-1, -1, -1, 4, -1],
        [-1, 4, -1, 8, 16],
        [1, 1, 1, -1, -1],
        [-1, -1, 0, -1, -1],
    ])
    mask = directions != -1
    order, magnitude = stream_order(directions, mask)
    assert order[2, 1] == 2
    assert order[1, 3] == 2
    assert order[2, 2] == 3
    assert magnitude[2, 2] == 4


def test_nonstream_cells_are_zero_and_invalid_cells_are_minus_one():
    directions = np.array([[1, 0, -1]])
    mask = np.array([[False, True, False]])
    order, magnitude = stream_order(directions, mask)
    assert order[0, 0] == 0 and magnitude[0, 0] == 0
    assert order[0, 1] == 1 and magnitude[0, 1] == 1
    assert order[0, 2] == -1 and magnitude[0, 2] == -1


def test_disconnected_stream_mask_is_rejected():
    with pytest.raises(ValueError, match="downstream-connected"):
        stream_order([[1, 0]], [[True, False]])


def test_stream_cycle_is_rejected():
    with pytest.raises(ValueError, match="cycle"):
        stream_order([[1, 16]], [[True, True]])


def test_stream_mask_cannot_include_nodata_or_have_wrong_shape():
    with pytest.raises(ValueError, match="invalid"):
        stream_order([[-1]], [[True]])
    with pytest.raises(ValueError, match="same shape"):
        stream_order([[0]], [[True, False]])
