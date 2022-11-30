from tools.utils import List


def main():
    f = open("./2021/j4.txt", 'r')
    data = f.read().splitlines()
    drawLot = [int(x) for x in data[0].split(',')]
    data.pop(0)
    data.append('')
    grids: List[Grid] = List()
    currentGrid: Grid = None
    for line in data:
        if(not line):
            if(currentGrid is not None):
                grids.append(currentGrid)
                currentGrid = None
            continue
        if(currentGrid is None):
            currentGrid = Grid()
        currentGrid.addRow(line)

    startDraw(drawLot, grids)
    startDraw(drawLot, grids, False)


def startDraw(drawLot, grids: List["Grid"], stopAtFirst=True):
    lastBingo: Grid = None
    for nb in drawLot:
        for grid in grids:
            bingo = grid.drawNumber(nb)
            if(bingo is not None):
                lastBingo = grid
                if(stopAtFirst):
                    break
        if(stopAtFirst and lastBingo is not None):
            break
        if(len(grids) == 1 and grids[0].bingo):
            break
        grids = grids.filter(lambda v: not v.bingo)

    print(lastBingo.grid)
    print(lastBingo.getScore()*nb)
    print()


class Grid:
    def __init__(self) -> None:
        self.rows: List[List[int]] = List()
        self.columns: List[List[int]] = List()
        self.bingo = False
        self.grid = ""

    def addRow(self, data: str):
        self.grid += data + "\n"
        self.rows.append(List([int(x) for x in data.split()]))
        if(not self.columns):
            self.columns = List(List() for x in data.split())
        for i, nb in enumerate(data.split()):
            self.columns[i].append(int(nb))

    def drawNumber(self, nb: int):
        newRows = List()
        for column in self.rows:
            column = column.filter(lambda v: v != nb)
            newRows.append(column)
            if(not column):
                self.bingo = True
        newCols = List()
        for column in self.columns:
            column = column.filter(lambda v: v != nb)
            newCols.append(column)
            if(not column):
                self.bingo = True

        self.rows = newRows
        self.columns = newCols
        if(self.bingo):
            self.grid = self.grid.strip()
            return self

    def getScore(self):
        res = 0
        for row in self.rows:
            res = res + sum(row)
        return res


main()
