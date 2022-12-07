from math import floor
from time import perf_counter

from numpy.fft import fft

from tools.utils import List


def getInput():
    input = open("./2019/j16.txt").read().strip()
    # input = "80871224585914546619083218645595"
    # input = "03036732577212944063491565474664"
    # input = "12345678"
    return input


input = getInput()

# input *= 10000
offset = input[:7]

basePattern = List([0, 1, 0, -1])
# basePattern.rotate(1)


def p1(input, basePattern):
    m = 0
    p = 0
    b = len(basePattern)
    l = len(input)
    while p < 100:
        nextInput = ""
        n = 0
        while n < l:
            nextValue = 0
            for index, value in enumerate(input):
                m += 1
                j = (index if n == 0 else ((index)//(n+1))) % b
                patternValue = basePattern[j]
                nextValue += int(value) * patternValue
            nextInput += str(abs(nextValue) % 10)
            input = input[1:]
            n += 1
        p += 1
        input = nextInput
    return input, m


def c(input, basePattern):
    input = List(input).map(int)
    for i in range(100):
        for j in range(len(input)):
            d = 0
            for k in range(len(input)):
                d += input[k]*m(j+1, k)
            input[j] = abs(d) % 10
    return List(input).join()


def m(n, i):
    return basePattern[floor(((i+1) % (4*n))/n)]


def p2(input, basePattern):
    m = 0
    p = 0
    b = len(basePattern)
    l = len(input)
    while p < 100:
        nextInput = ""
        n = 0
        s = []
        index = 0
        while index < l:
            # for index, value in enumerate(input):
            value = input[index]
            j = (index if n == 0 else ((index)//(n+1))) % b
            patternValue = basePattern[j]
            nextValue = int(value) * patternValue
            s.append([nextValue])

            i = 0
            while i < index:
                m += 1
                j = (index if i == 0 else ((index-i)//(i+1))) % b
                patternValue = basePattern[j]
                val = int(value) * patternValue
                s[i].append(val)
                i += 1
            n += 1
            index += 1
        p += 1
        input = List([abs(sum(f)) % 10 for f in s])
    return input.join(), m


t1 = perf_counter()
input = c(getInput(), basePattern)
t2 = perf_counter()
print(round(t2-t1), "s")
print("res", input[:8])

# t1 = perf_counter()
# input, m = p2(getInput(), basePattern)
# t2 = perf_counter()
# print(round(t2-t1), "s", m, "loop")
# print("res", input[:8])
