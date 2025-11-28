import os
from pathlib import Path
import sys
from math import ceil, floor
from collections import defaultdict
from itertools import product
sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
from functools import cache
Parts = ["everybody_codes_e2025_q19_p1.txt", "everybody_codes_e2025_q19_p2.txt", "everybody_codes_e2025_q19_p3.txt"]

@cache
def Pass(inp, height, prevDist): # This code barely works, I may need to rewrite it later...
    flaps = 0
    Startdistance, gapHeight, gap = inp
    distance = Startdistance - prevDist
    if height < gapHeight:
        HeightDifference = gapHeight - height
        flaps += HeightDifference
        height = gapHeight
        if HeightDifference < distance:
            flaps += ceil((distance-HeightDifference)/2)
            if (HeightDifference-distance) % 2 == 1:
                height += 1
        elif HeightDifference > distance:# Assume we can make up for it somewhere
            flaps += HeightDifference - distance - 1
            height = gapHeight
    elif height > gapHeight + gap:
        HeightDifference = height - gapHeight - gap
        height = gapHeight + gap
        if HeightDifference < distance:
            flaps += floor((distance-HeightDifference)/2)
            if (HeightDifference-distance) % 2 == 1:
                height -= 1
    else:
        if height == gapHeight:
            flaps += ceil((distance)/2)+1
            if (distance) % 2 == 1:
                height += 1
        else:
            flaps += floor((distance)/2)+1
            if (distance) % 2 == 1:
                height -= 1

    prevDist = Startdistance+1

    return flaps, height, prevDist

def BadFlappy(inp):
    height = 0
    prevDist = 0
    flaps = 0
    for i in range(len(inp)):
        newflaps, height, prevDist = Pass(tuple(inp[i]), height, prevDist)
        flaps += newflaps
    return flaps

@cache
def FlappyDistance(Initial, Final):
    x1 = Initial[0]
    x2 = Final[0]
    y1 = Initial[1]
    y2 = Final[1]
    flaps = 0
    xDiff = x2 - x1
    ydiff = y2 - y1
    if ydiff > 0:
        flaps += y2-y1
    ydiff = abs(ydiff)
    if xDiff - ydiff > 0:
        flaps += (xDiff-ydiff)//2
        if (xDiff - ydiff) % 2 == 1:
            flaps += 1
    return flaps, (2*flaps) - xDiff

@cache # Just cache everything at this point
def LoopFlap(wall, oldY):
    global walls, PipeGoals
    if wall == len(walls):
        return 0
    minFlaps = 100000000000000000000000000
    try:
        oldX = walls[wall-1]
    except:
        oldX = 0
    x = walls[wall]
    for y in PipeGoals[x]:
        if (y - oldY) >= 100000: # When in doubt, assume it's pretty 
            continue
        distance, modifier = FlappyDistance((oldX, oldY), (x, y))
        minFlaps = min(minFlaps, distance + LoopFlap(wall + 1, oldY+modifier))
    return minFlaps

    

def Solve(part):
    global walls, PipeGoals
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split(","), f.readlines()))
        for i in range(len(inp)):
            inp[i] = list(map(int, inp[i]))
        if part == 1:
            print(BadFlappy(inp))
        elif part == 2:
            LoopFlap.cache_clear()
            FlappyDistance.cache_clear()
            PipeGoals = defaultdict(list)
            for i in range(len(inp)):
                distance, gapHeight, gap = inp[i]
                for i in range(gap):
                    PipeGoals[distance].append(gapHeight+i)
            walls = dict()
            counter = 0
            for distance in PipeGoals.keys():
                walls[counter] = distance
                counter += 1
            print(LoopFlap(0, 0))
        elif part == 3:
            LoopFlap.cache_clear()
            FlappyDistance.cache_clear()
            PipeGoals = defaultdict(list)
            for i in range(len(inp)): # Surely just the edges
                distance, gapHeight, gap = inp[i]
                leeway = 5
                for i in range(leeway):
                    PipeGoals[distance].append(gapHeight+i)
                for i in range(leeway):
                    PipeGoals[distance].append(gapHeight+gap-i)
            walls = dict()
            counter = 0
            for distance in PipeGoals.keys():
                walls[counter] = distance
                counter += 1
            print(LoopFlap(0, 0))

                




                

Solve(1)
Solve(2)
Solve(3)