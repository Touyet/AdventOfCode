def main():
    f = open("./2017/j9.txt", 'r')
    data = f.read()
    # data = '<{o"i!a,<{i<a>'
    print(p1(data))


def p1(data):
    grpNb = 0
    garbage = 0
    score = 0
    skipNext = False
    skipUntilChevron = False
    for char in data:
        if(skipNext):
            skipNext = False
            continue
        if(skipUntilChevron):
            if(char == "!"):
                skipNext = True
            elif(char == ">"):
                skipUntilChevron = False
            else:
                garbage = garbage+1
            continue
        if(char == "{"):
            score = score + 1
        elif(char == "}"):
            grpNb = grpNb + score
            score = score - 1
        elif(char == "!"):
            skipNext = True
        elif(char == "<"):
            skipUntilChevron = True
    return grpNb, garbage


main()
