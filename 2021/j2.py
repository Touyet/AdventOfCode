import sys


def main():
    f = open("./2021/j2.txt", 'r')
    data: list[int] = f.read().splitlines()
    print(p1(data), p2(data))


def p1(data):
    h = 0
    d = 0
    for input in data:
        s = input.split()
        if(s[0] == "forward"):
            h = h + int(s[1])
        elif(s[0] == "down"):
            d = d + int(s[1])
        elif(s[0] == "up"):
            d = d - int(s[1])
    return h*d


def p2(data):
    h = 0
    d = 0
    a = 0
    for input in data:
        s = input.split()
        if(s[0] == "forward"):
            h = h + int(s[1])
            d = d + a*int(s[1])
        elif(s[0] == "down"):
            a = a + int(s[1])
        elif(s[0] == "up"):
            a = a - int(s[1])
    return h*d


main()
