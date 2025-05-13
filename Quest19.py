Parts = ["everybody_codes_e2024_q19_p1.txt", "everybody_codes_e2024_q19_p2.txt", "everybody_codes_e2024_q19_p3.txt"]
from itertools import cycle
def Spin(dir, Piece):
    if dir == "R":
        return [[Piece[1][0], Piece[0][0], Piece[0][1]], [Piece[2][0], Piece[1][1], Piece[0][2]], [Piece[2][1], Piece[2][2], Piece[1][2]]]
    elif dir == "L":
        return [[Piece[0][1], Piece[0][2], Piece[1][2]], [Piece[0][0], Piece[1][1], Piece[2][2]], [Piece[1][0], Piece[2][0], Piece[2][1]]]
    else:
        raise Exception("What are you doing?")
def Solve():
    with open(Parts[0]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        instructions = inp[0]
        grid = inp[2:]
        length = len(inp[2])
        for i in range(length-2):
            Piece = [grid[0][i:i+3], grid[1][i:i+3], grid[2][i:i+3]]
            Piece = Spin(cycle(instructions)[i], Piece)
            for a in range(3):
                for j in range(3):
                    grid[a][i+j] = Piece[a][j]
        print(grid)
        

Solve()