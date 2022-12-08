from tools.utils import List

input: "list[str]" = open("./2015/j7.txt").read().strip().splitlines()

operations: "List[Wire]" = List()


class Wire:
    value: int

    def __init__(self, name: str, op: str) -> None:
        self.name = name.strip()
        self.op = op.lower().strip().split(' ')
        self.value = None

    def getValue(self) -> int:
        if(self.value is not None):
            return self.value
        if(len(self.op) == 1):
            v = self.op[0]
            if(v.isnumeric()):
                self.value = int(v)
                return int(v)
            w = operations.find(lambda u: u.name == v)
            return w.getValue()

        if(len(self.op) == 2):  # NOT instruction
            w = operations.find(lambda u: u.name == self.op[-1])
            val = w.getValue()
            self.value = ~val
            return ~val

        instruction = self.op[1]
        left = int(self.op[0]) if self.op[0].isnumeric(
        ) else operations.find(lambda u: u.name == self.op[0]).getValue()
        right = int(self.op[2]) if self.op[2].isnumeric(
        ) else operations.find(lambda u: u.name == self.op[2]).getValue()

        if(instruction == "and"):
            self.value = left & right
            return left & right
        if(instruction == "or"):
            self.value = left | right
            return left | right
        if(instruction == "lshift"):
            self.value = left << right
            return left << right
        if(instruction == "rshift"):
            self.value = left >> right
            return left >> right
        return 0


for instruction in input:
    operation, wire = instruction.split("->")
    w = Wire(wire, operation)
    operations.append(w)

a = operations.find(lambda v: v.name == "a")
val = a.getValue()

print(val)

for wire in operations:
    wire.value = None

b = operations.find(lambda v: v.name == "b")
b.value = val

a = operations.find(lambda v: v.name == "a")
val = a.getValue()

print(val)
