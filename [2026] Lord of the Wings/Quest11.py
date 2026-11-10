import os
from pathlib import Path
import heapq
from copy import deepcopy
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q11_p1.txt", "everybody_codes_e2026_q11_p2.txt", "everybody_codes_e2026_q11_p3.txt"]

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

def FindPortalSum(Connections, nodeNum):
    total = 0
    for i in range(nodeNum): # iterate through every starting point
        Distances = Dijkstra(Connections, i+1) # Find all the distances
        total += sum(Distances.values()) # Sum the distances and then return it
    return total

def pairings(items): # This finds all the unique pairs
    if items == []: # If the list is empty, then yeild an empty list and stop the recursion
        yield []
        return
    first, rest = items[0], items[1:] # Take the first element
    for i, partner in enumerate(rest):
        remaining = rest[:i] + rest[i + 1:] # Find all the other possible elements
        for other in pairings(remaining):
            yield [(first, partner)] + other # Return the unique pairings


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        nodeNum = int(inp[0].split(" ")[1])
        Connections: dict[int, list] = dict()
        
        for i in range(nodeNum): # This is making the initial connections left and right of each node
            Connections[i+1] = [(i+1)%nodeNum + 1]
            Connections[i+1].append((i-1)%nodeNum + 1)

        if part == 1:
            normal = ((nodeNum//2) + ((nodeNum//2) * (nodeNum//2 - 1))) * nodeNum # This is the portal strain without any new connections. It's the distance to the opposite node, plus the triangle number up to that number * 2
        else:
            for i in range(nodeNum): # Part 2 wants the other two further left and right nodes
                Connections[i+1].append((i+2)%nodeNum + 1)
                Connections[i+1].append((i+3)%nodeNum + 1)
                Connections[i+1].append((i-2)%nodeNum + 1)
                Connections[i+1].append((i-3)%nodeNum + 1)
            normal = sum(Dijkstra(Connections, 1).values()) * nodeNum # Since it's symmetrical, we can multiply the first calculation by nodeNum
        
        for skip in inp[2:]: # This implements the new connections
            start, end = list(map(int, skip.split(" ")))
            Connections[start].append(end)
            Connections[end].append(start)

        total = FindPortalSum(Connections, nodeNum) if part == 1 else 0 # Do part 1

        if part == 2:
            totals = []
            originalConnections = deepcopy(Connections)
            for start in range(1, nodeNum + 1): # We literally just iterate over every possible connection
                for end in range(start + 1, nodeNum + 1):
                    if end in Connections[start]: # If the connection already exists, then just skip it
                        continue
                    Connections[start].append(end)
                    Connections[end].append(start)

                    totals.append(FindPortalSum(Connections, nodeNum))
                    
                    Connections = deepcopy(originalConnections)
            total = min(totals)
        elif part == 3:
            totals = []
            originalConnections = deepcopy(Connections)
            for start in range((nodeNum)//8): # Everything above this is just a repeat of a previous cycle
                links = [node for node in list(map(lambda x: (start + (x * (nodeNum/8))) % nodeNum + 1, range(8)))] # Calculate all of the nodes which are going to be linked
                for pairing in pairings(links): # Find the unique pairings, then connect them.
                    Connections[pairing[0][0]].append(pairing[0][1])
                    Connections[pairing[0][1]].append(pairing[0][0])

                    Connections[pairing[1][0]].append(pairing[1][1])
                    Connections[pairing[1][1]].append(pairing[1][0])

                    Connections[pairing[2][0]].append(pairing[2][1])
                    Connections[pairing[2][1]].append(pairing[2][0])

                    Connections[pairing[3][0]].append(pairing[3][1])
                    Connections[pairing[3][1]].append(pairing[3][0])

                    totals.append(FindPortalSum(Connections, nodeNum))
                    Connections = deepcopy(originalConnections)
            total = min(totals)
        print(normal - total)






for i in range(1, 4):
    Solve(i)