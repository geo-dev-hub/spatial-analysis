import unittest
from line_clipping import cohen_sutherland, liang_barsky, cyrus_beck
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
