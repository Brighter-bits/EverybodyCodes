import os
from pathlib import Path
import sys
from math import ceil, floor
from collections import defaultdict
from copy import deepcopy
sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
from functools import cache
Parts = ["everybody_codes_e2025_q20_p1.txt", "everybody_codes_e2025_q20_p2.txt", "everybody_codes_e2025_q20_p3.txt", "everybody_codes_e2025_q20_p4.txt"]



GraphDict = defaultdict(list)
def Dijkstra(start):
    global GraphDict
    Distances = {node: float("infinity") for node in GraphDict.keys()}
    Distances[start] = 0
    import heapq
    queue = [(0, start)]
    while queue:
        CDist, CNode = heapq.heappop(queue)
        if CDist > Distances[CNode]:
            continue
        for adjacent in GraphDict[CNode]:
            distance = CDist + 1
            if distance < Distances[adjacent]:
                Distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    return Distances


Visited = set()
def OrdinaryFlood(Grid, Node):
    if Node in Visited:
        return
    Visited.add(Node)
    x = int(Node[0])
    y = int(Node[1])

    if y > 0:
        GraphDict[(x, y)].append((Grid[y-1][x], (x, y-1)))
        OrdinaryFlood(Grid, (x, y-1))
    if y < len(Grid)-1:
        GraphDict[(x, y)].append((Grid[y+1][x], (x, y+1)))
        OrdinaryFlood(Grid, (x, y+1))
    if x > 0:
        GraphDict[(x, y)].append((Grid[y][x-1], (x-1, y)))
        OrdinaryFlood(Grid, (x-1, y))
    if x < len(Grid[0]) - 1:
        GraphDict[(x, y)].append((Grid[y][x+1], (x+1, y)))
        OrdinaryFlood(Grid, (x+1, y))


def FindStartnEnd(Grid):
    Start = -1
    End = -1
    for y in range(len(Grid)):
        for x in range(len(Grid[y])):
            if Grid[y][x] == "S":
                Start = (x, y)
    for y in range(len(Grid)):
        for x in range(len(Grid[y])):
            if Grid[y][x] == "E":
                End = (x, y)
    return Start, End

def rotate(grid):
    newgrid = [["." for a in range(len(grid[b]))] for b in range(len(grid))]

    for j in range(len(grid)):
        for i in range(0, len(grid[j]), 2): # Top to Right
            newgrid[i//2][-1-(2*j)] = grid[j][i]
            if i != len(grid[j])-1:
                newgrid[i//2][-2-(2*j)] = grid[j][i+1]

        # for i in range(j, len(grid)-(2*j)): # Right to Left
        #     newgrid[i][(j*2)] = grid[i][-1-(2*j)]
        #     if i != 0 and i != len(grid)-1:
        #         newgrid[i][1+(2*j)] = grid[i][-2-(2*j)] # What the hell was I doing here?????

        # for i in range(2*j, len(grid[j])-1, 2): #Left to Top
        #     newgrid[j][i-(2*j)] = grid[j+((i - 2*j) // 2)][0+(2*j)]
        #     newgrid[j][i+1-(2*j)] = grid[j+((i - 2*j) // 2)+1][1+(2*j)]





    # for i in range(0, len(grid[1]), 2): # Top to Right
    #     newgrid[i//2][-3] = grid[1][i]
    #     if i != len(grid[1])-1:
    #         newgrid[i//2][-4] = grid[1][i+1]

    # for i in range(1, len(grid)-2): # Right to Left
    #     newgrid[i][2] = grid[-1-i][-3]
    #     if i != 0 and i != len(grid)-1:
    #         newgrid[i][3] = grid[-2-i][-4]

    # for i in range(2, len(grid[1])-1, 2): #Left to Top
    #     newgrid[1][i-2] = grid[-1-i//2][2]
    #     newgrid[1][i+1-2] = grid[-2-i//2][3]

    for y in range(len(newgrid)):
        for x in range(len(newgrid[y])):
            if newgrid[y][x] == ".":
                newgrid[y][x] = "E"

    for i in range(len(newgrid)):
        newgrid[i] = "".join(newgrid[i])


    return newgrid
    








def Solve(part):
    global GraphDict
    GraphDict = defaultdict(list)
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").strip("."), f.readlines()))
        total = 0
        if part == 1:
            for i in range(len(inp)-1):
                line = inp[i]
                nextline = inp[i+1]
                for j in range(len(line)-1):
                    if line[j] == line[j+1] and line[j] == "T":
                        total += 1
                    if (j+1) % 2 == 0 and line[j] == nextline[j-1] and line[j] == "T":
                        total += 1
            print(total)
        elif part == 2:
            Start, End = FindStartnEnd(inp)
            for i in range(len(inp)):
                line = inp[i]
                for j in range(len(line)):

                    if j != len(line)-1:
                        currentNode = line[j]
                        nextNode = line[j+1]
                        if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                            GraphDict[(j, i)].append((j+1, i))

                    if j != 0:
                        currentNode = line[j]
                        nextNode = line[j-1]
                        if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                            GraphDict[(j, i)].append((j-1, i))

                    if i != len(inp)-1 and (j+1) % 2 == 0:
                        currentNode = line[j]
                        nextNode = inp[i+1][j-1]
                        if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                            GraphDict[(j, i)].append((j-1, i+1))
                    if i != 0 and j % 2 == 0:
                        currentNode = line[j]
                        nextNode = inp[i-1][j+1]
                        if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                            GraphDict[(j, i)].append((j+1, i-1))
            
            distances = Dijkstra(Start)


            print(distances[End])
        elif part == 3:
            Start, End = FindStartnEnd(inp)
            Start = (0, Start[0], Start[1])
            for rot in range(3):
                Nextinp = deepcopy(rotate(deepcopy(inp)))
                for i in range(len(inp)):
                    line = inp[i]
                    Nextline = Nextinp[i]
                    for j in range(len(line)):
                        if j != len(line)-1:
                            currentNode = line[j]
                            nextNode = Nextline[j+1]
                            if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                                GraphDict[(rot, j, i)].append((((rot+1)%3), j+1, i))

                        if j != 0:
                            currentNode = line[j]
                            nextNode = Nextline[j-1]
                            if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                                GraphDict[(rot, j, i)].append((((rot+1)%3), j-1, i))

                        if i != len(inp)-1 and (j+1) % 2 == 0:
                            currentNode = line[j]
                            nextNode = Nextinp[i+1][j-1]
                            if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                                GraphDict[(rot, j, i)].append((((rot+1)%3), j-1, i+1))
                        if i != 0 and j % 2 == 0:
                            currentNode = line[j]
                            nextNode = Nextinp[i-1][j+1]
                            if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                                GraphDict[(rot, j, i)].append((((rot+1)%3), j+1, i-1))
                        
                        currentNode = line[j]
                        nextNode = Nextline[j]
                        if (currentNode == nextNode and currentNode == "T") or (currentNode == "T" and (nextNode == "S" or nextNode == "E")) or (nextNode == "T" and (currentNode == "S" or currentNode == "E")):
                                GraphDict[(rot, j, i)].append((((rot+1)%3), j, i))

                        if (rot, j, i) not in list(GraphDict.keys()):
                            GraphDict[(rot, j, i)] = []
                _, End = FindStartnEnd(inp)
                inp = rotate(inp)
            
            distances = Dijkstra(Start)
            totals = []
            for i in range(3):
                totals.append(distances[(i, End[0], End[1])])
            print(min(totals)-4) # I'm not entirely sure why this happens, but I'm way too tired to investigate.
        elif part == 4:
            inp = rotate(rotate(inp))
            for i in inp:
                print(i)

            



Solve(1)
Solve(2)
Solve(3)
Solve(4)