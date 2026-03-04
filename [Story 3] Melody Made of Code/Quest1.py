import os
from pathlib import Path
os.chdir(Path(__file__).parent)
from collections import defaultdict
Parts = ["everybody_codes_e3_q01_p1.txt", "everybody_codes_e3_q01_p2.txt", "everybody_codes_e3_q01_p3.txt"]

class DNA:
    def __init__(self, _id, _red, _green, _blue, _shin = 0):
        self.id = int(_id)
        self.red = _red
        self.green = _green
        self.blue = _blue
        self.shine = _shin

    def CalculateGroup(self): # Calculate the group
        colours = [self.red, self.green, self.blue]
        if (colours.count(max(colours)) > 1) or (30 < self.shine < 33): # If the largest number is shared by one or more colours, or the shine is in that awkward middle bit, discard it.
            self.group = ""
            return
        highestNum = max(colours)
        colourGroup = ""
        match highestNum:
            case x if x == colours[0]:
                colourGroup = "red"
            case x if x == colours[1]:
                colourGroup = "green"
            case x if x == colours[2]:
                colourGroup = "blue"
        
        if self.shine >= 33:
            self.group = colourGroup + "Shiny"
        else:
            self.group = colourGroup + "Matte"
                


def LettersToBinary(letters:str):
    letters = list(letters)
    letters = "".join(list(map(lambda x: "0" if x.islower() else "1", letters)))
    return int(letters, 2)

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        DNAList:list[DNA] = []
        for line in inp: # For each line
            _id, colours = line.split(":")
            coloursList = list(map(LettersToBinary, colours.split(" ")))
            DNAList.append(DNA(_id, coloursList[0], coloursList[1], coloursList[2], 0 if part == 1 else coloursList[3])) # Only add the shine if we're above part 1
        if part == 1:
            total = 0
            for line in DNAList:
                if line.green > line.red and line.green > line.blue: # Find the total of all of the green dominated DNA
                    total += line.id
            print(total)
        elif part == 2:
            Max = -5
            Shiniest = []
            for line in DNAList:
                if line.shine > Max: # If we have a new maximum shinyness? (that's not how that's spelt)
                    Max = line.shine # Set the new value
                    Shiniest = [line] # Discard all the old values that were at the maximum sheen (that's the word).
                elif line.shine == Max:
                    Shiniest.append(line)
            print(min(Shiniest, key=lambda x: x.red + x.blue + x.green).id)
        elif part == 3:
            ShinyDict = defaultdict(list)
            for line in DNAList:
                line.CalculateGroup()
                # print(str(line.id), str(line.red), str(line.green), str(line.blue), str(line.shine), line.group, sep="\t")
                ShinyDict[line.group].append(line.id)
            ShinyDict[""] = []
            print(sum(max(list(ShinyDict.values()), key = len))) # Find the sum of the values of the list with the MOST values.

for i in range(1, 4):
    Solve(i)