# Forecast verification: implementation walkthrough

## 1. Start with paired cases

A verification sample consists of observations and forecasts for the same valid cases. The package refuses unequal lengths and empty samples. It accepts booleans or integer 0/1 values and builds the four contingency counts.

## 2. Derive categorical scores from counts

POD, FAR, false-positive rate and CSI are ratios with different denominators. FAR is not the false-positive rate: FAR conditions on forecast events, while false-positive rate conditions on observed non-events. ETS first estimates random hits from the table's row and column totals and subtracts them from the observed hits.

When a denominator is zero, the corresponding statistic is undefined. Returning zero would incorrectly suggest a measured score of zero, so this implementation returns None.

## 3. Evaluate probability forecasts

The Brier score averages squared probability error. Brier skill compares it with a reference forecast on exactly the same observations. A zero reference score makes the skill ratio undefined.

Reliability bins report the mean forecast probability and observed event frequency in each caller-defined probability interval. Empty bins remain in the result: silently dropping them can make a reliability plot look better supported than it is.

## 4. Evaluate ranking with ROC AUC

ROC AUC is calculated using the Mann–Whitney rank identity. Average ranks are assigned to tied scores, so ties contribute half credit. The function accepts arbitrary finite scores; they need not be calibrated probabilities. AUC is undefined if the sample contains only one observed class.

## 5. What remains outside the package

CRPS, ensemble rank histograms, neighbourhood FSS, SAL and MODE need separate data contracts and validation. In particular, spatial neighbourhood metrics must declare grid geometry, physical scale, thresholds and edge treatment. They should not be hidden inside a generic one-dimensional metric function.
