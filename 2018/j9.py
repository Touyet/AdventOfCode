from tools.utils import List
from collections import deque, defaultdict


def main():
    playerCount = 468
    players = List(Player() for x in range(playerCount))
    end = 7184300
    tower = [0]
    currentMarbleIndex = 0
    for i in range(1, end):
        currentPlayer: Player = players[(i-1) % playerCount]
        if(i % 23 == 0):
            currentMarbleIndex = (currentMarbleIndex - 7) % len(tower)
            marbleValue = tower.pop(currentMarbleIndex)
            currentPlayer.score += i + marbleValue
            continue
        currentMarbleIndex = (currentMarbleIndex+2) % (len(tower)+1)
        if(currentMarbleIndex == 0):
            currentMarbleIndex = 1
        tower.insert(currentMarbleIndex, i)

    print(max(x.score for x in players))


class Player:
    def __init__(self) -> None:
        self.score = 0


def main2():
    playerCount = 468
    end = 7184300
    print(play_game(playerCount, int(end/100)))
    print(play_game(playerCount, end))


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


main2()
