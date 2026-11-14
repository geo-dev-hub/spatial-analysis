import math, unittest
from hmm_viterbi import viterbi_decode
class ViterbiTests(unittest.TestCase):
 def setUp(self):
  self.states=('Rainy','Sunny'); self.symbols=('walk','shop','clean')
  self.start=(0.6,0.4); self.trans=((0.7,0.3),(0.4,0.6)); self.emit=((0.1,0.4,0.5),(0.6,0.3,0.1))
 def test_classic_sequence(self):
  path,score=viterbi_decode(('walk','shop','clean'),self.states,self.symbols,self.start,self.trans,self.emit)
  self.assertEqual(path,['Sunny','Rainy','Rainy']); self.assertTrue(math.isfinite(score))
 def test_empty_sequence(self):
  self.assertEqual(viterbi_decode((),self.states,self.symbols,self.start,self.trans,self.emit),([],0.0))
 def test_zero_probability_sequence_rejected(self):
  with self.assertRaises(ValueError): viterbi_decode(('clean',),self.states,self.symbols,(1,0),self.trans,((1,0,0),(1,0,0)))
 def test_unknown_symbol(self):
  with self.assertRaises(ValueError): viterbi_decode(('unknown',),self.states,self.symbols,self.start,self.trans,self.emit)
 def test_bad_probability_sum(self):
  with self.assertRaises(ValueError): viterbi_decode(('walk',),self.states,self.symbols,(0.2,0.2),self.trans,self.emit)
 def test_dimension_mismatch(self):
  with self.assertRaises(ValueError): viterbi_decode(('walk',),self.states,self.symbols,self.start,((1,0),),self.emit)
 def test_tie_breaks_by_state_order(self):
  path,_=viterbi_decode(('x',),('first','second'),('x',),(0.5,0.5),((0.5,0.5),(0.5,0.5)),((1.0,),(1.0,)))
  self.assertEqual(path,['first'])
if __name__=='__main__':unittest.main()
