import pytest
from simplification import _distance_to_line, douglas_peucker,lang,opheim,reumann_witkam,visvalingam_whyatt
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


def test_zhao_saalfeld_narrow_sleeve_simplifies_straight_line():
    from simplification import zhao_saalfeld_narrow_sleeve
    line=[(0,0),(1,0.02),(2,-0.01),(3,0.01),(4,0)]
    assert zhao_saalfeld_narrow_sleeve(line,0.05)==[(0.0,0.0),(4.0,0.0)]

def test_zhao_saalfeld_narrow_sleeve_retains_direction_change():
    from simplification import zhao_saalfeld_narrow_sleeve
    line=[(0,0),(1,0),(2,0),(2,1),(2,2)]
    out=zhao_saalfeld_narrow_sleeve(line,0.1)
    assert out[0]==(0.0,0.0) and out[-1]==(2.0,2.0)
    assert len(out)>=3

def test_zhao_saalfeld_sleeve_respects_supporting_line_tolerance():
    from simplification import zhao_saalfeld_narrow_sleeve
    line=[(0,0),(1,0.03),(2,-0.02),(3,0.01),(4,0),(4,1),(4,2)]
    eps=0.05;out=zhao_saalfeld_narrow_sleeve(line,eps)
    source_index={p:i for i,p in enumerate(line)}
    for a,b in zip(out,out[1:]):
        ia,ib=source_index[a],source_index[b]
        for p in line[ia+1:ib]:
            assert _distance_to_line(p,a,b)<=eps+1e-10

def test_zhao_saalfeld_handles_angle_wrap_and_duplicates():
    from simplification import zhao_saalfeld_narrow_sleeve
    line=[(0,0),(-1,0.01),(-2,0),(-2,0),(-3,-0.01)]
    out=zhao_saalfeld_narrow_sleeve(line,0.02)
    assert out[0]==(0.0,0.0) and out[-1]==(-3.0,-0.01)

def test_zhao_saalfeld_rejects_negative_tolerance():
    from simplification import zhao_saalfeld_narrow_sleeve
    with pytest.raises(ValueError):
        zhao_saalfeld_narrow_sleeve([(0,0),(1,1)],-1)


def test_douglas_peucker_retains_deviation_above_threshold():
    line = [(0, 0), (1, 1), (2, 0)]
    out = douglas_peucker(line, 0.9)
    assert out == [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)]


def test_douglas_peucker_discards_deviation_at_threshold():
    # The implementation splits only when maximum deviation is strictly > tolerance.
    line = [(0, 0), (1, 1), (2, 0)]
    assert douglas_peucker(line, 1.0) == [(0.0, 0.0), (2.0, 0.0)]


def test_douglas_peucker_handles_coincident_endpoints():
    line = [(0, 0), (1, 0), (0, 0)]
    assert douglas_peucker(line, 0.5) == [
        (0.0, 0.0), (1.0, 0.0), (0.0, 0.0)
    ]


def test_douglas_peucker_preserves_endpoints_and_order():
    line = [(0, 0), (1, 0.02), (2, 0.01), (3, 1), (4, 1)]
    out = douglas_peucker(line, 0.1)
    assert out[0] == (0.0, 0.0)
    assert out[-1] == (4.0, 1.0)
    positions = [line.index(point) for point in out]
    assert positions == sorted(positions)


def test_visvalingam_threshold_uses_triangle_area_units():
    triangle = [(0, 0), (1, 1), (2, 0)]
    assert visvalingam_whyatt(triangle, 0.5) == [
        (0.0, 0.0), (2.0, 0.0)
    ]
    assert visvalingam_whyatt(triangle, 0.49) == [
        (0.0, 0.0), (1.0, 1.0), (2.0, 0.0)
    ]


def test_visvalingam_preserves_endpoints_for_repeated_vertices():
    line = [(0, 0), (0, 0), (1, 0), (2, 0)]
    out = visvalingam_whyatt(line, 0.0)
    assert out[0] == (0.0, 0.0)
    assert out[-1] == (2.0, 0.0)


def test_simplifiers_return_empty_and_singleton_inputs():
    for fn, args in (
        (douglas_peucker, (0.1,)),
        (visvalingam_whyatt, (0.1,)),
        (reumann_witkam, (0.1,)),
        (lang, (0.1, 3)),
        (opheim, (0.1, 0.5, 2.0)),
        (zhao_saalfeld_narrow_sleeve, (0.1,)),
    ):
        assert fn([], *args) == []
        assert fn([(2, 3)], *args) == [(2.0, 3.0)]
