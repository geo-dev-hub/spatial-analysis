# Weights of evidence in Python

This package estimates positive and negative weights for binary spatial evidence themes and combines them in log-odds space. It is a NumPy teaching baseline for the Bayesian weights-of-evidence model.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from weights_of_evidence import weights_of_evidence

    known_deposits = np.array([[1, 1, 0, 0], [1, 0, 0, 0]])
    evidence = {
        "fault_buffer": np.array([[1, 1, 1, 0], [1, 0, 0, 0]]),
        "favourable_lithology": np.array([[1, 1, 0, 0], [0, 0, 1, 0]]),
    }

    result = weights_of_evidence(known_deposits, evidence, pseudocount=0.5)
    print(result.prior_probability)
    for item in result.weights:
        print(item.name, item.positive, item.negative, item.contrast)
    print(result.probability)

## Input contract

- Event labels and evidence layers are aligned, non-empty 2D arrays containing only 0, 1 or non-finite NoData.
- 1 means event/evidence present; 0 means absent.
- An optional study_area is a Boolean mask. Cells outside it are not used for estimating weights or scoring.
- A cell is scored only when the event and every evidence layer are finite. This complete-case rule is deliberately strict.
- Weights are estimated from the same labelled cells used to calculate the prior. Use independent spatial validation before interpreting a predictive map.
- pseudocount=0.5 is the default additive smoothing. Report it; it changes the estimates. With zero smoothing, zero contingency counts are rejected.

## Important limitations

The additive evidence model assumes conditional independence of evidence themes given event presence and given event absence. This package does not test that assumption, correct biased exploration effort, derive binary thresholds, resample spatial layers or perform spatial cross-validation. It is not a production prospectivity system and should not be used to claim calibrated discovery probabilities without further validation.

See the [method lesson](../../../methods/weights-of-evidence.md) and [intern walkthrough](implementation-walkthrough.md).
