import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q11_p1.txt", "everybody_codes_e2025_q11_p2.txt", "everybody_codes_e2025_q11_p3.txt"]

def P1(ducks):
    for i in range(len(ducks)-1):
        if ducks[i] > ducks[i+1]:
            ducks[i] -= 1
            ducks[i+1] += 1
    return ducks

def P2(ducks):
    for i in range(len(ducks)-1):
        if ducks[i] < ducks[i+1]:
            ducks[i] += 1
            ducks[i+1] -= 1
    return ducks

def Check(ducks):
    total = 0
    for i in range(len(ducks)):
        total += (i+1) * ducks[i]
    return total

def BecomeDifferences(ducks):
    LtoR = []
    for i in range(len(ducks)-1):
        LtoR.append(ducks[i+1] - ducks[i])
    return LtoR


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(int, f.readlines()))
        Phase1 = True
        if part == 1:
            for i in range(10):
                previnp = list(inp)
                if Phase1:
                    inp = P1(inp)
                else:
                    inp = P2(inp)
                if previnp == inp:
                    Phase1 = False 
                    inp = P2(inp)
            print(Check(inp))
        elif part == 2:
            counter = 0
            while True:
                counter += 1
                previnp = list(inp)
                if Phase1:
                    inp = P1(inp)
                else:
                    inp = P2(inp)
                if previnp == inp:
                    if not Phase1:
                        break
                    Phase1 = False 
                    inp = P2(inp)
            print(counter-1)
        elif part == 3:
            counter = 0
            while True:
                counter += 1
                previnp = list(inp)
                if Phase1:
                    inp = P1(inp)
                else:
                    inp = P2(inp)
                if previnp == inp:
                    middle = int(sum(inp)/len(inp))
                    LQ = int(middle * 0.25)
                    UQ = 3 * LQ
                    value = 0
                    for i in range(int(len(inp))):
                        if middle - inp[i] > 0:
                            value += middle - inp[i]
                    print(value)
                    break

for i in range(1, 4):
    Solve(i)
