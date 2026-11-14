# Intern walkthrough: TOPSIS

## 1. Read the decision matrix

Each row is one alternative and each column is one criterion. The criteria must use the same definitions for every alternative. Record units and whether each criterion is a benefit or a cost.

## 2. Vector-normalise each criterion

For each column, divide each value by the square root of the sum of squared values in that column. A zero-norm column cannot be normalised and is rejected.

## 3. Apply criterion weights

The implementation validates a non-negative weight for every criterion and normalises the vector to sum to one. This is a mathematical normalisation, not a method for eliciting defensible weights.

## 4. Construct the ideals

For benefit criteria, the positive ideal is the maximum weighted-normalised value and the negative ideal is the minimum. For cost criteria the directions reverse.

## 5. Calculate distances and closeness

Compute Euclidean distance to both ideals, then divide distance to the negative ideal by the sum of the two distances. Higher closeness ranks better.

If all alternatives are identical, both distances are zero and the ratio is undefined. The code returns 0.5 as a neutral placeholder; treat this as a degenerate comparison, not evidence of a meaningful tie-break.

## 6. Inspect the ranking

Do not publish only the sorted list. Show the original criterion values, weights, normalisation, ideal points and sensitivity to alternative sets. An alternative can rank first while still performing poorly on a critical criterion.

## 7. Extension exercise

Add a second normalisation strategy behind an explicit parameter, test it against a hand-worked example, and compare how the ranking changes. Document that this is a different TOPSIS variant.
