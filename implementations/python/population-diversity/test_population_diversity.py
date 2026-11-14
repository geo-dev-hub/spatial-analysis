import numpy as np
import pytest
from population_diversity import shannon_entropy,simpson_concentration,reardon_firebaugh_entropy_index,exposure_matrix,isolation_indices

def test_shannon_and_simpson_for_equal_two_group_counts():
    assert shannon_entropy([1,1])==pytest.approx(np.log(2))
    assert simpson_concentration([1,1])==pytest.approx(.5)

def test_multigroup_entropy_index_perfect_separation_and_evenness():
    assert reardon_firebaugh_entropy_index([[10,0],[0,10]])==pytest.approx(1)
    assert reardon_firebaugh_entropy_index([[5,5],[5,5]])==pytest.approx(0)

def test_exposure_matrix_identity_for_separate_units():
    out=exposure_matrix([[10,0],[0,10]])
    np.testing.assert_allclose(out,np.eye(2))

def test_exposure_matrix_equal_composition():
    out=exposure_matrix([[5,5],[5,5]])
    np.testing.assert_allclose(out,[[.5,.5],[.5,.5]])
    np.testing.assert_allclose(isolation_indices([[5,5],[5,5]]),[.5,.5])

def test_empty_categories_contribute_zero_entropy():
    assert shannon_entropy([10,0,0])==pytest.approx(0)
    assert simpson_concentration([10,0,0])==pytest.approx(1)

def test_invalid_counts_rejected():
    with pytest.raises(ValueError):reardon_firebaugh_entropy_index([[1,-1],[2,2]])
    with pytest.raises(ValueError):exposure_matrix([[1,0],[0,0]])
