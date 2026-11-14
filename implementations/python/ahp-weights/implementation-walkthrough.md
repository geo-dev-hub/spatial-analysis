# Intern walkthrough: deriving AHP priority weights

## Goal

Turn a pairwise-comparison matrix into relative priorities, then inspect—not blindly accept—the consistency diagnostic.

## 1. Install and run

From this directory:

    python -m pip install numpy pytest
    python -m pytest -q

## 2. Read the matrix

Rows and columns use the same criterion order. An entry a_ij=3 means the row criterion is judged three times as important as the column criterion under the elicited scale. The reciprocal entry must be a_ji=1/3; every diagonal entry is one.

The matrix records human judgement. Do not reverse-engineer values merely to obtain a desired ranking.

## 3. Validate the contract

The function rejects non-square, empty, non-finite, zero/negative, non-unit-diagonal and non-reciprocal matrices. These checks catch structural mistakes, not bad reasoning.

## 4. Find the principal eigenvector

The code calls NumPy's eigensolver, selects the eigenvalue with the largest real part, and takes its corresponding right eigenvector. Eigenvectors have arbitrary scale and sign, so the implementation orients the vector to have a positive sum and normalises it to sum to one.

## 5. Inspect consistency

It computes CI=(lambda_max-n)/(n-1), then divides by the conventional random index when available. The result is None for one or two criteria. A low CR does not prove the hierarchy is valid, criteria are independent, or the panel represents affected people.

## 6. Connect weights to a spatial decision

Before passing weights to WLC, ensure that:
- each raster criterion is standardised so larger means more preferred;
- grids, extents, resolution and coordinate systems are aligned;
- missing-data policy is explicit;
- hard exclusions are handled separately;
- the decision rule's compensation assumptions are acceptable.

## 7. Tests to study

The tests cover a perfectly consistent matrix with known weights, a worked inconsistent matrix, one- and two-criterion diagnostics, invalid matrix contracts and criterion-name validation.

## 8. Extension exercise

Ask a second person to make pairwise judgements independently. Compare the resulting weights and rankings. Do not average matrices without documenting the group aggregation rule. Report disagreement and test whether the final spatial pattern changes under each plausible set of weights.
