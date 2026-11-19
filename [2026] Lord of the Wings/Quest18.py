import os
from pathlib import Path
import heapq
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q18_p1.txt", "everybody_codes_e2026_q18_p2.txt", "everybody_codes_e2026_q18_p3.txt"]

def CheckHeightRollover(rollovers): # This is a simple function which eliminates any rolling over heights.
    newRolls = []
    for i in range(len(rollovers)):
        if rollovers[i][0] <= rollovers[i][1]: # Only allow a height to exist, if it's upper bound is higher than it's lower bound.
            newRolls.append(rollovers[i])
    return newRolls

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        currentHeightRollover = []
        total = 0

        if part != 1: # This part takes width into account by placing an integer into the list that the program sees as a block of the same height
            newInp = []
            for i in range(len(inp)):
                newInp.append(inp[i]) # Always append the first line to the list
                wdith = list(map(int, inp[i].replace("x=", "").replace("y=", "").replace("width=", "").split(" ")))[2] # How did I spell width wrong?? Anyway, this just extracts the width from the string (quite inefficiently really)
                if wdith > 1: # If the width is greater than 1
                    wdith -= 1 # This is the number of stacks not including the final one
                    newInp.append(wdith) # Append it as an integer
                    newInp.append(inp[i]) # Then append another stack so we can calculate the bit after the large block
            inp = newInp # Push the new input to inp

        buffer = 0 # This is buffer, which just holds how far from the original x coordinate a stack is due to its width.
        for i in range(len(inp)-1):

            if isinstance(inp[i], int): # If our first part is a large block, set x to -1 as an indicator
                x1 = -1
            else:
                x1, y1 = list(map(int, inp[i].replace("x=", "").replace("y=", "").split(" ")[:2])) # If not, grab the x and y of the stack

            if i == 0: # We always add the second stack when we're comparing, so we need to add the first stack on our first comparison
                total += y1

            if isinstance(inp[i+1], int): # If what's coming next is the giant block, just skip
                continue
            else:
                x2, y2 = list(map(int, inp[i+1].replace("x=", "").replace("y=", "").split(" ")[:2]))

            
            if x1 == -1: # If we're at a large block
                total += y2 * inp[i] # Add the block to our total
                buffer = inp[i] # Give our buffer a value
                continue
            else:
                total += y2 # If we're inbetween blocks, then just add the value of the next stack

            if y1 <= y2: # If the previous stack is shorter of the same height
                total += y1 * (x2 - (x1 + buffer) - 1) # We have no heigher rollover, so just add the space inbetween the stacks
                for j in range(len(currentHeightRollover)): # Now check if any rollovers apply
                    if y2 > currentHeightRollover[j][0]: # If the height of the next stack is higher than the lower bound of a rollover, then we can fill it in
                        if y2 <= currentHeightRollover[j][1]: # If the rollover's upper bound is greater than the next stack, then there will still be some height rollover left over
                            total += (y2-currentHeightRollover[j][0]) * (x2 - currentHeightRollover[j][2] - 1)
                            currentHeightRollover[j] = (y2, currentHeightRollover[j][1], currentHeightRollover[j][2])
                        else: # If not, then we can only go up to the height of the rolled-over stack
                            total += (currentHeightRollover[j][1] - currentHeightRollover[j][0]) * (x2 - currentHeightRollover[j][2] - 1)
                            currentHeightRollover[j] = (y2, currentHeightRollover[j][1], currentHeightRollover[j][2])

            else:
                currentHeightRollover.append((y2, y1, x1 + buffer)) # If our stack is than the next, we add it to the rollovers. The first element is the height of the next stack, as that section can't be rolled over. The next is the height of the current stack, once we find a stack higher than it, then we know that this rollover will not be going any further. The last is the x-coord with the buffer taken into account
                total += y2 * (x2 - (x1+buffer) - 1)

            currentHeightRollover = CheckHeightRollover(currentHeightRollover) # Get rid of any completed rollovers
            buffer = 0 # Set our buffer to zero

        print(total)


for i in range(1, 4):
    Solve(i)