import numpy as np
import pytest
from zonal_statistics import zonal_statistics

def test_zone_summaries_match_expected_values():
    values=[[1,2,10],[3,4,20]]
    zones=[[1,1,2],[1,1,2]]
    result=zonal_statistics(values,zones)
    assert result[1]["count"]==4
    assert result[1]["sum"]==10
    assert result[1]["mean"]==2.5
    assert result[1]["min"]==1
    assert result[1]["max"]==4
    assert result[1]["median"]==2.5
    assert result[2]["mean"]==15

def test_nodata_values_are_skipped_but_zone_is_preserved():
    values=[[1,np.nan],[np.nan,np.nan]]
    zones=[[7,7],[8,8]]
    result=zonal_statistics(values,zones)
    assert result[7]["count"]==1
    assert result[7]["mean"]==1
    assert result[8]["count"]==0
    assert np.isnan(result[8]["mean"])
    assert result[8]["sum"]==0

def test_nodata_zone_labels_are_excluded():
    result=zonal_statistics([[5,10]],[[1,np.nan]])
    assert list(result)==[1]
    assert result[1]["mean"]==5

def test_shape_and_zone_label_contracts():
    with pytest.raises(ValueError,match="same shape"):
        zonal_statistics([[1,2]],[[1]])
    with pytest.raises(ValueError,match="integers"):
        zonal_statistics([[1,2]],[[1,1.5]])
    with pytest.raises(ValueError,match="int64 range"):
        zonal_statistics([[1]],[[float(2**63)]])
    with pytest.raises(ValueError,match="2D"):
        zonal_statistics([1,2],[[1,1]])

def test_zonal_histogram_uses_explicit_bins_and_skips_nodata():
    from zonal_statistics import zonal_histogram
    values=[[1,2,2,4],[np.nan,1,3,5]]
    zones=[[1,1,2,2],[1,2,2,2]]
    result=zonal_histogram(values,zones,[0,2,3,5])
    np.testing.assert_array_equal(result[1],[1,1,0])
    np.testing.assert_array_equal(result[2],[1,1,3])

def test_zonal_histogram_preserves_empty_zones_and_validates_edges():
    from zonal_statistics import zonal_histogram
    result=zonal_histogram([[np.nan]],[[8]],[0,1,2])
    np.testing.assert_array_equal(result[8],[0,0])
    with pytest.raises(ValueError,match="bin_edges"):
        zonal_histogram([[1]],[[1]],[0,2,1])
