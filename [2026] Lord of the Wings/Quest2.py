import os
from pathlib import Path
from collections import defaultdict
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q02_p1.txt", "everybody_codes_e2026_q02_p2.txt", "everybody_codes_e2026_q02_p3.txt"]

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split(" "), f.readlines()))
        total = 0
        for alloys in inp:
            alloyTypes = list(set(list("".join(alloys))) - set(["<", ">"])) # This gets all of the numbers in the list, so we can see which one never showed up in our FindNumbersGreaterThan, which would be the largest number.
            comparisonInfo = FindNumbersGreaterThan(alloys)

            if part == 2:
                comparisonInfo = FillInTheBlanks(comparisonInfo, 2) # Since the missing comparison was always for one of the bottom two, this used to be a simple if-else statement that would add a -1 to the end of whichever number contained the other. For code conciseness, that is now gone
            elif part == 3:
                comparisonInfo = FillInTheBlanks(comparisonInfo, 10)

            comparisonInfo = sorted(comparisonInfo, key=lambda x: len(x[1]))
            comparisonInfo = list(map(lambda x: x[0], comparisonInfo))
            total += int("".join(list(set(alloyTypes) - set(comparisonInfo)) + comparisonInfo))
        print(total)

def FindNumbersGreaterThan(comparisons): # This function creates a dictionary which contains a list of all the numbers greater than the key, and returns it in items() form.
    comparisonInfo = defaultdict(list)

    for comparison in comparisons:
        if "<" in comparison:
            comparison = comparison.split("<")
            comparisonInfo[comparison[0]] += comparison[1] # Add the second number to the numbers greater than the first
        else:
            comparison = comparison.split(">")
            comparisonInfo[comparison[1]] += comparison[0]

    comparisonInfo = comparisonInfo.items()
    comparisonInfo = sorted(comparisonInfo, key=lambda x: len(x[1]))
    return comparisonInfo

def FillInTheBlanks(comparisonInfo, n): # This is an awful function, that checks for where a number appears in other numbers' greater list, then adds -1s proportional to the first number's greater list. Do this enough times and the stack sorts itself.
    comparisonInfo = sorted(comparisonInfo, key=lambda x: len(x[1]), reverse=True)
    for a in range(n):
        for i in range(len(comparisonInfo)):
            for j in range(len(comparisonInfo)):
                if comparisonInfo[i][0] in comparisonInfo[j][1]:
                    comparisonInfo[j] = (comparisonInfo[j][0], comparisonInfo[j][1] + ["-1" for _ in range(len(comparisonInfo[i][1]))])
    return comparisonInfo

for i in range(1, 4):
    Solve(i)