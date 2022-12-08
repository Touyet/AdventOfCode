from tools.utils import List

grid = List(open("./2022/j8.txt").read().strip().splitlines()
            ).map(lambda v: List(v).map(int))

res = 0


class Row:
    def __init__(self, x: int, content: list[int]) -> None:
        self.x = x
        self.content = content


class Column:
    def __init__(self, y: int, content: list[int]) -> None:
        self.y = y
        self.content = content


rows: "List[Row]" = List([Row(i, x) for i, x in enumerate(grid)])
columns: "List[Column]" = List([Column(i, []) for i in range(len(grid[0]))])

for row in rows:
    for y, c in enumerate(row.content):
        columns[y].content.append(c)

res = 0
for row in rows:
    # First and last row are always visible
    if (row.x == 0 or row.x == (len(rows)-1)):
        res += len(row.content)
        continue
    x = row.x

    for y, value in enumerate(row.content):
        column = columns[y]

        # First and last column are always visible
        if (column.y == 0 or column.y == (len(columns)-1)):
            res += 1
            continue

        if (value == max(row.content) or value == max(column.content)):
            res += 1
            continue
        if (value == min(row.content) or value == min(column.content)):
            continue

        left = [1 for i, j in enumerate(row.content) if (
            j >= value and i > y)]
        right = [1 for i, j in enumerate(row.content) if (
            j >= value and i < y)]
        up = [1 for i, j in enumerate(column.content) if (
            j >= value and i > x)]
        down = [1 for i, j in enumerate(column.content) if (
            j >= value and i < x)]

        if (len(down) == 0 or len(up) == 0 or len(left) == 0 or len(right) == 0):
            res += 1
            continue

print(res)
