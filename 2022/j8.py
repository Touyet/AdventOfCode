from tools.utils import List

grid = List(open("./2022/j8.txt").read().strip().splitlines()
            ).map(lambda v: List(v).map(int))

res = 0


class Row:
    def __init__(self, x, content) -> None:
        self.x = x
        self.content = content


class Column:
    def __init__(self, y, content) -> None:
        self.y = y
        self.content = content


rows = List([Row(i, x) for i, x in enumerate(grid)])
columns = List([Column(i, []) for i in range(len(grid[0]))])

for row in rows:
    for y, c in enumerate(row.content):
        columns[y].content.append(c)

res = 0
for row in rows:
    if(row.x == 0 or row.x == len(rows)-1):
        res += 1
        continue
    for column in columns:
        if(column.y == 0 or column.y == len(rows)-1):
            res += 1
            continue
