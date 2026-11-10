import os
from pathlib import Path
from collections import Counter # Let's GOOOOOO
from functools import cache
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2026_q09_p1.txt", "everybody_codes_e2026_q09_p2.txt", "everybody_codes_e2026_q09_p3.txt"]

def TurnCounterToLengths(counter:Counter): # A quick function which multiplies the length of the branch by how many branches of that length there are
    total = 0
    for key, val in counter.items():
        total += key * val
    return total

@cache
def Split(BranchesAtLimit, LeavesAtLimit, growth): # This function is given a certain number of branches and leaves that need to be split, and returns two counters containing the new branches and leaves created by the split
    Branches = Counter()
    Leaves = Counter()
    TrunkLength = growth//2
    if BranchesAtLimit != 0: # Branches split into two branches, and one new leaf
        Branches[TrunkLength] += BranchesAtLimit * 2
        Leaves[1] += BranchesAtLimit

    if LeavesAtLimit != 0: # Leaves split into a branch and two leaves
        Leaves[TrunkLength] += LeavesAtLimit
        Branches[TrunkLength] += LeavesAtLimit

        Leaves[1] += LeavesAtLimit

    return Branches, Leaves


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split(","), f.readlines()))
        total = 0
        for tree in inp:
            growth = int(tree[1].replace(" growth=", ""))
            limit = int(tree[2].replace(" limit=", ""))
            if part == 1:
                Elements = Counter()
                Elements[1] = 1
                Seconds = 1
                Splits = 0
                while TurnCounterToLengths(Elements) + Splits < limit:
                    for i in range(max(Elements.keys()), -1, -1): # increment the key, essentially simulating the growth by one
                        Elements[i+1] = Elements[i]
                    if Elements[growth] != 0:
                        newSplits = Elements[growth] # Find how many branches are at the limit
                        Elements[growth] = 0

                        Splits += newSplits

                        TrunkLength = growth//2
                        Elements[TrunkLength] += newSplits * 2 # Split the branches in two by adding two at half length

                        Elements[1] += newSplits # Add the new branches

                    Seconds += 1
                total += Seconds
            elif part == 2 or part == 3:
                Split.cache_clear() 
                Branches = Counter()
                Leaves = Counter()
                Leaves[1] = 1
                Seconds = 1
                while Leaves.total() < limit:
                    Branches = +Branches # Found this here https://stackoverflow.com/questions/70435586/how-can-i-remove-keys-with-values-of-0-while-scanning-the-dictionary-to-search, and wow it's useful.
                    Leaves = +Leaves
                    largestBranch = 0
                    try:
                        largestBranch = max(Branches.keys())
                    except:
                        pass

                    largestLeaf = max(Leaves.keys())

                    if largestLeaf > largestBranch: # We firsty find the longest branch/leaf, we then choose the larger. We don't want to skip and cause a branch or leaf to go over the growth limit
                        Diff = growth - largestLeaf
                    else:
                        Diff = growth - largestBranch


                    for value in sorted(list(Branches.keys()), reverse=True): # Sort the branches from largest to smallest to stop any values being overwritten before they move up. Then add the difference to each branch
                        Branches[value + Diff] = Branches[value]
                        Branches[value] = 0
                    for value in sorted(list(Leaves.keys()), reverse=True): # Sort the branches from largest to smallest to stop any values being overwritten before they move up. Then add the difference to each branch
                        Leaves[value + Diff] = Leaves[value]
                        Leaves[value] = 0

                    newBranches, newLeaves = Split(Branches[growth], Leaves[growth], growth) # Find how many new branches and leaves have just been created.
                    Branches.update(newBranches)
                    Leaves.update(newLeaves)
                    Branches[growth] = 0
                    Leaves[growth] = 0

                    Seconds += Diff
                total += Seconds
        print(total)

for i in range(1, 4):
    Solve(i)



### Old Slow Code for Reference ###
# Split.cache_clear()
# growth = int(tree[1].replace(" growth=", ""))
# limit = int(tree[2].replace(" limit=", ""))
# Branches = Counter()
# Leaves = Counter()
# Leaves[1] = 1
# Seconds = 1
# while Leaves.total() < limit:
#     try:
#         for i in range(max(Branches.keys()), -1, -1):
#             Branches[i+1] = Branches[i]
#     except:
#         pass
#     for i in range(max(Leaves.keys()), -1, -1):
#         Leaves[i+1] = Leaves[i]
#     newBranches, newLeaves = Split(Branches[growth], Leaves[growth], growth)
#     Branches.update(newBranches)
#     Leaves.update(newLeaves)
#     Branches[growth] = 0
#     Leaves[growth] = 0

#     Seconds += 1
# total += Seconds