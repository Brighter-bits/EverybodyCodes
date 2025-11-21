import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q14_p1.txt", "everybody_codes_e2025_q14_p2.txt", "everybody_codes_e2025_q14_p3.txt"]

def LTS(list):
    string = ""
    for part in list:
        for piece in part:
            string += piece + "|"
        string = string[:-1]
        string += ","
    return string[:-1]

def STL(string):
    list2 = string.split(",")
    list2 = list(map(lambda x: x.split("|"), list2))
    return list2

def Check(grid, coord:complex):
    x = int(coord.real)
    y = int(coord.imag)
    neighbours = 0
    if grid[y][x] == "#":
        active = True
    else:
        active = False
    if x > 0 and y > 0 and grid[y-1][x-1] == "#":
        neighbours += 1
    if x > 0 and y < len(grid)-1 and grid[y+1][x-1] == "#":
        neighbours += 1
    if x < len(grid[0]) - 1 and y > 0 and grid[y-1][x+1] == "#":
        neighbours += 1
    if x < len(grid[0]) - 1 and y < len(grid)-1 and grid[y+1][x+1] == "#":
        neighbours += 1
    
    if (active and neighbours % 2 == 1) or (not active and neighbours % 2 == 0):
        return True
    else:
        return False

def Extract(grid):
    answer = []
    for i in range(13, 21):
        answer.append(grid[i][13:21])
    return answer

from functools import cache
@cache
def FullCheck(Tiles):
    Tiles = STL(Tiles)
    newTiles = deepcopy(Tiles)
    for y in range(len(Tiles)):
        for x in range(len(Tiles[0])):
            if Check(Tiles, complex(x, y)):
                newTiles[y][x] = "#"
            else:
                newTiles[y][x] = "."
    
    return newTiles

from copy import deepcopy
def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))

        total = 0
        if part == 1 or part == 2:
            for i in range(2025 if part == 2 else 10):
                newinp = deepcopy(inp)
                for y in range(len(inp)):
                    for x in range(len(inp)):
                        if Check(inp, complex(x, y)):
                            newinp[y][x] = "#"
                        else:
                            newinp[y][x] = "."
                inp = deepcopy(newinp)
                for line in inp:
                    total += line.count("#")
            print(total)
        if part == 3:
            Tiles = [["." for a in range(34)] for b in range(34)]
            # adder = 0
            # for line in inp:
            #     adder += line.count("#")
            first = -1
            previous = []
            previ = 0
            i = 0
            possibleloop = False
            while True:
                Tiles = deepcopy(FullCheck(LTS(Tiles)))
                if inp == Extract(Tiles):
                    adder = 0
                    for line in Tiles:
                        adder += line.count("#")
                    if first == -1:
                        first = (i, adder)
                        previ = i
                    else:
                        diff = i - previ
                        previous.append((diff, adder))
                        if len(previous) > 1:
                            if not possibleloop:
                                if previous[:len(previous)//3] == previous[len(previous)//3:2*len(previous)//3] and previous[len(previous)//3:2*len(previous)//3] == previous[2*len(previous)//3:]: # If it loops three times then it MUST be a loop right?
                                    possibleloop = True
                            else:
                                if previous[0] == previous[-1]:
                                    break
                                else:
                                    possibleloop = False
                                    
                        previ = i
                i += 1
            previous = previous[:-1]
            Turns = 1000000000
            counter = 0
            Turns -= first[0]
            total += first[1]
            while Turns > 0:
                Turns -= previous[counter][0]
                if Turns > 0:
                    total += previous[counter][1]
                    counter = (counter+1)%len(previous)
            print(total)

for i in range(1, 4):
    Solve(i)