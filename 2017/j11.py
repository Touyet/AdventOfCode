def main():
    f = open("./2017/j11.txt", 'r')
    data = f.read()

    ex = "ne,ne,s,s"
    print(p1(ex))
    ex = "se,sw,se,sw,sw"
    print(p1(ex))
    ex = "ne,ne,sw,sw"
    print(p1(ex))
    ex = "ne,ne,ne"
    print(p1(ex))
    print(p1(data))


def p1(data: str):
    direction = data.split(',')
    cr: int = 0
    cs: int = 0
    cq: int = 0

    n = [-1, 1, 0]
    s = [1, -1, 0]
    ne = [-1, 0, 1]
    nw = [0, 1, -1]
    se = [0, -1, 1]
    sw = [1, 0, -1]

    for d in direction:
        v = [0, 0, 0]
        if(d == "n"):
            v = n
        elif(d == "s"):
            v = s
        elif(d == "sw"):
            v = sw
        elif(d == "se"):
            v = se
        elif(d == "ne"):
            v = ne
        elif(d == "nw"):
            v = nw
        cr = cr + v[0]
        cs = cs + v[1]
        cq = cq + v[2]
    return (abs(cr)+abs(cs)+abs(cq))/2


def main2():
    i = []
    with open("./2017/j11.txt") as f:
        i = f.read().split(",")

    dmap = {
        "n": (0, 1),
        "s": (0, -1),
        "ne": (.5, .5),
        "se": (.5, -.5),
        "nw": (-.5, .5),
        "sw": (-.5, -.5)
    }

    x, y = 0, 0  # x,y coordinates for tracking how far we've moved
    m = []
    for d in i:
        x += dmap[d][0]
        y += dmap[d][1]
        m.append(abs(x)+abs(y))

    print(abs(x)+abs(y))  # Part 1
    print(max(m))  # Part 2


main2()
