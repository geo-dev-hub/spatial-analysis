import random
import pytest
from status_treap import ImplicitTreap


def validate(tree, expected):
    assert tree.values() == expected
    assert len(tree) == len(expected)
    if tree.root:
        assert tree.root.parent is None
    for index, value in enumerate(expected):
        node = tree.at(index)
        assert node.value == value
        assert tree.rank(node) == index
        assert node.size == 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
        if node.left: assert node.left.parent is node
        if node.right: assert node.right.parent is node


def test_insert_remove_and_rank():
    tree=ImplicitTreap(seed=4); nodes={}; expected=[]
    for value,index in [(8,0),(3,0),(9,2),(5,1),(1,4)]:
        node=tree.new_node(value); tree.insert_at(index,node); nodes[value]=node; expected.insert(index,value); validate(tree,expected)
    for value in [3,1,8,9,5]:
        index=expected.index(value); removed=tree.remove_at(index); expected.pop(index); assert removed.value==value; validate(tree,expected)


def test_adjacent_swaps_preserve_node_identity():
    tree=ImplicitTreap(seed=8); nodes=[]
    for value in range(10):
        node=tree.new_node(value); tree.insert_at(len(tree),node); nodes.append(node)
    expected=list(range(10))
    for index in [0,4,7,2,5]:
        tree.swap_adjacent(index); expected[index],expected[index+1]=expected[index+1],expected[index]; validate(tree,expected)
    for value in range(10): assert tree.at(tree.rank(nodes[value])) is nodes[value]


def test_lower_bound():
    tree=ImplicitTreap(seed=3)
    for value in [2,4,6,8]: tree.insert_at(len(tree),tree.new_node(value))
    assert tree.lower_bound(lambda node:node.value,1)==0
    assert tree.lower_bound(lambda node:node.value,4)==1
    assert tree.lower_bound(lambda node:node.value,5)==2
    assert tree.lower_bound(lambda node:node.value,10)==4


def test_randomized_sequence_operations():
    rng=random.Random(77); tree=ImplicitTreap(seed=77); expected=[]
    for value in range(600):
        index=rng.randrange(len(expected)+1); tree.insert_at(index,tree.new_node(value)); expected.insert(index,value)
        if len(expected)>3 and rng.random()<0.55:
            index=rng.randrange(len(expected)); removed=tree.remove_at(index); assert removed.value==expected.pop(index)
        if len(expected)>1 and rng.random()<0.45:
            index=rng.randrange(len(expected)-1); tree.swap_adjacent(index); expected[index],expected[index+1]=expected[index+1],expected[index]
        validate(tree,expected)


def test_rejects_attached_node():
    tree=ImplicitTreap(); node=tree.new_node(1); tree.insert_at(0,node)
    with pytest.raises(ValueError): tree.insert_at(1,node)
