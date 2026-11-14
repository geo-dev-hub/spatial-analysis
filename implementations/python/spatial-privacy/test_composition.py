import pytest
from composition import SequentialPrivacyAccountant


def test_pure_dp_releases_compose_by_summing_epsilon():
    accountant = SequentialPrivacyAccountant(1.0)
    accountant.add_release("first", 0.2)
    result = accountant.add_release("second", 0.35)
    assert result["composed_epsilon"] == pytest.approx(0.55)
    assert result["composed_delta"] == 0
    assert result["remaining_epsilon"] == pytest.approx(0.45)


def test_approximate_dp_composes_epsilon_and_delta_separately():
    accountant = SequentialPrivacyAccountant(2.0, 1e-5)
    accountant.add_release("a", 0.5, 2e-6)
    result = accountant.add_release("b", 0.4, 3e-6)
    assert result["composed_epsilon"] == pytest.approx(0.9)
    assert result["composed_delta"] == pytest.approx(5e-6)


def test_over_budget_release_is_rejected_transactionally():
    accountant = SequentialPrivacyAccountant(0.5, 1e-5)
    accountant.add_release("first", 0.4, 2e-6)
    before = accountant.summary()
    with pytest.raises(ValueError, match="exceeds"):
        accountant.add_release("too-large", 0.2, 1e-6)
    assert accountant.summary() == before
    assert len(accountant.releases) == 1


def test_duplicate_release_names_are_rejected_after_normalization():
    accountant = SequentialPrivacyAccountant(1)
    accountant.add_release("daily-count", 0.2)
    with pytest.raises(ValueError, match="unique"):
        accountant.add_release(" daily-count ", 0.1)


@pytest.mark.parametrize("eps,delta", [(0, 0), (-1, 0), (float("nan"), 0), (0.1, -0.1), (0.1, 1)])
def test_invalid_release_parameters_are_rejected(eps, delta):
    accountant = SequentialPrivacyAccountant(1, 0.5)
    with pytest.raises(ValueError):
        accountant.add_release("bad", eps, delta)


def test_invalid_budgets_are_rejected():
    with pytest.raises(ValueError):
        SequentialPrivacyAccountant(0)
    with pytest.raises(ValueError):
        SequentialPrivacyAccountant(1, 1)


def test_release_list_is_immutable_snapshot():
    accountant = SequentialPrivacyAccountant(1)
    accountant.add_release("one", 0.1)
    snapshot = accountant.releases
    accountant.add_release("two", 0.1)
    assert len(snapshot) == 1
    assert len(accountant.releases) == 2
