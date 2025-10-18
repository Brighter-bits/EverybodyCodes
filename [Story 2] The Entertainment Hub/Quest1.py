# Yes I'm unoriginal with my names.
Parts = ["everybody_codes_e2_q01_p1.txt", "everybody_codes_e2_q01_p2.txt", "everybody_codes_e2_q01_p3.txt"]
import math
class Nail(): # I may as well just treat this like a tree, though this is a pretty terrible tree class
    Left = None
    Right = None

CoordToNail: dict[complex, Nail] = dict()

Visited = []
def FallFind(Start:complex, Grid):
    if Start in Visited:
        return CoordToNail[Start]
    x = int(Start.real)
    y = int(Start.imag)
    Visited.append(Start)
    def FindLeft():
        if x == 0:
            return FindRight()
        NewX = x-1
        NewY = y # Turn out that I have to set y to a new variable of the program gets angry.
        while True:
            NewY += 1
            try:
                if Grid[NewY][NewX] == "*":
                    return complex(NewX, NewY)
            except IndexError:
                return Grid[NewY-1][:NewX+1].count(".")


    def FindRight():
        if x == len(Grid[0])-1:
            return FindLeft()
        NewX = x + 1
        NewY = y
        while True:
            NewY += 1
            try:
                if Grid[NewY][NewX] == "*":
                    return complex(NewX, NewY)
            except IndexError:
                return Grid[NewY-1][:NewX+1].count(".")


    NewNode = Nail()
    NewNode.Left = FindLeft()
    NewNode.Right = FindRight()
    CoordToNail[Start] = NewNode
    if type(NewNode.Left) is complex:
        FallFind(NewNode.Left, Grid)
    if type(NewNode.Right) is complex:
        FallFind(NewNode.Right, Grid)

def FallDown(Start, Instructions): # May need to turn this into a cached function later...
    CNode = Start
    InstructionPointer = 0
    while type(CNode) != int:
        if Instructions[InstructionPointer] == "L":
            CNode = CoordToNail[CNode].Left
        elif Instructions[InstructionPointer] == "R":
            CNode = CoordToNail[CNode].Right
        else:
            raise ValueError("Oh NOOOOO! There's something wrong with the instructions")
        InstructionPointer += 1
    return CNode

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        gap = inp.index([])
        instruct = inp[gap+1:]
        inp = inp[:gap]
        StartingPoints = []
        for i in range(len(inp[0])):
            if inp[0][i] == "*":
                StartingPoints.append(complex(i, 0))
                FallFind(complex(i, 0), inp)
        total = []
        if part == 1:
            for i in range(len(StartingPoints)):
                End = FallDown(StartingPoints[i], instruct[i])
                total.append((End*2) - (i+1))
            print(total)
            total = list(map(lambda x: x if x > 0 else 0, total))
            print(sum(total))
        elif part == 2:
            for instruction in instruct:
                InstructionTotal = []
                for i in range(len(StartingPoints)):
                    End = FallDown(StartingPoints[i], instruction)
                    InstructionTotal.append((End*2) - (i+1))
                InstructionTotal = list(map(lambda x: x if x > 0 else 0, InstructionTotal))
                total.append(max(InstructionTotal))
            print(sum(total))
        elif part == 3:
            for instruction in instruct:
                InstructionTotal = []
                for i in range(len(StartingPoints)):
                    End = FallDown(StartingPoints[i], instruction)
                    InstructionTotal.append((End*2) - (i+1))
                InstructionTotal = list(map(lambda x: x if x > 0 else 0, InstructionTotal))
                total.append(InstructionTotal)
            min = 1000
            max = -1000

            # This code is bad yes, but do I want to do efficient code? no... Nevermind, I now longer need 6 nested loops
            from itertools import permutations
            for combination in permutations(range(len(total[0])), r=len(total)):
                candidate = sum(list(map(lambda x: total[x[0]][x[1]], list(enumerate(combination)))))
                if min > candidate:
                    min = candidate
                if max < candidate:
                    max = candidate
            print(f"{min} {max}")

                        
Solve(3)
