from tools.utils import List

input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
c = List([f for f in open("./2022/j1.txt").read().splitlines()])
lists = List()
currentList = []
for ca in c:
    if(len(ca) == 0):
        lists.append(currentList)
        currentList = []
        continue
    currentList.append(int(ca))

sumCal = lists.map(sum)
print(max(sumCal))

top3 = max(sumCal)
sumCal.remove(top3)
for i in range(0, 2):
    m = max(sumCal)
    top3 = top3 + m
    sumCal.remove(m)
print(top3)
