from tools.utils import List

input = open("./2022/j2.txt").read().splitlines()
# input = ["C X"]
guide = List([f for f in input]
             ).map(lambda v: v.split(" "))
# print(guide)

rock = ("A", "X", 1)
paper = ("B", "Y", 2)
scissor = ("C", "Z", 3)


def round(opponent: str, me: str) -> int:
    opponentR = rock[2] if opponent in rock else 0
    opponentP = paper[2] if opponent in paper else 0
    opponentS = scissor[2] if opponent in scissor else 0
    meR = rock[2] if me in rock else 0
    meP = paper[2] if me in paper else 0
    meS = scissor[2] if me in scissor else 0

    me = meR + meP + meS
    opponent = opponentR + opponentP + opponentS

    if(me == opponent):
        return me + 3

    if(meR != 0 and opponentS != 0):
        return me + 6

    if(meS != 0 and opponentR != 0):
        return me

    if (me < opponent):
        return me

    return me + 6


def round2(opponent: str, outcome: str) -> int:
    opponentR = rock[2] if opponent in rock else 0
    opponentP = paper[2] if opponent in paper else 0
    opponentS = scissor[2] if opponent in scissor else 0

    win = outcome == "Z"
    draw = outcome == "Y"
    lose = outcome == "X"

    opponent = opponentR + opponentP + opponentS

    if(win is True):
        score = 6
        if(opponentP != 0):
            return score+3
        if(opponentR != 0):
            return score+2
        if(opponentS != 0):
            return score+1
    if(draw is True):
        return opponent+3

    if(lose is True):
        if(opponentP != 0):
            return 1
        if(opponentS != 0):
            return 2
        if(opponentR != 0):
            return 3


finalScore = 0
finalScore2 = 0
for i in guide:
    finalScore = finalScore + round(i[0], i[1])
    finalScore2 = finalScore2 + round2(i[0], i[1])

print(finalScore, finalScore2)
# ax = 4 #draw
# by = 5 #draw
# cz = 6 #draw

# ay = 8
# print(guide.count(["A", "Z"]))
