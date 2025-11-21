import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q13_p1.txt", "everybody_codes_e2025_q13_p2.txt", "everybody_codes_e2025_q13_p3.txt"]


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        clockR = []
        clockL = []
        R = True
        if part == 1:
            inp = list(map(int, inp))
            for num in inp:
                if R:
                    clockR.append(num)
                else:
                    clockL.append(num)
                R = not R
        elif part == 2 or part == 3:
            inp = list(map(lambda x: (int(x.split("-")[0]), int(x.split("-")[1])), inp))
            for nums in inp:
                numlist = [a for a in range(nums[0], nums[1]+1)]
                if R:
                    clockR.extend(numlist)
                else:
                    clockL.extend(numlist)
                R = not R

        
        inp = [1]
        inp.extend(clockR)
        inp.extend(clockL[::-1])
        print(inp[2025%len(inp)] if part == 1 else (inp[20252025%len(inp)] if part == 2 else inp[202520252025%len(inp)]))

for i in range(1, 4):
    Solve(i)
        
