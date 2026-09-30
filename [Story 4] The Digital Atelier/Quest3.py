import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e4_q03_p1.txt", "everybody_codes_e4_q03_p2.txt", "everybody_codes_e4_q03_p3.txt"]
from itertools import cycle

def SolveBetween(minx, maxx, miny, maxy, InitialColourGreen = True):
    global Voffset, Hoffset

    HoffsetCycle = cycle(Hoffset)
    y1 = None
    y2 = next(HoffsetCycle)
    Groups = [0, 0]

    for y in range(miny, maxy + 1):
        VoffsetCycle = cycle(Voffset)
        x1 = None
        x2 = next(VoffsetCycle)

        y1 = y2
        y2 = next(HoffsetCycle)

        if not y1 and y != miny:
            InitialColourGreen = not InitialColourGreen
        Green = InitialColourGreen

        for x in range(minx, maxx + 1):
            add = False
            x1 = x2
            x2 = next(VoffsetCycle)
            if ((x1 and y % 2 == 0) or (not x1 and y % 2 == 1)) and x != minx:
                Green = not Green
            if x1 != x2 or y1 != y2:
                continue
            if x % 2 == 1 and y % 2 == 1 and not x1 and not x2 and not y1 and not y2:
                add = True
            elif x % 2 == 0 and y % 2 == 1 and not x1 and not x2 and y1 and y2:
                add = True
            elif x % 2 == 1 and y % 2 == 0 and x1 and x2 and not y1 and not y2:
                add = True
            elif x % 2 == 0 and y % 2 == 0 and x1 and x2 and y1 and y2:
                add = True
            if add:
                if Green:
                    Groups[0] += 1
                else:
                    Groups[1] += 1
    return Groups

def LengthCheck():
    global Voffset, Hoffset

    VoffsetCycle = cycle(Voffset)
    x2 = next(VoffsetCycle)

    TileLengths = []

    Green = True
    PrevTiles = [True]
    for x in range(1, len(Voffset)*10):
        x1 = x2
        x2 = next(VoffsetCycle)
        if not x1 and x != 1:
            Green = not Green
        PrevTiles.append(Green)
        if PrevTiles[:len(PrevTiles)//2] == PrevTiles[len(PrevTiles)//2:] and True in PrevTiles and False in PrevTiles:
            TileLengths.append(len(PrevTiles)//2)
            break
        
    HoffsetCycle = cycle(Hoffset)
    y2 = next(HoffsetCycle)

    Green = True
    PrevTiles = [True]

    for y in range(1, len(Hoffset)*10):
        y1 = y2
        y2 = next(HoffsetCycle)
        if y1 and y != 1:
            Green = not Green
        PrevTiles.append(Green)
        if PrevTiles[:len(PrevTiles)//2] == PrevTiles[len(PrevTiles)//2:] and True in PrevTiles and False in PrevTiles:
            TileLengths.append(len(PrevTiles)//2)
            return TileLengths
        




def Solve(part):
    global Voffset, Hoffset
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split("=")[1], f.readlines()))
        width = int(inp[0])
        height = int(inp[1])
        Hoffset = list(map(lambda x: False if x == "0" else True, inp[2]))
        Voffset = list(map(lambda x: False if x == "0" else True, inp[3]))


    
    if part == 1:
        print(sum(SolveBetween(1, width, 1, height)))
    elif part == 2:
        print(max(SolveBetween(1, width, 1, height)))
    elif part == 3:
        Groups = [0, 0]
        SingleCell = SolveBetween(1, 2*len(Voffset), 1, 2*len(Hoffset))

      
        rows = height//(2*len(Hoffset))
        columns = width//(2*len(Voffset))

        Groups = [SingleCell[0] * rows * columns, SingleCell[1] * rows * columns]

        SingleCell = SolveBetween(width - (width % (2*len(Voffset))) + 1, width, 1, (2*len(Hoffset)))
        Groups = [Groups[0] + (SingleCell[0] * rows), Groups[1] + (SingleCell[1] * rows)]

        SingleCell = SolveBetween(1, (2*len(Voffset)), height - (height % (2*len(Hoffset))) + 1, height)
        Groups = [Groups[0] + (SingleCell[0] * columns), Groups[1] + (SingleCell[1] * columns)]

        Groups = list(map(sum, zip(Groups, SolveBetween(width - (width % (2*len(Voffset))) + 1, width, height - (height % (2*len(Hoffset))) + 1, height))))


        print(max(Groups))


Solve(1)
Solve(2)
Solve(3)