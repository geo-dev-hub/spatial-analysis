"""Cross-validated domain-classifier diagnostic for source/target covariate shift."""
from __future__ import annotations
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def domain_classifier_diagnostic(source_features, target_features, *, n_splits=5,
                                 groups=None, random_state=0, max_iter=1000):
    """Estimate how distinguishable source and target covariates are.

    Fits a leakage-safe StandardScaler + logistic-regression pipeline and
    obtains out-of-fold target-domain probabilities. If groups are supplied,
    StratifiedGroupKFold keeps each group wholly in one fold; otherwise
    ordinary stratified folds are used and spatial dependence must be handled
    by the caller before interpreting inferentially.

    AUC near 0.5 indicates weak discrimination under this classifier and
    feature representation; larger AUC indicates greater distinguishability.
    This is a diagnostic, not a calibrated two-sample p-value or proof of
    covariate shift. It cannot detect concept shift from X alone.
    """
    source = np.asarray(source_features, dtype=float)
    target = np.asarray(target_features, dtype=float)
    if source.ndim != 2 or target.ndim != 2 or source.shape[1] == 0 or source.shape[1] != target.shape[1]:
        raise ValueError("source and target must be 2D arrays with the same non-zero feature count")
    if source.shape[0] < 2 or target.shape[0] < 2:
        raise ValueError("source and target each need at least two observations")
    if not np.all(np.isfinite(source)) or not np.all(np.isfinite(target)):
        raise ValueError("features must be finite; impute or remove missing values first")
    if isinstance(n_splits, bool) or not isinstance(n_splits, (int, np.integer)) or n_splits < 2:
        raise ValueError("n_splits must be an integer of at least 2")
    if isinstance(max_iter, bool) or not isinstance(max_iter, (int, np.integer)) or max_iter < 1:
        raise ValueError("max_iter must be a positive integer")
    if min(len(source), len(target)) < n_splits:
        raise ValueError("each domain must have at least n_splits observations")

    X = np.vstack((source, target))
    y = np.concatenate((np.zeros(len(source), dtype=int), np.ones(len(target), dtype=int)))
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=int(max_iter)))
    if groups is None:
        splitter = StratifiedKFold(n_splits=int(n_splits), shuffle=True, random_state=int(random_state))
        probabilities = cross_val_predict(model, X, y, cv=splitter, method="predict_proba")[:, 1]
        split_kind = "stratified_kfold"
    else:
        group_labels = np.asarray(groups, dtype=object)
        if group_labels.ndim != 1 or len(group_labels) != len(X):
            raise ValueError("groups must have one label per pooled source and target observation")
        if any(value is None for value in group_labels):
            raise ValueError("groups cannot contain missing labels")
        if len(set(group_labels.tolist())) < n_splits:
            raise ValueError("groups must contain at least n_splits distinct labels")
        splitter = StratifiedGroupKFold(n_splits=int(n_splits), shuffle=True, random_state=int(random_state))
        probabilities = cross_val_predict(
            model, X, y, cv=splitter, groups=group_labels, method="predict_proba"
        )[:, 1]
        split_kind = "stratified_group_kfold"

    predicted = probabilities >= 0.5
    return {
        "roc_auc": float(roc_auc_score(y, probabilities)),
        "balanced_accuracy": float(balanced_accuracy_score(y, predicted)),
        "probabilities_target_domain": probabilities,
        "domain_labels": y,
        "splitter": split_kind,
        "n_source": int(len(source)),
        "n_target": int(len(target)),
        "n_features": int(source.shape[1]),
        "interpretation": "higher_auc_means_more_distinguishable_domains",
    }
