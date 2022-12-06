from tools.utils import List

input = open("./2019/j16.txt").read().strip()
# input = "80871224585914546619083218645595"

basePattern = [0, 1, 0, -1]
patterns = List()
for i, j in enumerate(input):
    p = List()
    for b in basePattern:
        for inc in range(i+1):
            p.append(b)
    p.rotate(1)
    patterns.append(p)

for phase in range(100):
    nextInput = ""
    for i in range(len(input)):
        pattern = patterns[i]
        nextValue = 0
        for index, value in enumerate(input):
            patternValue = index % len(pattern)
            nextValue += int(value) * pattern[patternValue]
        nextInput += str(nextValue)[-1]
    input = nextInput

print(input[:8])
