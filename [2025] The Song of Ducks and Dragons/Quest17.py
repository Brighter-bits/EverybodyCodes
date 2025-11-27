from copy import deepcopy
import os
from pathlib import Path
import sys
from collections import defaultdict
sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q17_p1.txt", "everybody_codes_e2025_q17_p2.txt", "everybody_codes_e2025_q17_p3.txt"]

GraphDict = defaultdict(list)
ToVisitLater = set()
ToVisitNow = set()
Visited = set()

def OrdinaryFlood(Grid, Node):
    global Visited, ToVisitLater
    if Node in Visited:
        return
    Visited.add(Node)
    x = int(Node[0])
    y = int(Node[1])

    if y > 0:
        GraphDict[(x, y)].append((Grid[y-1][x], (x, y-1)))
        OrdinaryFlood(Grid, (x, y-1))
    if y < len(Grid)-1:
        GraphDict[(x, y)].append((Grid[y+1][x], (x, y+1)))
        OrdinaryFlood(Grid, (x, y+1))
    if x > 0:
        GraphDict[(x, y)].append((Grid[y][x-1], (x-1, y)))
        OrdinaryFlood(Grid, (x-1, y))
    if x < len(Grid[0]) - 1:
        GraphDict[(x, y)].append((Grid[y][x+1], (x+1, y)))
        OrdinaryFlood(Grid, (x+1, y))

def VolcanoCheck(Grid, VisitedBefore):
    def VolcanoFlood(Grid, Node):
        VisitedBefore.add(Node)
        x = int(Node[0])
        y = int(Node[1])

        if (x, y-1) not in VisitedBefore:
            Grid[y-1][x]
            VolcanoFlood(Grid, (x, y-1))
        if (x, y+1) not in VisitedBefore:
            Grid[y+1][x]
            VolcanoFlood(Grid, (x, y+1))
        if (x-1, y) not in VisitedBefore:
            Grid[y][x-1]
            VolcanoFlood(Grid, (x-1, y))
        if (x+1, y) not in VisitedBefore:
            Grid[y][x+1]
            VolcanoFlood(Grid, (x+1, y))
        
        # if (x+1, y-1) not in VisitedBefore:
        #     Grid[]
        #     VolcanoFlood(Grid, (x+1, y-1))
        # if (x+1, y+1) not in VisitedBefore:
        #     Grid[]
        #     VolcanoFlood(Grid, (x+1, y+1))
        # if (x-1, y-1) not in VisitedBefore:
        #     Grid[]
        #     VolcanoFlood(Grid, (x-1, y-1))
        # if (x-1, y+1) not in VisitedBefore:
        #     Grid[]
        #     VolcanoFlood(Grid, (x-1, y+1))
    try:
        VolcanoFlood(Grid, (len(Grid[0])//2, len(Grid)//2))
    except:
        return False
    return True

def JoinSet(sets):
    FullSet = set()
    for Cset in sets:
        FullSet |= Cset
    return FullSet

def Flood(Grid, Node, Circle):
    global Visited, ToVisitLater
    Visited.add(Node)
    x = int(Node[0])
    y = int(Node[1])
    val = Grid[y][x]

    if (x, y-1) not in Visited and CheckCircle((x, y-1), Circle):
        ToVisitLater.add((x, y-1))
    if (x, y+1) not in Visited and CheckCircle((x, y+1), Circle):
        ToVisitLater.add((x, y+1))
    if (x-1, y) not in Visited and CheckCircle((x-1, y), Circle):
        ToVisitLater.add((x-1, y))
    if (x+1, y) not in Visited and CheckCircle((x+1, y), Circle):
        ToVisitLater.add((x+1, y))
    
    if (x+1, y-1) not in Visited and CheckCircle((x+1, y-1), Circle):
        ToVisitLater.add((x+1, y-1))
    if (x+1, y+1) not in Visited and CheckCircle((x+1, y+1), Circle):
        ToVisitLater.add((x+1, y+1))
    if (x-1, y-1) not in Visited and CheckCircle((x-1, y-1), Circle):
        ToVisitLater.add((x-1, y-1))
    if (x-1, y+1) not in Visited and CheckCircle((x-1, y+1), Circle):
        ToVisitLater.add((x-1, y+1))

    return val

def CheckCircle(Node, Centre):
    return True if (Node[1]-Centre[1])**2 + (Node[0]-Centre[0])**2 <= (Centre[2]+1)**2 else False

def FindLetter(num, grid):
    answer = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == num:
                answer.append((x, y))
    return answer

def Dijkstra(Start, End, Banned:set, Limit, Grid):
    global Visited
    Distances = {node: float("infinity") for node in GraphDict.keys()}
    Paths = {node: [node] for node in GraphDict.keys()}
    Distances[Start] = 0
    import heapq
    queue = [(0, Start, Start)]
    while queue:
        CDist, CNode, Previous = heapq.heappop(queue)
        if CDist > Distances[CNode] or CNode in Banned:
            continue
        Paths[CNode] = Paths[Previous] + [Previous]

        for distance, adjacent in GraphDict[CNode]:
            distance = CDist + distance
            if distance < Distances[adjacent] and distance <= Limit:
                Distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent, CNode))
    return Distances[End], Paths[End]
    

def Solve(part):
    global Visited, ToVisitLater, ToVisitNow
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(map(int, list(x.replace("\n", "").replace("@", "0").replace("S", "0")))), f.readlines()))
        Visited = set()
        if part == 1:
            Cx, Cy = FindLetter(0, inp)[0]
            total = 0
            for y in range(len(inp)):
                for x in range(len(inp[0])):
                    if (y-Cy)**2 + (x-Cx)**2 <= 10**2:
                        total += inp[y][x]
            print(total)
        elif part == 2:
            Cx, Cy = FindLetter(0, inp)[0]
            total = [-1]
            turn = 0
            ToVisitLater = [(Cx, Cy)]
            while total[-1] != 0 or len(total) < 3:
                cumulative = 0
                ToVisitNow = deepcopy(ToVisitLater)
                ToVisitLater = set()
                for place in ToVisitNow:
                    try:
                        cumulative += Flood(inp, place, (Cx, Cy, turn))
                    except:
                        cumulative = 0
                        del total[-2:]
                        break
                total.append(cumulative*turn)
                turn += 1
                ToVisitLater = ToVisitLater - Visited
            print(max(total))
        if part == 3:
            OrdinaryFlood(inp, (0, 0))
            Start, (Cx, Cy) = FindLetter(0, inp)
            DeadPlaces = [-1]
            Visited = set()
            turn = 0
            ToVisitLater = set([(Cx, Cy)])
            while DeadPlaces[-1] != set([0]) or len(DeadPlaces) < 3:
                cumulative = 0
                ToVisitNow = deepcopy(ToVisitLater)
                ToVisitLater = set()
                for place in ToVisitNow:
                    try:
                        Flood(inp, place, (Cx, Cy, turn))
                    except:
                        ToVisitLater = set([0])
                        break
                DeadPlaces.append(ToVisitLater)
                turn += 1
                ToVisitLater = ToVisitLater - Visited
            del DeadPlaces[0]
            del DeadPlaces[-1]
            Searching = 0
            rounds = 1
            Finals = []
            gridd = [["#" for a in range(len(inp[0]))] for a in range(len(inp))]
            for x in range(len(gridd[0])):
                for y in range(len(gridd)):
                    if (x, y) in JoinSet(DeadPlaces[:9]):
                        gridd[y][x] = "."
            # for i in gridd:
            #     print(i)
            while Searching < 3:
                attempts = []
                for i in range(rounds+1, len(inp)-Cy):
                    attempts.append(((Cx, Cy+i), Dijkstra(Start, (Cx, Cy+i), JoinSet(DeadPlaces[:rounds]), (rounds+1)*30, inp)))
                SecondPart = []
                attempts = [attempt for attempt in attempts if attempt[1][0] != float("inf")]
                # if rounds == 9:
                #     breakpoint()
                for attempt in attempts:
                    tempBanned = set()
                    if attempt[1][1][len(attempt[1][1])//2][0] < len(inp[0])//2: # Left
                        for i in range(rounds-4, len(inp)-Cy):
                            tempBanned.add((Cx-3, Cy+i))
                        SecondPart.append((attempt[0], Dijkstra(attempt[0], Start, JoinSet(DeadPlaces[:rounds] + [tempBanned]), ((rounds+1)*30) - attempt[1][0], inp)))
                    else: # Right
                        for i in range(rounds-4, len(inp)-Cy):
                            tempBanned.add((Cx+3, Cy+i))
                        SecondPart.append((attempt[0], Dijkstra(attempt[0], Start, JoinSet(DeadPlaces[:rounds] + [tempBanned]), ((rounds+1)*30) - attempt[1][0], inp)))
                    
                    if rounds == 9 and attempt[0] == (15, 25):
                        for x in range(len(gridd[0])):
                            for y in range(len(gridd)):
                                if (x, y) in attempt[1][1] or (x, y) in SecondPart[0][1][1]:
                                    if gridd[y][x] == ".":
                                        gridd[y][x] = "%"
                                    else:
                                        gridd[y][x] = "*"
                        for i in gridd:
                            print(i)

                SecondPart = [attempt for attempt in SecondPart if attempt[1][0] != float("inf")]
                if len(SecondPart) > 0:
                    for P1 in attempts:
                        for P2 in SecondPart:
                            if P1[0] == P2[0]:
                                Finals.append(rounds * (P1[1][0] + P2[1][0]))
                    print(Finals[1])
                    Searching += 1
                
                rounds += 1
                        

for i in range(1, 4):
    print(Solve(i))


