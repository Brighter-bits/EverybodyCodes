import os
from pathlib import Path
from copy import deepcopy
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2026_q08_p1.txt", "everybody_codes_e2026_q08_p2.txt", "everybody_codes_e2026_q08_p3.txt"]

class Coord(): # A coordinate class.
    def __init__(self, x, y):
        self.x = x
        self.y = y


def FlattenSE(grid): # This takes the hexagonal grid, and condenses it to a rectangular grid.
    pointer = Coord(0, 0)
    while grid[pointer.y][pointer.x] == ".":
        pointer.y += 1
    FlatGrid = []

    while pointer.y > 0:
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y < len(grid) and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y += 1
            pointer.x += 1
        FlatGrid.insert(0, line)
        lineStart.y -= 1
        lineStart.x += 1
        pointer = deepcopy(lineStart)

    while grid[pointer.y][pointer.x] != ".":
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y < len(grid) and pointer.x < len(grid[0]) and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y += 1
            pointer.x += 1
        FlatGrid.insert(0, line)
        lineStart.x += 2
        pointer = deepcopy(lineStart)
    return FlatGrid

def FlattenSW(grid):
    pointer = Coord(len(grid[0])-1, 0)
    while grid[pointer.y][pointer.x] == ".":
        pointer.y += 1
    FlatGrid = []

    while pointer.y > 0:
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y < len(grid) and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y += 1
            pointer.x -= 1
        FlatGrid.insert(0, line)
        lineStart.y -= 1
        lineStart.x -= 1
        pointer = deepcopy(lineStart)

    while grid[pointer.y][pointer.x] != ".":
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y < len(grid) and pointer.x >= 0 and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y += 1
            pointer.x -= 1
        FlatGrid.insert(0, line)
        lineStart.x -= 2
        pointer = deepcopy(lineStart)
    return FlatGrid

def FlattenNE(grid):
    pointer = Coord(0, len(grid)-1)
    while grid[pointer.y][pointer.x] == ".":
        pointer.y -= 1
    FlatGrid = []

    while pointer.y < len(grid)-1:
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y < len(grid) and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y -= 1
            pointer.x += 1
        FlatGrid.insert(0, line)
        lineStart.y += 1
        lineStart.x += 1
        pointer = deepcopy(lineStart)

    while grid[pointer.y][pointer.x] != ".":
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y >= 0 and pointer.x < len(grid[0]) and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y -= 1
            pointer.x += 1
        FlatGrid.insert(0, line)
        lineStart.x += 2
        pointer = deepcopy(lineStart)
    return FlatGrid

def FlattenNW(grid):
    pointer = Coord(len(grid[0])-1, len(grid)-1)
    while grid[pointer.y][pointer.x] == ".":
        pointer.y -= 1
    FlatGrid = []

    while pointer.y < len(grid)-1:
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y >= 0 and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y -= 1
            pointer.x -= 1
        FlatGrid.insert(0, line)
        lineStart.y += 1
        lineStart.x -= 1
        pointer = deepcopy(lineStart)

    while grid[pointer.y][pointer.x] != ".":
        lineStart = deepcopy(pointer)
        line = []
        while pointer.y >= 0 and pointer.x < len(grid[0]) and grid[pointer.y][pointer.x] != ".":
            line.append((grid[pointer.y][pointer.x], pointer.x, pointer.y))
            pointer.y -= 1
            pointer.x -= 1
        FlatGrid.insert(0, line)
        lineStart.x -= 2
        pointer = deepcopy(lineStart)
    return FlatGrid

def FlattenE(grid):
    SquareGrid = []
    for i in range(len(grid)):
        line = []
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                line.append((grid[i][j], j, i))
        SquareGrid.append(line)
    return SquareGrid

def FlattenW(grid):
    SquareGrid = []
    for i in range(len(grid)):
        line = []
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                line.append((grid[i][j], j, i))
        SquareGrid.append(list(reversed(line)))
    return SquareGrid

def ShadowCheck(line):
    total = 0
    shadowHeight = -1
    illuminated = set()
    for ent in line:
        try:
            if int(ent[0]) >= shadowHeight:
                shadowHeight = int(ent[0]) + 1
                illuminated.add((ent[1], ent[2]))
                total += 1
            shadowHeight -= 1
        except:
            if ent[0] == ".":
                raise ValueError("Something has gone wrong, . found")
            illuminated.add((ent[1], ent[2]))
            shadowHeight -= 1
    return illuminated, total

def Grow(inp, growers):
    warriors = 0
    for coord in growers:
        try:
            inp[coord[1]][coord[0]] = str(int(inp[coord[1]][coord[0]]) + 1)
            if inp[coord[1]][coord[0]] == "10":
                inp[coord[1]][coord[0]] = "C" # It's a C-dling
                warriors += 1
        except:
            match inp[coord[1]][coord[0]]:
                case "C":
                    inp[coord[1]][coord[0]] = "B"
                case "B":
                    inp[coord[1]][coord[0]] = "A"
                case "A":
                    inp[coord[1]][coord[0]] = "1"
                case _:
                    raise ValueError("Something has gone wrong AHHH")
    return inp, warriors



def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        if part == 1:
            SquareGrid = FlattenSE(inp)
            illuminated = []
            for line in SquareGrid:
                illuminated.extend(list(ShadowCheck(line)))
            print(len(illuminated))
        elif part == 2:
            illuminated = []
            for line in FlattenE(inp):
                illuminated.extend(list(ShadowCheck(line)))
            for line in FlattenW(inp):
                illuminated.extend(list(ShadowCheck(line)))
            for line in FlattenNE(inp):
                illuminated.extend(list(ShadowCheck(line)))
            for line in FlattenNW(inp):
                illuminated.extend(list(ShadowCheck(line)))
            for line in FlattenSE(inp):
                illuminated.extend(list(ShadowCheck(line)))
            for line in FlattenSW(inp):
                illuminated.extend(list(ShadowCheck(line)))
            print(len(illuminated))
        elif part == 3:
            warriors = 0
            rounds = 0
            total = 0
            Directions = [FlattenSE, FlattenSW, FlattenW, FlattenNW, FlattenNE, FlattenE]
            while warriors < 100000:
                for line in Directions[rounds%len(Directions)](inp):
                    illuminated, energy = ShadowCheck(line)
                    total += energy
                    inp, newWarriors = Grow(inp, illuminated)
                    warriors += newWarriors
                rounds += 1
            print(total)






for i in range(1, 4):
    Solve(i)