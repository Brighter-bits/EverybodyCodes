Parts = ["everybody_codes_e2024_q15_p1.txt", "everybody_codes_e2024_q15_p2.txt", "everybody_codes_e2024_q15_p3.txt"]

GraphDict = dict()
Visited = []
import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(16000)

def GraphBuilder(grid: list):
    Start = complex(grid[0].index("."), 0)
    FloodFind(grid, Start)
    Ends = []
    for i in range(len(grid)):
        if "H" in grid[i]:
            Ends.append(complex(grid[i].index("H"), i))
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
    if y > 0 and grid[y-1][x] != "#" and grid[y-1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y-1), time))
        FloodFind(grid, complex(x, y-1))
    if y < len(grid)-1 and grid[y+1][x] != "#" and grid[y+1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y+1), time))
        FloodFind(grid, complex(x, y+1))
    if x > 0 and grid[y][x-1] != "#" and grid[y][x-1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x-1, y), time))
        FloodFind(grid, complex(x-1, y))
    if x < len(grid[0])-1 and grid[y][x+1] != "#" and grid[y][x+1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x+1, y), time))
        FloodFind(grid, complex(x+1, y))

#### ^^^^^ Look Familiar? ^^^^^ ####


def Solve():
    with open(Parts[0], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        grid = deepcopy(inp)
        Start, Herbs = GraphBuilder(grid)
        print(GraphDict)
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
Solve()