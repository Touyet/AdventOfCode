def main():
    data = ""
    with open("./2018/j8.txt", 'r') as f:
        data = f.read()

    ex = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

    print(p2(data))


def p2(data: str):
    entries = data.split()
    entryNode = getMetadataSumWithObject(entries)[0]
    return entryNode.getScore(), entryNode.getBruteScore()


def getMetadataSumWithObject(entries: "list[str]", index=0):
    nextIndex = 0
    while (1):
        child, metadata = int(entries[index]), int(entries[index+1])
        index = index+2  # first child or first metadata entry
        node = Node()
        for i in range(child):
            loop = getMetadataSumWithObject(entries, index)
            node.child.append(loop[0])
            index = loop[1]

        nextIndex = index + metadata
        for i in range(metadata):
            data = int(entries[index+i])
            node.metadata.append(data)
        index = nextIndex
        break
    return node, index


class Node:
    def __init__(self) -> None:
        self.child: list["Node"] = []
        self.metadata: list[int] = []
        self.score = None
        self.bruteScore = 0

    def getScore(self):
        if(self.score is not None):
            return self.score
        self.score = 0
        if(not self.child):
            self.score = sum(self.metadata)
        else:
            for i in self.metadata:
                if(i == 0):
                    continue
                if(i <= len(self.child)):
                    self.score += self.child[i-1].getScore()
        return self.score

    def getBruteScore(self):
        self.bruteScore = sum(self.metadata)
        for i in self.child:
            self.bruteScore += i.getBruteScore()
        return self.bruteScore


main()
