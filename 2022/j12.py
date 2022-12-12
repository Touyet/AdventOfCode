from tools.utils import List

input: "list[str]" = open("./2022/j12Test.txt").read().strip().splitlines()

grid = List(input).map(list)
print(grid)

rows = len(grid[0])
columns = len(grid)


class Node:
    x: int
    y: int
    name: str
    h = 1
    f = int(1e5)
    g = 0

    def __init__(self, x, y, name) -> None:
        self.x = x
        self.y = y
        self.name = name

    def neighbors(self, grid) -> "List[Node]":
        global rows, columns
        up = min(columns, max(0, self.y-1))
        down = min(columns, max(0, self.y+1))
        left = min(rows, max(0, self.x-1))
        right = min(rows, max(0, self.x+1))

        l = [grid[self.x][up], grid[self.x][down],
             grid[left][self.y], grid[right][self.y]]

        return l
