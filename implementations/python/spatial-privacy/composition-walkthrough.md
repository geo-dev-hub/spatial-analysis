# Sequential differential-privacy composition: walkthrough

A privacy guarantee applies to a release, not just to a single function call. Releasing several outputs about the same protected population consumes a cumulative budget.

## Basic sequential composition

If release i is (epsilon_i, delta_i)-differentially private, the basic sequential composition theorem gives:

\[
\epsilon_{\mathrm{total}}=\sum_i\epsilon_i,\qquad
\delta_{\mathrm{total}}=\sum_i\delta_i.
\]

For pure differential privacy, every delta is zero and only epsilon accumulates. This is deliberately the basic theorem; it is simple and conservative relative to some advanced accountants.

## Implementation

SequentialPrivacyAccountant stores named releases, computes cumulative and remaining budgets, rejects duplicate names and validates parameters. A proposed release that exceeds either budget is rejected before state changes. This transactional behaviour prevents a failed reservation from silently consuming budget.

## What it does not do

- It does not implement advanced composition, Rényi DP, privacy-loss distributions or subsampling amplification.
- It does not determine whether a mechanism is actually differentially private. Its inputs must come from a correct mechanism analysis.
- It does not solve identity linkage, contribution bounding, overlapping populations, adaptive query design or distributed accounting.
- The budget is a policy chosen by the data controller, not a universal safe threshold.
- A ledger must be durably stored and access-controlled in a production system; this in-memory teaching class is not a central privacy service.

## Reproduce

Run the package test suite with python -m pytest -q.
