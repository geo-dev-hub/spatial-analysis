"""Basic sequential composition accountant for differential privacy releases."""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class PrivacyRelease:
    name: str
    epsilon: float
    delta: float


class SequentialPrivacyAccountant:
    """Track basic sequential composition against a declared (epsilon, delta) budget.

    Uses the basic theorem only: epsilons and deltas add. It does not implement
    advanced composition or Rényi DP conversion.
    """
    def __init__(self, epsilon_budget: float, delta_budget: float = 0.0):
        self.epsilon_budget = self._positive(epsilon_budget, "epsilon_budget")
        self.delta_budget = self._delta(delta_budget)
        self._releases: list[PrivacyRelease] = []

    @staticmethod
    def _positive(value, name):
        value = float(value)
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be finite and positive")
        return value

    @staticmethod
    def _delta(value):
        value = float(value)
        if not math.isfinite(value) or value < 0 or value >= 1:
            raise ValueError("delta must be finite and in [0, 1)")
        return value

    @property
    def composed_epsilon(self):
        return sum(item.epsilon for item in self._releases)

    @property
    def composed_delta(self):
        return sum(item.delta for item in self._releases)

    @property
    def remaining_epsilon(self):
        return self.epsilon_budget - self.composed_epsilon

    @property
    def remaining_delta(self):
        return self.delta_budget - self.composed_delta

    @property
    def releases(self):
        return tuple(self._releases)

    def add_release(self, name: str, epsilon: float, delta: float = 0.0):
        """Record one release, or reject it without changing state if over budget."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("release name must be a non-empty string")
        normalized_name = name.strip()
        if any(item.name == normalized_name for item in self._releases):
            raise ValueError("release names must be unique")
        eps = self._positive(epsilon, "epsilon")
        delt = self._delta(delta)
        next_eps = self.composed_epsilon + eps
        next_delta = self.composed_delta + delt
        tolerance = 1e-12
        if next_eps > self.epsilon_budget + tolerance or next_delta > self.delta_budget + tolerance:
            raise ValueError("release exceeds the remaining sequential privacy budget")
        self._releases.append(PrivacyRelease(normalized_name, eps, delt))
        return self.summary()

    def summary(self):
        return {
            "epsilon_budget": self.epsilon_budget,
            "delta_budget": self.delta_budget,
            "composed_epsilon": self.composed_epsilon,
            "composed_delta": self.composed_delta,
            "remaining_epsilon": self.remaining_epsilon,
            "remaining_delta": self.remaining_delta,
            "release_count": len(self._releases),
            "composition": "basic_sequential_addition",
        }
