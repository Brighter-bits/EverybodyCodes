import os
from pathlib import Path
from collections import defaultdict
import sys

sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2026_q06_p1.txt", "everybody_codes_e2026_q06_p2.txt", "everybody_codes_e2026_q06_p3.txt"]



def Check(ingredient):
    global ingredientDict, visited
    if ingredient in visited:
        return
    visited.add(ingredient)
    
    newingredients = ingredientDict[ingredient]

    for ing in newingredients:
        Check(ing)


def CheckForNULL(ingredient):
    global ingredientDict, visited
    if ingredient in visited:
        return False

    visited.add(ingredient)

    if ingredient not in ingredientDict:
        return False

    newingredients = ingredientDict[ingredient]
    contaminated = False

    if "NULL" in newingredients:
        return True

    for ing in newingredients:
        contaminated = CheckForNULL(ing)
        if contaminated:
            break
    return contaminated


def CheckForNULLv(ingredient):
    global ingredientDict, visited
    if ingredient in visited:
        return 0b000

    visited.add(ingredient)

    if ingredient not in ingredientDict:
        return 0b000

    newingredients = ingredientDict[ingredient]

    contamination = 0b000

    if "NULLv1" in newingredients:
        contamination |= 0b100
    if "NULLv2" in newingredients:
        contamination |= 0b010
    if "NULLv3" in newingredients:
        contamination |= 0b001

    for ing in newingredients:
        contamination |= CheckForNULLv(ing)
    return contamination

def Solve(part):
    global ingredientDict, visited
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        ingredientDict = defaultdict(list)
        for line in inp:
            line = line.split(":")
            line[1] = line[1].split(",")
            ingredientDict[line[0]] = line[1]
        total = 0
        if part == 1:
            visited = set()
            Check("NULL")
            print(len(visited) - 1)
        elif part == 2:
            for product, _ in ingredientDict.items():
                if product == "NULL":
                    continue
                visited = set()
                Contaminated = CheckForNULL(product)
                if Contaminated:
                    total += 1

            print(total)
        elif part == 3:
            for product, _ in ingredientDict.items():
                if "NULL" in product:
                    continue
                visited = set()
                Contamination = CheckForNULLv(product)
                if Contamination == 3 or Contamination > 4:
                    total += 1

            print(total)
        


for i in range(1, 4):
    Solve(i)