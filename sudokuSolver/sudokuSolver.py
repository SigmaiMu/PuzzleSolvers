import math

testPuzzle = [
    [None, None, 1, 9, None, 5, None, None, 7],
    [2, None, None, None, 3, 8, None, 4, 9],
    [None, 4, None, 2, 7, 6, 5, None, 1],
    [None, 2, None, None, None, None, None, 9, 6],
    [None, 5, 4, None, None, 3, None, None, None],
    [1, None, 9, 4, 8, None, 7, None, None],
    [None, 8, 7, 5, None, None, 9, 6, None],
    [None, 1, None, 8, None, 9, None, 7, 4],
    [None, None, None, None, 6, None, None, 8, None]
]

class Puzzles:

    currentPuzzle = None

    def __init__(self, puzzleImported):
        self.imported = True
        self.puzzle = puzzleImported
        Puzzles.currentPuzzle = puzzleImported


    def getRow(self, row):
        return(self.puzzle[row])

    
    def getColumn(self, column):
        colArray = []
        for row in self.puzzle:
            colArray.append(row[column])
        return colArray

    
    def getChunk(self, row, column):
        chunkIndex = [math.floor(row/3)*3, math.floor(column/3)*3]
        chunkArray = []
        for row in range(3):
            for column in range(3):
                rowIndex = chunkIndex[0] + row
                columnIndex = chunkIndex[1] + column
                chunkArray.append(self.puzzle[rowIndex][columnIndex])
        return chunkArray


def solve(puzzle):
    solved = False
    unsolved = Puzzles(puzzle)
    noneExists = True
    while noneExists:
        noneCount = 0
        for row in range(0, 9, 1):
            for column in range(0, 9, 1):
                if unsolved.puzzle[row][column] == None:
                    noneCount += 1
                    probes = []
                    for probe in range(1, 10, 1):
                        inRow = probe in unsolved.getRow(row)
                        inColumn = probe in unsolved.getColumn(column)
                        inChunk = probe in unsolved.getChunk(row, column)
                        if not inRow and not inColumn and not inChunk:
                            probes.append(probe)
                    if len(probes) == 1:
                        unsolved.puzzle[row][column] = probes[0]
        if noneCount == 0:
            noneExists = False
    
    solved = unsolved.puzzle
    return solved


solved = solve(testPuzzle)
for i in solved:
    print(i)