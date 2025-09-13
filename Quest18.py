Parts = ["everybody_codes_e2024_q18_p1.txt", "everybody_codes_e2024_q18_p2.txt", "everybody_codes_e2024_q18_p3.txt"]
Visited = []
Times = dict()
import sys
sys.setrecursionlimit(16000)
def FloodFill(Grid, Node: complex, time):
    global Palms
    global DeadPalms
    if Node in Visited or len(Palms) == len(DeadPalms):
        return
    
    Visited.append(Node)
    x = int(Node.real)
    y = int(Node.imag)

    if Node in Palms:
        DeadPalms.append(Node)
        if (Node in Times.keys() and time < Times[Node]) or Node not in Times:
            Times[Node] = time

    time += 1



    if y > 0 and Grid[y-1][x] != "#":
        FloodFill(Grid, complex(x, y-1), time)
    if y < len(Grid)-1 and Grid[y+1][x] != "#":
        FloodFill(Grid, complex(x, y+1), time)
    if x > 0 and Grid[y][x-1] != "#":
        FloodFill(Grid, complex(x-1, y), time)
    if x < len(Grid[0])-1 and Grid[y][x+1] != "#":
        FloodFill(Grid, complex(x+1, y), time)

def FindP(Grid):
    global Palms
    Palms = []
    for y in range(len(Grid)):
        for x in range(len(Grid[0])):
            if Grid[y][x] == "P":
                Palms.append(complex(x, y))

def FindEntrance(Grid):
    Ent = []
    for y in [0, len(Grid)-1]:
        for x in range(len(Grid[0])):
            if Grid[y][x] == ".":
                Ent.append(complex(x, y))
    for x in [0, len(Grid[0])-1]:
        for y in range(len(Grid)):
            if Grid[y][x] == ".":
                Ent.append(complex(x, y))
    return Ent

def Solve1n2():
    global Visited
    global DeadPalms
    global Times
    with open(Parts[1], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        FindP(inp)
        for i in range(len(inp)):
            inp[i] = list(map(lambda x: "." if x == "P" else x, inp[i]))
        Entrances = FindEntrance(inp)
        for Entrance in Entrances:
            Visited = []
            DeadPalms = []
            FloodFill(inp, Entrance, 0)
        print(max(Times.values()))

def Solve3():
    global TimeSums, Visited, DeadPalms, Times
    with open(Parts[2], "r") as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        FindP(inp)
        TimeSums = []
        for y in range(int(len(inp)/3), int(2*len(inp)/3)):
            for x in range(int(len(inp[0])/3), int(2*len(inp[0])/3)): # The best hole is most likely in the center, so we just look between 25% and 75%
                if inp[y][x] == ".":
                    Visited = []
                    DeadPalms = []
                    Times = dict()
                    FloodFill(inp, complex(x, y), 0)
                    TimeSums.append(sum(Times.values()))
        print(min(TimeSums))
    
Solve3()
                    