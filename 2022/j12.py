from math import inf
from typing import Union

from tools.utils import List, alphabet

# input: "list[str]" = open("./2022/j12.txt").read().strip().splitlines()
input: "list[str]" = open("./2022/j12Test.txt").read().strip().splitlines()

grid = List(input).map(list)

columns = len(grid[0])-1
rows = len(grid)-1


class Node:
    x: int
    y: int
    name: str

    h = 0

    parent: "Node" = None
    elevation: int

    def __init__(self, *args) -> None:

        if (len(args) > 1):
            x, y, name, elevation = args
            self.x = x
            self.y = y
            self.name = name
            self.elevation = alphabet.index(elevation)+1
            return

        node: Node = args[0]
        self.x = node.x
        self.y = node.y
        self.name = node.name
        self.h = node.h
        self.parent = node.parent
        self.elevation = node.elevation

    def __eq__(self, __o: "Node") -> bool:
        return __o.x == self.x and __o.y == self.y

    def neighbors(self, grid) -> "List[Node]":
        global rows, columns
        up = min(columns, max(0, self.y-1))
        down = min(columns, max(0, self.y+1))
        left = min(rows, max(0, self.x-1))
        right = min(rows, max(0, self.x+1))

        up = grid[self.x][up]
        down = grid[self.x][down]
        left = grid[left][self.y]
        right = grid[right][self.y]

        l = List([up, down, left, right]).filter(lambda v, i: v != self)

        return l

    def level(self, node: "Node") -> int:
        d = self.elevation - node.elevation
        if (d < 2):
            return 1
        return 1000


nodeGrid: "list[list[Node]]" = []
for x, l in enumerate(grid):
    nodeGrid.append([])
    for y, n in enumerate(l):
        el = n
        if (n == "S"):
            el = "a"
        elif (n == "E"):
            el = "z"
        nodeGrid[x].append(Node(x, y, n, el))

        if (n == "S"):
            start = nodeGrid[x][y]
        elif (n == "E"):
            end = nodeGrid[x][y]


def manhattan(a: Node, b: Node) -> int:
    return abs(a.x-b.x)+abs(a.y-b.y)


def a_star(start: Node, end: Node):
    open_list: "List[Node]" = List([start])
    closed_list: "List[Node]" = List()
    start.h = manhattan(start, end)
    steps = 0
    while len(open_list) > 0:
        steps += 1
        open_list.sort(key=lambda v: v.h)
        currentNode: Node = open_list.pop(0)
        closed_list.append(Node(currentNode))
        if (currentNode == end):
            break
        neighbors = currentNode.neighbors(nodeGrid)
        for neighbor in neighbors:
            n = Node(neighbor)
            n.h = currentNode.h + n.level(currentNode) + manhattan(n, end)
            if (neighbor not in closed_list and neighbor not in open_list):
                n.parent = currentNode
                open_list.append(n)
                nodeGrid[neighbor.x][neighbor.y] = n
            elif (neighbor in open_list and neighbor.parent != currentNode):
                past = open_list.find(neighbor)
                if (n.h < past.h):
                    n.parent = currentNode
                    open_list.append(n)
                    nodeGrid[neighbor.x][neighbor.y] = n
    n = closed_list.pop()
    res = []
    while n.parent is not None:
        res.append(n)
        n = n.parent

    return len(res)


a = a_star(start, end)
print(a)
