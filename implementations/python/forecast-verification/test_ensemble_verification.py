import pytest
from ensemble_verification import crps_ensemble,mean_crps_ensemble,expected_rank_histogram

def test_single_member_crps_is_absolute_error():
    assert crps_ensemble([3.0],[[1.0]])==[2.0]

def test_two_member_empirical_crps_hand_calculation():
    assert crps_ensemble([1.0],[[0.0,2.0]])==[pytest.approx(.5)]

def test_mean_crps_across_cases():
    assert mean_crps_ensemble([0,2],[[0],[1]])==pytest.approx(.5)

def test_rank_histogram_places_non_tied_observation():
    assert expected_rank_histogram([1.0],[[0.0,2.0]])==[0.0,1.0,0.0]

def test_rank_histogram_fractionally_handles_ties():
    assert expected_rank_histogram([1.0],[[1.0,1.0]])==pytest.approx([1/3,1/3,1/3])

def test_rank_histogram_counts_each_case_once():
    hist=expected_rank_histogram([0,1,2],[[0,1],[0,2],[1,3]])
    assert sum(hist)==pytest.approx(3.0)

@pytest.mark.parametrize("obs,ens", [([],[]),([1],[]),([1],[[1],[2]]),([1],[[float("nan")]])])
def test_invalid_inputs_rejected(obs,ens):
    with pytest.raises(ValueError):
        crps_ensemble(obs,ens)
