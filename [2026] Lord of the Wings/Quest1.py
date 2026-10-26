import os
from pathlib import Path
from math import ceil, sqrt
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q01_p1.txt", "everybody_codes_e2026_q01_p2.txt", "everybody_codes_e2026_q01_p3.txt"]

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(int, list(map(lambda x: x.replace("\n", "").split(","), f.readlines()))[0]))
        total = 0
        if part == 1:
            for pinecones in inp:
                if sqrt(pinecones).is_integer(): # If we already have a perfect formation, then we just skip this one.
                    continue
                sideLength = ceil(sqrt(pinecones)) # Square's occur in square numbers. So finding the next whole number that makes a square is my target. This used to be floor(i) + 1, until I started commenting after the challenge.
                total += sideLength**2 - pinecones # Find the differece between the next square number and the number of pinecones we already have
        elif part == 2:
            for pinecones in inp:
                if pinecones < 8: # The minumum size is 8, which is a hollow 3x3 square.
                    total += 8 - pinecones
                    continue
                if pinecones % 4 == 0:
                    continue
                total += 4 - (pinecones % 4) # Hollow squares occur in multiples of four. As such, we can just add on 4 - the remainder after dividing by four.
        elif part == 3:
            for pinecones in inp:
                if pinecones < 8: # Again, the minimum size is a 3x3 square
                    total += 8 - pinecones
                    continue

                sideLength = ceil(sqrt(pinecones))

                if sideLength % 2 == 0: # Since we can only use odd formations, we just add 1 if we have an even side length
                    sideLength += 1
                
                if pinecones == sideLength ** 2 - 1: # Perfect formation, skip
                    continue

                total += (sideLength ** 2 - 1) - pinecones
        print(total)


            
for i in range(1, 4):
    Solve(i)