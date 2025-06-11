Parts = ["everybody_codes_e2024_q15_p1.txt", "everybody_codes_e2024_q15_p2.txt", "everybody_codes_e2024_q15_p3.txt"]
import heapq
from functools import cache
GraphDict = dict()
Visited = []
import sys
from copy import deepcopy
sys.setrecursionlimit(160000)
SwirlDict = dict()

def GraphBuilder(grid: list, part):
    Start = complex(grid[0].index("."), 0)
    FloodFind(grid, Start)
    Ends = []
    if part == 1:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if "H" in grid[i][j]:
                    Ends.append(complex(j, i))
    elif part == 2 or part == 3:
        Herbs = dict()
        Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in Herbs and grid[i][j] in Alphabet:
                    Herbs[grid[i][j]] = []
        for herb in Herbs.keys():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if herb in grid[i][j]:
                        Herbs[herb].append(complex(j, i))
    return Start, Herbs


def FloodFind(grid:list, Node:complex):
    if Node in Visited:
        return
    if Node not in GraphDict:
        GraphDict[Node] = []
    x = int(Node.real)
    y = int(Node.imag)
    Visited.append(Node)
    time = 1
    if y > 0 and grid[y-1][x] != "#" and grid[y-1][x] != "~" and grid[y-1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y-1), time))
        FloodFind(grid, complex(x, y-1))
    if y < len(grid)-1 and grid[y+1][x] != "#" and grid[y+1][x] != "~" and grid[y+1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y+1), time))
        FloodFind(grid, complex(x, y+1))
    if x > 0 and grid[y][x-1] != "#" and grid[y][x-1] != "~" and grid[y][x-1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x-1, y), time))
        FloodFind(grid, complex(x-1, y))
    if x < len(grid[0])-1 and grid[y][x+1] != "#" and grid[y][x+1] != "~" and grid[y][x+1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x+1, y), time))
        FloodFind(grid, complex(x+1, y))

#### ^^^^^ Look Familiar? ^^^^^ ####

def Solve(part):
    global Start
    global Herbs
    global DistanceHerbs
    global SwirlDict
    with open(Parts[part-1], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        grid = deepcopy(inp)
        Start, Herbs = GraphBuilder(grid, part)
        if part == 1:
            Solve1(Start, Herbs)
        elif part == 2 or part == 3:
            from itertools import permutations
            DistanceHerbs = dict()
            possibilities = permutations(range((len(Herbs)+1)))
            for possible in possibilities:
                SwirlDict = LTD(possible)
                Herbs["Start"] = [Start]
                for herb in Herbs.values():
                    for place in herb:
                        DistanceHerbs[place] = Dijk(place)
                result = Solve22((Start, 0))
                print(result)

def LTD(L):
    D = dict()
    for i in range(len(L)):
        D[L[i]] = L[(i+1)%len(L)]  
    return D        

def Solve1(Start:complex, Herbs):
    Distances = {node: float("infinity") for node in GraphDict.keys()}
    Distances[(Start.real,Start.imag)] = 0
    queue = [((Start.real,Start.imag), 0)]
    while queue:
        (CNodeX, CNodeY), CDistance = heapq.heappop(queue)
        CNode = complex(CNodeX, CNodeY)
        if CDistance > Distances[CNode]:
            continue
        for adjacent, weight in GraphDict[CNode]:
            distance = CDistance + weight
            if distance < Distances[adjacent]:
                Distances[adjacent] = distance
                heapq.heappush(queue, ((adjacent.real, adjacent.imag), distance))
    Paths = []
    for herb in Herbs:
        Paths.append(Distances[herb])
    print(min(Paths)*2)


def Solve22(CNode):
    if Start != DistanceHerbs[CNode[0]][0][0]:
        routes = []
        for herb in DistanceHerbs[CNode[0]]:
            routes.append(CNode[1] + Solve22(herb))
        return min(routes)
    else:
        return CNode[1] + DistanceHerbs[CNode[0]][0][1]


def Dijk(Start:complex):
    Distances = {node:float("infinity") for node in GraphDict.keys()}
    WhichHerb = -5
    for i in range(len(Herbs)):
        if Start in list(Herbs.values())[i]:
            WhichHerb = i
    Distances[Start] = 0
    queue = []
    heapq.heappush(queue, (0, (Start.real, Start.imag)))
    Visited = set() 
    while queue:
        CDistance, (CNodeX, CNodeY) = heapq.heappop(queue)
        CNode = complex(CNodeX, CNodeY)
        
        Visited.add(CNode)

        for adjacent, weight in GraphDict[CNode]:
            if adjacent in Visited:
                continue
            NDistance = CDistance + weight
            if NDistance < Distances[adjacent]:
                Distances[adjacent] = NDistance
                heapq.heappush(queue, (NDistance, (adjacent.real, adjacent.imag)))
    
    results = []
    for square in list(Herbs.values())[(SwirlDict[WhichHerb])]:
        if square != Start or WhichHerb == len(Herbs.items()):
            results.append((square, Distances[square]))
    return results


        

    



Solve(3)