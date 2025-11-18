import os
from pathlib import Path
os.chdir(Path(__file__).parent)
import sys
sys.setrecursionlimit(1000000)
Parts = ["everybody_codes_e2025_q12_p1.txt", "everybody_codes_e2025_q12_p2.txt", "everybody_codes_e2025_q12_p3.txt"]

total = 0
Visited = []
def Flood(Grid, Node:complex, rank = 0):
    global Visited
    if Node in Visited[rank]:
        return
    
    Visited[rank].add(Node)
    x = int(Node.real)
    y = int(Node.imag)
    val = Grid[y][x]

    if y > 0 and Grid[y-1][x] <= val:
        Flood(Grid, complex(x, y-1))
    if y < len(Grid)-1 and Grid[y+1][x] <= val:
        Flood(Grid, complex(x, y+1))
    if x > 0 and Grid[y][x-1] <= val:
        Flood(Grid, complex(x-1, y))
    if x < len(Grid[0])-1 and Grid[y][x+1] <= val:
        Flood(Grid, complex(x+1, y))


def Solve(part):
    with open(Parts[part-1]) as f:
        global Visited
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        for i in range(len(inp)):
            inp[i] = list(map(int, inp[i]))
        if part == 1:
            Visited = [set()]
            Flood(inp, complex(0, 0))
            print(len(Visited[0]))
        elif part == 2:
            Visited = [set(), set()]
            Flood(inp, complex(0, 0), rank=0)
            Flood(inp, complex(len(inp[0])-1, len(inp)-1), rank=1)
            print(len(Visited[0]|Visited[1]))
        elif part == 3:
            Visited = [set()]
            possible = []
            for x in range(len(inp[0])-1):
                for y in range(len(inp)-1):
                        if inp[y][x] != 1:
                            Visited = [set()]
                            Flood(inp, complex(x, y))
                            possible.append(Visited[0])
            best = max(possible, key=lambda x: len(x))
            possible = list(map(lambda x: x-best, possible))
            best2 = max(possible, key=lambda x: len(x))
            possible = list(map(lambda x: x-best2, possible))
            best3 = max(possible, key=lambda x: len(x))
            print(len(best) + len(best2) + len(best3))





Solve(1)
Solve(2)
Solve(3)