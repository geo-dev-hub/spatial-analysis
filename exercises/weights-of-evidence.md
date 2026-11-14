# Exercise: calculate and question weights of evidence

## Part A — calculate one evidence weight by hand

A study area contains 100 valid cells. Twenty cells contain known occurrences. One evidence theme is present in 15 occurrence cells and 20 non-occurrence cells.

1. Fill the 2-by-2 contingency table.
2. Calculate \(P(B\mid D)\) and \(P(B\mid\neg D)\).
3. Calculate \(W^+\).
4. Calculate \(W^-\) using the absence probabilities.
5. Calculate the prior odds and the posterior odds for a cell where the evidence is present.
6. Convert the posterior odds to a probability.

Check your arithmetic against the worked calculation in [the method lesson](../methods/weights-of-evidence.md#8-worked-calculation).

## Part B — inspect the implementation

Run the tests in [the Python package](../implementations/python/weights-of-evidence/README.md). Identify which tests cover zero counts, NoData and study-area masks.

## Part C — challenge the model

Imagine that the evidence layers are distance to mapped faults and fault density.

- Why might these layers violate conditional independence?
- What happens if both are added to the same model?
- Why is an unrecorded occurrence not necessarily a true absence?
- What spatial validation design would reduce leakage between training and validation data?

Write a short note distinguishing a model score, a posterior probability under assumptions and a calibrated prediction.
