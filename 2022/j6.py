input = open("./2022/j6.txt").read().strip()
res = ""
l = 14
for i in range(0, len(input)-l+1):
    res = input[i:i+l]
    a = set(res)
    if(len(a) == l):
        break
print(res, i+l)
