import os
from pathlib import Path
import sys
from copy import deepcopy
sys.setrecursionlimit(1000000)
from itertools import product
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q12_p1.txt", "everybody_codes_e2026_q12_p2.txt", "everybody_codes_e2026_q12_p3.txt"]

def Flood(inp, x, y): # A simple floodfill algorithm that returns all the coordinates of each block
    global visited
    if (x, y) in visited:
        return []

    visited.add((x, y))

    coords = []

    if x + 1 < len(inp[0]) and inp[y][x+1] == "#":
        coords.extend(Flood(inp, x+1, y))
    if x - 1 >= 0 and inp[y][x-1] == "#":
        coords.extend(Flood(inp, x-1, y))
    if y + 1 < len(inp) and inp[y+1][x] == "#":
        coords.extend(Flood(inp, x, y+1))
    if  y - 1 > 0 and inp[y-1][x] == "#":
        coords.extend(Flood(inp, x, y-1))

    return coords + [(x, y)]

def CreateVerticalCheck(inp, startingCoord): # This and the function beneath take a coordinate and find every single coordinate that a spell could destroy if used.
    line = set([startingCoord])

    counter = 1

    while True:
        if startingCoord[1] + counter < len(inp) and inp[startingCoord[1] + counter][startingCoord[0]] == "#":
            line.add((startingCoord[0], startingCoord[1] + counter))
            counter += 1
        else:
            break
    
    counter = -1

    while True:
        if startingCoord[1] + counter >= 0 and inp[startingCoord[1] + counter][startingCoord[0]] == "#":
            line.add((startingCoord[0], startingCoord[1] + counter))
            counter -= 1
        else:
            break

    return line

def CreateHorizontalCheck(inp, startingCoord):
    line = set([startingCoord])

    counter = 1

    while True:
        if startingCoord[0] + counter < len(inp) and inp[startingCoord[1]][startingCoord[0] + counter] == "#":
            line.add((startingCoord[0] + counter, startingCoord[1]))
            counter += 1
        else:
            break
    
    counter = -1

    while True:
        if startingCoord[0] + counter >= 0 and inp[startingCoord[1]][startingCoord[0] + counter] == "#":
            line.add((startingCoord[0] + counter, startingCoord[1]))
            counter -= 1
        else:
            break
    
    return line

def Reflect(inp, Coords): # This calculates the number of spells required to reflect a block
    spell = 0
    while Coords:
        SpellList = []
        for startingCoord in Coords: # While a bit overkill, we check every single vertical and horizontal spell we could use on the block 
            Horizontal = [a for a in Coords if a[1] == startingCoord[1]] # Find every single coordinate on the same row as the current one
            Horizontal = set(Horizontal) & CreateHorizontalCheck(inp, startingCoord) # Now get rid of any coordinates that are blocked by a hole

            Vertical = [a for a in Coords if a[0] == startingCoord[0]] # Do the same with the Vertical spell
            Vertical = set(Vertical) & CreateVerticalCheck(inp, startingCoord)

            Coords = set(Coords) # Turn the coords list into a set so we can do set manipulation on it
            
            if len(Horizontal) > len (Vertical): # We find which direction would be better
                SpellList.append(Coords - set(Horizontal)) # Add the result of using the spell to the SpellList
            else:
                SpellList.append(Coords - set(Vertical))
            Coords = list(Coords)
        ChosenSpell = min(SpellList, key=lambda x: len(x)) # Now choose the smallest result, and then update the state of our block
        Coords = list(ChosenSpell)
        spell += 1
    return spell


def Solve(part):
    global visited
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        visited = set()
        total = 0
        for x, y, in product(range(len(inp[0])), range(len(inp))): # Iterate over every single x and y coordinate. If it's in a block that we have already visited, then skip it
            if (x, y) in visited:
                continue
            if inp[y][x] == ".":
                visited.add((x, y))
            else:
                BlockCoords = Flood(inp, x, y) # Find the block
                total += Reflect(inp, BlockCoords) # Add the spell number to the total
                    
        print(total)


for i in range(1, 4):
    Solve(i)