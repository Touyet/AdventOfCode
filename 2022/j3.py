from tools.utils import List, alphabet

input = open("./2022/j3.txt").read().splitlines()

compartmentList: List[str] = List(input)

res = 0
for compartment in compartmentList:
    itemSize = len(compartment)//2
    (item1, item2) = (compartment[slice(0, itemSize)],
                      compartment[slice(itemSize, len(compartment))])
    priorityItem = set(item1).intersection(item2).pop()
    res = res + alphabet.index(priorityItem)+1

print(res)

res2 = 0
for index in range(0, len(compartmentList), 3):
    (item1, item2, item3) = (
        compartmentList[index], compartmentList[index+1], compartmentList[index+2])
    # print(item1, item2, item3)
    priorityItem = set(item1).intersection(item2).intersection(item3).pop()
    res2 = res2 + alphabet.index(priorityItem)+1

print(res2)
