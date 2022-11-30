from tools.utils import List


def main():
    f = open("./2021/j3.txt", 'r')
    data = f.read().splitlines()
    print(p1(data))
    print(p2(List(data)))


def p1(lines: "list[str]"):
    data:  "list[list[str]]" = [[] for i in range(len(lines[0]))]
    for line in lines:
        input = list(line)
        for i in range(len(input)):
            data[i].append(input[i])

    g = 0
    e = 0
    data.reverse()
    for i in range(len(data)):
        bit = data[i]
        c0 = bit.count('0')
        c1 = bit.count('1')
        if(c0 > c1):
            g = g + (0 << i)
            e = e + (1 << i)
        else:
            g = g + (1 << i)
            e = e + (0 << i)
    return g*e


def p2(lines: "List[str]"):
    bitLength = len(lines[0])

    g = List(lines)
    e = List(lines)
    for i in range(bitLength):
        if(len(g) > 1):
            data = parseLines(g, bitLength)
            g = computeBit(data, g, i)
        if(len(e) > 1):
            data = parseLines(e, bitLength)
            e = computeBit(data, e, i, False)

    g = int(g[0], 2)
    e = int(e[0], 2)
    return g*e


def computeBit(data, g, i, max=True):
    bit = data[i]
    c0 = bit.count('0')
    c1 = bit.count('1')
    str = "0"
    if(c0 > c1):
        if(max):
            str = "0"
        else:
            str = "1"
    else:
        if(max):
            str = "1"
        else:
            str = "0"
    g = g.filter(lambda v: v[i] == str)

    return g


def parseLines(lines, bitLength):
    data:  "List[List[str]]" = [[] for i in range(bitLength)]
    for line in lines:
        input = list(line)
        for i in range(len(input)):
            data[i].append(input[i])
    return data


main()
