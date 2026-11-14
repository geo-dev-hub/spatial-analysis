import math
import pytest
from splines import bspline_point,bspline_curve,nurbs_point,nurbs_curve

def test_linear_clamped_bspline_is_linear_interpolation():
    cp=[(0,0),(2,2),(4,0)]; knots=[0,0,0.5,1,1]
    assert bspline_point(cp,1,knots,0)==(0.0,0.0)
    assert bspline_point(cp,1,knots,0.5)==(2.0,2.0)
    assert bspline_point(cp,1,knots,1)==(4.0,0.0)

def test_quadratic_bspline_bezier_equivalence():
    cp=[(0,0),(1,2),(2,0)];knots=[0,0,0,1,1,1]
    assert bspline_point(cp,2,knots,0)==(0.0,0.0)
    assert bspline_point(cp,2,knots,1)==(2.0,0.0)
    assert bspline_point(cp,2,knots,.5)==(1.0,1.0)

def test_nurbs_quarter_circle_exact_midpoint():
    w=math.sqrt(.5);cp=[(1,0),(1,1),(0,1)];weights=[1,w,1];knots=[0,0,0,1,1,1]
    x,y=nurbs_point(cp,weights,2,knots,.5)
    assert x==pytest.approx(math.sqrt(.5));assert y==pytest.approx(math.sqrt(.5))

def test_curve_sampling_includes_domain_endpoints():
    cp=[(0,0),(1,1),(2,0)];knots=[0,0,0,1,1,1]
    out=bspline_curve(cp,2,knots,5)
    assert len(out)==5 and out[0]==(0.,0.) and out[-1]==(2.,0.)

def test_nurbs_curve_and_validation():
    cp=[(1,0),(1,1),(0,1)];w=[1,math.sqrt(.5),1];knots=[0,0,0,1,1,1]
    assert len(nurbs_curve(cp,w,2,knots,9))==9
    with pytest.raises(ValueError):bspline_point(cp,2,[0,0,1,1],.5)
    with pytest.raises(ValueError):nurbs_point(cp,[1,0,1],2,knots,.5)
    with pytest.raises(ValueError):bspline_point(cp,2,knots,2)
