import regex as re # Regex for finding items
import os
from pathlib import Path # Some path stuff that I have to do so a program called AREPL works.
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2025_q06_p1.txt", "everybody_codes_e2025_q06_p2.txt", "everybody_codes_e2025_q06_p3.txt"]
Types = ["a", "b", "c"] # These are all the types of squires




def Solve(part):
    with open(Parts[part-1]) as f:
        inp = f.readline().replace("\n", "") # Easy input, we just need to get rid of the \n at the end
        total = 0
        places = [re.finditer(r"A", inp), re.finditer(r"B", inp), re.finditer(r"C", inp)] # We find all of the fully grown knights
        if part == 1 or part == 2: # If it's part 1 or 2
            for Type in enumerate(Types): # Enumerate takes a list like ["a", "b", "c"] and turns it into [(0, "a"), (1, "a"), (2, "c")]. Or essentially [(index, value)]
                index = int(Type[0])
                letter = Type[1]
                for place in places[index]: # For every fully grown knight
                    total += inp[place.start(0):].count(letter) # Add the number of squires to the right of it, which are the ones it could tutor
                if part == 1:
                    return total # If it's part one, then we only need the "A"s and so can immediately return
            return total # This is for part 2 and returns after the whole thing. Yes I'm inconsistent as to whether my subroutines return values or just print them; I'm also inconsistent as to whether I say part two or part 1.


        inp2 = "".join(inp for i in range(2)) # This is just twice the input, which is more than enough to manipulate and find all the values I need (as long as the length is more than 500)
        leftvals = [0, 0, 0] # All values in the inp behind.
        middlevals = [0, 0, 0] # All values to the current inp.
        rightvals = [0, 0, 0] # All values to the right of the inp
        for Type in enumerate(Types):
            index = int(Type[0])
            letter = Type[1]
            for place in places[index]:
                if place.start(0) < 1000: # If the old knight's left will overflow
                    leftvals[index] += inp2[place.start(0)+len(inp)-1000:len(inp)].count(letter) # We add len(inp) to put the knight into the next inp, then subtract 1000 to see how far back it would go. We then take that number from there to the end of that inp so we get everything in that behind inp 
                    middlevals[index] += inp[place.start(0):place.start(0)+1001].count(letter) # We assume that there's going to be more than 1000 in each
                    middlevals[index] += inp[:place.start(0)].count(letter) # Everything from inside the middle inp
                elif place.start(0) > len(inp)-1000:
                    rightvals[index] += inp2[len(inp)+1:place.start(0)+1001].count(letter)
                    middlevals[index] += inp[place.start(0)-1000:place.start(0)].count(letter)
                    middlevals[index] += inp[place.start(0):].count(letter)
                else:
                    middlevals[index] += inp[place.start(0):place.start(0)+1001].count(letter)
                    middlevals[index] += inp[place.start(0)-1000:place.start(0)].count(letter)
        total = 0

        total += sum(middlevals)*1000 # 1000 inps
        
        total += sum(leftvals)*999 # 999 inps behind as the first inp has nothing behind it
        total += sum(rightvals)*999 # Repeat for the inps in front
        return total





for i in range(1, 4):
    print(Solve(i))