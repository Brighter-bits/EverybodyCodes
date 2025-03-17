Parts = ["everybody_codes_e2024_q10_p1.txt", "everybody_codes_e2024_q10_p2.txt", "everybody_codes_e2024_q10_p3.txt"]

def WordMaker(grid):
    rows = list(map(lambda x: x.replace(".", ""), grid[2:6]))
    CMaker = lambda x, b: ''.join(x[a][b] for a in range(0, len(x))).replace(".", "")
    columns = []
    for i in range(2, 6):
        columns.append(CMaker(grid, i))
    word = ""
    for row in rows:
        for column in columns:
            for letter in row:
                if letter in column:
                    word += letter
                    break
    return word

with open(Parts[0], "r") as f:
    grid = list(map(lambda x: x.replace("\n", ""), f.readlines()))
    rows = list(map(lambda x: x.replace(".", ""), grid[2:6]))
    CMaker = lambda x, b: ''.join(x[a][b] for a in range(0, len(x))).replace(".", "")
    columns = []
    for i in range(2, 6):
        columns.append(CMaker(grid, i))
    word = ""
    for row in rows:
        for column in columns:
            for letter in row:
                if letter in column:
                    word += letter
                    break
    print(word)















