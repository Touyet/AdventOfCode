from tools.utils import List

input = "16,1,2,0,4,2,7,1,2,14"
file = List([f for f in open("./2021/j7.txt").read().split(",")]).map(int)
file2 = List(file)

minFuel = 1e50
minFuel2 = 1e50

minPos = 0
maxPos = max(file)

for i in range(maxPos):
    sum, sum2 = 0, 0
    for j in file:
        sum = sum + abs(i-j)
        sum2 = sum2 + abs(i-j)*(abs(i-j)+1)/2
    minFuel = min(minFuel, sum)
    minFuel2 = min(minFuel2, sum2)
print(minFuel, minFuel2)
