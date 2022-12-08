from tools.utils import List

grid = List(open("./2022/j8.txt").read().strip().splitlines()
            ).map(lambda v: List(v).map(int))
# grid = List(open("./2022/j8Test.txt").read().strip().splitlines()
#             ).map(lambda v: List(v).map(int))

rows: "List[int]" = List([x for i, x in enumerate(grid)])
columns: "List[int]" = List([[]for i in range(len(grid[0]))])

for row in rows:
    for y, c in enumerate(row):
        columns[y].append(c)

visible = (len(rows[0]) * 4) - 4  # EDGE
scenic = 0
for row in range(1, len(rows) - 1):
    for column in range(1, len(rows) - 1):
        tree = rows[row][column]

        right = rows[row][column + 1:]
        left = rows[row][:column]
        down = columns[column][row + 1:]
        up = columns[column][:row]

        left.reverse()
        up.reverse()

        right_visible = tree > max(right)
        left_visible = tree > max(left)
        down_visible = tree > max(down)
        up_visible = tree > max(up)

        if right_visible or left_visible or up_visible or down_visible:
            visible += 1

        scene_right = 0
        scene_left = 0
        scene_up = 0
        scene_down = 0
        for r in right:
            scene_right += 1
            if (tree <= r):
                break
        for r in left:
            scene_left += 1
            if (tree <= r):
                break
        for r in up:
            scene_up += 1
            if (tree <= r):
                break
        for r in down:
            scene_down += 1
            if (tree <= r):
                break
        scenic = max(scenic, scene_down*scene_left*scene_right*scene_up)

print(visible, scenic)
