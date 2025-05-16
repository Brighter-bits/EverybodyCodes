Parts = ["everybody_codes_e2024_q19_p1.txt", "everybody_codes_e2024_q19_p2.txt", "everybody_codes_e2024_q19_p3.txt"]
from itertools import cycle
from copy import deepcopy
def Spin(dir, Piece):
    if dir == "R":
        return [[Piece[1][0], Piece[0][0], Piece[0][1]], [Piece[2][0], Piece[1][1], Piece[0][2]], [Piece[2][1], Piece[2][2], Piece[1][2]]]
    elif dir == "L":
        return [[Piece[0][1], Piece[0][2], Piece[1][2]], [Piece[0][0], Piece[1][1], Piece[2][2]], [Piece[1][0], Piece[2][0], Piece[2][1]]]
    else:
        raise Exception("What are you doing?")


def Pass(instructions, grid):
    for row in range(len(grid)-2):
        for i in range(len(grid[2])-2):
            Piece = [grid[row][i:i+3], grid[row+1][i:i+3], grid[row+2][i:i+3]]
            Piece = Spin(next(instructions), Piece)
            for a in range(3):
                for j in range(3):
                    grid[row+a][i+j] = Piece[a][j]
    return grid


def Solve1n2(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        grid = inp[2:]
        for times in range(1 if part == 1 else (100 if part == 2 else  1048576000 )):
            instructions = cycle(inp[0])
            grid = Pass(instructions, grid)
        for line in grid:
            if ">" in line and "<" in line:
                import regex as re
                num = "".join(list(re.findall(r'>(.*?)<', "".join(line))))
            print("".join(line))
        print("\n\n" + num)
jump = 4000
def GuideGrid(instructions, rows, columns):
    counter = 0
    grid = []
    for row in range(rows):
        line = []
        for column in range(columns):
            line.append(counter)
            counter += 1
        grid.append(line)
    
    for i in range(jump):
        instruct = cycle(instructions)
        grid = Pass(instruct, grid)
    transform = dict()
    for i in range(rows):
        for j in range(columns):
            transform[(grid[i][j]//len(grid[0]), grid[i][j]%len(grid[0]))] = (i, j)
    return transform

def Solve3():
    with open(Parts[2]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        grid = inp[2:]
        instructions = inp[0]
        Guide = GuideGrid(instructions, len(grid), len(grid[0]))
        newgrid = [["." for a in range(len(grid[0]))] for b in range(len(grid))]
        for a in range(1048576000//jump):
            for key, value in Guide.items():
                newgrid[value[0]][value[1]] = grid[key[0]][key[1]]
            grid = deepcopy(newgrid)
        for line in grid:
            print("".join(line))

Solve3()