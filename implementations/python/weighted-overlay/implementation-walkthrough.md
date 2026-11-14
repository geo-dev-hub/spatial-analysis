# How the weighted linear combination implementation works

This walkthrough explains the aggregation stage of a spatial weighted linear combination. The implementation expects the criterion layers to be prepared already; it does not hide the modelling decisions that come before the weighted sum.

## 1. Keep criterion preparation separate

Every input array must represent the same two-dimensional grid. Its finite values must be on a common [0, 1] preference scale, with larger values consistently representing greater preference.

A raw distance layer, for example, cannot be passed in metres and added directly to a slope layer in degrees. Choose a defensible value function first, including whether high or low raw values are preferred.

## 2. Check the names and weights

The criteria and weight mappings must contain exactly the same names. The code preserves the criterion mapping order when building its internal arrays.

Weights must be finite and non-negative, and their total must be positive. The function normalises them by their sum:

$$
\hat w_i=\frac{w_i}{\sum_j w_j}.
$$

This makes the inputs relative importance values. It does not make the judgements behind them objective.

## 3. Validate the raster contract

The function checks that every criterion is a non-empty two-dimensional array with the same shape. Finite values outside [0, 1] are rejected.

Non-finite values are treated as NoData. The implementation uses a strict common-footprint rule: if any criterion is missing at a cell, that cell is not scored.

## 4. Apply eligibility constraints

An optional Boolean mask identifies alternatives that are allowed to participate. A False value excludes the cell and the output is NaN there.

This keeps hard exclusions separate from compensatory factors. Do not encode a non-negotiable constraint as an ordinary low-scoring factor.

## 5. Calculate the weighted sum

For each valid cell, the implementation accumulates:

$$
S(a)=\sum_i \hat w_i x_i(a).
$$

The output remains between zero and one because it is a convex combination of inputs that are already between zero and one.

## 6. Reproduce the tests

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The tests cover weight normalisation, zero-weight criteria, constraints, NoData, invalid scores, shape mismatches, mask types and bounded output.

## 7. What the code cannot decide

The code cannot tell you whether the criteria are appropriate, whether two criteria double-count the same underlying phenomenon, whether the weights reflect affected stakeholders, whether the score is validated or whether WLC's compensation assumption is acceptable.

Those questions belong in the decision model and its evidence record. A technically correct weighted sum can still support a poor decision if those choices are not defensible.
