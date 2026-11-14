import math
import pytest
from curve_fitting import fit_bezier_curves

def evaluate(curve,u):
    v=1-u
    return tuple(curve[0][j]*v**3+3*curve[1][j]*v*v*u+3*curve[2][j]*v*u*u+curve[3][j]*u**3 for j in range(2))

def sample(curve,n=31):
    return [evaluate(curve,i/(n-1)) for i in range(n)]

def test_two_point_fit_preserves_endpoints():
    curves=fit_bezier_curves([(0,0),(3,0)],.01)
    assert len(curves)==1 and curves[0][0]==(0.0,0.0) and curves[0][-1]==(3.0,0.0)

def test_exact_cubic_samples_fit_with_small_error():
    source=((0,0),(1,2),(3,2),(4,0))
    curves=fit_bezier_curves(sample(source,25),1e-3,max_iterations=5)
    assert len(curves)==1
    for p,u in zip(sample(source,25),[i/24 for i in range(25)]):
        q=evaluate(curves[0],u)
        assert math.dist(p,q)<.04

def test_sharp_corner_is_split_into_connected_segments():
    points=[(0,0),(1,0),(2,0),(2,1),(2,2)]
    curves=fit_bezier_curves(points,.01)
    assert len(curves)>=2
    for a,b in zip(curves,curves[1:]):
        assert a[-1]==b[0]
    assert curves[0][0]==(0.0,0.0) and curves[-1][-1]==(2.0,2.0)

def test_duplicate_points_do_not_break_fit():
    curves=fit_bezier_curves([(0,0),(0,0),(1,0),(2,0),(2,0)],.01)
    assert curves[0][0]==(0.0,0.0) and curves[-1][-1]==(2.0,0.0)

def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):fit_bezier_curves([(0,0)],.1)
    with pytest.raises(ValueError):fit_bezier_curves([(0,0),(1,1)],-1)


def test_malformed_points_rejected():
    with pytest.raises(ValueError):
        fit_bezier_curves([(0,0),(1,2,3)],.1)
