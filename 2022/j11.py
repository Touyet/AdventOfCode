from functools import reduce
from typing import Callable

from tools.utils import List

# input = open("./2022/j11.txt").read().strip().split("\n\n")
input = open("./2022/j11.txt").read().strip().split("\n\n")


class Monkey:
    text: "List[str]"
    items: "list[int]"
    operation: "list[str]"
    test: Callable[[int], int]
    inspectedItem = 0
    relief = 1

    def __init__(self, text: str) -> None:
        self.text = List(text.splitlines()).map(lambda v: v.strip())
        self.text.pop(0)

        items = self.text[0].split(':')[1]
        self.items = List(items.split(",")).map(int)

        self.operation = self.text[1].split(':')[1].split('=')[1].split()

        self.testValue = int(self.text[2].split().pop())
        true = int(self.text[3].split().pop())
        false = int(self.text[4].split().pop())

        self.test = lambda v: true if v % self.testValue == 0 else false

    def turn(self, monkeys: "list[Monkey]"):
        for item in self.items:
            item = self.computeItem(item)
            passTo = self.test(item)
            monkeys[passTo].items.append(item)
            pass
        self.items = List()

    def computeItem(self, item: int) -> int:
        self.inspectedItem += 1
        left, operand, right = self.operation

        left = item if left == "old" else int(left)
        right = item if right == "old" else int(right)

        if(operand == "+"):
            # return (left+right)//self.relief # Part 1
            return (left+right) % self.relief

        if(operand == "*"):
            # return (left*right)//self.relief # Part 1
            return (left*right) % self.relief

        # return (item)//self.relief # Part 1
        return (item) % self.relief


monkeys: "List[Monkey]" = List(input).map(Monkey)
round = 10000

testValues = monkeys.map(lambda v: v.testValue)

relief = 3  # Part 1

# For part 2, we need to find a relief value to manage the stress.
# It needs to be divisible by every value tested by the monkeys as to not hinder the tests performed.
# We also need to change how we perform the relief process from // to % for the same reasons
relief = reduce(lambda a, b: a*b, testValues)  # Part 2

for i in range(round):
    for monkey in monkeys:
        monkey.relief = relief
        monkey.turn(monkeys)

business = monkeys.map(lambda v: v.inspectedItem)
business.sort(reverse=True)

print(business[0]*business[1])
