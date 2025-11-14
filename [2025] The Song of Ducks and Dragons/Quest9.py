import os
from pathlib import Path
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2025_q09_p1.txt", "everybody_codes_e2025_q09_p2.txt", "everybody_codes_e2025_q09_p3.txt"]
families:list[list[int]] = []
def FindChildren(list):
    children = [a for a in range(len(list))]
    for i in range(len(list[0])):
        for child in range(len(list)):
            counter = 0
            for parent in range(len(list)):
                if child == parent:
                    continue
                if list[child][i] != list[parent][i]:
                    counter += 1
                if counter == len(list)-1 and child in children:
                    children.remove(child)
    return children

def CheckParent(child, parent1, parent2):
    if len(child) != len(parent1) or len(child) != len(parent2):
        return False
    for i in range(len(child)):
        if child[i] != parent1[i] and child[i] != parent2[i]:
            return False
    return True

def FamilyCheck(child, parents):
    HasFam = False
    for family in range(len(families)):
        if child in families[family]:
            HasFam = True
            if parents[0] not in families[family]:
                families[family].append(parents[0])
            if parents[1] not in families[family]:
                families[family].append(parents[1]) 
        if parents[0] in families[family]:
            HasFam = True
            if child not in families[family]:
                families[family].append(child)
            if parents[1] not in families[family]:
                families[family].append(parents[1]) 
        if parents[1] in families[family]:
            HasFam = True
            if parents[0] not in families[family]:
                families[family].append(parents[0])
            if child not in families[family]:
                families[family].append(child) 
    if not HasFam:
        families.append([child, parents[0], parents[1]])

def Similarities(child, parent):
    counter = 0
    for i in range(len(child)):
        if child[i] == parent[i]:
            counter += 1
    return counter

def merge(data): # Alright, let's unpack what the hell this does
    data = [set(x) for x in data] # So, firstly the set gets rid of any duplicates in the families
    Finished = False # Then we're going to continue until we do no merges, it's a bit like bubble sort
    while not Finished:
        Finished = True
        out = []
        for a in data:
            for b in out:
                if a & b: # If there is any overlap in the intersection
                    b |= a # Add a to b, without duplicating any of the data. It's like Venn Diagrams with the U and the n.
                    Finished = False # We're going to have to loop over everything again.
                    break # Break
            else:
                out.append(a) # If the for loop doesn't break, append the data to the output
        data = out # We now 
    return [list(x) for x in data]

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.split(":")[1].replace("\n", ""), f.readlines()))
        child = [a for a in range(len(inp))]
        children = FindChildren(inp)
        FamilyDict = dict()
        for child in children:
            Break = False
            for i in range(len(inp)):
                for j in range(len(inp)):
                    if child == i or i == j or child == j:
                        continue
                    if CheckParent(inp[child], inp[i], inp[j]):
                        FamilyDict[child] = [i, j]
                        Break = True
                        break
                if Break:
                    break
        total = 0
        for child, parents in FamilyDict.items():
            if part != 3:
                total += Similarities(inp[child], inp[parents[0]]) * Similarities(inp[child], inp[parents[1]])
            if part == 3:
                FamilyCheck(child, parents)
        
        if part != 3:
            print(total)
            return
        TrueFams = merge(families)
        TrueFams = sorted(TrueFams, key= lambda x:len(x), reverse=True)
        print(sum(TrueFams[0]) + len(TrueFams[0]))



Solve(1)
Solve(2)
Solve(3)