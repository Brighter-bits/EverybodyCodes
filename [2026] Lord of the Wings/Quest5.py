import os
from pathlib import Path
from itertools import product
from copy import deepcopy
from math import ceil
import sys
os.chdir(Path(__file__).parent)
sys.setrecursionlimit(16000)
Parts = ["everybody_codes_e2026_q05_p1.txt", "everybody_codes_e2026_q05_p2.txt", "everybody_codes_e2026_q05_p3.txt"]


def LandFill(y, x): # The function to fill out the Land, it's a floodfill as land must be connected.
    global grid, visited
    if (x, y) in visited:
        return

    visited.add((x, y))

    count = 0

    for i, j in product(range(-1, 2), range(-1, 2)): # This is used to check the surrounding tiles
        if i == 0 and j == 0: # Don't count the central tile in the count
            continue
        if y + i >= 0 and y + i < len(grid) and x + j >= 0 and x + j < len(grid[0]) and (grid[y + i][x + j] == "#" or grid[y + i][x + j] == "1"):
            count += 1 # If the coordinate is a valid and the tile is either land or a dark space, add one to the counter

    if count >= 5: # If the requirements are met, we can change the tile to land, and then check the surrounding tiles for if they are land.
        grid[y][x] = "#"
        for i, j in product(range(-1, 2), range(-1, 2)):
            LandFill(y + i, x + j)

def SandFill(y, x): # The function to fill out the Sand. But it doesn't need to be a flood fill since it doesn't need to be connected.
    global grid, visited

    count = 0
    for i, j in product(range(-1, 2), range(-1, 2)):
        if i == 0 and j == 0:
            continue
        
        if not(y + i >= 0 and y + i < len(grid) and x + j >= 0 and x + j < len(grid[0])) or (grid[y + i][x + j] == "." or grid[y + i][x + j] == "="):
            try: # Since we need to check if there's a water tile nearby, this has to be put into a try except loop so that the program doesn't stop if the tile is outside the grid
                if grid[y + i][x + j] == ".": # If the nearest tile is water, then we can skip all the checking and turn this tile into a sand tile.
                    count += 1000
                    break
            except: pass
            finally: # If the tile is a sand tile or a tile outside the grid, then we add 1
                count += 1

    if count >= 5:
        grid[y][x] = "="



def TreeFill1(y, x): # This is the first tree fill type.
    global grid, visited
    for i, j in product(range(-2, 3), range(-2, 3)):
        if (i == 0 and j == 0) or (i + j == 4) or (i + j == -4) or (i == 2 and j == -2) or (i == -2 and j == 2): # This takes into account the four corners
            continue
        
        if not(y + i >= 0 and y + i < len(grid) and x + j >= 0 and x + j < len(grid[0]) and (grid[y + i][x + j] == "#" or grid[y + i][x + j] == "@")): # If even one of the tiles doesn't meet the condition, then we don't make the tile a tree
            return

    grid[y][x] = "@"

def TreeFill2(y, x): # Unlike the others, this functions returns just the coordinate of the new tree so it doesn't affect the growing of other trees in this pass.
    global grid, visited
    
    count = 0
    
    for i, j in product(range(-1, 2), range(-1, 2)):
        if i == 0 and j == 0:
            continue
        
        if y + i >= 0 and y + i < len(grid) and x + j >= 0 and x + j < len(grid[0]) and (grid[y + i][x + j] == "@" or grid[y + i][x + j] == "="):
            if grid[y + i][x + j] == "=": # If an adjacent tile is sand, then immediately stop.
                return
            else:
                count += 1

    if count >= 4:
        return (y, x)
    else:
        return None

def Solve(part):
    global grid, visited
    with open(Parts[part-1]) as f:
        grid = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))

        if part != 3: # For some reason, Part 3 doesn't like having the center tile as the starting point?
            grid[len(grid)//2][len(grid[0])//2] = "#"
        else:
            grid[ceil(len(grid)/2)][ceil(len(grid[0])/2)] = "#"

        while True: # This loop continually runs the landfill program until a pass doesn't create any more land
            visited = set()
            oldGrid = deepcopy(grid) # Keep a copy of the current grid

            if part != 3:
                LandFill(len((grid))//2, len(grid[0])//2)
            else:
                LandFill(ceil(len((grid))/2), ceil(len(grid[0])/2))
            
            if oldGrid == grid: # If nothing has changed, then stop
                break

        if part >= 2: # If we need to fill in sand
            for y, x in product(range(len(grid)), range(len(grid[0]))): # Now, we turn all the leftover tiles into water tiles
                if grid[y][x] != "#":
                    grid[y][x] = "."
            while True: # Then, just like the Land section, we continually try to fill in sand until there is no change
                oldGrid = deepcopy(grid)

                for y, x in product(range(len(grid)), range(len(grid[0]))): # Iterate over the entire grid, checking for sand
                    if grid[y][x] == "#":
                        SandFill(y, x)
                
                if oldGrid == grid:
                    break

        if part == 3: # If we need to fill in trees
            while True:
                oldGrid = deepcopy(grid)

                for y, x in product(range(len(grid)), range(len(grid[0]))): # Same as the previous fills
                    if grid[y][x] == "#":
                        TreeFill1(y, x)

                if oldGrid == grid:
                    break


            for i in range(2): # The next fill only happens twice, and trees can only affect steps after theirs.
                newTreeCoords = [] # This is a list of all the trees we'll plant once we've checked all the spots they could be
                for y, x in product(range(len(grid)), range(len(grid[0]))):
                    if grid[y][x] == "#":
                        newTreeCoords.append(TreeFill2(y, x)) # If the tile is valid, add it to the list

                for coord in [x for x in newTreeCoords if x != None]: # Now, get rid of all the Nones in the Trees, and then plant them
                    grid[coord[0]][coord[1]] = "@"




        total = 0

        for line in grid: # Count up the Part's tile
            match part:
                case 1: total += line.count("#")
                case 2: total += line.count("=")
                case 3: total += line.count("@")
        
        print(total)



for i in range(1, 4):
    Solve(i)