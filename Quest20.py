Parts = ["everybody_codes_e2024_q20_p1.txt", "everybody_codes_e2024_q20_p2.txt", "everybody_codes_e2024_q20_p3.txt"]
Dirs = [0+1j, complex(1), 0-1j, complex(-1)] # Up, Right, Down, Left. +1 on the pointer is turn right, -1 on the pointer is turn left

def FindStart(Grid):
    for y in [0, len(Grid)-1]:
        for x in range(len(Grid[0])):
            if Grid[y][x] == "S":
                return complex(x, y)

def FloodFind(grid:list, Node:complex):
    if Node in Visited:
        return
    if Node not in GraphDict:
        GraphDict[Node] = []
    x = int(Node.real)
    y = int(Node.imag)
    Visited.append(Node)
    time = 1
    if y > 0 and grid[y-1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y-1), time))
        FloodFind(grid, complex(x, y-1))
    if y < len(grid)-1 and grid[y+1][x] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x, y+1), time))
        FloodFind(grid, complex(x, y+1))
    if x > 0 and grid[y][x-1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x-1, y), time))
        FloodFind(grid, complex(x-1, y))
    if x < len(grid[0])-1 and grid[y][x+1] not in GraphDict[Node]:
        GraphDict[Node].append((complex(x+1, y), time))
        FloodFind(grid, complex(x+1, y))

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
#         if Grid[int(Glider.imag)][int(Glider.real)] == "#":
#             return -1
#         if Grid[int(Glider.imag)][int(Glider.real)] == ".":
#             Height -= 1
#         if Grid[int(Glider.imag)][int(Glider.real)] == "-":
#             Height -= 2
#         if Grid[int(Glider.imag)][int(Glider.real)] == "+":
#             Height += 1
#     return Height

def WeirdDijkstra(Grid, Start):

with open(Parts[0]) as f:
    inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
    Starts = FindStart(inp)

