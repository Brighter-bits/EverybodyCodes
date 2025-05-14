Parts = ["everybody_codes_e2024_q19_p1.txt", "everybody_codes_e2024_q19_p2.txt", "everybody_codes_e2024_q19_p3.txt"]
from itertools import cycle
def Spin(dir, Piece):
    if dir == "R":
        return [[Piece[1][0], Piece[0][0], Piece[0][1]], [Piece[2][0], Piece[1][1], Piece[0][2]], [Piece[2][1], Piece[2][2], Piece[1][2]]]
    elif dir == "L":
        return [[Piece[0][1], Piece[0][2], Piece[1][2]], [Piece[0][0], Piece[1][1], Piece[2][2]], [Piece[1][0], Piece[2][0], Piece[2][1]]]
    else:
        raise Exception("What are you doing?")

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        instructions = cycle(inp[0])
        grid = inp[2:]
        length = len(grid[2])
        for times in range(1 if part == 1 else 1000):
            for row in range(len(grid)-2):
                for i in range(length-2):
                    Piece = [grid[row][i:i+3], grid[row+1][i:i+3], grid[row+2][i:i+3]]
                    Piece = Spin(next(instructions), Piece)
                    for a in range(3):
                        for j in range(3):
                            grid[row+a][i+j] = Piece[a][j]
        for line in grid:
            # if ">" in line and "<" in line:
                # import regex as re
                # print("".join(list(re.findall(r'>(.*?)<', "".join(line)))))
            print("".join(line))


Solve(2)