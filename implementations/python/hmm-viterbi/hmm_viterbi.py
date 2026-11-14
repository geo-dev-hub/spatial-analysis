from __future__ import annotations
from math import isfinite, log
from typing import Hashable, Sequence

def _prob_vector(values, name):
 row=tuple(float(x) for x in values)
 if not row or any(not isfinite(x) or x<0 for x in row): raise ValueError(name+' must contain finite non-negative probabilities')
 if abs(sum(row)-1.0)>1e-9: raise ValueError(name+' must sum to one')
 return row

def _prob_matrix(values, name):
 rows=tuple(_prob_vector(row,name+' row') for row in values)
 if not rows or len({len(row) for row in rows})!=1: raise ValueError(name+' must be a non-empty rectangular matrix')
 return rows

def viterbi_decode(observations:Sequence[Hashable], states:Sequence[Hashable], symbols:Sequence[Hashable], start_probabilities, transition_probabilities, emission_probabilities):
 """Decode a discrete HMM; return (best_state_path, joint_log_probability).

    Matrix row/column order follows the supplied `states` and `symbols`.
    Ties are resolved by the first state in `states` order. Zero probabilities
    are valid and map to negative infinity in log space.
    """
 states=tuple(states); symbols=tuple(symbols); observations=tuple(observations)
 if not states or len(set(states))!=len(states): raise ValueError('states must be non-empty and unique')
 if not symbols or len(set(symbols))!=len(symbols): raise ValueError('symbols must be non-empty and unique')
 start=_prob_vector(start_probabilities,'start probabilities')
 trans=_prob_matrix(transition_probabilities,'transition probabilities')
 emit=_prob_matrix(emission_probabilities,'emission probabilities')
 n,m=len(states),len(symbols)
 if len(start)!=n or len(trans)!=n or any(len(row)!=n for row in trans): raise ValueError('transition dimensions must match states')
 if len(emit)!=n or any(len(row)!=m for row in emit): raise ValueError('emission dimensions must match states and symbols')
 index={symbol:i for i,symbol in enumerate(symbols)}
 try: obs=[index[x] for x in observations]
 except KeyError as exc: raise ValueError('observation is not in the declared symbol alphabet') from exc
 if not obs: return [],0.0
 neg_inf=float('-inf')
 def lp(p): return log(p) if p>0 else neg_inf
 log_start=[lp(p) for p in start]
 log_trans=[[lp(p) for p in row] for row in trans]
 log_emit=[[lp(p) for p in row] for row in emit]
 score=[log_start[i]+log_emit[i][obs[0]] for i in range(n)]
 back=[]
 for symbol in obs[1:]:
  next_score=[]; parents=[]
  for j in range(n):
   candidates=[score[i]+log_trans[i][j] for i in range(n)]
   parent=max(range(n),key=lambda i:candidates[i])
   parents.append(parent); next_score.append(candidates[parent]+log_emit[j][symbol])
  back.append(parents); score=next_score
 last=max(range(n),key=lambda i:score[i]); best=score[last]
 if best==neg_inf: raise ValueError('observation sequence has zero probability under this model')
 path=[last]
 for parents in reversed(back): path.append(parents[path[-1]])
 path.reverse()
 return [states[i] for i in path],best
