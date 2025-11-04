parts = ["everybody_codes_e1_q01_p1.txt", "everybody_codes_e1_q01_p2.txt", "everybody_codes_e1_q01_p3.txt"]
from itertools import cycle
import sys
sys.setrecursionlimit(15000)
def eni(Start, exp, mod):
    global left
    left = exp
    num = []
    previous = []
    def work(N):
        global left
        newnum = (N*Start)%mod
        if part > 1 and newnum in previous:
            return newnum
        if left == 1:
            return newnum
        left -= 1
        previous.append(newnum)
        num.append(work(newnum))
        return newnum
    
    piece = work(1)
    num.append(piece)
    summed = sum(num) - num[0]
    num = list(map(lambda x: str(x), num))
    total = 0
    if (part == 2 and exp > 5) or part == 3:
        before = list(map(lambda x: int(x), num[num.index(str(num[0]), 1)+1:]))
        summed -= sum(before)
        if part == 3:
            total = sum(before)
        num = num[:num.index(str(num[0]), 1)]
        num.append(num[0])
        del num[0]
        length = len(num)
        exp -= len(before)
        if part == 3:
            total += summed * (exp//length)
            num = cycle(list(reversed(list(map(lambda x: int(x), num)))))
            for i in range(exp%length):
                total += next(num)
            return total
        numcyc = cycle(num)
        for i in range(length-((exp)%length)):
            next(numcyc)
        num = []
        for i in range(5):
            num.append(next(numcyc))
    return int(''.join(num))


trans_table = str.maketrans({chr(c): "" for c in range(65, 91)} | {"\n": "", "=": ""})

def Solve():
    with open(parts[part-1], "r") as f:
        inp = list(map(lambda x: x.split(), list(map(lambda x: x.translate(trans_table), f.readlines()))))
        for i in range(len(inp)):
            inp[i]=list(map(lambda x: int(x), inp[i]))
        results = []
        for line in inp:
            # print(eni(line[0], line[3], line[6]))
            # print(eni(line[1], line[4], line[6]))
            # print(eni(line[2], line[5], line[6]))
            results.append(eni(line[0], line[3], line[6])+eni(line[1], line[4], line[6])+eni(line[2], line[5], line[6]))
        print(max(results))
        # print(list(sorted(results)))
part = 0
for i in range(3):
    part += 1
    Solve()
