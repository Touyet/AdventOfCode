from math import sqrt

instructions = open("./2022/j9Test.txt").read().strip().splitlines()


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.visited = False
        self.x = x
        self.y = y

    def distance(self, p: "Point") -> int:
        dX = self.x - p.x
        dY = self.y - p.y
        return sqrt(dX**2 + dY**2)


def move(ins: str):
    if(ins == "D"):
        return (0, -1)
    if(ins == "U"):
        return (0, 1)
    if(ins == "L"):
        return (-1, 0)
    return (1, 0)


grid = [[Point(x, y) for y in range(1000)] for x in range(1000)]

startX, startY = 500, 500
s = grid[startX][startY]
grid[s.x][s.y].visited = True

head = s
tail = s

for instruction in instructions:
    a = instruction.split(" ")
    direction = a[0]
    qty = int(a[1])
    while qty > 0:
        m = move(direction)
        h = grid[head.x+m[0]][head.y+m[1]]
        d = h.distance(tail)
        if(d > 1):
            tail = grid[head.x][head.y]
            grid[tail.x][tail.y].visited = True
        head = h
        qty -= 1

print("end")
