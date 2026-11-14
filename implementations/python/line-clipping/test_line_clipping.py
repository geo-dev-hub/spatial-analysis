import unittest
import pytest
from line_clipping import cohen_sutherland, liang_barsky, cyrus_beck, nicholl_lee_nicholl
R=(0,0,10,10)
class LineClippingTests(unittest.TestCase):
 def test_crossing_segment(self):
  expected=((0.0,5.0),(10.0,5.0))
  for fn in (cohen_sutherland,liang_barsky):
   got=fn((-5,5),(15,5),R)
   for a,b in zip(got,expected):
    self.assertAlmostEqual(a[0],b[0]); self.assertAlmostEqual(a[1],b[1])
 def test_reject_outside(self):
  self.assertIsNone(cohen_sutherland((-2,-2),(-1,-1),R))
  self.assertIsNone(liang_barsky((-2,-2),(-1,-1),R))
 def test_inside_and_boundary(self):
  self.assertEqual(liang_barsky((2,2),(8,8),R),((2.0,2.0),(8.0,8.0)))
  self.assertEqual(cohen_sutherland((0,0),(0,10),R),((0.0,0.0),(0.0,10.0)))
 def test_parallel_outside(self):
  self.assertIsNone(liang_barsky((-2,11),(12,11),R))
 def test_cyrus_beck_convex_ccw_and_cw(self):
  square=[(0,0),(10,0),(10,10),(0,10)]
  for ring in (square,list(reversed(square))):
   got=cyrus_beck((-5,5),(15,5),ring)
   self.assertAlmostEqual(got[0][0],0); self.assertAlmostEqual(got[1][0],10)
 def test_cyrus_beck_reject(self):
  self.assertIsNone(cyrus_beck((-5,-5),(-1,-1),[(0,0),(10,0),(10,10),(0,10)]))
 def test_cyrus_beck_rejects_concave_window(self):
  with self.assertRaises(ValueError): cyrus_beck((-1,2),(5,2),[(0,0),(4,0),(2,1),(4,4),(0,4)])
 def test_invalid_window(self):
  with self.assertRaises(ValueError): cyrus_beck((0,0),(1,1),[(0,0),(1,1)])
  with self.assertRaises(ValueError): liang_barsky((0,0),(1,1),(2,0,1,1))
if __name__=='__main__':unittest.main()


def test_nicholl_lee_nicholl_matches_other_clippers_on_basic_cases():
    square=(0,0,10,10)
    cases=[
        ((-5,5),(15,5)), ((5,-5),(5,15)), ((-5,-5),(15,15)),
        ((-5,12),(12,-5)), ((5,5),(15,5)), ((-5,5),(5,5)),
        ((-5,15),(5,5)), ((-5,-5),(5,5)), ((5,5),(-5,-5)),
        ((0,0),(10,10)), ((-5,0),(15,0)), ((-5,10),(15,10)),
    ]
    for a,b in cases:
        expected=liang_barsky(a,b,square)
        got=nicholl_lee_nicholl(a,b,square)
        if expected is None:
            assert got is None
        else:
            assert got is not None
            for p,q in zip(got,expected):
                assert p==pytest.approx(q,abs=1e-9)


def test_nicholl_lee_nicholl_randomized_against_liang_barsky():
    import random
    rng=random.Random(42)
    rect=(-3.0,-2.0,7.0,5.0)
    for _ in range(2000):
        a=(rng.uniform(-10,12),rng.uniform(-9,10))
        b=(rng.uniform(-10,12),rng.uniform(-9,10))
        expected=liang_barsky(a,b,rect)
        got=nicholl_lee_nicholl(a,b,rect)
        if expected is None:
            assert got is None, (a,b,got)
        else:
            assert got is not None, (a,b,expected)
            for p,q in zip(got,expected):
                assert p==pytest.approx(q,abs=1e-8)


def test_nicholl_lee_nicholl_handles_vertical_and_horizontal_segments():
    r=(0,0,10,10)
    for got, expected in [
        (nicholl_lee_nicholl((5,-2),(5,12),r), ((5,0),(5,10))),
        (nicholl_lee_nicholl((-2,5),(12,5),r), ((0,5),(10,5))),
        (nicholl_lee_nicholl((-2,0),(12,0),r), ((0,0),(10,0))),
        (nicholl_lee_nicholl((-2,10),(12,10),r), ((0,10),(10,10))),
    ]:
        assert got[0] == pytest.approx(expected[0])
        assert got[1] == pytest.approx(expected[1])

def test_nicholl_lee_nicholl_boundary_start_outward_is_single_point():
    r=(0,0,10,10)
    assert nicholl_lee_nicholl((10,5),(12,5),r)==((10.0,5.0),(10.0,5.0))
    assert nicholl_lee_nicholl((5,10),(5,12),r)==((5.0,10.0),(5.0,10.0))


def test_nicholl_lee_nicholl_rejects_degenerate_window():
    with pytest.raises(ValueError):
        nicholl_lee_nicholl((0,0),(1,1),(0,0,0,1))
