import numpy as np
import pytest
from object_verification import identify_objects, match_objects


def test_object_identification_restores_original_intensity_attributes():
    field=np.zeros((12,12)); field[2:5,3:7]=np.array([[1,2,3,2],[2,4,5,2],[1,2,3,1]])
    result=identify_objects(field,threshold=1,min_area=3)
    assert len(result["objects"])==1
    obj=result["objects"][0]
    assert obj["area"]==12
    assert obj["intensity_max"]==5
    assert 3<=obj["centroid_x"]<5


def test_connectivity_and_minimum_area_control_object_count():
    field=np.zeros((8,8)); field[1,1]=2; field[2,2]=2; field[6,6]=2
    assert len(identify_objects(field,threshold=1,connectivity=4)["objects"])==3
    assert len(identify_objects(field,threshold=1,connectivity=8)["objects"])==2
    assert len(identify_objects(field,threshold=1,connectivity=8,min_area=2)["objects"])==1


def test_matching_finds_nearby_object_and_reports_unmatched():
    forecast=[{"id":1,"area":8,"centroid_x":4,"centroid_y":4,"intensity_mean":3.0},
              {"id":2,"area":3,"centroid_x":17,"centroid_y":17,"intensity_mean":2.0}]
    observed=[{"id":7,"area":8,"centroid_x":5,"centroid_y":4,"intensity_mean":3.1}]
    result=match_objects(forecast,observed,(20,20),max_centroid_distance=.2)
    assert result["matches"][0]["forecast_id"]==1
    assert result["matches"][0]["observed_id"]==7
    assert result["unmatched_forecast"]==[2]
    assert result["unmatched_observed"]==[]


def test_empty_fields_and_invalid_parameters_are_explicit():
    empty=identify_objects(np.zeros((5,5)),threshold=1)
    assert empty["objects"]==[]
    result=match_objects([],[],(5,5))
    assert result["matches"]==[]
    with pytest.raises(ValueError): identify_objects(np.ones((4,4)),threshold=0)
    with pytest.raises(ValueError): identify_objects(np.ones((4,4)),threshold=1,connectivity=6)
    with pytest.raises(ValueError): match_objects([],[],(5,5),max_centroid_distance=0)
