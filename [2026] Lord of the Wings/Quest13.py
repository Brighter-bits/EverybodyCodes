import os
from pathlib import Path
import sys
from math import prod, floor
sys.setrecursionlimit(1000000)
os.chdir(Path(__file__).parent)
degreesInACircle = -1 # This will not be 360

Parts = ["everybody_codes_e2026_q13_p1.txt", "everybody_codes_e2026_q13_p2.txt", "everybody_codes_e2026_q13_p3.txt"]

class Hand(): # This class is a hand on a clock
    def __init__(self, i, div, dir, currentDiv, moves):
        global degreesInACircle
        self.id = i
        self.velocity = (degreesInACircle)//div # The number of degrees we complete each second
        self.position = currentDiv * self.velocity # We find our current position
        self.dir = dir
        self.velocity *= dir # Set our velocity's direction
        self.moves = moves # The number of moves left
        self.prevPosition = -1
        self.HitsSinceLastCycle = []

    def Move(self): # This just moves the position along
        self.prevPosition = self.position
        if self.moves == 0:
            self.velocity = 0
            return
        self.position = (self.position + self.velocity)
        self.moves -= 1

    def TimeToDie(self, index): # A lot like the ghosts, we need to find how many cycles until they run out of steam
        if len(self.HitsSinceLastCycle) == 0 or self.moves == 0: return float('inf')
        return self.moves / (len(self.HitsSinceLastCycle) - index)

    def resetHits(self, index): # Reset our hits, and return the number of hits we had
        HitsCollected = sum(self.HitsSinceLastCycle[index:])
        self.HitsSinceLastCycle = []
        return HitsCollected

def LongCheck(Hand1:Hand, Hand2:Hand): # This used to be longer.
    global degreesInACircle
    relativeMovement = Hand1.velocity - Hand2.velocity # How much the gap between the two hands has changed
    gap = (Hand1.prevPosition - Hand2.prevPosition) % degreesInACircle # The original gap
    if gap == 0: # If they start ontop of each other, then it doesn't count
        return False
    return gap + relativeMovement <= 0 or gap + relativeMovement >= degreesInACircle # If we predict that our gap will fall to zero or go all away around the circle, then we've hit


def CheckOverlap(HandList: list[Hand]):
    for i in range(len(HandList)):
        HandList[i].HitsSinceLastCycle.append(0) # Append zero so that every hand has a value for this cycle
    Checked = []
    total = 0
    for Hand1 in range(len(HandList)):
        for Hand2 in range(Hand1 + 1, len(HandList)):
            Hands = (Hand1, Hand2)
            if LongCheck(HandList[Hand1], HandList[Hand2]): # Check if there was an overlap
                if Hands in Checked: # If there was an overlap last turn, then discard it (this is mostly for those which have gone still on top of each other)
                    Checked.append(Hands)
                    continue
                Checked.append(Hands) # Stop a second hit from happening exactly the next turn
                total += 1 # Add one to the total
                HandList[Hand1].HitsSinceLastCycle[-1] += 1 # Add one to this cycle's hits. Since we take all the hands into account at the same time, it doesn't actually matter which hand gets the hit
    return total

def MoveAllTheHands(HandList:list[Hand]): # Guess
    for Hand in HandList:
        Hand.Move()

def HashClocks(HandList:list[Hand]): # Hash the clock's current state for comparison later
    global degreesInACircle
    answer = ""
    for Hand in HandList:
        answer += str(Hand.id) + "." + str(Hand.position%degreesInACircle) + "." + str(Hand.prevPosition%degreesInACircle) + "." + str(Hand.velocity) + "." + str(Hand.moves > 0) + "|"
    return answer 

def DoAClock(inp:list[str]): # This completes the calculation of an entire clock
    global degreesInACircle
    total = 0
    HandList:list[Hand] = []
    divs = list(map(int, inp[0].replace("hands ", "").split(":")))
    degreesInACircle = prod(divs)
    dirs = list(map(int, inp[1].replace("direction ", "").replace("CCW", "-1").replace("CW", "1").split(":")))
    currents = list(map(int, inp[2].replace("current", "").split(":")))
    moves = list(map(int, inp[3].replace("move ", "").split(":")))
    for i in range(len(divs)): # First we make the clocks
        HandList.append(Hand(i, divs[i], dirs[i], currents[i], moves[i]))
    
    prevStates = []
    while not all(a.moves == 0 for a in HandList): # While all of our clocks are moving
        HashedHands = HashClocks(HandList)
        if HashedHands in prevStates: # This is very similar to Quest 10's ghost algorithm (Because I copy and pasted it)
            index = list(prevStates).index(HashedHands)
            onTheChoppingBlock = 0
            for i in range(1, len(HandList)): # Find the hand closest to stopping
                if HandList[i].TimeToDie(index) < HandList[onTheChoppingBlock].TimeToDie(index):
                    onTheChoppingBlock = i
            cycles = floor(HandList[onTheChoppingBlock].TimeToDie(index))
            if cycles > 2:
                cycles -= 3 # Go back three round to keep the skipping more stable
            else:
                cycles = 0 # If we have less than a couple rounds left, then just don't skip
            if cycles > 0:
                for hand in HandList:
                    total += cycles * hand.resetHits(index) # Only reset hits if we are doing a cycle
                    if hand.moves > 0:
                        hand.moves -= cycles * (len(prevStates) - index) # Don't reduce hands if it's a stopped hand
            else:
                for hand in HandList:
                    hand.HitsSinceLastCycle = [] # If we're not looping, then just get rid of the Hits stored up
            prevStates = []
        else:
            prevStates.append(HashedHands) # Do a normal loop
            MoveAllTheHands(HandList)
            newOverlaps = CheckOverlap(HandList)
            total += newOverlaps
    return total

def Solve(part):
    global degreesInACircle
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        total = 0
        for i in range(0, len(inp), 5): # Quite simple, just split the inp by each clock and then add each clock's value on
            total += DoAClock(inp[i:i+4])
        print(total)


for i in range(1, 4):
    Solve(i)