input: "list[str]" = open("./2015/j6.txt").read().strip().splitlines()

grid = [[0 for i in range(1000)] for j in range(1000)]

for instruction in input:
    turnOn = instruction.startswith('turn on')
    turnOff = instruction.startswith('turn off')
    toggle = instruction.startswith('toggle')

    if (turnOn):
        instruction = instruction.replace('turn on', '')
    elif (turnOff):
        instruction = instruction.replace('turn off', '')
    elif (toggle):
        instruction = instruction.replace('toggle', '')

    instruction = instruction.strip().split('through')

    xS, yS = map(int, instruction[0].strip().split(","))
    xE, yE = map(int, instruction[1].strip().split(","))

    for x in range(xS, xE+1):
        for y in range(yS, yE+1):
            if (toggle):
                grid[x][y] += 2
            else:
                grid[x][y] = max(0, grid[x][y] + (1 if turnOn else -1))

res = sum(map(sum, grid))
print(res)
