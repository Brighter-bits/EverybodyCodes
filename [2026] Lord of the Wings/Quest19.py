import os
from pathlib import Path
from collections import Counter
from itertools import permutations
from math import prod
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q19_p1.txt", "everybody_codes_e2026_q19_p2.txt", "everybody_codes_e2026_q19_p3.txt"]

def Mix(Under, Over): # This mixes the background and foreground
    Colours = Counter() # We make a acounter
    for i in range(len(Under)):
        if Under[i] == Over[i]: # If the colours are the same, then we add one for the same colour
            Colours[Under[i]] += 1
            continue

        ColourMix = "".join(sorted(Under[i] + Over[i])) # We then turn it into a string to make it a bit easier to deal with

        if "K" in ColourMix: # If there's a K in there, we add one to K
            Colours["K"] += 1
            continue

        match ColourMix: # Then we just match the rest of the colours up
            case "CM":
                Colours["B"] += 1
            case "CY":
                Colours["G"] += 1
            case "MY":
                Colours["R"] += 1
    return prod(list(map(lambda x: x[1], Colours.most_common(3)))) # We return the product of the three most common colours
    

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        Under = ""
        Over = ""
        CurrentlyUnder = True
        for line in inp: # This splits our grid into two straight lines of text.
            if CurrentlyUnder:
                if line != "":
                    Under += line
                else:
                    CurrentlyUnder = False # We now begin filling in the other square
            else:
                Over += line

        if part == 1:
            print(Mix(Under, Over)) # Just mix it
        elif part == 2:
            originalOver = str(Over)
            totals = []
            for combo in permutations(["C", "K", "Y", "M"], 4): # We find every possible permutation and find the largest one
                for j in range(4):
                    Over = Over.replace(str(j+1), combo[j]) # Substitute our colours in

                totals.append(Mix(Under, Over)) # Mix and append to the possible totals

                Over = str(originalOver)
            print(max(totals))
        elif part == 3:
            counts = sorted([Under.count("C"), Under.count("M"), Under.count("Y"), Under.count("K")]) # Find the counts of each of the colours
            smallest = counts.pop(0)
            totalOfTheOtherThree = sum(counts)

            # Okay, at this point I'm pretty sure my solution falls apart if your K isn't the smallest of the groups.
            totals = []

            if totalOfTheOtherThree % 3 == 0: # This is the case where the smallest one is negligable
                totals.append((totalOfTheOtherThree//3) ** 3)
            elif totalOfTheOtherThree % 3 == 1:
                totals.append(int(totalOfTheOtherThree//3) ** 2 * (int(totalOfTheOtherThree//3) + 1))
            else:
                totals.append(int(totalOfTheOtherThree//3) * (int(totalOfTheOtherThree//3) + 1) ** 2)

            if totalOfTheOtherThree % 2 == 0: # This is the case where the smallest one isn't negligable
                totals.append((totalOfTheOtherThree//2) ** 2 * smallest)
            else:
                totals.append(int(totalOfTheOtherThree//2) * (int(totalOfTheOtherThree//2) + 1) * smallest)
            print(max(totals))
            # print((19045**2) * 3894) # This was how I originally clculated it, I just plugged in numbers and found the largest one
            # print(12696 * 12697 * 12697)
            


for i in range(1, 4):
    Solve(i)