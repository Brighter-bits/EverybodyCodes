Parts = ["everybody_codes_e2024_q15_p1.txt", "everybody_codes_e2024_q15_p2.txt", "everybody_codes_e2024_q15_p3.txt"]

GraphDict = dict()
Visited = []
import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(16000)

def GraphBuilder(grid: list, part):
    Start = complex(grid[0].index("."), 0)
    FloodFind(grid, Start)
    Ends = []
    if part == 1:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if "H" in grid[i][j]:
                    Ends.append(complex(j, i))
    elif part == 2:
        Ends = [[]*3]
        Herbs = dict()
        counter = 0
        Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in Herbs and grid[i][j] in Alphabet:
                    Herbs[grid[i][j]] = counter
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if "A" in grid[i][j]:
                    Ends[0].append(complex(j, i))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if "B" in grid[i][j]:
                    Ends[1].append(complex(j, i))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if "C" in grid[i][j]:
                    Ends[2].append(complex(j, i))
    return Start, Ends

def FloodFind(grid:list, Node:complex):
    if Node in Visited:
        return
    if Node not in GraphDict:
        GraphDict[Node] = []
    x = int(Node.real)
    y = int(Node.imag)
    Visited.append(Node)
    time = 1
    if y > 0 and grid[y-1][x] != "#" and grid[y][x+1] != "~" and grid[y-1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y-1), time))
        FloodFind(grid, complex(x, y-1))
    if y < len(grid)-1 and grid[y+1][x] != "#" and grid[y][x+1] != "~" and grid[y+1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y+1), time))
        FloodFind(grid, complex(x, y+1))
    if x > 0 and grid[y][x-1] != "#" and grid[y][x+1] != "~" and grid[y][x-1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x-1, y), time))
        FloodFind(grid, complex(x-1, y))
    if x < len(grid[0])-1 and grid[y][x+1] != "#" and grid[y][x+1] != "~" and grid[y][x+1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x+1, y), time))
        FloodFind(grid, complex(x+1, y))

#### ^^^^^ Look Familiar? ^^^^^ ####


def Solve(part):
    with open(Parts[part-1], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        grid = deepcopy(inp)
        Start, Herbs = GraphBuilder(grid, part)
        print(GraphDict)
        if part == 1:
            Solve1(Start, Herbs)
        elif part == 2:


def Solve1(Start, Herbs):
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

Solve(2)