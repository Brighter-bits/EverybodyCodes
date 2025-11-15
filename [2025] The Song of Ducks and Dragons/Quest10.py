from copy import deepcopy
import os
from pathlib import Path
os.chdir(Path(__file__).parent)
import sys
sys.setrecursionlimit(1000000)

Parts = ["everybody_codes_e2025_q10_p1.txt", "everybody_codes_e2025_q10_p2.txt", "everybody_codes_e2025_q10_p3.txt"]
moves = [complex(1, -2), complex(-1, -2), complex(1, 2), complex(-1, 2), complex(2, 1), complex(-2, -1), complex(-2, 1), complex(2, -1)]
inp = []

def LTS(list):
    string = ""
    for part in list:
        for piece in part:
            string += piece + "|"
        string = string[:-1]
        string += ","
    return string[:-1]

def STL(string):
    list2 = string.split(",")
    list2 = list(map(lambda x: x.split("|"), list2))
    return list2

def Find(letter, multiple=False, board = -1):
    if not multiple:
        for x in range(len(inp[0])):
            for y in range(len(inp)):
                if inp[y][x] == letter:
                    return complex(x, y)
    else:
        answer = []
        for x in range(len(board[0])):
            for y in range(len(board)):
                if board[y][x] in letter:
                    answer.append(complex(x, y))
        return answer

def Moves(position:complex):
    ends = []
    for move in moves:
        NPosition = position + move
        if NPosition.real >= 0 and NPosition.imag >= 0 and NPosition.real <= len(inp[0])-1 and NPosition.imag <= len(inp)-1:
            ends.append(NPosition)
    return set(ends)

def Check(position:complex):
    global inp
    y = int(position.imag)
    x = int(position.real)
    if inp[y][x] == "S":
        inp[y][x] = "."
        return True
    return False

def SheepMove():
    global inp
    newinp = [["." for b in range(len(inp[0]))] for a in range(len(inp))]
    for x in range(len(inp[0])): # @ = sheep in hideout
        for y in range(len(inp)-1):
            if inp[y][x] == "S":
                if inp[y+1][x] == "#" or inp[y+1][x] == "@":
                    newinp[y+1][x] = "@"
                else:
                    newinp[y+1][x] = "S"
            elif inp[y][x] == "@":
                if inp[y+1][x] == "#" or inp[y+1][x] == "@":
                    newinp[y+1][x] = "@"
                else:
                    newinp[y+1][x] = "S"
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if newinp[y][x] == "." and (inp[y][x] == "#" or inp[y][x] == "@"):
                newinp[y][x] = "#"
    inp = newinp

def MoveOneSheep(board, position:complex):
    board = deepcopy(board)
    y = int(position.imag)
    x = int(position.real)
    if y == len(board)-1:
        return 1
    match board[y+1][x]:
        case "D":
            return 0
        case "#":
            board[y+1][x] = "@"
        case ".":
            board[y+1][x] = "S"
        case "!":
            board[y+1][x] = "*"
    match board[y][x]:
        case "S" | "@":
            board[y][x] = "."
        case "!" | "*":
            board[y][x] = "D"
    return board


def MoveOneDragon(board, position:complex, move):
    board = deepcopy(board)
    y = int(position.imag)
    x = int(position.real)
    NPosition = position + move
    Ny = int(NPosition.imag)
    Nx = int(NPosition.real)
    if Nx < 0 or Ny < 0 or Nx > len(board[0])-1 or Ny > len(board)-1:
        return 0

    match board[Ny][Nx]:
        case "S":
            board[Ny][Nx] = "D"
        case "#":
            board[Ny][Nx] = "!"
        case "@":
            board[Ny][Nx] = "*"
        case ".":
            board[Ny][Nx] = "D"
    match board[y][x]:
        case "D":
            board[y][x] = "."
        case "!":
            board[y][x] = "#"
        case "*":
            board[y][x] = "@"
    return board

def SheepTurn(board):
    IBoard = deepcopy(board)
    Sheep = Find("S@*", True, IBoard)
    boards = []
    ends = []
    for Shep in Sheep:
        NewBoard = MoveOneSheep(IBoard, Shep)
        if type(NewBoard) == int:
            ends.append(NewBoard)
        if NewBoard != 0 and NewBoard != 1:
            boards.append(NewBoard)
    if len(ends) == len(Sheep) and 1 not in ends:
        boards.append(board)
    return boards

def DragonTurn(board):
    IBoard = deepcopy(board)
    Dragon = Find("D!*", True, IBoard)[0] # ! is a dragon over a hideout, and * will be all three
    boards = []
    for move in moves:
        NewBoard = MoveOneDragon(IBoard, Dragon, move)
        if NewBoard != 0:
            boards.append(NewBoard)
    return boards
from functools import cache
@cache
def Game(board, SheepTurnTime = True):
    total = 0
    board = STL(board)
    if SheepTurnTime:
        boards = SheepTurn(board)
    else:
        boards = DragonTurn(board)
        ValidBoards = []
        for i in range(len(boards)):
            Sheep = Find("S@*", True, boards[i])
            if len(Sheep) == 0:
                total += 1
            elif set(list(map(lambda x: x.imag, Sheep))) == set([len(board)-1]):
                pass    
            else:
                ValidBoards.append(boards[i])
        boards = ValidBoards
    
    for Newboard in boards:
        total += Game(LTS(Newboard), not SheepTurnTime)
    return total
    

    

def Solve(part):
    with open(Parts[part-1]) as f:
        global inp, total
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        start = Find("D")
        places = set([start])
        total = 0
        if part == 1:
            for i in range(4):
                newplaces = set()
                for positions in places:
                    newplaces |= Moves(positions)
                places |= newplaces
            for place in places:
                if Check(place):
                    total += 1
        elif part == 2:
            for i in range(20):
                newplaces = set()
                for positions in places:
                    newplaces |= Moves(positions)
                places = newplaces
                for place in places:
                    if Check(place):
                        total += 1
                SheepMove()
                for place in places:
                    if Check(place):
                        total += 1
        elif part == 3:
            total = Game(LTS(inp))

        
        print(total)

for i in range(1, 4):
    Solve(i)