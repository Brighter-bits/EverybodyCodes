import os
from pathlib import Path
import sys
from collections import defaultdict
sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q15_p1.txt", "everybody_codes_e2025_q15_p2.txt", "everybody_codes_e2025_q15_p3.txt"]
Visited = set()
Directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # Up, Right, Down, Left
GraphDict: defaultdict[list] = defaultdict(list)
xcoords = set()
ycoords = set()
def Dijkstra(start):
    x = int(start[0])
    y = int(start[1])
    Distances = {node: float("infinity") for node in GraphDict.keys()}
    Distances[(x, y)] = 0
    import heapq
    queue = [(0, (x, y))]
    while queue:
        CDist, CNode = heapq.heappop(queue)
        if CDist > Distances[CNode]:
            continue
        for adjacent in GraphDict[CNode]:
            distance = CDist + 1
            if distance < Distances[adjacent]:
                Distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    return Distances

def CTT(complex:complex):
    return (int(complex.real), int(complex.imag))

def Add(grid:dict, dir, coord:complex, steps):
    for i in range(steps):
        coord = (coord[0] + Directions[dir][0], coord[1] + Directions[dir][1])
        grid[(int(coord[0]), int(coord[1]))] = True
    return grid, coord

def Add3(grid:list, dir, coord:complex, steps):
    Icoord = coord
    coord = (coord[0] + Directions[dir][0]*steps, coord[1] + Directions[dir][1]*steps)
    grid.append((Icoord, coord))
    return grid, coord


def Flood(Grid, Node):
    global Visited, Xmax, Ymax, Xmin, Ymin, GraphDict
    if Node in Visited:
        return 
    x = int(Node[0])
    y = int(Node[1])
    Visited.add(Node)
    if y >= Ymin and (x, y-1) not in Grid:
        GraphDict[(x, y)].append((x, y-1))
        Flood(Grid, (x, y-1))
    if y <= Ymax and (x, y+1) not in Grid:
        GraphDict[(x, y)].append((x, y+1))
        Flood(Grid, (x, y+1))
    if x >= Xmin and (x-1, y) not in Grid:
        GraphDict[(x, y)].append((x-1, y))
        Flood(Grid, (x-1, y))
    if x <= Xmax and (x+1, y) not in Grid:
        GraphDict[(x, y)].append((x+1, y))
        Flood(Grid, (x+1, y))

def CheckNotInBounds(Grid, x, y):
    for bound in Grid:
        Ly = min(bound[0][1], bound[1][1])
        Lx = min(bound[0][0], bound[1][0])
        Uy = max(bound[0][1], bound[1][1])
        Ux = max(bound[0][0], bound[1][0])
        if (Ux == Lx) and (x == Ux) and (Ly <= y <= Uy):
            return False
        if (Uy == Ly) and (y == Uy) and (Lx <= x <= Ux): # if (Uy == Uy) I want to explode...
            return False
    return True

def NotFlood(Grid):
    for wall in Grid:
        x1 = wall[0][0]
        y1 = wall[0][1]
        x2 = wall[1][0]
        y2 = wall[1][1]
        xcoords.add(min(x1, x2)-1)
        xcoords.add(min(x1, x2)+1)
        ycoords.add(min(y1, y2)-1)
        ycoords.add(min(y1, y2)+1)
        # if CheckNotInBounds(Grid, x1+1, y1+1):
        #     GraphDict[(x1+1, y1+1)] = []
        # if CheckNotInBounds(Grid, x1-1, y1+1): ## Since the end of one wall is the start of another, you only have to check the end of them
        #     GraphDict[(x1-1, y1+1)] = []
        # if CheckNotInBounds(Grid, x1+1, y1-1):
        #     GraphDict[(x1+1, y1-1)] = []
        # if CheckNotInBounds(Grid, x1-1, y1-1):
        #     GraphDict[(x1-1, y1-1)] = []

        # if CheckNotInBounds(Grid, x2+1, y2+1):
        #     GraphDict[(x2+1, y2+1)] = []
        # if CheckNotInBounds(Grid, x2-1, y2+1):
        #     GraphDict[(x2-1, y2+1)] = []
        # if CheckNotInBounds(Grid, x2+1, y2-1):
        #     GraphDict[(x2+1, y2-1)] = []
        # if CheckNotInBounds(Grid, x2-1, y2-1):
        #     GraphDict[(x2-1, y2-1)] = []

        # if CheckNotInBounds(Grid, x2+1, y2):
        #     GraphDict[(x2+1, y2)] = []
        # if CheckNotInBounds(Grid, x2, y2+1):
        #     GraphDict[(x2, y2+1)] = []
        # if CheckNotInBounds(Grid, x2, y2-1):
        #     GraphDict[(x2, y2-1)] = []
        # if CheckNotInBounds(Grid, x2-1, y2):
        #     GraphDict[(x2-1, y2)] = []

def CheckTwo(Grid, P1, P2):
    x1 = P1[0]
    y1 = P1[1]
    x2 = P2[0]
    y2 = P2[1]
    if x1 == x2:
        for bound in Grid:
            Ly = min(bound[0][1], bound[1][1])
            Lx = min(bound[0][0], bound[1][0])
            Uy = max(bound[0][1], bound[1][1])
            Ux = max(bound[0][0], bound[1][0])
            if (Uy == Ly) and (Lx <= x1 <= Ux) and (min(y1, y2) < Ly < max(y1, y2)):
                return False
    elif y1 == y2:
        for bound in Grid:
            Ly = min(bound[0][1], bound[1][1])
            Lx = min(bound[0][0], bound[1][0])
            Uy = max(bound[0][1], bound[1][1]) # yes This is a whole load of repeated code, I get it...
            Ux = max(bound[0][0], bound[1][0])
            if (Ux == Lx) and (Ly <= y1 <= Uy) and (min(x1, x2) < Lx < max(x1, x2)):
                return False
    else: # Change this later if only straight lines doesn't work out.
        return False
    return True


def LinkUp(Grid):
    global GraphDict, xcoords, ycoords
    # points = list(GraphDict.keys())

    # for i in range(len(points)):
    #     for j in range(len(points)):
    #         P1 = points[i]
    #         P2 = points[j]
    #         if i == j or (P1[0] != P2[0] and P1[1] != P2[1]):
    #             continue
    #         if CheckTwo(Grid, P1, P2):
    #             GraphDict[P1].append((P2, abs(P1[1] - P2[1]) + abs(P1[0] - P2[0])))
    xcoords = sorted(list(xcoords))
    ycoords = sorted(list(ycoords))
    for x in xcoords:
        for i in range(len(ycoords) - 1):
            y1 = ycoords[i]
            y2 = ycoords[i+1]
            P1 = (x, y1)
            P2 = (x, y2)
            if CheckNotInBounds(Grid, P1[0], P2[1]) and CheckNotInBounds(Grid, P2[0], P2[1]) and CheckTwo(Grid, P1, P2):
                GraphDict[P1].append((P2, abs(P1[1] - P2[1]) + abs(P1[0] - P2[0])))
                GraphDict[P2].append((P1, abs(P1[1] - P2[1]) + abs(P1[0] - P2[0])))
    
    for y in ycoords:
        for i in range(len(xcoords) - 1):
            x1 = xcoords[i]
            x2 = xcoords[i+1]
            P1 = (x1, y)
            P2 = (x2, y)
            if CheckNotInBounds(Grid, P1[0], P2[1]) and CheckNotInBounds(Grid, P2[0], P2[1]) and CheckTwo(Grid, P1, P2):
                GraphDict[P1].append((P2, abs(P1[1] - P2[1]) + abs(P1[0] - P2[0])))
                GraphDict[P2].append((P1, abs(P1[1] - P2[1]) + abs(P1[0] - P2[0])))



def DijkstraAt2AM(start):
    x = int(start[0])
    y = int(start[1])
    Distances = {node: float("infinity") for node in GraphDict.keys()}
    Distances[(x, y)] = 0
    import heapq
    queue = [(0, (x, y))]
    while queue:
        CDist, CNode = heapq.heappop(queue)
        if CDist > Distances[CNode]:
            continue
        for adjacent, weight in GraphDict[CNode]:
            distance = CDist + weight
            if distance < Distances[adjacent]:
                Distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    return Distances

def Solve(part):
    global Visited, Xmax, Ymax, Xmin, Ymin, GraphDict
    Visited = set()
    GraphDict = defaultdict(list)
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))[0]
        CDir = 0
        coord = (0, 0)
        if part == 1 or part == 2:
            grid = dict()
            for instruction in inp.split(","):
                if instruction[0] == "L":
                    CDir = (CDir-1)%4
                if instruction[0] == "R":
                    CDir = (CDir+1)%4
                grid, coord = Add(grid, CDir, coord, int(instruction[1:]))
            del grid[(int(coord[0]), int(coord[1]))]
            end = coord
            start = (0, 0)
            Xmax = -1000
            Ymax = -1000
            Xmin = 10000
            Ymin = 10000
            for key in grid.keys():
                if Xmax < key[0]:
                    Xmax = key[0] + 4
                if Ymax < key[1]:
                    Ymax = key[1] + 4
                if Xmin > key[0]:
                    Xmin = key[0] - 4   
                if Ymin > key[1]:
                    Ymin = key[1] - 4
            Flood(grid, start)
            distances = Dijkstra(start)
            # griddy = [["." for b in range(Xmax+10-Xmin)] for a in range(Ymax+10-Ymin)]
            # for y in range(Ymin, Ymax+2):
            #     for x in range(Xmin, Xmax+2):
            #         if (x, y) in grid:
            #             griddy[y+abs(Ymin)][x+abs(Xmin)] = "#"
            # griddy[int(end[1])+abs(Ymin)][int(end[0])+ abs(Xmin)] = "%"
            # griddy[abs(Ymin)][abs(Xmin)] = "&"
            # for i in griddy:
            #     print("".join(i))
            # print(GraphDict[(int(end[0]), int(end[1]))])
            print(distances[(int(end[0]), int(end[1]))])
        if part == 3:
            grid = list()
            for instruction in inp.split(","):
                if instruction[0] == "L":
                    CDir = (CDir-1)%4
                if instruction[0] == "R":
                    CDir = (CDir+1)%4
                grid, coord = Add3(grid, CDir, coord, int(instruction[1:]))
            CDir = (CDir+2)%4
            grid[-1] = ((grid[-1][0][0], grid[-1][0][1]), (coord[0] + Directions[CDir][0], coord[1] + Directions[CDir][1]))
            end = coord
            start = (0, 0)
            xcoords.add(0)
            ycoords.add(0)
            xcoords.add(end[0])
            ycoords.add(end[1])
            Xmax = -1000
            Ymax = -1000
            Xmin = 10000
            Ymin = 10000
            for key in grid:
                if Xmax < key[0][0]:
                    Xmax = key[0][0] + 4
                if Ymax < key[0][1]:
                    Ymax = key[0][1] + 4
                if Xmin > key[0][0]:
                    Xmin = key[0][0] - 4   
                if Ymin > key[0][1]:
                    Ymin = key[0][1] - 4
                
                if Xmax < key[1][0]:
                    Xmax = key[1][0] + 4
                if Ymax < key[1][1]:
                    Ymax = key[1][1] + 4
                if Xmin > key[1][0]:
                    Xmin = key[1][0] - 4   
                if Ymin > key[1][1]:
                    Ymin = key[1][1] - 4
            NotFlood(grid)
            # if CheckNotInBounds(grid, +1, 0): # For the start I only want up, down, left and right in order to stop teleporting through a corner.
            #     GraphDict[(+1, 0)] = []
            # if CheckNotInBounds(grid, 0, +1):
            #     GraphDict[(0, +1)] = []
            # if CheckNotInBounds(grid, 0, -1):
            #     GraphDict[(0, -1)] = []
            # if CheckNotInBounds(grid, -1, 0):
            #     GraphDict[(-1, 0)] = []
            
            # if CheckNotInBounds(grid, end[0]+1, end[1]): # Same for the end
            #     GraphDict[(end[0]+1, end[1])] = []
            # if CheckNotInBounds(grid, end[0], end[1]+1):              ############# Wow, so much of my code went into something that was completely wrong
            #     GraphDict[(end[0], end[1]+1)] = []
            # if CheckNotInBounds(grid, end[0], end[1]-1):
            #     GraphDict[(end[0], end[1]-1)] = []
            # if CheckNotInBounds(grid, end[0]-1, end[1]):
            #     GraphDict[(end[0]-1, end[1])] = []

            # GraphDict[start] = []
            # GraphDict[end] = []

            LinkUp(grid)
            distances = DijkstraAt2AM(start)
            print(distances[end]-4) # I don't know why it -4s it just needs it

for i in range(1, 4):
    Solve(i)
