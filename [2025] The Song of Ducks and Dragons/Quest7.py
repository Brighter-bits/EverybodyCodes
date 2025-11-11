import os
from pathlib import Path
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2025_q07_p1.txt", "everybody_codes_e2025_q07_p2.txt", "everybody_codes_e2025_q07_p3.txt"]

def Check(dict, name):
    for j in range(len(name)-1):
        try:
            if name[j+1] not in dict[name[j]]:
                return False
        except:
            pass
    return True




def Dig(dict, Initial, currentnum):
    Min = 7 - currentnum
    Max = 11 - currentnum
    total = 0
    for i in range(Min, Max+1):
        total += DictDelve(dict, Initial, i)
    return total


def DictDelve(dict, letter, num):
    list = []
    try:
        list = dict[letter]
    except:
        pass
    total = 0
    if num == 0:
        return 1
    for i in list:
        total += DictDelve(dict, i, num-1)
    return total
    


def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        names = inp[0].split(",")
        worddict = dict()
        for rule in inp[2:]:
            letters = rule[4:].split(",")
            worddict[rule[0]] = letters
        total = 0
        namelist = []
        for i in range(len(names)):
            if Check(worddict, names[i]):
                if part == 1:
                    print(names[i])
                    return
                if part == 2:
                    total += i+1
                else:
                    namelist.append(names[i])
        if part == 3:
            namelist.sort(reverse=True)
            truenames = []

            for name in namelist:
                shortest = True
                for rest in namelist:
                    if rest != name and rest in name:
                        shortest = False
                        break
                if shortest:
                    truenames.append(name)

            for name in truenames:
                total += Dig(worddict, name[-1], len(name))
            
        
        print(total)



for i in range(1, 4):
    Solve(i)