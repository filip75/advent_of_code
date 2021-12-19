from copy import deepcopy
from dataclasses import dataclass
from itertools import product
from string import digits

from aoc import *


@dataclass
class Node:
    value: Optional[int] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None

    def __str__(self) -> str:
        if self.value is not None:
            return str(self.value)
        else:
            return f"[{self.left},{self.right}]"

    def __repr__(self) -> str:
        return self.__str__()

    def is_pair_of_values(self) -> bool:
        return (self.right and self.right.value is not None) and (
            self.left and self.left.value is not None
        )

    def is_value(self) -> bool:
        return self.value is not None

    def is_right(self) -> bool:
        return self.parent and self.parent.right is self

    def is_left(self) -> bool:
        return self.parent and self.parent.left is self

    @property
    def magnitude(self) -> int:
        if self.is_value():
            return self.value
        else:
            return 3 * self.left.magnitude + 2 * self.right.magnitude

    @property
    def depth(self) -> int:
        pointer = self
        d = 0
        while pointer.parent is not None:
            d += 1
            pointer = pointer.parent

        return d

    def append(self, new_node: "Node") -> None:
        new_node.parent = self
        if self.left is None:
            self.left = new_node
        else:
            self.right = new_node

    def get_left_neighbour(self) -> Optional["Node"]:
        pointer = self
        while pointer and pointer.is_left():
            pointer = pointer.parent
        pointer = pointer.parent

        if not pointer:
            return None

        pointer = pointer.left

        while pointer and not pointer.is_value():
            pointer = pointer.right

        if pointer:
            return pointer
        return None

    def get_right_neighbour(self) -> Optional["Node"]:
        pointer = self
        while pointer and pointer.is_right():
            pointer = pointer.parent
        pointer = pointer.parent

        if not pointer:
            return None

        pointer = pointer.right

        while pointer and not pointer.is_value():
            pointer = pointer.left

        if pointer:
            return pointer
        return None

    def split(self) -> None:
        l = self.value // 2
        r = self.value - l
        self.value = None
        self.left = Node(value=l, parent=self)
        self.right = Node(value=r, parent=self)
        if self.depth >= 4:
            self.explode()

    def explode(self) -> None:
        left_neighbour = self.get_left_neighbour()
        if left_neighbour:
            left_neighbour.value += self.left.value
        right_neighbour = self.get_right_neighbour()
        if right_neighbour:
            right_neighbour.value += self.right.value

        self.value = 0
        self.left = None
        self.right = None


def get_data() -> list[Node]:
    data = read_list(18)

    nodes: list[Node] = []
    for line in data:
        node = Node()
        stack = [node]
        for c in line[1:-1]:
            if c == "[":
                new_node = Node(parent=stack[-1])
                stack[-1].append(new_node)
                stack.append(new_node)
            elif c == "]":
                stack.pop()
            elif c in digits:
                new_node = Node(value=int(c))
                new_node.parent = stack[-1]
                stack[-1].append(new_node)
        nodes.append(node)
    return nodes


def reduce(node: Node) -> None:
    while True:
        to_visit: list[Node] = [node]
        while to_visit:
            current = to_visit.pop(0)
            if current.is_pair_of_values() and current.depth >= 4:
                current.explode()
                break
            else:
                if current.right and not current.right.value:
                    to_visit.insert(0,current.right)
                if current.left and not current.left.value:
                    to_visit.insert(0,current.left)
        else:
            break

    while True:
        to_visit: list[Node] = [node]

        while to_visit:
            current = to_visit.pop(0)
            if current.is_value():
                if current.value > 9:
                    current.split()
                    break
            else:
                to_visit.insert(0, current.right)
                to_visit.insert(0, current.left)
        else:
            break


def add(n1: Node, n2: Node) -> Node:
    new_node = Node(left=n1, right=n2)
    n1.parent = new_node
    n2.parent = new_node
    reduce(new_node)
    return new_node


def first() -> int:
    data = get_data()

    n = add(data[0], data[1])
    for d in data[2:]:
        n = add(n, d)

    return n.magnitude


def second() -> int:
    data = get_data()

    m = 0
    for x, y in product(data, data):
        x = deepcopy(x)
        y = deepcopy(y)
        result = add(x, y)
        m = max(m, result.magnitude)

    return m
