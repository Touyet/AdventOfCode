input: "list[str]" = open("./2015/j3.txt").read().strip()
# input = "^v^v^v^v^v"
# input = "^>v<"
l = len(input)*2
houses = [[0 for i in range(l)] for j in range(l)]


def move(v: str):
    if (v == ">"):
        return 1, 0
    elif (v == "<"):
        return -1, 0
    elif (v == "^"):
        return 0, 1
    return 0, -1


x, y = l//2, l//2
x1, y1 = l//2, l//2
houses[x][y] = 1

res = 1


def deliver(houses, x, y, res):
    houses[x][y] += 1
    if (houses[x][y] == 1):
        res += 1
    return res


for i in range(0, int(l/2), 2):
    h = input[i]
    x += move(h)[0]
    y += move(h)[1]
    res = deliver(houses, x, y, res)
    h = input[i+1]
    x1 += move(h)[0]
    y1 += move(h)[1]
    res = deliver(houses, x1, y1, res)

print(res)
