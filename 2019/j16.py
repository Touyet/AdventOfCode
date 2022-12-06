from collections import deque

from tools.utils import List

input = open("./2019/j16.txt").read().strip()
input = "80871224585914546619083218645595"

# input *= 10000
offset = int(input[:7])

basePattern = deque([0, 1, 0, -1])
patterns = [None for i in input]
for phase in range(100):
    nextInput = ""
    for index, value in enumerate(input):
        pass

    # for i in range(len(input)):
    #     pattern = patterns[i]
    #     nextValue = 0
    #     for index, value in enumerate(input):
    #         patternValue = index % len(pattern)
    #         nextValue += int(value) * pattern[patternValue]
    #     nextInput += str(nextValue)[-1]
    # input = nextInput

print(input[:8])
assert input[:8] == "24176176"
