import os
from pathlib import Path
import sys
from itertools import product
from collections import defaultdict
from copy import deepcopy
sys.setrecursionlimit(1000000)
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q14_p1.txt", "everybody_codes_e2026_q14_p2.txt", "everybody_codes_e2026_q14_p3.txt"]

visited = set()
bindings = set()

def Flood(inp, x, y, piece): # Flood Fill to get all of the binding lines.
    global visited
    if (x, y) in visited:
        return 0

    visited.add((x, y))

    if x + 1 < len(inp[0]) and inp[y][x+1] == piece:
        Flood(inp, x+1, y, piece)
    else:
        if not x + 1 < len(inp[0]):
            bindings.add(f"FRAME.{piece}.H.{x+1}.{y}")
        else:
            a, b = sorted([piece, inp[y][x+1]])
            bindings.add(f"{a}.{b}.H.{x+1}.{y}")

    if x - 1 >= 0 and inp[y][x-1] == piece:
        Flood(inp, x-1, y, piece)
    else:
        if not x - 1 >= 0: # If we're out of bounds, we have hit the frame
            bindings.add(f"FRAME.{piece}.H.{x}.{y}")
        else:
            a, b = sorted([piece, inp[y][x-1]]) # To make sure the set works, we sort the two pieces
            bindings.add(f"{a}.{b}.H.{x}.{y}") # group1.group2.HorizontalOrVertical.xCoord.yCoord

    if y + 1 < len(inp) and inp[y+1][x] == piece:
        Flood(inp, x, y+1, piece)
    else:
        if not y + 1 < len(inp):
            bindings.add(f"FRAME.{piece}.V.{x}.{y+1}")
        else:
            a, b = sorted([piece, inp[y+1][x]])
            bindings.add(f"{a}.{b}.V.{x}.{y+1}")


    if  y - 1 >= 0 and inp[y-1][x] == piece:
        Flood(inp, x, y-1, piece)
    else:
        if not y - 1 >= 0:
            bindings.add(f"FRAME.{piece}.V.{x}.{y}")
        else:
            a, b = sorted([piece, inp[y-1][x]])
            bindings.add(f"{a}.{b}.V.{x}.{y}")

def DijkstraIThinkFFSItsPrims(GraphDict:defaultdict[str, defaultdict[str, int]], start) -> dict: # Prim's algorithm, not Dijkstra
    cheapestCost = dict()
    cheapestEdge = dict()

    for key in GraphDict.keys():
        cheapestCost[key] = (float("inf"))
        cheapestEdge[key] = None

    explored = set()
    unexplored = set(list(GraphDict.keys()))

    while unexplored:
        currentNode, cost = sorted([a for a in sorted(list(cheapestCost.items())) if a[0] in unexplored], key=lambda x: (x[1], x[0]))[0]
        unexplored.remove(currentNode)
        explored.add(currentNode)

        for adjacent in GraphDict[currentNode]:
            if adjacent in unexplored and GraphDict[currentNode][adjacent] < cheapestCost[adjacent]:
                cheapestCost[adjacent] = GraphDict[currentNode][adjacent]
                cheapestEdge[adjacent] = (currentNode, adjacent)
    result = 0
    for node in GraphDict.keys():
        result += cheapestCost[node] if cheapestCost[node] != float("inf") else 0
    return result


def Solve(part):
    global bindings, visited
    with open(Parts[part-1]) as f:
        bindings = set()
        visited = set()
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        pieces = []
        for x, y in product(range(len(inp[0])), range(len(inp))): # Find every piece, a coordinate of one of the cells, and also what symbol is in the cell. Weirdly I didn't use this list again, I sort of forgot about it.
            if inp[y][x] not in [a[0] for a in pieces]:
                pieces.append((inp[y][x], x, y))
        for piece in list(pieces):
            Flood(inp, piece[1], piece[2], piece[0])
        


        if part == 1:
            print(len(bindings)) # Just print the number of unique bindings
        else:
            GraphDict: defaultdict[str, defaultdict[str, int]] = defaultdict(lambda: defaultdict(int)) # We now have our GraphDict, which I have decided to overcomplicate
            panes = set()
            for binding in bindings: # Take our bindings, and parse the input into the dictionary
                binding = binding.split(".")
                nodeA = binding[0]
                nodeB = binding[1]
                panes.add(nodeA)
                panes.add(nodeB)
                GraphDict[nodeA][nodeB] += 1
                GraphDict[nodeB][nodeA] += 1
            if part == 2:
                print(DijkstraIThinkFFSItsPrims(GraphDict, "FRAME")) # For part 2, we just need to run this once.
            elif part == 3:
                keys = list(GraphDict.keys()) # Get all of the pieces' symbols
                totals = []
                for key1 in range(len(keys)):
                    for key2 in range(key1 + 1, len(keys)): # Choose the two pieces to zap
                        if keys[key1] == "FRAME" or keys[key2] == "FRAME": # DO NOT ZAP THE FRAME, that would be very bad and it makes the answer a lot lower than it should be
                            continue
                        Original = deepcopy(GraphDict) # Keep a copy of the original so we can reset back to it
                        GraphDict[keys[key1]] = dict.fromkeys(GraphDict[keys[key1]], 0) # Set all of the outgoing connections to 0
                        GraphDict[keys[key2]] = dict.fromkeys(GraphDict[keys[key2]], 0)
                        for key in keys: # Here we set all the outgoing connections to zero, making sure we aren't making any new connections
                            if keys[key1] in GraphDict[key]:
                                GraphDict[key][keys[key1]] = 0
                            if keys[key2] in GraphDict[key]:
                                GraphDict[key][keys[key2]] = 0
                        totals.append(DijkstraIThinkFFSItsPrims(GraphDict, "FRAME")) # Find the binding number
                        GraphDict = deepcopy(Original)
                print(min(totals))

for i in range(1, 4):
    Solve(i)