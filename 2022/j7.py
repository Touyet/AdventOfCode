from tools.utils import List

input: "list[str]" = open("./2022/j7Test.txt").read().strip().splitlines()


class FS:
    isDir: bool
    name: str
    parent: "FS"
    children: List["FS"]
    size: int

    def __init__(self, name: str, isDir=False, size=0, parent: "FS" = None) -> None:
        self.children = List()
        self.name = name
        self.size = size
        self.parent = parent
        self.isDir = isDir

    def getTotalSize(self) -> int:
        res = self.size
        if(self.isDir):
            for i in self.children:
                res += i.getTotalSize()
        return res


fs: FS = None


def navigate(fs: FS, command):
    if(fs is None):
        fs = FS(name=command[2], isDir=True)
    elif(command[2] == ".."):
        fs = fs.parent
    else:
        child = FS(name=command[2], isDir=True, parent=fs)
        fs.children.append(child)
        fs = child
    return fs


waitUntilNextCD = False
for command in input:
    c = command.split(' ')
    if(c[0] == "$"):
        instruction = c[1]
        if(instruction == "cd"):
            fs = navigate(fs, c)

    if(c[0].isnumeric()):
        file = FS(name=c[1], isDir=False, size=int(c[0]), parent=fs)
        fs.children.append(file)

s = 0
t = 100000
while fs.parent is not None:
    size = fs.getTotalSize()
    if(size < t):
        s += size

    fs = fs.parent

print(s)
