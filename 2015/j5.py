from tools.utils import List, alphabet

input: "list[str]" = open("./2015/j5.txt").read().strip().splitlines()

vowels = List("aeiou")
forbidden = List(["ab", "cd", "pq", "xy"])
# input = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp",
#          "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
# input = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg",
#          "ieodomkazucvgmuy"]

lower = List(alphabet[:26]).map(lambda v: v*3)
# lower = List(alphabet[:26]).map(lambda v: v*2)
triple = [a+b+a for a in alphabet[:26] for b in alphabet[:26] if a != b]
pair = [a+b for a in alphabet[:26] for b in alphabet[:26]]

res = 0
for string in input:
    # forbid = [string.count(f) > 0 for f in forbidden].count(True) > 0
    # vowelCnt = sum([string.count(v) for v in vowels]) < 3
    # doubleLetter = sum([string.count(v) for v in lower]) < 1
    # if (forbid or vowelCnt or doubleLetter):
    #     continue
    wanted = sum([string.count(v) for v in triple]) < 1
    if (wanted):
        continue
    p = [v for v in pair if string.count(v) > 1]
    if (len(p) < 1):
        continue
    res += 1

print(res)
