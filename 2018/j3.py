def main():
    f = open("./2018/j3.txt", 'r')
    data: list[str] = f.read().splitlines()
    # data = [
    #     "#1 @ 1,3: 4x4",
    #     "#2 @ 3,1: 4x4",
    #     "#3 @ 5,5: 2x2"]

    nb = 1000
    arr = [[{"claimList": [], "nb":0} for i in range(nb)] for j in range(nb)]

    res = p1(data, arr)

    print(res)


def p1(data: "list[str]", arr: "list[list[dict[str, int]]]"):
    res = 0
    uniq = []
    for d in data:
        input = d.replace(':', '').split()
        id = int(input[0].replace('#', ''))
        x, y = input[2].split(',')
        l, w = input[3].split('x')

        uniq.append(id)

        for i in range(int(l)):
            for j in range(int(w)):
                cell = arr[int(x)+i][int(y)+j]
                cell["nb"] = cell["nb"]+1
                cell["claimList"].append(id)
                if(cell["nb"] == 2):
                    res = res+1
                if(cell["nb"] >= 2):
                    claimList = cell["claimList"]
                    for claimedId in claimList:
                        if(claimedId in uniq):
                            uniq.remove(claimedId)

    uniqId = uniq[0]

    return res, uniqId


main()
