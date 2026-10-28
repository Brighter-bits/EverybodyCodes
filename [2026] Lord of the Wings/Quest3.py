import os
from pathlib import Path
from itertools import cycle
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q03_p1.txt", "everybody_codes_e2026_q03_p2.txt", "everybody_codes_e2026_q03_p3.txt"]

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split(" "), f.readlines())) # ISO-ABCD WXYZ => A*W^3 + B*X^2 + C*Y + D
        total = 0
        for vote in inp:
            bases = list(map(int, list(vote[0].replace("ISO-", "").replace("ISO2-", "")))) # Read the first part (the bases), and get rid of the ISO bits at the start. I turn these into numbers as these don't need to be re-reversed back later.
            normal = list(vote[1]) # Get the second part. This originally converted immediately to integers, but this didn't work so well in part 3

            normal.reverse() # Reverse both of the inputs, so that my for loop goes up rather than down (and thus looks prettier)
            bases.reverse()
            if part == 3 and not isSmallest(normal, bases): # If we're doing part three, just make sure that the ISO2 is valid
                continue

            total += ISO2Dec(normal, bases) # Add onto the total

        print(total)

def ISO2Dec(normal: list[str], bases: list[int]):
    """
    Convert the ISO or ISO2 format into it's Decimal equivalent.
    """
    bases = cycle(bases) # Turn the bases into a cycle so they can be reused
    total = 0
    for i in range(len(normal)):
        total += int(normal[i]) * (next(bases)**i) # This is just the formula on line 10, just reversed in ascending powers
    return total

def isSmallest(normal, bases):
    """
    Check if this ISO2 is the smallest method possible to get that Decimal value. Returns True if no smaller methods are found, and False if there are smaller methods.
    """
    target = ISO2Dec(normal, bases) # First find what the Decimal value we are aiming for is
    normalValue = int("".join(reversed(normal))) # Undo the reversal, and turn the normal into an integer
    for i in range(normalValue): # Check every number lower than the integer
        i = "".join(list(reversed(str(i)))) # Reverse the new number
        if ISO2Dec(i, bases) == target:
            return False
    return True

for i in range(1, 4):
    Solve(i)