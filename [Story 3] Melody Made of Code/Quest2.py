import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e3_q02_p1.txt", "everybody_codes_e3_q02_p2.txt", "everybody_codes_e3_q02_p3.txt"]

def FindPoint(Grid, Letter): # This finds a single point and returns it
    for y in range(0, len(Grid)):
        for x in range(len(Grid[0])):
            if Grid[y][x] == Letter:
                return complex(x, y)

FloodVisited = set() # This contains all the points that a FloodFill has gone to
def FloodFill(Grid, Node: complex): # This is a normal flood fill
    if Node in FloodVisited:
        return
    
    FloodVisited.add(Node)
    x = int(Node.real)
    y = int(Node.imag)

    if y > 0 and Grid[y-1][x] != "#":
        FloodFill(Grid, complex(x, y-1))
    if y < len(Grid)-1 and Grid[y+1][x] != "#":
        FloodFill(Grid, complex(x, y+1))
    if x > 0 and Grid[y][x-1] != "#":
        FloodFill(Grid, complex(x-1, y))
    if x < len(Grid[0])-1 and Grid[y][x+1] != "#":
        FloodFill(Grid, complex(x+1, y))

def FindPointList(Grid, Letter): # This is the same as FindPoint, except it looks for every single point that matches the letter, not just the first one
    array = []
    for y in range(0, len(Grid)):
        for x in range(len(Grid[0])):
            if Grid[y][x] == Letter:
                array.append(complex(x, y))
    return array

Directions = [0-1j, 1+0j, 0+1j, -1+0j]

FloodRun = True # Checks if a Flood is running, if it isn't, then it must have hit one of the limits
def FloodFillWithLimit(Node: complex, Visited, LowerLimit, UpperLimit): # A flood fill which stops if one of the floods hits an outer wall
    global FloodVisited, FloodRun
    if Node in FloodVisited or Node in Visited or not FloodRun:
        return
    
    FloodVisited.add(Node)
    x = int(Node.real)
    y = int(Node.imag)

    if x < LowerLimit or x > UpperLimit or y < LowerLimit or y > UpperLimit:
        FloodRun = False

    if complex(x, y-1) not in Visited:
        FloodFillWithLimit(complex(x, y-1), Visited, LowerLimit, UpperLimit)
    if complex(x, y+1) not in Visited:
        FloodFillWithLimit(complex(x, y+1), Visited, LowerLimit, UpperLimit)
    if complex(x-1, y) not in Visited:
        FloodFillWithLimit(complex(x-1, y), Visited, LowerLimit, UpperLimit)
    if complex(x+1, y) not in Visited:
        FloodFillWithLimit(complex(x+1, y), Visited, LowerLimit, UpperLimit)


def Solve(part):
    global FloodVisited, FloodRun
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        Start = FindPoint(inp, "@")
        End = FindPoint(inp, "#") if part != 3 else FindPointList(inp, "#")
        CPoint = Start
        Visited = set([Start]) # While this is called visited, it's more just a no-go zone containing Visited Nodes, Filled Nodes, and Bones
        steps = 0
        dir = 0

        if part == 1:
            while CPoint != End: # until we get to the end
                if CPoint + Directions[dir] not in Visited: # Keep moving
                    CPoint += Directions[dir]
                    Visited.add(CPoint)
                    steps += 1
                dir = (dir+1)%4
            print(steps)

        elif part == 2:
            NeedToVisit = set()
            Visited.add(End)
            for direction in Directions:
                NeedToVisit.add(End + direction) # Add all the points we need to hit to surround the bone
            
            while len(NeedToVisit) != 0: # Until we have reached every single point we need to 
                if CPoint + Directions[dir] not in Visited:
                    CPoint += Directions[dir]
                    Visited.add(CPoint)
                    steps += 1
                    if CPoint in NeedToVisit: # If we're at one of the points that we need to get to, remove it from the list
                        NeedToVisit.remove(CPoint)
                dir = (dir+1)%4
            print(steps)

        elif part == 3:
            NeedToVisit = set()
            Visited.update(set(End))
            FloodFill(inp, CPoint) # This flood is simply used to get a gist of all of the NeedToVisit spots that we can actually reach and aren't trapped inside other bones 
            for point in End: # For every point
                for direction in Directions:
                    newPoint = point + direction 
                    if newPoint.real < 0 or newPoint.imag < 0 or newPoint.real >= len(inp[0]) or newPoint.imag >= len(inp) or inp[int(newPoint.imag)][int(newPoint.real)] == "#": # If the point we need to visit is inside another bone, or outside of the map, we disregard it. In hindsight, this would not work if the outer edge wasn't properly covered.
                        continue
                    NeedToVisit.add(newPoint)
            NeedToVisit = NeedToVisit.intersection(FloodVisited) # We find the intersection between these two as these are the ones which we can actually go to
            
            while len(NeedToVisit) != 0:
                if CPoint + Directions[dir//3] not in Visited: # Since the directions are now tripled, rather than making a new list, I just changed how the dir variable is interpreted
                    CPoint += Directions[dir//3]
                    Visited.add(CPoint)
                    steps += 1
                    if CPoint in NeedToVisit:
                        NeedToVisit.remove(CPoint)
                    dir = (dir+1)%12
                else:
                    dir = (((dir//3)+1) *3)%12 # If we can't move into a certain direction, just move on to the next one, no point in doing 6 extra flood fills.
                for direction in Directions: # Flood fill basically everywhere to check if there are any boxed in areas.
                    FloodVisited = set()
                    FloodRun = True    
                    FloodFillWithLimit(CPoint + direction, Visited, -100, 100)
                    if FloodRun: # If this thing is still on, then that means that we didn't escape and hit the outer wall, meaning we're boxed in!
                        # if len(FloodVisited) != 0:
                        #     breakpoint()
                        Visited.update(FloodVisited)
                        NeedToVisit = NeedToVisit - FloodVisited
            print(steps)


for i in range(1, 4):
    Solve(i)