"""Exact 2D orientation sign using rational arithmetic as a reference predicate."""
from __future__ import annotations

from fractions import Fraction
from numbers import Rational, Real
from typing import Iterable


def _as_fraction(value: Real) -> Fraction:
    if isinstance(value, bool):
        raise TypeError("Boolean values are not coordinates.")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, Rational):
        return Fraction(value)
    if isinstance(value, float):
        if not __import__("math").isfinite(value):
            raise ValueError("Coordinates must be finite.")
        return Fraction.from_float(value)
    if isinstance(value, Real):
        converted = float(value)
        if not __import__("math").isfinite(converted):
            raise ValueError("Coordinates must be finite.")
        return Fraction.from_float(converted)
    raise TypeError("Coordinates must be real numbers.")


def orientation_sign(a: Iterable[Real], b: Iterable[Real],
                     c: Iterable[Real]) -> int:
    """Return +1 for counter-clockwise, -1 for clockwise, 0 for collinear.

    Integer and Fraction inputs are represented exactly. Float inputs are
    interpreted as their exact binary floating-point values. This is a
    correctness-oriented reference implementation, not an adaptive fast filter.
    """
    points = []
    for point in (a, b, c):
        values = tuple(point)
        if len(values) != 2:
            raise ValueError("Each point must contain exactly two coordinates.")
        points.append((_as_fraction(values[0]), _as_fraction(values[1])))

    (ax, ay), (bx, by), (cx, cy) = points
    determinant = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    return (determinant > 0) - (determinant < 0)
