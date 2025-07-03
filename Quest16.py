Parts = ["everybody_codes_e2024_q16_p1.txt", "everybody_codes_e2024_q16_p2.txt", "everybody_codes_e2024_q16_p3.txt"]
from collections import Counter
from math import lcm
from functools import cache

def Increment(pointers, rot,  resets):
    Npointers = []
    for i in range(len(pointers)):
        Npointers.append((pointers[i]+rot[i])%resets[i])
    return Npointers

@cache
def CatScore(pointers):
    global cats
    catline = ""
    for i in range(len(cats)):
        catline += cats[i][int(pointers[i])]
    counter = Counter(catline)
    overs = [a-2 for a in list(counter.values()) if a >= 3]
    return catline, sum(overs)

# def HCF(a, b):
#     if b == 0:
#         return a, 1, 0
#     factor, x, y = HCF(b, a%b)
#     return factor, y, x - (a//b) * y

# def InverseMod(value, mod):
#     factor, inverse, _ = HCF(value, mod) ######## Literally don't need this at all
#     return inverse % mod

# def CRT(remainders, mods):
#     Tmod = 1
#     for mod in mods:
#         Tmod += mod
#     Solution = 0
#     for remainder, mod in zip(remainders, mods):
#         PartialProd = Tmod // mod
#         inverse = InverseMod(PartialProd, mod)
#         Solution += remainder * PartialProd * inverse
#     return Solution % Tmod

def ListLcm(nums):
    Factor = lcm(nums[0], nums[1])
    for i in range(2, len(nums)):
        Factor = lcm(Factor, nums[i])
    return Factor

def Up(l):
    for i in range(len(l)):
        l[i] += 1
    return l

def Down(l):
    for i in range(len(l)):
        l[i] -= 1
    return l

LtoStr = lambda L : ''.join(list(map(str, L)))

def Solve(part):
    CatScore.cache_clear()
    RecursiveScore.cache_clear()
    with open("16C.txt", "r") as f:
        global rot, resets, cats
        inp = list(map(lambda x : x.replace("\n", ""), f.readlines()))
        rot = list(map(int, inp[0].split(",")))
        cats = inp[2:]
        lines = [[] for a in range(len(cats[0]))]
        for y in range(len(cats)):
            for x in range(len(cats[0])):
                try:
                    if cats[y][x] != " ":
                        lines[x].append(cats[y][x])
                except: pass
        lines = [a for a in list(lines) if len(a) != 0]
        cats = [[] for a in range(len(lines)//3)]
        for i in range(0, len(lines), 3):
            for piece in range(len(lines[i])):
                cats[i//3].append(lines[i][piece] + lines[i+1][piece] + lines[i+2][piece])
        pointers = [0 for a in range(len(cats))]
        resets = list(map(lambda x: len(x), cats))
        if part == 1:
            for i in range(100):
                pointers = Increment(pointers, rot, resets)
            line = CatScore(LtoStr(pointers))
            newline = ""
            for i in range(len(line[0])//3):
                newline += line[0][3*i:(3*i)+3] + " "
            print(newline)
        elif part == 2:
            for i in range(len(cats)):
                cats[i] = list(map(lambda x : x[0] + x[2], cats[i]))
            total = 0
            Tmod = ListLcm(resets)
            for i in range(Tmod):
                pointers = Increment(pointers, rot, resets)
                total += CatScore(LtoStr(pointers))[1]
            total *= 202420242024//Tmod
            leftover = 202420242024%Tmod
            for i in range(leftover):
                pointers = Increment(pointers, rot, resets)
                total += CatScore(LtoStr(pointers))[1]
            print(total)
        elif part == 3:
            for i in range(len(cats)):
                cats[i] = list(map(lambda x : x[0] + x[2], cats[i]))
            from itertools import product
            status = product("NFB", repeat=256)
            Highest = -10
            Lowest = 100000000000000
            while status:
                Cstatus = ''.join(reversed(next(status)))
                total = RecursiveScore(Cstatus, "000")
                if total > Highest:
                    Highest = total
                if total < Lowest:
                    Lowest = total
                print(f'{Highest} {Lowest}')


@cache
def RecursiveScore(left, pointers):
    pointers = list(map(int, list(pointers)))
    match left[0]:
        case "F":
            pointers = Up(pointers)
        case "B":
            pointers = Down(pointers)
    pointers = Increment(pointers, rot, resets)
    if len(left) != 1:
        return CatScore(LtoStr(pointers))[1] + RecursiveScore(left[1:], LtoStr(pointers))
    else:
        return CatScore(LtoStr(pointers))[1]
        





                


            

            


Solve(3)
                
    
    


