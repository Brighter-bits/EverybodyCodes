Parts = ["everybody_codes_e2024_q20_p1.txt", "everybody_codes_e2024_q20_p2.txt", "everybody_codes_e2024_q20_p3.txt"]
Dirs = [0+1j, complex(1), 0-1j, complex(-1)] # Up, Right, Down, Left. +1 on the pointer is turn right, -1 on the pointer is turn left

def FindStart(Grid):
    Starts = []
    for y in [0, len(Grid)-1]:
        for x in range(len(Grid[0])):
            if Grid[y][x] == "S":
                Starts.append(complex(x, y))
    for x in [0, len(Grid[0])-1]:
        for y in range(len(Grid)):
            if Grid[y][x] == "S":
                Starts.append(complex(x, y))
    return Starts

def Feeler(Grid, Start:complex, Instructions):
    Glider = Start
    Direction = 0 # Downwards
    Height = 1000
    for char in Instructions:
        if char == "1":
            Direction += 1
        if char == "2":
            Direction -= 1
        Direction %= 4
        Glider += Dirs[Direction]
        if Grid[int(Glider.imag)][int(Glider.real)] == "#":
            return -1
        if Grid[int(Glider.imag)][int(Glider.real)] == ".":
            Height -= 1
        if Grid[int(Glider.imag)][int(Glider.real)] == "-":
            Height -= 2
        if Grid[int(Glider.imag)][int(Glider.real)] == "+":
            Height += 1
    return Height

with open(Parts[0]) as f:
    inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
    Starts = FindStart(inp)
    if len(Starts) == 1:
        Starts = Starts[0]
    Heights = []
    from itertools import product
    for instruct in product("012", repeat=100):
        Heights.append(Feeler(inp, Starts, instruct))
    print(max(Heights))
