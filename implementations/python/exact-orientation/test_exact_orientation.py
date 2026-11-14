from fractions import Fraction
import math
import pytest

from exact_orientation import orientation_sign


def test_known_turn_directions():
    a, b = (0, 0), (1, 0)
    assert orientation_sign(a, b, (0, 1)) == 1
    assert orientation_sign(a, b, (0, -1)) == -1
    assert orientation_sign(a, b, (2, 0)) == 0


def test_exact_large_integer_coordinates():
    base = 10**30
    assert orientation_sign((base, base), (base + 2, base + 2),
                            (base + 4, base + 5)) == 1


def test_fraction_inputs_remain_exact():
    assert orientation_sign((Fraction(0), Fraction(0)),
                            (Fraction(1, 3), Fraction(1, 3)),
                            (Fraction(2, 3), Fraction(2, 3) + Fraction(1, 10**30))) == 1


def test_float_inputs_use_exact_represented_values():
    a = (5528636682.011507, -1595419105.704565)
    b = (3096585648.789674, 6380875131.612917)
    c = (4421959453.453243, 2034103087.7611067)
    assert orientation_sign(a, b, c) == -1
    naive = ((b[0]-a[0])*(c[1]-a[1])
             - (b[1]-a[1])*(c[0]-a[0]))
    assert naive == 0.0


def test_translation_invariance_for_integer_coordinates():
    a, b, c = (1, 2), (7, 5), (4, 9)
    shift = (10**20, -(10**20))
    moved = tuple((p[0] + shift[0], p[1] + shift[1]) for p in (a, b, c))
    assert orientation_sign(a, b, c) == orientation_sign(*moved)


def test_swapping_two_points_reverses_sign():
    a, b, c = (2, 3), (8, 4), (5, 10)
    assert orientation_sign(a, b, c) == -orientation_sign(b, a, c)


def test_rejects_bad_points_and_nonfinite_values():
    with pytest.raises(ValueError, match="exactly two"):
        orientation_sign((0, 0, 0), (1, 1), (2, 2))
    with pytest.raises(ValueError, match="finite"):
        orientation_sign((0, 0), (1, 1), (math.inf, 2))
    with pytest.raises(TypeError, match="real numbers"):
        orientation_sign((0, 0), (1, 1), ("x", 2))
