import numpy as np
import pytest
from nt_xent import nt_xent_loss

def test_identical_paired_views_have_low_loss_with_orthogonal_negatives():
    view=np.eye(4)
    assert nt_xent_loss(view,view,temperature=0.1)<1e-3

def test_loss_is_invariant_to_positive_per_row_rescaling():
    rng=np.random.default_rng(4)
    a=rng.normal(size=(5,8)); b=rng.normal(size=(5,8))
    base=nt_xent_loss(a,b)
    scaled=nt_xent_loss(a*np.arange(1,6)[:,None],b*np.arange(2,7)[:,None])
    np.testing.assert_allclose(base,scaled,rtol=1e-12,atol=1e-12)

def test_temperature_must_be_positive_and_finite():
    with pytest.raises(ValueError,match="temperature"):
        nt_xent_loss(np.eye(2),np.eye(2),temperature=0)
    with pytest.raises(ValueError,match="temperature"):
        nt_xent_loss(np.eye(2),np.eye(2),temperature=float("inf"))

def test_invalid_batches_and_zero_vectors_are_rejected():
    with pytest.raises(ValueError,match="aligned 2D"):
        nt_xent_loss([[1,0]],[[1,0]])
    with pytest.raises(ValueError,match="non-zero"):
        nt_xent_loss([[0,0],[1,0]],[[0,0],[0,1]])
    with pytest.raises(ValueError,match="finite"):
        nt_xent_loss([[1,0],[np.nan,1]],[[1,0],[0,1]])
