# Ooh, Quests
import math
with open("input1.txt", "r") as f:
    Monsters = f.readline()
    ants = Monsters.count("A")
    beetles = Monsters.count("B")
    roach = Monsters.count("C")
    print((beetles*1)+(roach*3))

with open("input1B.txt", "r") as f:
    Monsters = f.readline()
    MonsterList = []
    for i in range(0, math.floor(len(Monsters)), 2):
        MonsterList.append(Monsters[i:i+2])
    if len(MonsterList[-1]) == 1:
        MonsterList[-1] += "x"
    MonsterList = list(map(lambda x: list(x), MonsterList))
    total = 0
    for i in MonsterList:
        if "x" not in i:
            total += 2
        for j in range(len(i)):
            match i[j]:
                case "B":
                    total += 1
                case "C":
                    total += 3
                case "D":
                    total += 5
    print(total)

with open("input1C.txt", "r") as f:
    Monsters = f.readline()
    MonsterList = []
    for i in range(0, math.floor(len(Monsters)), 3):
        MonsterList.append(Monsters[i:i+3])
    if len(MonsterList[-1]) == 1:
        MonsterList[-1] += "x"
    elif len(MonsterList[-1]) == 2:
        MonsterList[-1] += "xx"
    MonsterList = list(map(lambda x: list(x), MonsterList))
    total = 0
    for i in MonsterList:
        if "x" not in i:
            total += 6
        if i.count("x") == 1:
            total += 2
        for j in range(len(i)):
            match i[j]:
                case "B":
                    total += 1
                case "C":
                    total += 3
                case "D":
                    total += 5
    print(total)
    