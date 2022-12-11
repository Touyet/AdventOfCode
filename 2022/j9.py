from math import sqrt

instructions = open("./2022/j9.txt").read().strip().splitlines()


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.visited = False
        self.x = x
        self.y = y

    def distance(self, p: "Point") -> int:
        dX = self.x - p.x
        dY = self.y - p.y
        return sqrt(dX**2 + dY**2)

    def isAdjacent(self, p: "Point") -> bool:
        dX = self.x - p.x
        dY = self.y - p.y
        return abs(dX) <= 1 and abs(dY) <= 1


def move(ins: str):
    if (ins == "D"):
        return (0, -1)
    if (ins == "U"):
        return (0, 1)
    if (ins == "L"):
        return (-1, 0)
    return (1, 0)


gridSize = 2000
grid = [[Point(x, y) for y in range(gridSize)] for x in range(gridSize)]

startX, startY = gridSize//2, gridSize//2
s = grid[startX][startY]
grid[s.x][s.y].visited = True


def p1(grid: "list[list[Point]]", s: Point):
    head = s
    tail = s
    res = 1
    for i, instruction in enumerate(instructions):
        a = instruction.split(" ")
        direction = a[0]
        qty = int(a[1])
        while qty > 0:
            m = move(direction)
            h = grid[head.x+m[0]][head.y+m[1]]

            if (h.isAdjacent(tail)):
                head = h
                qty -= 1
                continue
            tail = grid[head.x][head.y]
            if (not tail.visited):
                grid[tail.x][tail.y].visited = True
                res += 1
            head = h
            qty -= 1

    return res


def p2(grid: "list[list[Point]]", s: Point):
    head = s
    tails = [s for i in range(9)]
    res: set[Point] = set([s])
    for instruction in instructions:
        a = instruction.split(" ")
        direction = a[0]
        qty = int(a[1])
        mx, my = move(direction)
        while qty > 0:
            h = grid[head.x+mx][head.y+my]

            for i in range(len(tails)):
                if (i == 0):
                    previousHead = h

                tail = tails[i]
                if (previousHead.isAdjacent(tail)):
                    break
                dx = (previousHead.x - tail.x)
                if (dx != 0):
                    dx = dx//abs(dx)
                dy = (previousHead.y - tail.y)
                if (dy != 0):
                    dy = dy//abs(dy)
                tail = grid[tail.x + dx][tail.y+dy]
                if (i == (len(tails)-1)):
                    res.add((tail.x, tail.y))
                previousHead = tail
                tails[i] = tail
            head = h
            qty -= 1
    return len(res)


# res = p1(grid, s)
res = p2(grid, s)

print(res)
print("end")
