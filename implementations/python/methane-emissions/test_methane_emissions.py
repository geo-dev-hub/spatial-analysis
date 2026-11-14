import numpy as np
import pytest
from methane_emissions import (
    gaussian_plume_template, matched_filter_plume,
    ime_emission_rate, cross_sectional_flux,
)


def test_matched_filter_detects_injected_gaussian_plume():
    rng=np.random.default_rng(7)
    image=rng.normal(0,0.2,(81,91))
    template=gaussian_plume_template((15,25),2.0,5.0,0.3)
    image[33:48,34:59]+=4.0*template
    result=matched_filter_plume(image,[template],noise_sigma=0.2,threshold=5)
    peak=np.unravel_index(np.argmax(result["score"]),image.shape)
    assert abs(peak[0]-40)<=1 and abs(peak[1]-46)<=1
    assert result["amplitude"][peak]==pytest.approx(4.0,abs=0.3)
    assert result["detections"][peak]


def test_matched_filter_selects_best_template_scale():
    image=np.zeros((61,61))
    template=gaussian_plume_template((13,21),2,4,0)
    image[24:37,20:41]=3*template
    other=gaussian_plume_template((13,21),4,8,0)
    result=matched_filter_plume(image,[other,template],0.1,threshold=1)
    assert result["template_index"][30,30]==1


def test_matched_filter_validates_noise_templates_and_shapes():
    with pytest.raises(ValueError):
        matched_filter_plume(np.ones((5,5)),[],1)
    with pytest.raises(ValueError):
        matched_filter_plume(np.ones((5,5)),[np.ones((3,3))],0)
    with pytest.raises(ValueError):
        gaussian_plume_template((4,5),1,2)


def test_ime_emission_rate_units_and_zero_cases():
    assert ime_emission_rate(100,5,20)==pytest.approx(25)
    assert ime_emission_rate(0,5,20)==0
    with pytest.raises(ValueError):
        ime_emission_rate(1,2,0)
    with pytest.raises(ValueError):
        ime_emission_rate(-1,2,3)


def test_cross_sectional_flux_integrates_signed_normal_transport():
    c=np.array([1,2,3.0])
    u=np.array([2,2,-1.0])
    width=np.array([1,0.5,2.0])
    assert cross_sectional_flux(c,u,width)==pytest.approx(-2.0)
    with pytest.raises(ValueError):
        cross_sectional_flux([1,2],[1],[1,1])



def test_hysteresis_keeps_low_threshold_regions_connected_to_high_seed():
    from methane_emissions import hysteresis_plume_segmentation
    image=np.zeros((20,24))
    image[5:9,4:12]=1.5
    image[6:8,6:9]=4.0
    image[13:16,17:20]=1.5  # low-only island must be discarded
    result=hysteresis_plume_segmentation(image,1.0,3.0,min_area=3)
    assert len(result["objects"])==1
    assert result["objects"][0]["area"]==32
    assert result["mask"][6,7]
    assert not result["mask"][14,18]


def test_hysteresis_thresholds_smoothing_and_connectivity_contract():
    from methane_emissions import hysteresis_plume_segmentation
    image=np.zeros((8,8)); image[1,1]=4; image[2,2]=2
    four=hysteresis_plume_segmentation(image,1,3,connectivity=4)
    eight=hysteresis_plume_segmentation(image,1,3,connectivity=8)
    assert len(four["objects"])==1
    assert len(eight["objects"])==1
    with pytest.raises(ValueError):
        hysteresis_plume_segmentation(image,3,2)
    with pytest.raises(ValueError):
        hysteresis_plume_segmentation(image,1,2,connectivity=6)
