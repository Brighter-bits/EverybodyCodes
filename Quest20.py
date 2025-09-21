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

# def WeirdDijkstra(Start):
#     distances = {node:float("infinity") for node in GraphDict.keys()}
#     distances[Start] = 0
#     for i in range(100):
#         for a in GraphDict.keys():
#             for b in range(len(GraphDict[a])):
#                 if distances[a] + GraphDict[a][b][1] < distances[GraphDict[a][b][0]]:
#                     distances[GraphDict[a][b][0]] = distances[a] + GraphDict[a][b][1]
#     return distances

ManHat = lambda x, y: int(abs(x.real + y.real) + abs(x.imag, y.imag))

def NormalDijkstra(Start, Tlimit):
    Distances = {node: (float("infinity"), 0) for node in GraphDict.keys()}
    Distances[Start] = (0, 0)
    import heapq
    queue = [(0, 0, 0, Start[0], Start[1].real, Start[1].imag)] # Distance, Time, Dir, Real, Imag
    ShortestParent = {node: None for node in GraphDict.keys()}
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
            Points.insert(Start)
            distances = dict()
            for StartingPoint in Points:
                distances[StartingPoint] = 

Solve(2)