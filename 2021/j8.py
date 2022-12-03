from tools.utils import List

file = List(open("./2021/j8.txt").readlines()
            ).map(lambda v: v.split("|")[1].strip().split(' '))

lenOfOne, lenOfFour, lenOfSeven, lenOfEight = 2, 4, 3, 7

one = (1, ("c", "f"))
two = (2, ("a", "c", "d", "e", "g"))
three = (3, ("a", "c", "d", "f", "g"))
four = (4, ("b", "c", "d", "f"))
five = (5, ("a", "b", "d", "f", "g"))
six = (6, ("a", "b", "d", "e", "f", "g"))
seven = (7, ("a", "c", "f"))
eight = (8, ("a", "b", "c", "d", "e", "f", "g"))
nine = (9, ("a", "b", "c", "d", "f", "g"))
zero = (0, ("a", "b", "c", "e", "f", "g"))

res1 = 0
for i in file:
    input = List(i).map(lambda v: len(v))
    res1 = res1 + input.count(lenOfOne) + input.count(lenOfFour) + \
        input.count(lenOfSeven) + input.count(lenOfEight)

print(res1)
