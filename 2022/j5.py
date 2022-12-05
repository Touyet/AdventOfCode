input: "list[str]" = open("./2022/j5.txt").read().strip().splitlines()

'''
            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9 
'''

crates = [
    ["Q", "F", "L", "S", "R"],
    ["T", "P", "G", "Q", "Z", "N"],
    ["B", "Q", "M", "S"],
    ["Q", "B", "C", "H", "J", "Z", "G", "T", ],
    ["S", "F", "N", "B", "M", "H", "P"],
    ["G", "V", "L", "S", "N", "Q", "C", "P"],
    ["F", "C", "W", ],
    ["M", "P", "V", "W", "Z", "G", "H", "Q"],
    ["R", "N", "C", "L", "D", "Z", "G"],
]

for i in range(100):
    crates.append([])

instructions = []
for i in input:
    ins = i.split(' ')
    instructions.append((int(ins[1]), int(ins[3])-1, int(ins[5])-1))

for instruction in instructions:
    nb = instruction[0]
    source = instruction[1]
    target = instruction[2]

    for i in range(nb):
        c = crates[source][0]
        crates[source] = crates[source][1:]
        crates[target].insert(0, c)

res = ""
for crate in crates:
    if(len(crate) == 0):
        continue
    res = res+crate[0]

print(res.strip())

crates = [
    ["Q", "F", "L", "S", "R"],
    ["T", "P", "G", "Q", "Z", "N"],
    ["B", "Q", "M", "S"],
    ["Q", "B", "C", "H", "J", "Z", "G", "T", ],
    ["S", "F", "N", "B", "M", "H", "P"],
    ["G", "V", "L", "S", "N", "Q", "C", "P"],
    ["F", "C", "W", ],
    ["M", "P", "V", "W", "Z", "G", "H", "Q"],
    ["R", "N", "C", "L", "D", "Z", "G"],
]

for instruction in instructions:
    nb = instruction[0]
    source = instruction[1]
    target = instruction[2]

    c = crates[source][:nb]
    crates[source] = crates[source][nb:]
    c.reverse()
    for i in c:
        crates[target].insert(0, i)

res = ""
for crate in crates:
    if(len(crate) == 0):
        continue
    res = res+crate[0]

print(res)
