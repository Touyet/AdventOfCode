from time import perf_counter

from tools.utils import List

input = open("./2019/j16.txt").read().strip()
# input = "80871224585914546619083218645595"
# input = "12345678"
basePattern = List([0, 1, 0, -1])
basePattern.rotate(1)

b = len(basePattern)
l = len(input)

t1 = perf_counter()
m = 0
p = 0
while p < 100:
    nextInput = ""
    n = 0
    while n < l:
        nextValue = 0
        for index, value in enumerate(input):
            m += 1
            # if (index < n):
            #     continue
            # else:
            j = (index if n == 0 else ((index)//(n+1))) % b
            patternValue = basePattern[j]
            nextValue += int(value) * patternValue
        nextInput += str(nextValue)[-1]
        input = input[1:]
        n += 1
    p += 1
    input = nextInput

t2 = perf_counter()
print(round(t2-t1), "s", m, "loop")
print("res", input[:8])
