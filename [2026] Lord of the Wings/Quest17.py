import os
from pathlib import Path
import heapq
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q17_p1.txt", "everybody_codes_e2026_q17_p2.txt", "everybody_codes_e2026_q17_p3.txt"]

def Flood(inp, x, y): # A simple floodfill algorithm that returns all the coordinates of each block
    global visited, GraphDict
    if (x, y) in visited:
        return
    visited.add((x, y))
    GraphDict[(x, y)] = []

    if x + 1 < len(inp[0]) and inp[y][x+1] == "#":
        GraphDict[(x, y)].append((x+1, y))
        Flood(inp, x+1, y)
    if x - 1 >= 0 and inp[y][x-1] == "#":
        GraphDict[(x, y)].append((x-1, y))
        Flood(inp, x-1, y)
    if y + 1 < len(inp) and inp[y+1][x] == "#":
        GraphDict[(x, y)].append((x, y+1))
        Flood(inp, x, y+1)
    if  y - 1 >= 0 and inp[y-1][x] == "#":
        GraphDict[(x, y)].append((x, y-1))
        Flood(inp, x, y-1)

def DotFlood(inp, x, y): # A more complex floodfill which finds all of the edges of the dots in a group
    global visited
    if (x, y) in visited:
        return []
    lines = []
    visited.add((x, y))
    GraphDict[(x, y)] = []

    if x + 1 < len(inp[0]) and inp[y][x+1] == ".": # If the adjacent is a dot, then fill it, if it isn't a dot, then its an edge
        lines.extend(DotFlood(inp, x+1, y))
    elif x + 1 < len(inp[0]):
        lines.append(f"{x}.{y+1}.V")

    if x - 1 >= 0 and inp[y][x-1] == ".":
        lines.extend(DotFlood(inp, x-1, y))
    elif x - 1 >= 0:
        lines.append(f"{x}.{y}.V")

    if y + 1 < len(inp) and inp[y+1][x] == ".":
        lines.extend(DotFlood(inp, x, y+1))
    elif y + 1 < len(inp):
        lines.append(f"{x}.{y+1}.H")

    if  y - 1 >= 0 and inp[y-1][x] == ".":
        lines.extend(DotFlood(inp, x, y-1))
    elif y - 1 >= 0:
        lines.append(f"{x}.{y}.H")


    if x + 1 < len(inp[0]) and y + 1 < len(inp) and inp[y+1][x+1] == ".": # Diagonals
        lines.extend(DotFlood(inp, x+1, y + 1))

    if x - 1 >= 0 and y - 1 >= 0 and inp[y-1][x-1] == ".":
        lines.extend(DotFlood(inp, x-1, y - 1))

    if x - 1 >= 0  and y + 1 < len(inp) and inp[y+1][x-1] == ".":
        lines.extend(DotFlood(inp, x - 1, y+1))

    if x + 1 < len(inp[0]) and y - 1 >= 0 and inp[y-1][x+1] == ".":
        lines.extend(DotFlood(inp, x + 1, y-1))

    return lines

def LineFlood(inp, x, y): # This finds every edge that LegoLink will traverse
    global visited, GraphDict, bindings
    if (x, y) in visited:
        return
    visited.add((x, y))

    if x + 1 < len(inp[0]) and inp[y][x+1] == "#":
        LineFlood(inp, x+1, y)
    else:
        bindings.append(f"{x}.{y+1}.V")
    if x - 1 >= 0 and inp[y][x-1] == "#":
        LineFlood(inp, x-1, y)
    else:
        bindings.append(f"{x}.{y}.V")
    if y + 1 < len(inp) and inp[y+1][x] == "#":
        LineFlood(inp, x, y+1)
    else:
        bindings.append(f"{x}.{y+1}.H")
    if y - 1 >= 0 and inp[y-1][x] == "#":
        LineFlood(inp, x, y-1)
    else:
        bindings.append(f"{x}.{y}.H")

def Dijkstra(connections, start) -> dict: # YAY!
    distances = {node:float("infinity") for node in connections.keys()}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        newDistance, node = heapq.heappop(queue)
        if newDistance > distances[node]:
            continue
        for adjacent in connections[node]:
            distanceSum = newDistance + 1
            if distanceSum < distances[adjacent]:
                distances[adjacent] = distanceSum
                heapq.heappush(queue, (distanceSum, adjacent))
    return distances

def Solve(part):
    global visited, GraphDict, bindings
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        visited = set()
        GraphDict = dict()
        if part == 1: # For part 1, we just flood fill the hashtags, and then we get the distances, and then we find the shortest distance to the end
            Flood(inp, 0, 0)
            distances = Dijkstra(GraphDict, (0, 0))
            print(distances[(len(inp[0])-1, len(inp)-1)])
        elif part == 2: # For Part 2, we find all of the little edges that will be traversed, then find how many there are
            bindings = []
            LineFlood(inp, 0, 0)
            print(len(bindings))
        elif part == 3:
            totalUpRight = 1
            totalDownLeft = 1
            visited = set()

            ######## I'm doing comments like this now. This part calculates the route that goes along the top edge and the right edge of the entire map
            for i in range(len(inp[0])):
                if inp[0][i] == ".": # If we have a gap
                    newLines = DotFlood(inp, i, 0) # We go down this gap and find all the edges it creates
                    totalUpRight += len(newLines) # Then add that on to the total for this route
                else:
                    totalUpRight += 1 # If it's just a rock, then we have a straight edge and just add one

            for i in range(len(inp)): # We do this for the right edge as well
                if inp[i][len(inp[0])-1] == ".":
                    newLines = DotFlood(inp, len(inp[0])-1, i)
                    totalUpRight += len(newLines)
                else:
                    totalUpRight += 1

            visited = set()
            ######## This bit is identical except we're now going down the left and along the bottom
            for i in range(len(inp[0])):
                if inp[len(inp)-1][i] == ".":
                    newLines = DotFlood(inp, i, len(inp)-1)
                    totalDownLeft += len(newLines)
                else:
                    totalDownLeft += 1

            for i in range(len(inp)-1):
                if inp[i][0] == ".":
                    newLines = DotFlood(inp, 0, i)
                    totalDownLeft += len(newLines)
                else:
                    totalDownLeft += 1

            print(min(totalDownLeft, totalUpRight)) # Print the shortest route


for i in range(1, 4):
    Solve(i)