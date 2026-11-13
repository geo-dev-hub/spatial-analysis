# Intern walkthrough: a weights-of-evidence model

## Goal

Estimate how the presence and absence of binary evidence themes are associated with known event locations, then combine those contributions as posterior log odds.

This is a statistical model, not a drawing operation. The counts, study-area definition and occurrence data determine the result.

## 1. Install and run the tests

From this directory:

    python -m pip install numpy pytest
    python -m pytest -q

Read the tests before changing the implementation. They show the expected behaviour for zero counts, missing cells, masks and invalid inputs.

## 2. Prepare the spatial data before calling Python

For a real raster workflow, first ensure all layers share the same CRS, grid origin, resolution, dimensions and study-area extent. Create binary evidence themes using documented thresholds or classification rules. Keep the original continuous layers so the classification can be audited.

The event raster should distinguish known event cells (1), known non-event cells (0) and unknown cells (NoData). Do not label every unrecorded cell as a confirmed absence if the survey or reporting process was incomplete.

## 3. Understand the 2-by-2 table

For each evidence theme, the implementation counts:

- \(n_{11}\): event present, evidence present;
- \(n_{10}\): event present, evidence absent;
- \(n_{01}\): event absent, evidence present;
- \(n_{00}\): event absent, evidence absent.

From these counts it estimates conditional probabilities and takes log ratios to obtain \(W^+\) and \(W^-\). The contrast is \(C=W^+-W^-\).

## 4. Follow the computation

1. Validate that event and evidence arrays are non-empty, two-dimensional and binary apart from NoData.
2. Build one complete-case validity mask across the event and every evidence layer.
3. Apply the optional Boolean study-area mask.
4. Estimate prior event prevalence from valid cells.
5. Count the four combinations for each evidence theme.
6. Apply the declared pseudocount and calculate positive and negative log weights.
7. For each valid cell, add the appropriate weight for each evidence theme to the prior log odds.
8. Convert the combined log odds to a probability using the logistic function.

The strict complete-case rule is intentional: it avoids comparing cells whose scores were built from different subsets of evidence. It can, however, reduce coverage when layers have substantial NoData.

## 5. Why the pseudocount matters

When a count is zero, an unsmoothed conditional probability can be zero, which makes a log weight infinite. The default pseudocount of 0.5 prevents this numerical singularity. It also changes the estimated probabilities, particularly for small samples. Record it and test sensitivity to alternatives.

## 6. Interpret the conditional-independence assumption

The WofE model adds evidence weights under its specialised conditional-independence assumption with respect to the target-event occurrence pattern. This is not justified merely because layers have different names. Fault proximity and fault density, for example, may be strongly related. If dependent evidence is added as if independent, the model may overstate support.

Use domain knowledge, exploratory analysis and an appropriate conditional-independence test. A simple pairwise correlation check is only a screening step. Validate predictions on spatially independent occurrences.

## 7. Study the outputs

The result prior_probability is the event prevalence in the valid study cells. Each item in result.weights reports positive weight, negative weight, contrast and all four counts. result.log_odds and result.probability are 2D arrays; cells outside the valid mask are NaN.

The probability is conditional on the fitted model and its assumptions. It is not automatically calibrated, causal or a guarantee of discovery.

## 8. Extension exercise

Create two evidence layers with deliberately overlapping patterns. Compare the resulting weights and posterior map with a model that uses only one of them. Explain why adding a correlated layer can exaggerate confidence.

Then change one evidence threshold and repeat the calculation. Record how the counts, weights and map change. Do not choose the threshold only because it produces the most attractive map.
