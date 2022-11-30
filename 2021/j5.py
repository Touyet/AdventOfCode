def main():
    f = open("./2021/j5.txt", 'r')
    data: list[str] = f.read().splitlines()

    print(p1(data), p1(data, True))


def p1(data: "list[str]", useDiag=False):
    res = 0
    nb = 1000
    arr = [[0 for i in range(nb)] for j in range(nb)]
    for d in data:
        input = d.split()
        x1, y1 = input[0].split(',')
        x2, y2 = input[2].split(',')

        l = int(x2)-int(x1)
        w = int(y2)-int(y1)
        if(l == 0 and w == 0):
            continue

        if(l == 0):
            stepY = int(w/abs(w))
            for y in range(int(y1), int(y2)+stepY, stepY):
                cell = arr[int(x1)][y]
                cell = cell + 1
                arr[int(x1)][y] = cell
                if(cell == 2):
                    res = res + 1
        elif(w == 0):
            stepX = int(l/abs(l))
            for x in range(int(x1), int(x2)+stepX, stepX):
                cell = arr[x][int(y1)]
                cell = cell + 1
                arr[x][int(y1)] = cell
                if(cell == 2):
                    res = res + 1
        elif(useDiag):
            stepY = int(w/abs(w))
            stepX = int(l/abs(l))
            t = zip(range(int(x1), int(x2)+stepX, stepX),
                    range(int(y1), int(y2)+stepY, stepY))
            for i, j in t:
                cell = arr[i][j]
                cell = cell + 1
                arr[i][j] = cell
                if(cell == 2):
                    res = res + 1

    return res


main()
