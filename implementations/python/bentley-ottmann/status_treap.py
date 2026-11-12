"""Implicit randomized treap for an ordered sweep-line status.

The tree stores sequence order, not a mutable geometric comparator. Crossing
segments are adjacent in that sequence and are explicitly swapped at events.
Expected operation time is O(log n) with independent randomized priorities.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Callable


@dataclass
class Node:
    value: int
    priority: tuple[float, int]
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None
    size: int = 1
    owner: object | None = field(default=None, repr=False, compare=False)


def _size(node: Node | None) -> int:
    return node.size if node else 0


def _update(node: Node) -> None:
    node.size = 1 + _size(node.left) + _size(node.right)
    if node.left:
        node.left.parent = node
    if node.right:
        node.right.parent = node


def _merge(left: Node | None, right: Node | None) -> Node | None:
    if left is None:
        if right:
            right.parent = None
        return right
    if right is None:
        left.parent = None
        return left
    if left.priority > right.priority:
        left.right = _merge(left.right, right)
        _update(left)
        left.parent = None
        return left
    right.left = _merge(left, right.left)
    _update(right)
    right.parent = None
    return right


def _split(root: Node | None, count: int) -> tuple[Node | None, Node | None]:
    """Split into the first count sequence items and the remaining items."""
    if root is None:
        return None, None
    if count < 0 or count > _size(root):
        raise IndexError("split position out of range")
    left_size = _size(root.left)
    if count <= left_size:
        first, remainder = _split(root.left, count)
        root.left = remainder
        _update(root)
        root.parent = None
        if first:
            first.parent = None
        return first, root
    first, remainder = _split(root.right, count - left_size - 1)
    root.right = first
    _update(root)
    root.parent = None
    if remainder:
        remainder.parent = None
    return root, remainder


class ImplicitTreap:
    """Sequence tree with expected logarithmic rank and neighbour operations."""

    def __init__(self, seed: int = 20261113):
        self.root: Node | None = None
        self._rng = random.Random(seed)
        self._serial = 0

    def __len__(self) -> int:
        return _size(self.root)

    def new_node(self, value: int) -> Node:
        self._serial += 1
        return Node(value, (self._rng.random(), self._serial))

    def insert_at(self, index: int, node: Node) -> None:
        if node.owner is not None or node.parent or node.left or node.right or node.size != 1:
            raise ValueError("Only detached singleton nodes can be inserted")
        if not 0 <= index <= len(self):
            raise IndexError("insert position out of range")
        left, right = _split(self.root, index)
        node.owner = self
        self.root = _merge(_merge(left, node), right)
        if self.root:
            self.root.parent = None

    def remove_at(self, index: int) -> Node:
        if not 0 <= index < len(self):
            raise IndexError("remove position out of range")
        left, rest = _split(self.root, index)
        middle, right = _split(rest, 1)
        if middle is None:
            raise RuntimeError("treap split invariant failed")
        self.root = _merge(left, right)
        middle.left = middle.right = middle.parent = None
        middle.size = 1
        middle.owner = None
        if self.root:
            self.root.parent = None
        return middle

    def swap_adjacent(self, index: int) -> None:
        """Swap items at index and index+1 without changing node identities."""
        if not 0 <= index < len(self) - 1:
            raise IndexError("adjacent swap position out of range")
        left, rest = _split(self.root, index)
        first, rest = _split(rest, 1)
        second, right = _split(rest, 1)
        if first is None or second is None:
            raise RuntimeError("treap split invariant failed")
        self.root = _merge(_merge(_merge(left, second), first), right)
        if self.root:
            self.root.parent = None

    def rank(self, node: Node) -> int:
        """Return a node's zero-based sequence position in expected O(log n)."""
        if node is self.root:
            return _size(node.left)
        result = _size(node.left)
        current = node
        while current.parent:
            parent = current.parent
            if current is parent.right:
                result += _size(parent.left) + 1
            current = parent
        if current is not self.root:
            raise ValueError("Node does not belong to this treap")
        return result

    def at(self, index: int) -> Node:
        if not 0 <= index < len(self):
            raise IndexError("treap index out of range")
        current = self.root
        while current:
            left_size = _size(current.left)
            if index < left_size:
                current = current.left
            elif index == left_size:
                return current
            else:
                index -= left_size + 1
                current = current.right
        raise RuntimeError("treap size invariant failed")

    def lower_bound(self, key: Callable[[Node], object], target: object) -> int:
        """Return insertion rank before the first node whose key is >= target."""
        current = self.root
        skipped = 0
        answer = len(self)
        while current:
            left_size = _size(current.left)
            if key(current) < target:
                skipped += left_size + 1
                current = current.right
            else:
                answer = skipped + left_size
                current = current.left
        return answer

    def values(self) -> list[int]:
        result: list[int] = []
        stack: list[Node] = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result
