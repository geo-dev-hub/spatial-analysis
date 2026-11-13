import numpy as np
import pytest
from transform import transform_points

def test_geographic_origin_maps_to_projected_origin():
    result=transform_points([[0,0]],"EPSG:4326","EPSG:3857")
    np.testing.assert_allclose(result,[[0,0]],atol=1e-8)

def test_web_mercator_known_coordinate_and_round_trip():
    point=np.array([[10.0,50.0]])
    projected=transform_points(point,"EPSG:4326","EPSG:3857")
    np.testing.assert_allclose(projected,[[1113194.9079,6446275.8410]],rtol=1e-6)
    restored=transform_points(projected,"EPSG:3857","EPSG:4326")
    np.testing.assert_allclose(restored,point,atol=1e-8)

def test_always_xy_means_longitude_then_latitude():
    projected=transform_points([[9.0,0.0]],"EPSG:4326","EPSG:32632")
    np.testing.assert_allclose(projected,[[500000,0]],atol=1e-5)

def test_same_crs_preserves_coordinates():
    points=np.array([[12.5,-4.25],[0,0]])
    np.testing.assert_allclose(transform_points(points,"EPSG:4326","EPSG:4326"),points)

def test_invalid_shapes_nonfinite_coordinates_and_crs_are_rejected():
    with pytest.raises(ValueError,match="N×2"):
        transform_points([[1,2,3]],"EPSG:4326","EPSG:3857")
    with pytest.raises(ValueError,match="finite"):
        transform_points([[np.nan,0]],"EPSG:4326","EPSG:3857")
    with pytest.raises(ValueError,match="failed"):
        transform_points([[0,0]],"not-a-real-crs","EPSG:3857")
