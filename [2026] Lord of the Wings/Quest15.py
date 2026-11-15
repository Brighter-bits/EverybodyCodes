import os
from pathlib import Path
import sys
from collections import defaultdict
from functools import cache
import sys

sys.setrecursionlimit(1000000000)
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q15_p1.txt", "everybody_codes_e2026_q15_p2.txt", "everybody_codes_e2026_q15_p3.txt"]

def FindStartnEnd(Grid): # This is an old function that finds the start and end points of the mine
    Start = -1
    End = -1
    for y in range(len(Grid)):
        for x in range(len(Grid[y])): # Go through every single x and y Coordinate
            if Grid[y][x] == "S": # If we find the start coordinate, save it.
                Start = (x, y)
            if Grid[y][x] == "E":
                End = (x, y)
    return Start, End

def FindLetter(letter, grid): # This is another old function which finds every use of a letter
    answer = []
    for y in range(len(grid)):
        for x in range(len(grid[0])): # Go through every cell and add each coordinate we find
            if grid[y][x] == letter:
                answer.append((x, y))
    return answer

def SendFeeler(inp, x, y, Up): # This is a "feeler", which goes down a loop and records it. If we're in the left entrance, then we will complete a loop. If we go down the right entrance, then we will turn around and end at the same starting point, which allows us to discard it so we don't get duplicate loops.
    time = 0
    origX = x
    origY = y
    dirs = [(0, -1), (1, 0), (0, 1)] if Up else [(0, 1), (1, 0), (0, -1)] # If up is true, then we go up, right, down. If up is false, then we go down, right, up
    dir = 0
    deposits = 0
    while True:
        x += dirs[dir][0] # We move in the direction we are facing
        y += dirs[dir][1]
        if inp[y][x] == "#": # If we're at a wall, then turn
            x -= dirs[dir][0]
            y -= dirs[dir][1]
            dir += 1
            continue # Continue so we don't count turning as a second, and don't recount a sulphur deposit twice.
        if inp[y][x] == "@": # Add one to the deposits if we see an @
            deposits += 1
        time += 1
        if y == origY:
            break
    return (*sorted([origX, x]), time, deposits) if deposits > 0 else None # Make sure that the x coordinates are sorted to allow easier checking of duplicates. Also we probably don't want to go into loops which have no deposits so don't add any which don't

def val(x): # This is just a helper function to turn 9A into 9
    return int(x[:-1]) if isinstance(x, str) else x

def FindLoops(inp, start): # This goes along the central line, and sends feelers up and down the loops to find all of them.
    x = int(start[0])
    y = int(start[1])
    loops = []
    while inp[y][x] != "E": # Before we get to the end
        if inp[y-1][x] == "." or inp[y-1][x] == "@": # If there's an entrance then send a feeler
            result = SendFeeler(inp, x, y, True)
            if result != None and result[0] != result[1]: # Only add the loop if it goes all the way around the loop, and had more than one deposit
                loops.append(result)
        if inp[y+1][x] == "." or inp[y+1][x] == "@":
            result = SendFeeler(inp, x, y, False)
            if result != None and result[0] != result[1]: 
                loops.append(result)
        x += 1
    return loops

@cache
def BruteForce(Start, End, POI): # POI is all of the entrances and exists we haven't been to yet 
    global LoopDict
    if len(POI) == 0: # If we've gone through every loop, then go straight to the end
        return abs(Start - End)
    POI = sorted(list(map(int, POI.split("|"))))
    totals = []
    
    for point in POI:
        distance = abs(point - Start) # We're all on a line, so our distance is just the absolute value of destination - where we are
        nextPoint = list(LoopDict[point].items())[0][0] # This is where we end up after we get out of the loop. And where we will start our next check
        newPOI = list(POI)
        del newPOI[newPOI.index(point)]
        del newPOI[newPOI.index(nextPoint)] # We get rid of the loops entrances
        totals.append(BruteForce(nextPoint, End, "|".join(list(map(str, newPOI)))) + list(LoopDict[point].items())[0][1] + distance)
    return min(totals) # Return the minimum distance to get all of the sulphur and make it to the end from here.

@cache
def BruteForceP2(Start, End, amount, threshold):
    global LoopDict, LoopX, SulphurDict
    if amount >= threshold: # If we're over the threshold, then beeline it to the end
        return abs(val(Start) - End)
    totals = []
    for point in [a for a in LoopX if a != Start]: # We can go to any other loop, just not backwards
        nextPoint = list(LoopDict[point].items())[0][0]
        cStart = val(Start) # We translate our Start and End to proper numbers, just in case they are strings
        cpoint = val(point)
        distance = abs(cpoint - cStart)
        totals.append(BruteForceP2(nextPoint, End, amount + SulphurDict[point], threshold) + list(LoopDict[point].items())[0][1] + distance)
    return min(totals)

@cache
def FindPathLength(Start, End, depth): # It's not a very good name, but essentially, it is the previous algorithms, but it stops after a certain number of steps.
    global LoopDict, LoopX, SulphurDict
    if depth == 0:
        return 0, [Start], 0, 0
    totals = []
    for point in [a for a in LoopX if a != Start]:
        nextPoint = list(LoopDict[point].items())[0][0]
        cStart = val(Start)
        cpoint = val(point)
        distance = abs(cpoint - cStart)
        Time, Node, Sulf, TpS = FindPathLength(nextPoint, End, depth-1)
        Time += list(LoopDict[point].items())[0][1] + distance
        Sulf += SulphurDict[point]
        totals.append([Time, [Start, *Node], Sulf, Time/Sulf]) # We include Time per Sulphur in the totals, so we can optimise for it. The optimal sequence of loops should have a small amount of time between getting more sulphur
    return min(totals, key=lambda x: x[3])

def Solve(part):
    BruteForce.cache_clear() # Clear the caches
    BruteForceP2.cache_clear()
    FindPathLength.cache_clear()
    global LoopDict, LoopX, SulphurDict
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        LoopDict = defaultdict(lambda: defaultdict(int))
        Start, End = FindStartnEnd(inp)

        loops = FindLoops(inp, Start)
        if part != 1:
            for i in range(len(loops)): # We need to check if we have any loops where we can go to the above loop and the below loop.
                for j in range(i+1, len(loops)):
                    if loops[i][:2] == loops[j][:2]: # We then split the two loops into A and B, so that we know we can just go straight from one to the other
                        loops[i] = (str(loops[i][0]) + "A", str(loops[i][1]) + "A", *loops[i][2:])
                        loops[j] = (str(loops[j][0]) + "B", str(loops[j][1]) + "B", *loops[j][2:])
        
        SulphurDict = dict()
        for loop in loops: # This is so we can look up how much sulphur each loop gives
            SulphurDict[loop[0]] = loop[3]
            SulphurDict[loop[1]] = loop[3]
        
        LoopX = [] # This just contains the x coordinates of all the entrances and exits to loops.

        for i in loops:
            LoopX.append(i[0])
            LoopX.append(i[1])

        for loop in loops: # This oart here contains where the cart ends up after it enters a loop
            LoopDict[loop[0]][loop[1]] = loop[2]
            LoopDict[loop[1]][loop[0]] = loop[2]

        if part == 1:
            print(BruteForce(Start[0], End[0], "|".join(list(map(str, LoopX)))))
        elif part == 2:
            LoopX = set(LoopX)
            print(BruteForceP2(Start[0], End[0], 0, 2026))
        elif part == 3:
            LoopX = set(LoopX)
            Thresh = 202620262026
            cycle = FindPathLength(Start[0], End[0], 16) # We go for 16 steps, which is enough to find the optimal loop
            tail = cycle[1][-4:] # We take the last 4 steps
            if tail[:2] == tail[2:]: # Thank god I only had an optimal cycle containing two loops
                a, b = tail[0], tail[1] # Find which two loops we're going in and out of
                bCoord, bCost = list(LoopDict[b].items())[0] 
                aCoord, aCost = list(LoopDict[a].items())[0] 
                cost = abs(val(bCoord) - val(a)) + bCost + abs(val(aCoord) - val(b)) + aCost # We then calculate the cost of going through and between the two loops
                gain = SulphurDict[bCoord] + SulphurDict[aCoord] # Find how much sulphur we get each cycle
                k = (Thresh // gain) - 40 # We find the number of complete cycles - 40, because we still need to manually calculate getting to the loops and getting to the end.
                Thresh -= k * gain # Subtract the middle sulphur that we will collect
                print(BruteForceP2(Start[0], End[0], 0, Thresh) + k * cost) # Then we find the sulphur and add in the middle bit

for i in range(1, 4):
    Solve(i)