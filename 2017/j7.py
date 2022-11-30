from typing import TypedDict
from tools.utils import List


def main():
    f = open("./2017/j7.txt", 'r')
    data: list[str] = f.read().splitlines()

    base, tower = p1(data)
    res = p2(tower, base)
    print(base["name"], res)


NodeDict = TypedDict("NodeDict", name=str, nominalWeight=int,
                     held=bool, branchesWeight="List[int]", hold=List[str], isBalanced=bool,
                     totalWeight=int)


def p1(lines: "list[str]"):
    tower: "List[NodeDict]" = List()
    for line in lines:
        input = line.replace('(', '').replace(')', '').replace(',', '').split()
        d: NodeDict = {"name": input[0],
                       "nominalWeight": int(input[1]),
                       "held": len(input[3:]) == 0,
                       "branchesWeight": List(),
                       "totalWeight": 0,
                       "hold": List(input[3:]),
                       "isBalanced": False}

        if(len(d["hold"]) > 0):
            d["hold"].sort()
        tower.append(d)

        if(d["held"] is False):
            childs = tower.filter(
                lambda v:  d["hold"].find(v["name"]) is not None)
            for c in childs:
                c["held"] = True
            d["held"] = tower.find(
                lambda v:  v["hold"].find(d["name"]) is not None) is not None
    base = tower.find(lambda v: v["held"] is False)
    return base, tower


def p2(tower: "List[NodeDict]", startNode: NodeDict):

    computeNodeWeigth(tower, startNode)
    hasBalanced = True
    while(hasBalanced):
        topLevel = tower.filter(lambda v: len(
            v["hold"]) == 0).map(lambda v: v["name"])
        topLevelParent: "List[NodeDict]" = List()
        for name in topLevel:
            node = tower.find(lambda v: name in v["hold"])
            if(node is not None):
                topLevelParent.append(node)

        nonBalancedNode = topLevelParent.find(
            lambda v: v["isBalanced"] is False)
        if(nonBalancedNode is not None):
            faultyChildIndex = -1
            for branch in nonBalancedNode["branchesWeight"]:
                if(len(nonBalancedNode["branchesWeight"].filter(lambda v: v == branch)) == 1):
                    faultyChildIndex = nonBalancedNode["branchesWeight"].index(
                        branch)
                    break
            faultyChildName = nonBalancedNode["hold"][faultyChildIndex]
            faultyWeight = nonBalancedNode["branchesWeight"][faultyChildIndex]
            faultyChild = tower.find(
                lambda v: v["name"] == faultyChildName)
            if(faultyChildIndex == 0):
                correctWeight = nonBalancedNode["branchesWeight"][faultyChildIndex+1]
            elif(faultyChildIndex == len(nonBalancedNode["branchesWeight"])-1):
                correctWeight = nonBalancedNode["branchesWeight"][faultyChildIndex-1]

            newWeight = faultyChild["nominalWeight"] + \
                correctWeight - faultyWeight
            return newWeight

        tower = tower.filter(lambda v: len(v["hold"]) > 0)

        for parent in topLevelParent:
            parent["hold"].clear()

        topLevel = tower.filter(lambda v: len(
            v["hold"]) == 0)


def computeNodeWeigth(tower: "List[NodeDict]", node: NodeDict):
    if(len(node["hold"]) == 0):
        node["isBalanced"] = True
        return
    if(len(node["branchesWeight"]) > 0):
        return
    heldNode = tower.filter(lambda v: v["name"] in node["hold"])
    for h in heldNode:
        if(h["totalWeight"] == 0):
            computeNodeWeigth(tower, h)
        node["branchesWeight"].append(h["nominalWeight"]+h["totalWeight"])
        node["totalWeight"] = node["totalWeight"] + \
            h["nominalWeight"]+h["totalWeight"]
    currentWeight = None
    for branch in node["branchesWeight"]:
        if(currentWeight is None):
            currentWeight = branch

        if(branch != currentWeight):
            node["isBalanced"] = False
            break
        node["isBalanced"] = True


main()
