import sys
from tools.utils import List


def main():
    f = open("./2015/j2.txt", 'r')
    data = f.read().splitlines()
    print(p1(data), p2(data))


def p1(lines: "list[str]"):
    res = 0
    for line in lines:
        l, w, h = line.split('x')

        lw = int(l)*int(w)
        hw = int(h)*int(w)
        hl = int(h)*int(l)

        res = res + 2*lw+2*hw+2*hl + min(lw, hw, hl)

    return res


def p2(lines: "list[str]"):
    res = 0
    for line in lines:
        l, w, h = line.split('x')

        lw = 2*int(l)+2*int(w)
        hw = 2*int(h)+2*int(w)
        hl = 2*int(h)+2*int(l)
        v = int(h)*int(l)*int(w)

        res = res + v + min(lw, hw, hl)

    return res


main()
