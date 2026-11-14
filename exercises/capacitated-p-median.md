# Exercise: capacity changes the location decision

## Objective

Compare uncapacitated p-median assignment with a capacitated version. Explain why the cheapest assignment may be operationally impossible.

## Starter instance

\[
C=\begin{bmatrix}0&5&9\\1&4&8\\8&1&4\\9&0&3\end{bmatrix},
\quad q=[2,1,2,1],\quad u=[2,2,4].
\]

Rows are demand points; columns are candidate sites. Open exactly two facilities. Capacity and demand use the same unit.

## Tasks

1. Solve uncapacitated p-median with \(p=2\).
2. Solve the capacitated model with the supplied capacities.
3. Recalculate the load at each selected facility.
4. Reduce candidate 2's capacity from 4 to 2. Does the optimal pair change?
5. Reduce total available capacity below total demand. Explain infeasibility.
6. Change objective weights without changing demand quantities. Explain why cost changes but capacity load does not.
7. Discuss whether real demand zones can be split. If they can, explain what changes in the model.

## Validation checklist

- Every demand row is assigned exactly once.
- Every assignment points to an opened facility.
- Exactly two facilities are open.
- No selected facility exceeds capacity.
- The reported objective equals weighted assigned costs.
- Infeasible cases are reported rather than silently assigning overflow.
