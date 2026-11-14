import numpy as np
import pytest
from domain_classifier import domain_classifier_diagnostic


def test_identical_domains_are_hard_to_distinguish():
    rng = np.random.default_rng(11)
    source = rng.normal(size=(300, 3))
    target = rng.normal(size=(300, 3))
    result = domain_classifier_diagnostic(source, target, n_splits=5)
    assert 0.40 <= result["roc_auc"] <= 0.60
    assert result["splitter"] == "stratified_kfold"
    assert result["probabilities_target_domain"].shape == (600,)


def test_shifted_domains_are_distinguishable():
    rng = np.random.default_rng(12)
    source = rng.normal(loc=0, scale=1, size=(200, 2))
    target = rng.normal(loc=2.5, scale=1, size=(200, 2))
    result = domain_classifier_diagnostic(source, target, n_splits=4)
    assert result["roc_auc"] > 0.95
    assert result["balanced_accuracy"] > 0.90


def test_grouped_cv_uses_group_splitter():
    rng = np.random.default_rng(13)
    source = rng.normal(size=(100, 2))
    target = rng.normal(loc=.4, size=(100, 2))
    groups = np.repeat(np.arange(20), 10)
    result = domain_classifier_diagnostic(source, target, n_splits=5, groups=groups)
    assert result["splitter"] == "stratified_group_kfold"
    assert np.isfinite(result["roc_auc"])


@pytest.mark.parametrize("source,target", [
    (np.ones(10), np.ones((10, 1))),
    (np.ones((10, 2)), np.ones((10, 3))),
    (np.ones((1, 2)), np.ones((10, 2))),
    (np.full((10, 2), np.nan), np.ones((10, 2))),
])
def test_invalid_feature_arrays_rejected(source, target):
    with pytest.raises(ValueError):
        domain_classifier_diagnostic(source, target)


def test_invalid_fold_contract_rejected():
    with pytest.raises(ValueError):
        domain_classifier_diagnostic(np.ones((10, 2)), np.ones((10, 2)), n_splits=1)
    with pytest.raises(ValueError):
        domain_classifier_diagnostic(np.ones((10, 2)), np.ones((10, 2)), n_splits=11)


def test_group_array_contract_rejected():
    source = np.ones((10, 2))
    target = np.ones((10, 2))
    with pytest.raises(ValueError):
        domain_classifier_diagnostic(source, target, n_splits=2, groups=np.arange(10))
    with pytest.raises(ValueError):
        domain_classifier_diagnostic(source, target, n_splits=2, groups=[None] * 20)



@pytest.mark.parametrize("groups", [
    [None] * 20,
    [float("nan")] * 20,
    [[i] for i in range(20)],
])
def test_invalid_group_labels_rejected(groups):
    source = np.ones((10, 2))
    target = np.ones((10, 2))
    with pytest.raises(ValueError):
        domain_classifier_diagnostic(source, target, n_splits=2, groups=groups)
