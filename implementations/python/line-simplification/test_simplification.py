import pytest
from simplification import douglas_peucker,lang,reumann_witkam,visvalingam_whyatt
def test_existing_methods():
    line=[(0,0),(1,.1),(2,-.1),(3,0)]
    assert douglas_peucker(line,.2)==[line[0],line[-1]]
    assert visvalingam_whyatt([(0,0),(1,0),(2,0),(3,0)],0)==[(0.,0.),(3.,0.)]
def test_reumann_witkam_turn_and_endpoints():
    line=[(0,0),(1,0),(2,.05),(3,.02),(4,2),(5,2)]
    out=reumann_witkam(line,.1)
    assert out[0]==line[0] and out[-1]==line[-1] and len(out)<len(line)
def test_reumann_witkam_straight():
    assert reumann_witkam([(0,0),(1,0),(2,0),(3,0)],0)==[(0.,0.),(3.,0.)]
def test_lang_collinear():
    assert lang([(0,0),(1,0),(2,0),(3,0),(4,0)],0,4)==[(0.,0.),(4.,0.)]
def test_lang_retains_deviation():
    line=[(0,0),(1,0),(2,2),(3,0),(4,0)];out=lang(line,.5,4)
    assert out[0]==line[0] and out[-1]==line[-1] and len(out)>2
@pytest.mark.parametrize("fn",[douglas_peucker,visvalingam_whyatt,reumann_witkam])
def test_negative_tolerance(fn):
    with pytest.raises(ValueError):fn([(0,0),(1,1)],-1)
def test_invalid_lang_lookahead():
    with pytest.raises(ValueError):lang([(0,0),(1,1)],1,0)
def test_nonfinite():
    with pytest.raises(ValueError):reumann_witkam([(0,0),(1,float("nan"))],1)


def test_opheim_collinear_respects_maximum_search_distance():
    line = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)]
    out = opheim(line, strip_half_width=0.1, min_distance=1, max_distance=3)
    assert out == [(0.0,0.0),(3.0,0.0),(6.0,0.0)]

def test_opheim_preserves_endpoints_and_handles_short_line():
    line = [(0,0),(0.2,0),(0.4,0)]
    out = opheim(line, 0.1, 1, 3)
    assert out[0] == (0.0,0.0) and out[-1] == (0.4,0.0)

def test_opheim_rejects_invalid_distance_constraints():
    with pytest.raises(ValueError):
        opheim([(0,0),(1,0)], 0.1, 2, 1)
