from fractions import Fraction
import random
import pytest
from bentley_ottmann import Segment,bentley_ottmann
from bentley_ottmann_treap import bentley_ottmann_treap
from segment_intersection import segment_intersection

def pairs(results):return {(a,b) for a,b,_ in results}
def oracle(ss):
 out=set()
 for i,a in enumerate(ss):
  for b in ss[i+1:]:
   r=segment_intersection(a.a,a.b,b.a,b.b)
   if r.kind=='point':out.add(tuple(sorted((a.id,b.id))))
 return out

def test_one_exact_crossing():
 ss=[Segment(1,(0,0),(6,6)),Segment(2,(0,6),(6,0))]
 assert bentley_ottmann_treap(ss)==bentley_ottmann(ss)==[(1,2,(Fraction(3),Fraction(3)))]

def test_multiple_crossings():
 ss=[Segment(1,(0,0),(10,10)),Segment(2,(0,8),(10,2)),Segment(3,(2,10),(8,2)),Segment(4,(3,5),(9,10))]
 assert pairs(bentley_ottmann_treap(ss))==oracle(ss)

def test_rational_crossing_exact():
 ss=[Segment(1,(0,0),(3,3)),Segment(2,(0,2),(3,0))]
 assert bentley_ottmann_treap(ss)==[(1,2,(Fraction(6,5),Fraction(6,5)))]

def test_changing_status():
 ss=[Segment(1,(0,0),(12,10)),Segment(2,(1,9),(11,0)),Segment(3,(2,4),(10,8)),Segment(4,(3,10),(9,2))]
 assert pairs(bentley_ottmann_treap(ss))==oracle(ss)

def test_seeded_random_differential():
 rng=random.Random(20261113); checked=0
 for _ in range(500):
  xs=list(range(16)); rng.shuffle(xs); ss=[]
  for sid in range(8):
   x1,x2=sorted((xs[2*sid],xs[2*sid+1])); y1,y2=rng.sample(range(-30,31),2); ss.append(Segment(sid,(x1,y1),(x2,y2)))
  hits=[]; valid=True; endpoint_x={p[0] for s in ss for p in (s.a,s.b)}
  for i,a in enumerate(ss):
   for b in ss[i+1:]:
    r=segment_intersection(a.a,a.b,b.a,b.b)
    if r.kind=='overlap':valid=False
    elif r.kind=='point':
     if r.geometry[0] in endpoint_x:valid=False
     hits.append(r.geometry)
  if not valid or len({p[0] for p in hits})!=len(hits):continue
  expected=oracle(ss)
  assert pairs(bentley_ottmann_treap(ss))==expected
  assert pairs(bentley_ottmann(ss))==expected
  checked+=1
 assert checked>=10

def test_rejects_vertical_and_duplicate_ids():
 with pytest.raises(ValueError,match='Vertical'):Segment(1,(2,0),(2,4))
 with pytest.raises(ValueError,match='unique'):
  bentley_ottmann_treap([Segment(1,(0,0),(4,2)),Segment(1,(0,4),(4,0))])
