from math import prod, lcm
import os
from pathlib import Path
import sys
from collections import defaultdict
sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q16_p1.txt", "everybody_codes_e2025_q16_p2.txt", "everybody_codes_e2025_q16_p3.txt"]

def Checkabove(list, num):
    for i in list:
        if i < num:
            return False
    return  True

def CheckAll(list):
    for i in list:
        if i != 0:
            return False
    return  True

def CheckPerfectFit(num, list):
    for i in list:
        if num % i != 0:
            return False
    return True

def ListDown(num, list):
    total = 0
    for i in list:
        total += num//i
    return total

def AllDivide(block,  rules):
    counter = 0
    Ones = ""
    for rule in rules:
        if block % rule == 0:
            counter += 1
            Ones += str(rule)
    return counter, Ones

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(int, f.readline().split(",")))
        if part == 1:
            total = 0
            for num in inp:
                total += 90//num
            print(total)
        elif part == 2 or part == 3:
            counter = 1
            total = []
            while not CheckAll(inp):
                if Checkabove(inp[counter-1::counter], 1):
                    for i in range(counter-1, len(inp), counter):
                        inp[i] = inp[i] - 1
                    total.append(counter)
                    print(counter)
                counter += 1
            if part == 2:
                print(prod(total))
            else:
                totalBlocks = 202520252025000
                ctotal = 0
                difference = 1000000000
                done = False
                result = 0
                while not done:
                    while result < totalBlocks:
                        ctotal += difference
                        result = ListDown(ctotal, total)
                    ctotal -= difference
                    difference //= 1000
                    result = 0
                    if difference == 1:
                        break
                difference = 1
                while result < totalBlocks:
                    ctotal += difference
                    result = ListDown(ctotal, total)
                ctotal -= difference
                print(ctotal) # WAIT THIS WORKS???
                


for i in range(1, 4):
    Solve(i)