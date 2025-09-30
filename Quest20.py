import heapq
from itertools import permutations
from copy import deepcopy
Parts = ["everybody_codes_e2024_q20_p1.txt", "everybody_codes_e2024_q20_p2.txt", "everybody_codes_e2024_q20_p3.txt"]
Dirs = [0+1j, complex(1), 0-1j, complex(-1)] # Up, Right, Down, Left. +1 on the pointer is turn right, -1 on the pointer is turn left
import sys
sys.setrecursionlimit(16000)
HeightChangeFunc = lambda x: -1 if x == "+" else (2 if x == "-" else 1)
def FindPoint(Grid, Letter):
    for y in range(0, len(Grid)-1):
        for x in range(len(Grid[0])):
            if Grid[y][x] == Letter:
                return complex(x, y)
Visited = []
GraphDict = dict()

def FloodFind(grid:list, Node: tuple[int, complex]):
    x = int(Node[1].real)
    y = int(Node[1].imag)
    if Node in Visited:
        return
    if Node not in GraphDict:
        GraphDict[Node] = list()
    Visited.append(Node)
    GraphNodes = []
    if len(GraphDict[Node]) != 0:
        for piece in GraphDict[Node]:
            GraphNodes.append(piece[0][1])

    if y > 0 and Node[0] != 2 and complex(x, y-1) not in GraphNodes and grid[y-1][x] != "#":
        HeightChange = HeightChangeFunc(grid[y-1][x])
        GraphDict[Node].append(((0, (complex(x, y-1))), HeightChange))
        FloodFind(grid, (0, complex(x, y-1)))

    if y < len(grid)-1 and Node[0] != 0 and complex(x, y+1) not in GraphNodes and grid[y+1][x] != "#":
        HeightChange = HeightChangeFunc(grid[y+1][x])
        GraphDict[Node].append(((2, (complex(x, y+1))), HeightChange))
        FloodFind(grid, (2, complex(x, y+1)))

    if x > 0 and Node[0] != 1 and complex(x-1, y) not in GraphNodes and grid[y][x-1] != "#":
        HeightChange = HeightChangeFunc(grid[y][x-1])
        GraphDict[Node].append(((3, (complex(x-1, y))), HeightChange))
        FloodFind(grid, (3, complex(x-1, y)))

    if x < len(grid[0])-1 and Node[0] != 3 and complex(x+1, y) not in GraphNodes and grid[y][x+1] != "#":
        HeightChange = HeightChangeFunc(grid[y][x+1])
        GraphDict[Node].append(((1, (complex(x+1, y))), HeightChange))
        FloodFind(grid, (1, complex(x+1, y)))

# def Feeler(Grid, Start:complex, Instructions):
#     Glider = Start
#     Direction = 0 # Downwards
#     Height = 1000
#     for char in Instructions:
#         if char == "1":
#             Direction += 1
#         if char == "2":
#             Direction -= 1
#         Direction %= 4
#         Glider += Dirs[Direction]
#         if Grid[int(Glider.imag)][int(Glider.real)] == "#":   #### Brute Force approach did not work ####
#             return -1
#         if Grid[int(Glider.imag)][int(Glider.real)] == ".":
#             Height -= 1
#         if Grid[int(Glider.imag)][int(Glider.real)] == "-":
#             Height -= 2
#         if Grid[int(Glider.imag)][int(Glider.real)] == "+":
#             Height += 1
#     return Height
def BellManFord(Start, Time, previousDistances = []):
    if len(previousDistances) == 0:
        Distances = {node: (float("infinity"), 0) for node in GraphDict.keys()}
        Distances[Start] = (0, 0)
    else:
        Distances = previousDistances
    NewDistances = deepcopy(Distances)
    for CNode in GraphDict.keys():
        for ANode in GraphDict[CNode]:
            if Distances[CNode][0] + ANode[1] < NewDistances[ANode[0]][0]:
                NewDistances[ANode[0]] = (Distances[CNode][0] + ANode[1], Time)
    return NewDistances


    


def WeirdDijkstra(Start, Tlimit, previousQueue = [], previousDistances = {}):
    if len(previousQueue) == 0:
        Distances = {node: (float("infinity"), 0) for node in GraphDict.keys()}
        Distances[Start] = (0, 0)
        queue = [(0, 0, Start[0], Start[1].real, Start[1].imag)] #Distance, Time, Dir, Real, Imag
    else:
        Distances = previousDistances
        queue = previousQueue
    Going = True
    while queue and Going:
        CDistance, CTime, CDir, CReal, CImag = heapq.heappop(queue)
        CNode = (CDir, complex(CReal, CImag))
        if CTime >= Tlimit:
            heapq.heappush(queue, (CTime, CDistance, CDir, CReal, CImag))
            Going = False
            break
        if CDistance > Distances[CNode][0]:
            continue
        for adjacent, weight in GraphDict[CNode]:
            distance = (CDistance + weight, CTime + 1)
            if distance[0] < Distances[adjacent][0]:
                Distances[adjacent] = distance
                heapq.heappush(queue, (distance[0], distance[1], adjacent[0], adjacent[1].real, adjacent[1].imag))
    return Distances, queue

def AddTuples(x:tuple[int, int], y:tuple[int, int]) -> tuple[int, int]: return (x[0] + y[0], x[1] + y[1])

from functools import cache
@cache
def AddFourTuples(a:tuple[int, int], b:tuple[int, int], c:tuple[int, int], d:tuple[int, int]): return AddTuples(AddTuples(AddTuples(a, b), c), d)

def DictMix(Dict:dict, Start):
    option = [x for x in Dict.keys() if x != Start]
    Totals = []
    individualTotals = []
    option = list(option)
    option.append(Start)
    option.insert(0, Start)

    for i in range(len(option) - 1):
        individualTotals.append(Dict[option[i]][option[i+1]])
    for i in individualTotals[0]:
        for j in individualTotals[1]:
            for k in individualTotals[2]:
                for l in individualTotals[3]:
                    Totals.append(AddFourTuples(i, j, k, l))


    return Totals

def ListCheck(value, list):
    for i in list:
        if value >= i[0]:
            return False
    return True



def NormalDijkstra(Start, Tlimit):
    Distances = {node: (float("infinity"), 0) for node in GraphDict.keys()}
    Distances[Start] = (0, 0)
    queue = [(0, 0, 0, Start[0], Start[1].real, Start[1].imag)] # Distance, Time, Dir, Real, Imag
    while queue:
        IDK, CDistance, CTime, CDir, CReal, CImag = heapq.heappop(queue)
        CNode = (CDir, complex(CReal, CImag))
        if CDistance > Distances[CNode][0] or CTime == Tlimit:
            continue
        for adjacent, weight in GraphDict[CNode]:
            distance = (CDistance + weight, CTime + 1)
            if distance[0] < Distances[adjacent][0]:
                Distances[adjacent] = distance
                heapq.heappush(queue, (distance[1]-distance[0], distance[0], distance[1], adjacent[0], adjacent[1].real, adjacent[1].imag))
    return Distances

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        Start = FindPoint(inp, "S")
        FloodFind(inp, (2, Start))
        if part == 1:
            distances = NormalDijkstra((2, Start), 100)
            distances = [x for x in list(map(lambda x: x[0] if x[1] == 100 else None, distances.values())) if x is not None]
            import os
            os.system("cls")
            print(1000 - min(distances))
        elif part == 2:
            Points = [x for x in list(map(lambda x: FindPoint(inp, x), list("ABCDEFGHIJKLMNOPQRTUVWXYZ"))) if x is not None]
            Points.insert(0, Start)
            ShortestDistances = dict()
            for point in Points:
                ShortestDistances[point] = {}
                for OtherPoint in Points:
                    if point != OtherPoint:
                        ShortestDistances[point][OtherPoint] = [(1000, 1000)]
            dists = {}
            round = 1
            while True:
                distances = dict()
                for StartingPoint in Points:
                    dists[StartingPoint] = BellManFord((2, StartingPoint), round, dists[StartingPoint] if StartingPoint in dists else [])
                    distances[StartingPoint] = [x for x in list(dists[StartingPoint].items()) if x[0][1] in Points and x[0][1] != StartingPoint and x[1][1] != 0]
                for i in distances:
                    CacheDict = dict()
                    for j in range(len(distances[i])):
                        if distances[i][j][0][1] not in CacheDict or distances[i][j][1][0] < distances[i][j][1][0]:
                            CacheDict[distances[i][j][0][1]] = distances[i][j][1]
                    distances[i] = CacheDict
                for point in list(distances.keys()):
                    for OtherPoint in list(distances[point].keys()):
                        if len(distances[point][OtherPoint]) != 0 and ListCheck(distances[point][OtherPoint][0], ShortestDistances[point][OtherPoint]):
                            ShortestDistances[point][OtherPoint].append(distances[point][OtherPoint])

                values = [x for x in DictMix(ShortestDistances, Points[-1]) if x[0] <= 0]
                
                if len(values) != 0:
                    print(min(values, key=lambda x: x[1])+4) # We add four (one for each node we visit apart from the last one).
                    # breakpoint()
                
                round += 1
        elif part == 3:
            pass

                        

Solve(2)