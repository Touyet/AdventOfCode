import sys


def main():
    f = open("./2021/j1.txt", 'r')
    data: list[int] = f.read().splitlines()
    res = p1(data)
    print("res1", res)
    res = p2(data)
    print("res2", res)


def p1(data):
    previousInput = None
    res = 0
    for input in data:
        if(previousInput is None):
            previousInput = int(input)
        if(int(input) > previousInput):
            res = res+1
        previousInput = int(input)
    return res


def p2(data):
    acc = 0
    arr = []
    for i in range(len(data)-2):
        acc = int(data[i])
        acc = acc + int(data[i+1])
        acc = acc + int(data[i+2])
        arr.append(acc)

    return p1(arr)


main()
