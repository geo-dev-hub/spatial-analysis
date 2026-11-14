import unittest
from rasterization import bresenham_line, dda_line, scanline_polygon_fill, supercover_line, wu_line

class RasterizationTests(unittest.TestCase):
 def test_bresenham_octants(self):
  for end in [(5,2),(2,5),(-2,5),(-5,2),(-5,-2),(-2,-5),(2,-5),(5,-2)]:
   a=bresenham_line((0,0),end); self.assertEqual((a[0],a[-1]),((0,0),end)); self.assertEqual(set(a),set(bresenham_line(end,(0,0))))
 def test_bresenham_integer_contract(self):
  with self.assertRaises(ValueError): bresenham_line((0.5,0),(3,2))
 def test_dda_degenerate(self):
  self.assertEqual(dda_line((1,1),(1,1)),[(1,1)])
 def test_supercover_corner(self):
  self.assertEqual(set(supercover_line((0,0),(2,2))),{(0,0),(1,0),(0,1),(1,1),(2,1),(1,2),(2,2)})
 def test_wu_bounds(self):
  values=wu_line((0,0),(5,2)); self.assertTrue(values); self.assertTrue(all(0 < v <= 1 for v in values.values()))
 def test_scanline_square(self):
  self.assertEqual(len(scanline_polygon_fill([(0,0),(3,0),(3,3),(0,3)])),9)
 def test_scanline_triangle(self):
  self.assertEqual(len(scanline_polygon_fill([(0,0),(4,0),(0,4)])),6)
 def test_invalid_ring(self):
  with self.assertRaises(ValueError): scanline_polygon_fill([(0,0),(1,1)])

if __name__ == '__main__': unittest.main()
