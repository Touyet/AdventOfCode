from tools.utils import List

input: "list[str]" = open("./2022/j7.txt").read().strip().splitlines()


class FS:
    isDir: bool
    name: str
    parent: "FS"
    children: List["FS"]
    size: int
    seen = False

    def __init__(self, name: str, isDir=False, size=0, parent: "FS" = None) -> None:
        self.children = List()
        self.name = name
        self.size = size
        self.parent = parent
        self.isDir = isDir

    def getTotalSize(self) -> int:
        res = self.size
        return res


fs: FS = None


def navigate(fs: FS, command):
    if (fs is None):
        fs = FS(name=command[2], isDir=True)
    elif (command[2] == ".."):
        fs = fs.parent
    else:
        child = FS(name=command[2], isDir=True, parent=fs)
        fs.children.append(child)
        fs = child
    return fs


waitUntilNextCD = False
for command in input:
    c = command.split(' ')
    if (c[0] == "$"):
        instruction = c[1]
        if (instruction == "cd"):
            fs = navigate(fs, c)

    if (c[0].isnumeric()):
        file = FS(name=c[1], isDir=False, size=int(c[0]), parent=fs)
        fs.children.append(file)

while fs.parent is not None:
    fs = fs.parent

# We are in / directory
s = 0
t = 100000
dir = List()


def through(fs: FS) -> int:
    global s, t
    size = fs.getTotalSize()
    for child in fs.children:
        size += through(child)
    if (fs.isDir and size < t):
        s += size
    fs.size = size
    if (fs.isDir):
        dir.append(fs)
    return size


through(fs)
total = 70000000 - fs.size
necessary = 30000000
d = abs(total-necessary)

sDir = dir.map(lambda v: v.size).filter(lambda v, i: v >= d)

print(s, min(sDir))
