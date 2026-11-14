import numpy as np
import pytest
from spatial_microsimulation import ipf_rake

def test_ipf_recovers_compatible_two_way_margins():
    controls=np.array([[1,0,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1]],float)
    result=ipf_rake(np.ones(4),controls,[30,70,40,60])
    assert result["converged"]
    np.testing.assert_allclose(result["fitted_margins"],[30,70,40,60],atol=1e-6)
    assert result["iterations"]>1

def test_ipf_preserves_structural_zero_seed_records():
    result=ipf_rake([1,0,1],[[1,0],[1,0],[0,1]],[4,6])
    assert result["weights"][1]==0
    np.testing.assert_allclose(result["fitted_margins"],[4,6],atol=1e-7)

def test_ipf_rejects_positive_control_without_seed_support():
    with pytest.raises(ValueError,match="zero seed support"):
        ipf_rake([1,1],[[1,0],[1,0]],[2,1])

def test_ipf_reports_incompatible_margins_without_claiming_convergence():
    result=ipf_rake([1,1],[[1,1],[1,1]],[10,20],max_iter=2)
    assert not result["converged"] and result["iterations"]==2

@pytest.mark.parametrize("seed,design,target",[
    ([1,-1],[[1],[1]],[1]),([1],[[0.5]],[1]),([1,1],[[1],[-1]],[1]),
    ([1,1],[[1,0],[1,0]],[1]),
])
def test_ipf_rejects_invalid_inputs(seed,design,target):
    with pytest.raises(ValueError): ipf_rake(seed,design,target)


def test_systematic_resampling_returns_requested_size_and_reproducible_donors():
    from spatial_microsimulation import systematic_resample_records
    records = np.array([["A"], ["B"]])
    first = systematic_resample_records(records, [1, 3], 40, rng=np.random.default_rng(12))
    second = systematic_resample_records(records, [1, 3], 40, rng=np.random.default_rng(12))
    assert first["synthetic_records"].shape == (40, 1)
    np.testing.assert_array_equal(first["donor_indices"], second["donor_indices"])
    assert first["donor_counts"].sum() == 40
    assert abs(first["donor_counts"][0] / 40 - 0.25) <= 0.025


def test_systematic_resampling_rejects_invalid_population_or_weights():
    from spatial_microsimulation import systematic_resample_records
    with pytest.raises(ValueError):
        systematic_resample_records([[1], [2]], [0, 0], 10)
    with pytest.raises(ValueError):
        systematic_resample_records([[1], [2]], [1, 1], 0)
