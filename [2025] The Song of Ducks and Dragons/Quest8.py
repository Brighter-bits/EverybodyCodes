import os
from pathlib import Path
from collections import defaultdict
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2025_q08_p1.txt", "everybody_codes_e2025_q08_p2.txt", "everybody_codes_e2025_q08_p3.txt"]

def intersect(NewLine, OldLine):
    if OldLine[0] > OldLine[1]:
        OldLine = [OldLine[1], OldLine[0]]
    if NewLine[0] > NewLine[1]:
        NewLine = [NewLine[1], NewLine[0]]
    if NewLine [0] < OldLine[0] < NewLine[1] and (OldLine[1] > NewLine[1] or OldLine[1] < NewLine[0]):
        return 1
    elif NewLine [0] < OldLine[1] < NewLine[1] and (OldLine[0] > NewLine[1] or OldLine[0] < NewLine[0]):
        return 1
    else:
        return 0
        


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(int, f.readline().replace("\n", "").split(",")))
        naildiff = int(max(inp)/2)
        total = 0
        lines = []
        for i in range(len(inp)-1):
            if part == 1 and abs(inp[i] - inp[i+1]) == naildiff:
                total += 1 
            if part == 2:
                # Let's scrap all of that and try this one again.
                for j in range(len(lines)):
                    total += intersect((inp[i], inp[i+1]), lines[j])
            lines.append(sorted([inp[i], inp[i+1]]))
        if part == 3:
            lines = sorted(lines)
            possibilities = []
            for i in range(1, (naildiff*2)+1): # Since this is a circle, I'm going to assume that the area around middle has the highest concentration of lines
                if i+3*((naildiff*2)/4) > (naildiff*2) + 1:
                    for j in range(int(i+((naildiff*2)/4)), (naildiff*2)+1):
                        cuts = 0
                        for k in range(len(lines)):
                            cuts += intersect((i, j), lines[k])
                            if [i, j] == lines[k]:
                                cuts += 1
                            if lines[k][0] > j:
                                break
                        possibilities.append(cuts)
                else:
                    for j in range(int(i+((naildiff*2)/4)), int(i+3*((naildiff*2)/4))):
                        cuts = 0
                        for k in range(len(lines)):
                            cuts += intersect((i, j), lines[k])
                            if [i, j] == lines[k]:
                                cuts += 1
                            if lines[k][0] > j:
                                break
                        possibilities.append(cuts)
            total = max(possibilities)


                     

        print(total)


        




for i in range(1, 4):
    Solve(i)












# if abs(inp[i+1] - inp[i]) < naildiff: # I hope this works
#     if inp[i] < inp[i+1]:
#         for nail in range(1, abs(inp[i+1]-inp[i])):
#             currentNail = inp[i] + nail
#             if currentNail > naildiff*2:
#                 currentNail = currentNail - (naildiff*2)
#             for diff in NailDict[currentNail]:
#                 if inp[i] not in diff[0] and inp[i+1] not in diff[0] and diff[0] not in diffs and not (inp[i] < diff[0][0]):
#                     diffs.append(diff[0])
#     else:
#         for nail in range(1, abs(inp[i+1]-inp[i])):
#             currentNail = inp[i] - nail
#             if currentNail < 1:
#                 currentNail = (naildiff*2) + currentNail
#             for diff in NailDict[currentNail]:
#                 if inp[i] not in diff[0] and inp[i+1] not in diff[0] and diff[0] not in diffs:
#                     diffs.append(diff[0])
# else:
#     if inp[i] < inp[i+1]:
#         for nail in range(1, abs(inp[i] + (naildiff*2) - inp[i+1])):
#             currentNail = inp[i] - nail
#             if currentNail < 1:
#                 currentNail = (naildiff*2) + currentNail
#             for diff in NailDict[currentNail]:
#                 if inp[i] not in diff[0] and inp[i+1] not in diff[0] and diff[0] not in diffs:
#                     diffs.append(diff[0])
#     else:
#         for nail in range(1, abs(-inp[i] + (naildiff*2) + inp[i+1])):
#             currentNail = inp[i] + nail
#             if currentNail > naildiff*2:
#                 currentNail = currentNail - (naildiff*2)
#             for diff in NailDict[currentNail]:
#                 if inp[i] not in diff[0] and inp[i+1] not in diff[0] and diff[0] not in diffs:
#                     diffs.append(diff[0])