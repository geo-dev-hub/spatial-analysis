from fractions import Fraction
import random
import pytest
from bentley_ottmann import Segment, bentley_ottmann
from segment_intersection import segment_intersection

def pairs(results):
    return {(a,b) for a,b,_ in results}

def oracle(segments):
    out=set()
    for i,a in enumerate(segments):
        for b in segments[i+1:]:
            r=segment_intersection(a.a,a.b,b.a,b.b)
            if r.kind=="point":
                out.add(tuple(sorted((a.id,b.id))))
    return out

def test_exact_single_crossing():
    assert bentley_ottmann([Segment(1,(0,0),(6,6)),Segment(2,(0,6),(6,0))]) == [
        (1,2,(Fraction(3),Fraction(3)))
    ]

def test_multiple_crossings_against_oracle():
    ss=[Segment(1,(0,0),(10,10)),Segment(2,(0,8),(10,2)),
        Segment(3,(2,10),(8,2)),Segment(4,(3,5),(9,10))]
    assert pairs(bentley_ottmann(ss)) == oracle(ss)

def test_rational_intersection_coordinates_are_exact():
    ss=[Segment(1,(0,0),(3,3)),Segment(2,(0,2),(3,0))]
    assert bentley_ottmann(ss)==[(1,2,(Fraction(6,5),Fraction(6,5)))]

def test_no_intersections():
    assert bentley_ottmann([Segment(1,(0,0),(4,0)),Segment(2,(0,3),(4,3))]) == []

def test_changing_status_against_oracle():
    ss=[Segment(1,(0,0),(12,10)),Segment(2,(1,9),(11,0)),
        Segment(3,(2,4),(10,8)),Segment(4,(3,10),(9,2))]
    assert pairs(bentley_ottmann(ss)) == oracle(ss)

def test_rejects_vertical():
    with pytest.raises(ValueError,match="Vertical"):
        Segment(1,(2,0),(2,5))

def test_rejects_shared_endpoints():
    with pytest.raises(ValueError,match="Shared endpoints"):
        bentley_ottmann([Segment(1,(0,0),(4,2)),Segment(2,(0,0),(4,4))])

def test_rejects_duplicate_ids():
    with pytest.raises(ValueError,match="unique"):
        bentley_ottmann([Segment(1,(0,0),(4,2)),Segment(1,(0,4),(4,0))])

def test_seeded_random_cases_against_oracle():
    rng=random.Random(20261113); checked=0
    for _ in range(300):
        xs=list(range(16)); rng.shuffle(xs); ss=[]
        for sid in range(8):
            x1,x2=sorted((xs[2*sid],xs[2*sid+1]))
            y1,y2=rng.sample(range(-30,31),2)
            ss.append(Segment(sid,(x1,y1),(x2,y2)))
        hits=[]; valid=True
        all_endpoint_x={p[0] for s in ss for p in (s.a,s.b)}
        for i,a in enumerate(ss):
            for b in ss[i+1:]:
                r=segment_intersection(a.a,a.b,b.a,b.b)
                if r.kind=="overlap": valid=False
                elif r.kind=="point":
                    p=r.geometry
                    if p[0] in all_endpoint_x: valid=False
                    hits.append(p)
        if not valid or len({p[0] for p in hits}) != len(hits): continue
        assert pairs(bentley_ottmann(ss)) == oracle(ss)
        checked += 1
    assert checked >= 10
