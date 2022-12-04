from tools.utils import List

input = "2-4,6-8\n\
2-3,4-5\n\
5-7,7-9\n\
2-8,3-7\n\
6-6,4-6\n\
2-6,4-8".splitlines()
input: "list[str]" = open("./2022/j4.txt").read().strip().splitlines()

pairs = List(input).map(lambda v: v.split(",")).map(
    lambda v: [List(i.split("-")).map(int) for i in v])

res = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    # print(elf1, elf2)

    minElf1 = elf1[0]
    maxElf1 = elf1[1]
    minElf2 = elf2[0]
    maxElf2 = elf2[1]

    if(minElf1 <= minElf2 and maxElf1 >= maxElf2):
        res += 1
    elif(minElf2 <= minElf1 and maxElf2 >= maxElf1):
        res += 1

print(res)

res = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]

    minElf1 = elf1[0]
    maxElf1 = elf1[1]
    minElf2 = elf2[0]
    maxElf2 = elf2[1]

    elf1 = [f for f in range(minElf1, maxElf1+1)]
    elf2 = [f for f in range(minElf2, maxElf2+1)]

    # print(elf1, elf2)
    inter = set(elf1).intersection(elf2)
    if(len(inter) > 0):
        res += 1

print(res)
