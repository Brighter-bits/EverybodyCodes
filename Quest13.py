Parts = ["everybody_codes_e2024_q13_p1.txt", "everybody_codes_e2024_q13_p2.txt", "everybody_codes_e2024_q13_p3.txt"]

GraphDict = dict()
Visited = []
dir = [1j, 1, -1j, -1]
def GraphBuilder(grid: list):
    Start = 0
    End = 0
    for i in range(len(grid)):
        if "S" in grid[i]:
            Start = (complex(grid[i].index("S"), i))
    for i in range(len(grid)):
        if "E" in grid[i]:
            End = (complex(grid[i].index("E"), i))
    FloodFind(grid, Start)

    
def FloodFind(grid:list, Node:complex):
    if Node in Visited:
        return
    if Node not in GraphDict:
        GraphDict[Node] = []
    x = int(Node.real)
    y = int(Node.imag)
    Visited.append(Node)
    if y > 0 and grid[y-1][x] != "#" and grid[y-1][x] not in GraphDict[Node]:
        time = grid[y-1][x] - grid[y][x] 
        if time > 5:
            time = 10-time
        time += 1
        GraphDict[Node].append((complex(x, y-1), time))
        FloodFind(grid, complex(x, y-1))
    if y < len(grid) and grid[y+1][x] != "#" and grid[y+1][x] not in GraphDict[Node]:
        time = grid[y+1][x] - grid[y][x] 
        if time > 5:
            time = 10-time
        time += 1
        GraphDict[Node].append((complex(x, y+1), time))
        FloodFind(grid, complex(x, y+1))
    if x > 0 and grid[y][x-1] != "#" and grid[y][x-1] not in GraphDict[Node]:
        time = grid[y][x-1] - grid[y][x-1] 
        if time > 5:
            time = 10-time
        time += 1
        GraphDict[Node].append((complex(x-1, y), time))
        FloodFind(grid, complex(x-1, y))
    if x > len(grid) and grid[y][x+1] != "#" and grid[y][x+1] not in GraphDict[Node]:
        time = grid[y][x+1] - grid[y][x+1] 
        if time > 5:
            time = 10-time
        time += 1
        GraphDict[Node].append((complex(x+1, y), time))
        FloodFind(grid, complex(x+1, y))
    





def Solve():
    with open(Parts[0], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        for line in range(len(inp)):
            for char in range(len(inp[0])):
                if inp[line][char].isdigit():
                    inp[line][char] = int(inp[line][char])
        for i in inp:
            print(i)
        GraphBuilder(inp)
        print(GraphDict)

Solve()