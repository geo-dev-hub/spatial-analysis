import unittest
from curves_smoothing import chaikin, catmull_rom, bezier_curve

class CurveTests(unittest.TestCase):
    def test_chaikin_open_preserves_endpoints_and_doubles_segments(self):
        p=[(0,0),(2,2),(4,0)]
        out=chaikin(p)
        self.assertEqual(out[0],(0.0,0.0)); self.assertEqual(out[-1],(4.0,0.0))
        self.assertEqual(len(out),6)
    def test_chaikin_closed_wraps_without_duplicate_endpoint(self):
        p=[(0,0),(2,0),(1,2)]
        out=chaikin(p,closed=True)
        self.assertEqual(len(out),6)
        self.assertNotEqual(out[0],out[-1])
    def test_chaikin_zero_iterations(self):
        self.assertEqual(chaikin([(0,0),(1,1)],0),[(0.0,0.0),(1.0,1.0)])
    def test_catmull_rom_interpolates_controls(self):
        p=[(0,0),(1,2),(3,1),(4,3)]
        out=catmull_rom(p, samples_per_segment=8)
        self.assertEqual(out[0],p[0]); self.assertEqual(out[-1],p[-1])
        for q in p[1:-1]: self.assertIn(q,out)
        self.assertEqual(len(out),(len(p)-1)*8+1)
    def test_catmull_rom_rejects_duplicate_and_invalid_alpha(self):
        with self.assertRaises(ValueError): catmull_rom([(0,0),(0,0),(1,1)])
        with self.assertRaises(ValueError): catmull_rom([(0,0),(1,1)],alpha=1.5)
    def test_bezier_endpoints_and_linear_case(self):
        p=[(0,0),(2,2),(4,0)]
        out=bezier_curve(p,5)
        self.assertEqual(out[0],(0.0,0.0)); self.assertEqual(out[-1],(4.0,0.0))
        self.assertEqual(out[2],(2.0,1.0))
    def test_bezier_two_controls_is_linear(self):
        out=bezier_curve([(0,0),(4,2)],3)
        self.assertEqual(out,[(0.0,0.0),(2.0,1.0),(4.0,2.0)])
    def test_validation(self):
        with self.assertRaises(ValueError): chaikin([(0,0)],1)
        with self.assertRaises(ValueError): chaikin([(0,0),(1,1)],-1)
        with self.assertRaises(ValueError): bezier_curve([(0,0),(1,1)],1)

if __name__=="__main__": unittest.main()
