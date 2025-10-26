Parts = ["everybody_codes_e2_q03_p1.txt", "everybody_codes_e2_q03_p2.txt", "everybody_codes_e2_q03_p3.txt"]
import regex as re
import sys
from copy import deepcopy
sys.setrecursionlimit(10000)
# GridDict = dict()
Visited = []
Cache = dict()
class Die():
    id = -100
    seed = -100
    pulse = -100
    faces = []
    RollNum = 1
    index = 0
    def __init__(self, _id, _faces, _seed):
        self.pulse = _seed
        self.seed = _seed
        self.faces = _faces
        self.id = _id
    def Roll(self):
        spin = self.RollNum * self.pulse
        self.index = (self.index + spin) % len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse += 1 + self.RollNum + self.seed
        self.RollNum += 1
        return self.faces[self.index]
    def Reset(self):
        self.pulse = self.seed
        self.index = 0
        self.RollNum = 1

def DiceMaker(inp) -> list[Die]:
    Dice = []
    for i in range(len(inp)):
        pieces = inp[i].split()
        pieces[0] = int(re.findall(r"[0-9]+", pieces[0])[0])
        pieces[1] = list(map(int, re.findall(r"[-0-9]+", pieces[1])))
        pieces[2] = int(re.findall(r"[-0-9]+", pieces[2])[0])
        Dice.append(Die(pieces[0], pieces[1], pieces[2]))
    return Dice

# def FloodDict(Node, grid):
#     if Node in Visited:
#         return
#     Visited.append(Node)
#     x = Node[0]
#     y = Node[1]
#     GridDict[Node] = {}
#     if y != 0:
#         GridDict[Node][grid[y-1][x]] = (x, y-1)
#         FloodDict((x, y-1), grid)
#     if y != len(grid)-1:
#         GridDict[Node][grid[y+1][x]] = (x, y+1)
#         FloodDict((x, y+1), grid)
#     if x != 0:
#         GridDict[Node][grid[y][x-1]] = (x-1, y)
#         FloodDict((x-1, y), grid)
#     if x != len(grid[0])-1:
#         GridDict[Node][grid[y][x+1]] = (x+1, y)
#         FloodDict((x+1, y), grid)

grid = []
def Move(Node, Roller: Die):
    global grid
    if (Node, Roller.id, Roller.RollNum) in Cache:
        return
    else:
        Cache[(Node, Roller.id, Roller.RollNum)] = True
    if Node not in Visited:
        Visited.append(Node)
    NextRoller = deepcopy(Roller)
    NextValue = NextRoller.Roll()
    x = Node[0]
    y = Node[1]
    if y != 0 and grid[y-1][x] == NextValue:
        Move((x, y-1), NextRoller)
    if y != len(grid)-1 and grid[y+1][x] == NextValue:
        Move((x, y+1), NextRoller)
    if x != 0 and grid[y][x-1] == NextValue:
        Move((x-1, y), NextRoller)
    if x != len(grid[0])-1 and grid[y][x+1] == NextValue:
        Move((x+1, y), NextRoller)
    if grid[y][x] == NextValue:
        Move((x, y), NextRoller)

def Solve(part):
    global grid
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        Dice: list[Die] = []
        if part == 1:
            Dice = DiceMaker(inp)
            total = 0
            count = 0
            while total < 10000:
                for roller in Dice:
                    total += roller.Roll()
                count += 1
            print(count)
        elif part == 2:
            target = list(map(int, list(inp[-1])))
            Dice = DiceMaker(inp[:-2])
            
            total = []
            for roller in Dice:
                counter = 0
                place = 0
                while True:
                    try:
                        if roller.Roll() == target[place]:
                            place += 1
                        counter += 1
                    except:
                        break
                total.append(counter)
            total = enumerate(total)
            total = sorted(total, key=lambda x: x[1])
            total = list(map(lambda x: x[0]+1, total))
            print(total)
        elif part == 3:
            SplitPoint = inp.index("")
            Dice = DiceMaker(inp[:SplitPoint])
            grid = list(map(lambda x: list(map(int, list(x))), inp[SplitPoint+1:]))
            for Roller in Dice:
                Cache = []
                IValue: int = Roller.Roll()
                for y in range(len(grid)):
                    for x in range(len(grid[0])):
                        if grid[y][x] == IValue:
                            Move((x, y), Roller)
                            Roller.Reset()
                            Roller.Roll()
            print(len(Visited))
            


Solve(3)