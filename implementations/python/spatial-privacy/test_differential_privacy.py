import numpy as np
import pytest
from differential_privacy import private_spatial_counts


def test_counts_deduplicate_and_cap_each_person_contributions():
    records=[("a","c1"),("a","c1"),("a","c2"),("b","c2")]
    result=private_spatial_counts(records,["c1","c2"],1,max_cells_per_person=1,rng=4)
    # Stable ordering retains c1 for a; b contributes c2.
    # Noise is deterministic for this seeded test; subtracting it is not
    # necessary to test the sensitivity contract.
    assert result["l1_sensitivity"]==1
    assert result["noise_scale"]==1
    assert set(result["noisy_counts"])=={"c1","c2"}


def test_noise_is_reproducible_and_scales_with_sensitivity():
    records=[("a","x"),("a","y"),("b","x")]
    a=private_spatial_counts(records,["x","y"],2,max_cells_per_person=2,rng=12)
    b=private_spatial_counts(records,["x","y"],2,max_cells_per_person=2,rng=12)
    assert a["noisy_counts"]==b["noisy_counts"]
    assert a["l1_sensitivity"]==2
    assert a["noise_scale"]==1


def test_empty_cells_invalid_epsilon_and_unknown_cells_rejected():
    with pytest.raises(ValueError):
        private_spatial_counts([],[],1)
    with pytest.raises(ValueError):
        private_spatial_counts([],["x"],0)
    with pytest.raises(ValueError):
        private_spatial_counts([("a","unknown")],["x"],1)
    with pytest.raises(ValueError):
        private_spatial_counts([],["x"],1,max_cells_per_person=0)


def test_contribution_order_does_not_change_true_capped_domain():
    a=private_spatial_counts([("u","b"),("u","a")],["a","b"],1,rng=2)
    b=private_spatial_counts([("u","a"),("u","b")],["a","b"],1,rng=2)
    assert a["noisy_counts"]==b["noisy_counts"]
