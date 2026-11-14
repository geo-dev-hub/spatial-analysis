import numpy as np
import pytest
from sal_verification import sal_score


def test_identical_fields_have_zero_sal_components():
    field=np.zeros((20,20)); field[4:9,5:12]=np.array([[1,2,3,4,3,2,1],[2,4,6,8,6,4,2],[1,2,3,4,3,2,1],[0,1,2,3,2,1,0],[0,0,1,2,1,0,0]])
    result=sal_score(field,field)
    assert result["structure"]==pytest.approx(0)
    assert result["amplitude"]==pytest.approx(0)
    assert result["location"]==pytest.approx(0)
    assert result["location_l1"]==pytest.approx(0)
    assert result["location_l2"]==pytest.approx(0)


def test_amplitude_component_has_expected_factor_of_three_sign():
    observed=np.zeros((12,12)); observed[3:6,3:6]=1
    result=sal_score(3*observed,observed)
    assert result["amplitude"]==pytest.approx(1.0)
    assert result["structure"]==pytest.approx(0.0)
    assert result["location"]==pytest.approx(0.0)
    assert sal_score(observed/3,observed)["amplitude"]==pytest.approx(-1.0)


def test_location_component_detects_translated_single_object():
    observed=np.zeros((20,20)); observed[4:7,4:7]=1
    forecast=np.zeros_like(observed); forecast[4:7,7:10]=1
    result=sal_score(forecast,observed)
    assert result["location_l1"]==pytest.approx(3/np.hypot(19,19))
    assert result["location_l2"]==pytest.approx(0.0)


def test_dry_fields_and_one_sided_missing_event_are_explicit():
    dry=np.zeros((5,5)); wet=dry.copy(); wet[2,2]=1
    both=sal_score(dry,dry)
    assert (both["structure"],both["amplitude"],both["location"])==(0,0,0)
    one=sal_score(wet,dry)
    assert one["amplitude"]==2
    assert one["structure"] is None and one["location"] is None


@pytest.mark.parametrize("forecast,observation,kwargs",[
    (np.ones((4,4)),np.ones((5,5)),{}),
    (np.ones((4,4)),np.ones((4,4)),{"threshold_fraction":0}),
    (np.ones((4,4)),np.ones((4,4)),{"threshold_fraction":1.1}),
    (np.ones((4,4)),np.ones((4,4)),{"connectivity":6}),
    (np.array([[1,-1],[1,1]]),np.ones((2,2)),{}),
])
def test_invalid_fields_and_parameters_are_rejected(forecast,observation,kwargs):
    with pytest.raises(ValueError): sal_score(forecast,observation,**kwargs)
