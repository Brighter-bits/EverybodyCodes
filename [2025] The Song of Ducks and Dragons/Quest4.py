Parts = ["everybody_codes_e2025_q04_p1.txt", "everybody_codes_e2025_q04_p2.txt", "everybody_codes_e2025_q04_p3.txt"]
def Solve(part):
    with open(Parts[part-1]) as f:
        if part == 3:
            inp = list(map(lambda x: (int(x[0]), int(x[1])) if len(x) == 2 else int(x[0]), list(map(lambda x: x.replace("\n", "").split("|"), f.readlines()))))
            seconds = list(map(lambda x: x[1] if type(x) != int else 0, inp))
        else:
            inp = list(map(int, list(map(lambda x: x.replace("\n", ""), f.readlines()))))
        inp = list(map(lambda x: x[0] if type(x) != int else x, inp))
        if part == 3:
            sizedifferences = []
            for i in range(1, len(inp)-1):
                sizedifferences.append(seconds[i]/inp[i])
        differences = []
        for i in range(len(inp)-1):
            differences.append(1/(inp[i+1]/inp[i]))
        turns = 100 if part == 3 else (10000000000000 if part == 2 else 2025)
        if part == 3:
            for diff in range(len(differences)):
                if diff < len(sizedifferences):
                    turns = turns * differences[diff] * sizedifferences[diff]
                else:
                    turns = turns * differences[diff]
        elif part == 2:
            for diff in range(len(differences)):
                    turns = turns * 1/(differences[diff])
        else:
            for diff in range(len(differences)):
                turns = turns * differences[diff]
        print(int(turns) if part != 2 else int(turns)+1)

for i in range(1, 4):
    Solve(i)