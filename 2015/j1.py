from tools.utils import List


def main():
    f = open("./2015/j1.txt", 'r')
    data = List(f.read())

    print(p1(data), p2(data))


def p1(data: List[str]):
    plus = len(data.filter(lambda v: v == "("))
    minus = len(data.filter(lambda v: v == ")"))

    return plus - minus


def p2(data: List[str]):
    floor = 0
    for i in range(len(data)):
        char = data[i]
        if (char == "("):
            floor = floor+1
        elif (char == ")"):
            floor = floor-1
        if (floor == -1):
            return i+1


main()
