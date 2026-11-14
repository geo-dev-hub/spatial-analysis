from fractions import Fraction

import pytest

from minkowski_sum import minkowski_sum


F = Fraction


def canonical(ring):
    """Rotate a ring to its lexicographically smallest vertex."""
    start = min(range(len(ring)), key=lambda i: (ring[i][0], ring[i][1]))
    return ring[start:] + ring[:start]


def test_rectangle_sum_from_compendium_exercise():
    p = [(0, 0), (4, 0), (4, 2), (0, 2)]
    q = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert minkowski_sum(p, q) == [
        (F(0), F(0)), (F(5), F(0)), (F(5), F(3)), (F(0), F(3))
    ]


def test_accepts_clockwise_input():
    p = [(0, 0), (0, 2), (4, 2), (4, 0)]
    q = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert minkowski_sum(p, q) == minkowski_sum(list(reversed(p)), q)


def test_commutativity_up_to_cyclic_start():
    p = [(0, 0), (3, 0), (2, 2), (0, 1)]
    q = [(0, 0), (2, 0), (1, 1)]
    assert canonical(minkowski_sum(p, q)) == canonical(minkowski_sum(q, p))


def test_point_translation():
    p = [(0, 0), (3, 0), (0, 2)]
    point = [(7, -4), (7, -4), (7, -4)]
    # A point is not a polygon under this API; translation is checked via a
    # small-area polygon whose vertices are all shifted by the same vector.
    q = [(7, -4), (8, -4), (7, -3)]
    result = minkowski_sum(p, q)
    shifted = [(x + 7, y - 4) for x, y in minkowski_sum(p, [(0, 0), (1, 0), (0, 1)])]
    assert result == shifted


def test_fractional_coordinates_are_exact():
    p = [(0, 0), ("1/2", 0), ("1/2", "1/2"), (0, "1/2")]
    q = [(0, 0), (1, 0), (1, 1), (0, 1)]
    result = minkowski_sum(p, q)
    assert result == [
        (F(0), F(0)), (F(3, 2), F(0)),
        (F(3, 2), F(3, 2)), (F(0), F(3, 2))
    ]


def test_redundant_collinear_vertices_are_removed():
    p = [(0, 0), (2, 0), (4, 0), (4, 2), (0, 2)]
    q = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert len(minkowski_sum(p, q)) == 4


def test_parallel_edges_are_merged():
    p = [(0, 0), (4, 0), (4, 2), (0, 2)]
    q = [(0, 0), (2, 0), (2, 3), (0, 3)]
    result = minkowski_sum(p, q)
    assert result == [
        (F(0), F(0)), (F(6), F(0)), (F(6), F(5)), (F(0), F(5))
    ]


@pytest.mark.parametrize("bad", [
    [(0, 0), (1, 1), (0, 1), (1, 0)],
    [(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (2, 0), (1, 0), (0, 2)],
])
def test_rejects_non_convex_or_degenerate_input(bad):
    with pytest.raises(ValueError):
        minkowski_sum(bad, [(0, 0), (1, 0), (0, 1)])


def test_rejects_self_crossing_star_with_consistent_local_turns():
    # A pentagram can have consistently signed local turns while crossing itself.
    star = [(0, 3), (2, -3), (-3, 1), (3, 1), (-2, -3)]
    with pytest.raises(ValueError, match="simple and convex"):
        minkowski_sum(star, [(0, 0), (1, 0), (0, 1)])


def test_closing_vertex_is_optional():
    p = [(0, 0), (2, 0), (0, 2), (0, 0)]
    q = [(0, 0), (1, 0), (0, 1)]
    assert minkowski_sum(p, q) == minkowski_sum(p[:-1], q)
