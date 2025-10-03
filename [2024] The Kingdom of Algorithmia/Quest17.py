import heapq
from copy import deepcopy
Parts = ["everybody_codes_e2024_q17_p1.txt", "everybody_codes_e2024_q17_p2.txt", "everybody_codes_e2024_q17_p3.txt"]

Dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1]-y[1])

def GroupMaker(coords, oldcoords:list=[], leniency:int=100000):
    DictCoords = dict()
    OldDict = {"Placeholder": 0}
    OlderDict = {"Placeholder2": 2}
    if leniency == 100000:
        while DictCoords != OlderDict:
            for i in range(len(coords)):
                if coords[i] not in DictCoords:
                    DictCoords[coords[i]] = []
                for j in range(len(coords)):
                    if coords[i] != coords[j]:
                        dist = Dist(coords[i], coords[j])
                        NodeDist = (dist, coords[j])
                        if dist < leniency and NodeDist not in DictCoords[coords[i]]:
                            DictCoords[coords[i]].append(NodeDist)
            OlderDict = deepcopy(OldDict)
            OldDict = deepcopy(DictCoords)
    else:
        newcoords = []
        for i in range(len(coords)):
            if coords[i] not in oldcoords:
                newcoords.append(coords[i])
                break
        while DictCoords != OlderDict:
            for i in range(len(newcoords)):
                if newcoords[i] not in DictCoords:
                    DictCoords[newcoords[i]] = []
                for j in range(len(coords)):
                    if newcoords[i] != coords[j]:
                        dist = Dist(newcoords[i], coords[j])
                        NodeDist = (dist, coords[j])
                        if dist < leniency and NodeDist not in DictCoords[newcoords[i]]:
                            DictCoords[newcoords[i]].append(NodeDist)
                            if coords[j] not in newcoords:
                                newcoords.append(coords[j])
            OlderDict = deepcopy(OldDict)
            OldDict = deepcopy(DictCoords)
        oldcoords.extend(newcoords)         
    return DictCoords, oldcoords

def Solve1n2(part):
    with open(Parts[part-1], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        coords = []
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                if inp[y][x] == "*":
                    coords.append((y, x))
        DictCoords = GroupMaker(coords)[0]
        print(DictCoords)
        print(Primmy(coords, DictCoords))

def Primmy(coords:list, DictCoords:dict):
    Distances = []
    Visited = set()
    total = 0
    STart = list(DictCoords.keys())[0]
    Visited.add(STart)
    for NDist, NNode in DictCoords[STart]:
        heapq.heappush(Distances, (NDist, STart, NNode))
    while Distances:
        NDist, CNode, NNode = heapq.heappop(Distances)
        if NNode in Visited:
            continue
        total += NDist
        Visited.add(NNode)
        for ADist, ANode in DictCoords[NNode]:
            if ANode not in Visited:
                heapq.heappush(Distances, (ADist, NNode, ANode))
    return total + len(list(DictCoords.values()))

def Solve3():
    with open(Parts[2], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        coords = []
        oldcoords = []
        Constellations = []
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                if inp[y][x] == "*":
                    coords.append((y, x))
        while len(oldcoords) != len(coords):
            DictCoords, oldcoords = GroupMaker(coords, oldcoords, 6)
            Constellations.append(DictCoords)
        BrightestConstellations = []
        for Constellation in Constellations:
            if list(Constellation.values()) != [[]]:
                BrightestConstellations.append(Constellation)
        print(*BrightestConstellations, sep="\n\n")
        Constellations = list(map(lambda x: Primmy(coords, x), BrightestConstellations))
        Constellations.sort(reverse=True)
        print(Constellations)
        print(Constellations[0]*Constellations[1]*Constellations[2])
        


Solve3()