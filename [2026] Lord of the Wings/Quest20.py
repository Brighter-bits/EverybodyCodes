import os
from pathlib import Path
from itertools import product
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q20_p1.txt", "everybody_codes_e2026_q20_p2.txt", "everybody_codes_e2026_q20_p3.txt"]

SymToSeg = {"1": 2, "2": 5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, "0":6, "+":2, "-":1, "=":2, "A":6, " ": 0} # Converts symbols to the number of sticks
Rem = {"1": [], "2": [], "3":[], "4":[], "5":[], "6":["5"], "7":["1"], "8":["9", "6", "A", "0"], "9":["3", "5"], "0":[], "+":["-"], "-":[], "=":[], "A":[], " ": []} # Converts everything to all the possible variations without a stick
RemAndAdd = {"1": [], "2": ["3", "5"], "3":["2", "5"], "4":[], "5":["2", "3"], "6":["0", "9", "A"], "7":[], "8":[], "9":["0", "6", "A"], "0":["9", "6", "A"], "+":[], "-":[], "=":[], "A":["0", "9", "6"], " ": []} # Converts everything to all the possible variations if you take a stick and put it back into the same number
Add = {"1": ["7"], "2": [], "3":["9"], "4":[], "5":["6", "9"], "6":["8"], "7":[], "8":[], "9":["8"], "0":["8"], "+":[], "-":["+"], "=":[], "A":["8"], " ": []} # Converts everything to all the possible variation if it had an extra stick


def dectoel(num): # Converts the numbers from decimal to Base 11.
    digits = "0123456789A"
    result = []
    while num > 0:
        num, remainder = divmod(num, 11) # Forgot this function existed, typed div by accident and went oh, this thing.
        result.append(digits[remainder])
    return "".join(result[::-1])

def CheckEquation11(equ): # This just checks whether the equation works. 
    exp1, exp2 = equ.split("=") # Split the equation into two expression
    exp1 = exp1.split(" ") # Convert into individual terms of the expression
    exp2 = exp2.split(" ")[1:]
    sum1 = int(exp1[0], 11) + int(exp1[2], 11) if exp1[1] == "+" else int(exp1[0], 11) - int(exp1[2], 11) # Then add or subtract in base 11
    sum2 = int(exp2[0], 11) + int(exp2[2], 11) if exp2[1] == "+" else int(exp2[0], 11) - int(exp2[2], 11)
    return sum1 == sum2 # Return True if they are equal

def CheckEquation10(equ): # The above function but in base 10. I wasn't going to make it a function, but then it looked ugly by itself on part 1
    equ = equ.replace(" ", "")
    exp1, exp2 = equ.split("=")
    sum1 = int(exp1[0]) + int(exp1[2]) if exp1[1] == "+" else int(exp1[0]) - int(exp1[2]) 
    sum2 = int(exp2[0]) + int(exp2[2]) if exp2[1] == "+" else int(exp2[0]) - int(exp2[2]) 
    return sum1 == sum2

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        total = 0
        if part == 1:
            for equ in inp: 
                if CheckEquation10(equ):
                    for char in equ:
                        total += SymToSeg[char]
            print(total)

        elif part == 2:
            for equ in inp:
                if CheckEquation11(equ):
                    for char in equ:
                        total += SymToSeg[char]
                
            print(dectoel(total))

        elif part == 3:
            for equ in inp: 
                checking = True
                if CheckEquation11(equ): # First we just check if it works without any manipulation
                    for char in equ:
                        total += SymToSeg[char]
                    continue

                originalEqu = equ

                for i in range(len(originalEqu)): # We now try and change every item in place. Assuming that we take the stick and place it back into the same term of the equation
                    for substitute in RemAndAdd[equ[i]]:
                        equ = list(equ)
                        equ[i] = substitute # Put in our substitute
                        equ = "".join(equ)
                        if CheckEquation11(equ):
                            for char in equ:
                                total += SymToSeg[char]
                            checking = False
                            break
                        equ = originalEqu
                    if not checking:
                        break
                    
                if not checking:
                    continue

                for i, j in product(range(len(originalEqu)), range(len(originalEqu))): # We now try to 'cross-pollinate' (that is not the right word), our terms, taking a stick from one and adding a stick to another.
                    if i == j: # We have already checked giving and taking to the same element
                        continue
                    for sub1, sub2 in product(Rem[equ[i]], Add[equ[j]]): # We now check every possible combination of taking and adding
                        equ = list(equ)
                        equ[i] = sub1
                        equ[j] = sub2
                        equ = "".join(equ)
                        if CheckEquation11(equ):
                            for char in equ:
                                total += SymToSeg[char]
                            checking = False
                            break
                        equ = originalEqu
                    if not checking:
                        break
                        
            print(dectoel(total))

for i in range(1, 4):
    Solve(i)