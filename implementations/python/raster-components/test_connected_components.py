import numpy as np
import pytest
from connected_components import connected_components

def test_separate_regions_receive_distinct_row_major_labels():
    mask=np.array([[1,1,0,0],[1,0,0,1],[0,0,1,1]],dtype=bool)
    labels,sizes=connected_components(mask,connectivity=4)
    assert list(sizes)==[1,2,3]
    assert sizes=={1:3,2:1,3:2}
    assert labels[0,0]==1 and labels[1,3]==2 and labels[2,2]==3

def test_diagonal_contact_depends_on_connectivity():
    mask=np.array([[1,0],[0,1]],dtype=bool)
    _,four=connected_components(mask,connectivity=4)
    _,eight=connected_components(mask,connectivity=8)
    assert len(four)==2
    assert len(eight)==1
    assert list(eight.values())==[2]

def test_invalid_cells_act_as_barriers_and_remain_zero():
    mask=np.ones((1,3),dtype=bool)
    valid=np.array([[1,0,1]],dtype=bool)
    labels,sizes=connected_components(mask,connectivity=4,valid=valid)
    np.testing.assert_array_equal(labels,[[1,0,2]])
    assert sizes=={1:1,2:1}

def test_background_is_zero_and_empty_foreground_has_no_components():
    labels,sizes=connected_components(np.zeros((3,4),dtype=bool))
    assert not labels.any()
    assert sizes=={}

def test_invalid_shapes_and_connectivity_are_rejected():
    with pytest.raises(ValueError,match="2D"):
        connected_components([1,0])
    with pytest.raises(ValueError,match="same 2D shape"):
        connected_components([[1,0]],valid=[[1]])
    with pytest.raises(ValueError,match="connectivity"):
        connected_components([[1]],connectivity=6)
