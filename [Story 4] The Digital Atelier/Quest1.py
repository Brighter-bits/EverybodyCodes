import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e4_q01_p1.txt", "everybody_codes_e4_q01_p2.txt", "everybody_codes_e4_q01_p3.txt"]


def Weave1(orders: list[int]):
    prevSpaces = [0]
    currentSpace = 0
    for order in orders:
        if currentSpace - order < 0 or currentSpace - order in prevSpaces:
            currentSpace += order
            prevSpaces.append(currentSpace)
        else:
            currentSpace -= order
            prevSpaces.append(currentSpace)
    return currentSpace

def Weave2(orders: list[int]):
    prevSpaces = [0]
    currentSpace = 0
    for order in orders:
        if currentSpace - order < 0 or currentSpace - order in prevSpaces:
            while currentSpace + order in prevSpaces:
                currentSpace += 1
            currentSpace += order
            prevSpaces.append(currentSpace)
        else:
            currentSpace -= order
            prevSpaces.append(currentSpace)
    return currentSpace

def CheckCrossover(newSpaces: list[int], oldSpaces: list[list[int]]):
    newSpaces.sort()
    for arc in oldSpaces:
        if (arc[0] < newSpaces[0] < arc[1]) !=  (arc[0] < newSpaces[1] < arc[1]):
            return True
    return False

def Weave3(orders: list[int]):
    prevSpaces = [0]
    currentSpace = 0
    belows = []
    aboves = []
    below = True
    for order in orders:
        if currentSpace - order < 0 or currentSpace - order in prevSpaces or CheckCrossover([currentSpace - order, currentSpace], belows if below else aboves): # I feel as if I have sinned
            prevSpaces.sort()
            while (currentSpace + order in prevSpaces or CheckCrossover([currentSpace, currentSpace + order], belows if below else aboves)) and currentSpace + order <= prevSpaces[-1]:
                order += 1

            if CheckCrossover([currentSpace, currentSpace + order], belows if below else aboves):
                continue
        
            if below:
                belows.append([currentSpace, currentSpace + order])
            else:
                aboves.append([currentSpace, currentSpace + order])

            currentSpace += order
            prevSpaces.append(currentSpace)
        else:

            if below:
                belows.append([currentSpace - order, currentSpace])
            else:
                aboves.append([currentSpace - order, currentSpace])
            currentSpace -= order
            prevSpaces.append(currentSpace)

        below = not below
    return currentSpace

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(map(int, x.replace("\n", "").split(","))), f.readlines()))
        total = 0
        for i in inp:
            if part == 1:
                total += Weave1(i)
            elif part == 2:
                total += Weave2(i)
            else:
                total += Weave3(i)
        print(total)

for i in range(1, 4):
    Solve(i)