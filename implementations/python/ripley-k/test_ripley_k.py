import numpy as np
import pytest
from ripley_k import ripley_k

def test_two_point_pattern_counts_ordered_pairs_at_inclusive_radius():
    result=ripley_k([(0.5,0.5),(1.5,0.5)],bounds=(0,2,0,2),radii=[0.9,1.0,1.1])
    np.testing.assert_allclose(result.k_values,[0,2,2])
    np.testing.assert_allclose(result.l_values,[0,np.sqrt(2/np.pi),np.sqrt(2/np.pi)])

def test_k_and_l_are_monotone_for_increasing_radii():
    points=[(0,0),(1,0),(2,0),(2,2)]
    result=ripley_k(points,bounds=(-1,3,-1,3),radii=[0.5,1,2,3])
    assert np.all(np.diff(result.k_values)>=0)
    assert np.all(np.diff(result.l_values)>=0)

def test_zero_radius_includes_duplicate_event_pairs():
    result=ripley_k([(1,1),(1,1)],bounds=(0,2,0,2),radii=[0])
    assert result.k_values[0]==2

def test_translation_correction_weights_pair_by_window_overlap():
    points=[(0.5,0.5),(1.5,0.5)]
    result=ripley_k(points,bounds=(0,2,0,2),radii=[1],edge_correction="translation")
    # Window area 4; shifted overlap area 2; ordered-pair count 2.
    np.testing.assert_allclose(result.k_values,[4])

def test_translation_weight_increases_as_shifted_window_overlap_shrinks():
    short_shift=[(0.5,1),(1.5,1)]
    long_shift=[(0.5,1),(3.5,1)]
    a=ripley_k(short_shift,bounds=(0,4,0,4),radii=[3],edge_correction="translation")
    b=ripley_k(long_shift,bounds=(0,4,0,4),radii=[3],edge_correction="translation")
    assert b.k_values[0]>a.k_values[0]

def test_translation_correction_rejects_zero_overlap_pairs():
    with pytest.raises(ValueError,match="zero overlap"):
        ripley_k([(0,1),(4,1)],bounds=(0,4,0,4),radii=[4],edge_correction="translation")

def test_invalid_points_bounds_radii_and_correction_are_rejected():
    with pytest.raises(ValueError,match="at least two"):
        ripley_k([(0,0)],bounds=(0,1,0,1),radii=[1])
    with pytest.raises(ValueError,match="inside bounds"):
        ripley_k([(0,0),(2,2)],bounds=(0,1,0,1),radii=[1])
    with pytest.raises(ValueError,match="positive width"):
        ripley_k([(0,0),(0,1)],bounds=(0,0,0,1),radii=[1])
    with pytest.raises(ValueError,match="non-empty"):
        ripley_k([(0,0),(1,1)],bounds=(0,2,0,2),radii=[])
    with pytest.raises(ValueError,match="non-negative"):
        ripley_k([(0,0),(1,1)],bounds=(0,2,0,2),radii=[-1])
    with pytest.raises(ValueError,match="edge_correction"):
        ripley_k([(0,0),(1,1)],bounds=(-1,2,-1,2),radii=[1],edge_correction="isotropic")
