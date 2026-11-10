import os
from pathlib import Path
from itertools import product
from math import floor
from copy import deepcopy
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2026_q10_p1.txt", "everybody_codes_e2026_q10_p2.txt", "everybody_codes_e2026_q10_p3.txt"]

class NullGhost(): # A class containing everything one would want to know about a Nullghost
    def __init__(self, id, dir, health):
        self.id = id # A unique ID for the bash
        self.direction = dir # The current direction
        self.health = health # The amount of health the ghost has
        self.healthLostSinceLastCycle = [] # A list of how much damage each ghost took on each round
    def __str__(self): # Makes printing the grid a bit pretiter
        return self.direction
    def TimeToDie(self, index): # The number of cycles it would take for the ghost to perish
        if sum(self.healthLostSinceLastCycle) == 0: return float('inf')
        return self.health / sum(self.healthLostSinceLastCycle[index:])
    def FastPain(self, Cycles, index): # Quickly hurt the ghosts by iterating over cycles
        self.health -= Cycles * sum(self.healthLostSinceLastCycle[index:])
        self.healthLostSinceLastCycle = []

def NextRoundMovement(inp): # This function calculates where each ghost will be next turn if they just moved forward
    nextSpaces = []
    for x, y in product(range(len(inp[0])), range(len(inp))): # Check every square
        if type(inp[y][x]) == list and len(inp[y][x]) > 1: # If we have more than one ghost, then do each ghost individually.
            for ghost in inp[y][x]:
                if ghost.health == 0:
                    continue
                if ghost.direction == ">":
                    nextSpaces.append((ghost, (x+1, y)))
                if ghost.direction == "<":
                    nextSpaces.append((ghost, (x-1, y)))
                if ghost.direction == "^":
                    nextSpaces.append((ghost, (x, y-1)))
                if ghost.direction == "v":
                    nextSpaces.append((ghost, (x, y+1)))
            continue
        if type(inp[y][x]) != str: # If the square has something on it
            if type(inp[y][x]) == list: # The square may have a single ghost inside a list, so we take the ghost out.
                if len(inp[y][x]) == 1:
                    inp[y][x] = inp[y][x][0]
                else:
                    inp[y][x] = "." # If the list is empty, then both ghosts died, and so it's now an empty square
                    continue
            if inp[y][x].health == 0: # If it's dead don't let it go.
                continue
            if inp[y][x].direction == ">":
                nextSpaces.append((inp[y][x], (x+1, y)))
            if inp[y][x].direction == "<":
                nextSpaces.append((inp[y][x], (x-1, y)))
            if inp[y][x].direction == "^":
                nextSpaces.append((inp[y][x], (x, y-1)))
            if inp[y][x].direction == "v":
                nextSpaces.append((inp[y][x], (x, y+1)))
    return nextSpaces

def SpacesToHashable(spaces: list): # Turn the list of ghosts into a hash
    hashable = ""
    for space in sorted(spaces, key=lambda x: x[0].id): # We always have the ghost sorted in ID order
        hashable += str(space[0].id) + str(space[0].direction) + "." + str(space[1][0]) + "." +  str(space[1][1]) + "|" # The hash only matches if each ghost is in the same place in the same direction it was.
    return hashable

def loop(inp, nextSpaces): # The main loop that updates the grid
    Part1Total = 0
    for placement in nextSpaces: # Firstly, we check for walls
        x, y = placement[1]
        ghost:NullGhost = placement[0]

        if inp[y][x] == "#": # If the ghost hits a wall
            ghost.health -= 1 # Decrease health by 1
            ghost.healthLostSinceLastCycle.append(1) # Add on a hit for this cycle.
            if ghost.health == 0: # Kill the ghost if it has run out of health
                continue
            match ghost.direction: # Depending on the ghost directions, change it's direction and put it back before it hit the wall.
                case "<":
                    ghost.direction = "^"
                    inp[y][x+1] = ghost
                case ">":
                    ghost.direction = "v"
                    inp[y][x-1] = ghost
                case "^":
                    ghost.direction = ">"
                    inp[y+1][x] = ghost
                case "v":
                    ghost.direction = "<"
                    inp[y-1][x] = ghost
            Part1Total += 1
    
    for placement in nextSpaces: # Now update all the other ghosts
        x, y = placement[1]
        ghost = placement[0]
        if inp[y][x] == ".": # If it's an open space, then append 0
            inp[y][x] = ghost
            ghost.healthLostSinceLastCycle.append(0)

        elif inp[y][x] != "#":
            if type(inp[y][x]) == NullGhost: # If there's currently only one NullGhost in the spot, then this is the first collision.
                inp[y][x].health -= 1
                inp[y][x].healthLostSinceLastCycle[-1] += 1 # Add one to this round's pain
                if inp[y][x].health != 0: # If the ghost isn't dead then change its direction. If it is then make it an empty list
                    match inp[y][x].direction:
                        case "<":
                            inp[y][x].direction = ">"
                        case ">":
                            inp[y][x].direction = "<"
                        case "^":
                            inp[y][x].direction = "v"
                        case "v":
                            inp[y][x].direction = "^"
                    inp[y][x] = [inp[y][x]]
                else:
                    inp[y][x] = []
                Part1Total += 1

            ghost.health -= 1 # We now update the current ghost
            ghost.healthLostSinceLastCycle.append(1)
            if ghost.health == 0:
                continue

            match ghost.direction:
                case "<":
                    ghost.direction = ">"
                    inp[y][x].append(ghost)
                case ">":
                    ghost.direction = "<"
                    inp[y][x].append(ghost)
                case "^":
                    ghost.direction = "v"
                    inp[y][x].append(ghost)
                case "v":
                    ghost.direction = "^"
                    inp[y][x].append(ghost)
            Part1Total += 1
    return inp, Part1Total


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        EmptyGrid = deepcopy(inp)
        for x, y in product(range(len(inp[0])), range(len(inp))):
            if "<" in EmptyGrid[y][x] or "^" in EmptyGrid[y][x] or ">" in EmptyGrid[y][x] or "v" in EmptyGrid[y][x]: # Make a grid without any ghosts on it
                EmptyGrid[y][x] = "."

        for x, y in product(range(len(inp[0])), range(len(inp))):
            if inp[y][x] == "<":
                inp[y][x] = NullGhost((2**x * 3**y), "<", 10000) if part != 3 else NullGhost((2**x * 3**y), "<", 1000000000000) # Create the ghosts, the ID is just a simple prime factor key of it's initial position
            if inp[y][x] == ">":
                inp[y][x] = NullGhost((2**x * 3**y), ">", 10000) if part != 3 else NullGhost((2**x * 3**y), ">", 1000000000000)
            if inp[y][x] == "^":
                inp[y][x] = NullGhost((2**x * 3**y), "^", 10000) if part != 3 else NullGhost((2**x * 3**y), "^", 1000000000000)
            if inp[y][x] == "v":
                inp[y][x] = NullGhost((2**x * 3**y), "v", 10000) if part != 3 else NullGhost((2**x * 3**y), "v", 1000000000000)
            

        rounds = -1
        nextSpaces = ["."]
        prevSpaces = []
        if part == 1:
            rounds += 1
            for i in range(10):
                nextSpaces = NextRoundMovement(inp)

                inp = deepcopy(EmptyGrid)
                inp, newCollisions = loop(inp, nextSpaces)
                rounds += newCollisions
        else:
            while len(nextSpaces) != 0:
                nextSpaces = NextRoundMovement(inp) # Find where the ghosts will be next turn

                hashedNextSpaces = SpacesToHashable(nextSpaces) # Hash the next state

                if hashedNextSpaces in prevSpaces: # If we're in a loop
                    index = list(prevSpaces).index(hashedNextSpaces) # Find where the loop begins
                    onTheChoppingBlock = NullGhost(-1, ">", 1)
                    for ghost, _ in nextSpaces: # Find the ghost who is closest to dying
                        if ghost.TimeToDie(index) < onTheChoppingBlock.TimeToDie(index):
                            onTheChoppingBlock = ghost
                    cycles = floor(onTheChoppingBlock.TimeToDie(index)) # We don't do decimal cycles
                    if cycles > 2:
                        cycles -= 3 # Go back three round to keep the skipping more stable
                    else:
                        cycles = 0 # If we have less than a couple rounds left, then just don't skip
                    for i in range(len(nextSpaces)): # Now, apply the skips
                        nextSpaces[i][0].FastPain(cycles, index)
                    rounds += cycles * (len(prevSpaces) - index) # Add on the number of rounds
                    prevSpaces = [] # Reset the list of previous states

                else: # If we aren't skipping, then do a normal loop.
                    prevSpaces.append(hashedNextSpaces)
                    inp = deepcopy(EmptyGrid)
                    inp, _ = loop(inp, nextSpaces)
                    rounds += 1


        print(rounds)
            


            
            

for i in range(1, 4):
    Solve(i)