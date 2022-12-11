import matplotlib.pyplot as plt
import numpy as np

signals = open("./2022/j10.txt").read().strip().splitlines()

x = 1
i = 0
res = 0
stopAt = [20, 60, 100, 140, 180, 220]

crt = [[0 for x in range(40)] for y in range(6)]


def inc(x, i):
    try:
        stopAt.index(i)
        return (i)*x
    except:
        return 0


def handleCRT(cycle: int, sprite: int):
    y = (cycle-1) // 40
    x = (cycle-1) % 40

    draw = abs(x-sprite) < 2

    crt[y][x] = int(draw)*255
    pass


cycle = 1
# while cycle < 221:

for signal in signals:
    # start of cycle
    res += inc(x, cycle)
    handleCRT(cycle, x)
    if(signal == "noop"):
        # end of cycle
        cycle += 1
        continue
    instruction, value = signal.split()
    # end of cycle
    cycle += 1
    res += inc(x, cycle)
    handleCRT(cycle, x)
    x += int(value)
    cycle += 1


print(res)

npa = np.array(crt)
plt.imsave("res.png", npa)
