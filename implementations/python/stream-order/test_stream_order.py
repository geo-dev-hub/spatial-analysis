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
    # Two first-order tributaries meet, then their second-order stream meets a
    # separate first-order tributary: the downstream order remains two.
    directions = np.array([
        [-1, 4, -1, -1, -1],
        [-1, 1, 1, 4, -1],
        [-1, -1, -1, 64, -1],
        [-1, -1, -1, 64, -1],
    ])
    mask = directions != -1
    order, magnitude = stream_order(directions, mask)
    assert order[1, 1] == 2
    assert order[1, 3] == 2
    assert magnitude[1, 3] == 3


def test_two_equal_second_order_tributaries_create_third_order():
    # Four headwaters form two second-order tributaries, which meet downstream.
    directions = np.array([
        [-1, 4, -1, -1, -1],
        [-1, 1, -1, 4, -1],
        [-1, -1, 1, 1, -1],
        [-1, -1, -1, 64, -1],
    ])
    # Build a deliberately simple stream network mask for the directed paths.
    mask = directions != -1
    order, magnitude = stream_order(directions, mask)
    assert order[1, 1] == 2
    assert order[2, 3] == 2
    assert order[3, 3] == 2


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
