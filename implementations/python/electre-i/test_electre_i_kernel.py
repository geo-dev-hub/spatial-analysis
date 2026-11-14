import numpy as np
import pytest

from electre_i_kernel import enumerate_electre_kernels


def test_single_source_that_outranks_every_other_alternative_is_unique_kernel():
    relation = np.array([
        [1, 1, 1],
        [0, 1, 0],
        [0, 0, 1],
    ], dtype=bool)
    result = enumerate_electre_kernels(relation, ["A", "B", "C"])
    assert result.kernels == (("A",),)
    assert result.has_kernel
    assert result.is_unique


def test_chain_requires_an_independent_set_of_non_adjacent_endpoints():
    relation = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ], dtype=bool)
    result = enumerate_electre_kernels(relation, ["A", "B", "C"])
    assert result.kernels == (("A", "C"),)


def test_directed_three_cycle_has_no_kernel():
    relation = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ], dtype=bool)
    result = enumerate_electre_kernels(relation)
    assert result.kernels == ()
    assert not result.has_kernel
    assert not result.is_unique


def test_mutual_outranking_can_produce_multiple_kernels():
    relation = np.array([
        [1, 1],
        [1, 1],
    ], dtype=bool)
    result = enumerate_electre_kernels(relation, ["A", "B"])
    assert result.kernels == (("A",), ("B",))
    assert not result.is_unique


def test_no_edges_selects_all_alternatives():
    result = enumerate_electre_kernels(np.zeros((3, 3), dtype=bool))
    assert result.kernels == (("A1", "A2", "A3"),)


def test_diagonal_is_ignored():
    result = enumerate_electre_kernels(np.eye(2, dtype=bool))
    assert result.kernels == (("A1", "A2"),)


def test_invalid_relation_shape_values_and_names_are_rejected():
    with pytest.raises(ValueError, match="square"):
        enumerate_electre_kernels([[1, 0, 1], [0, 1, 0]])
    with pytest.raises(ValueError, match="0/1"):
        enumerate_electre_kernels([[0, 2], [0, 0]])
    with pytest.raises(ValueError, match="unique"):
        enumerate_electre_kernels([[0, 0], [0, 0]], ["X", "X"])


def test_exact_search_limit_is_explicit():
    with pytest.raises(ValueError, match="limited"):
        enumerate_electre_kernels(np.zeros((3, 3), dtype=bool), max_alternatives=2)
