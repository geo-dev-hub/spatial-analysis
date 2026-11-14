# Forecast verification teaching package

A dependency-free baseline for binary-event forecast verification.

Implemented:
- contingency-table construction (hits, misses, false alarms, correct negatives);
- probability of detection (POD), false alarm ratio (FAR), false-positive rate, critical success index (CSI) and equitable threat score (ETS);
- Brier score and Brier skill score against an explicitly supplied reference forecast;
- reliability-bin summaries with empty bins retained;
- empirical ROC AUC using average ranks for tied scores.

Run tests from this directory:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Contract and interpretation

Observations and deterministic forecasts are binary 0/1 values (booleans are accepted). Probability forecasts must be finite and lie in [0, 1]. ROC scores may be any finite ranking score and need not be probabilities. Paired arrays must have equal lengths.

Undefined ratios return `None`, not zero. ROC AUC returns `None` if either observed class is absent. Reliability bins use caller-specified edges from exactly 0 to 1; bins are left-closed/right-open except the final bin, which includes 1. Empty bins remain visible with null means.

## Explicit limits

This package does not implement CRPS, ensemble rank histograms, Fractions Skill Score, SAL or MODE. It does not handle multi-category events, censoring, missing-value masks, spatial neighbourhoods, temporal dependence, confidence intervals or forecast-threshold selection. The scores are not a complete verification report: stratification, sample sizes, uncertainty and a defensible held-out design remain the analyst's responsibility.

These are transparent teaching implementations, not a substitute for a domain-validated operational verification system.
