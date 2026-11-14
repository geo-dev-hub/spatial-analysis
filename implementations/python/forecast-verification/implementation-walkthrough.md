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


## 6. Fractions Skill Score on a grid

FSS is separate from the one-dimensional functions because it needs a spatial data contract. It accepts equally shaped rectangular numeric grids, a threshold, an odd square window size in cells and an explicit edge policy. Each cell becomes an event indicator using value >= threshold. At each evaluated centre, the implementation calculates forecast and observation event fractions and compares them using the FSS formula.

A summed-area table (integral image) makes each rectangular event-count query constant time after a single grid pass. The default truncate policy clips windows at the domain boundary and uses the smaller actual area. The valid policy excludes centres whose full window would extend beyond the grid. These choices change the evaluated population and must be reported.

A one-cell window reduces FSS to gridpoint comparison. Larger windows test agreement at broader neighbourhood scales, so a displaced feature can receive more credit. Window size is in cells, not metres: the same 5-by-5 window has different physical meaning on 1 km and 10 km grids. The implementation returns None when both thresholded fields contain no events because the denominator is zero.

The code cannot choose a scientifically meaningful threshold, projection, grid spacing, resampling method, mask or neighbourhood scale. Forecast and observation must refer to the same valid time and accumulation period. A scale curve across several neighbourhood sizes is often more informative than one selected value.


## CRPS decomposition by threshold integration

The CRPS has the threshold-integral identity

`CRPS(F,y) = ∫ BS_z dz`, where `BS_z` is the Brier score for the event `Y > z`.

At every threshold, an ensemble gives an event probability equal to the fraction of members exceeding that threshold. Grouping cases by forecast probability gives the Murphy decomposition:

`BS = REL - RES + UNC`

with reliability `Σ w_k(p_k-o_k)^2`, resolution `Σ w_k(o_k-ō)^2`, and uncertainty `ō(1-ō)`. Integrating these three terms over the threshold axis gives an additive CRPS decomposition.

The implementation uses finite trapezoidal quadrature and a fixed threshold grid. It is a clear approximation to the integral identity, not the exact ensemble-bin-width formula derived by Hersbach (2000). The quadrature residual is returned so the additive identity can be checked numerically.
