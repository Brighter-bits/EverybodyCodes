Parts = ["everybody_codes_e2024_q07_p1.txt", "everybody_codes_e2024_q07_p2.txt", "everybody_codes_e2024_q07_p3.txt"]


def Solve():
    with open(Parts[0], "r") as f:
        lines = list(map(lambda x: x.replace("\n", ""), sorted(f.readlines())))
        for i in range(len(lines)):
            num = []
            power = 10
            # while len(lines[i]) != 21:
            #     if len(lines[i]) < 21:
            #         lines[i] += lines[i][2:]
            #     else:
            #         lines[i] = lines[i][:22]
            for j in range(2, len(lines[i]), 2):
                match lines[i][j]:
                    case "+":
                        power += 1
                    case "-":
                        power -= 1
                num.append(power)
            lines[i] = str(sum(num)) + lines[i][0]
        racedict = dict()
        for i in range(len(lines)):
            racedict[lines[i][:-1]] = lines[i][-1]
        print(racedict)
        lines = list(map(lambda x: racedict.get(str(x)), sorted(list(map(lambda x: int(x[:-1]), lines)), reverse=True)))
        print(''.join(lines))
        
def Reconstruct(orig, mask) -> str:
    outp = ""
    for i in range(len(mask)):
        match mask[i]:
            case "+":
                outp += "+"
            case "-":
                outp += "-"
            case _:
                outp += orig[i]
    return outp

def Solve2():
    with open(Parts[1], "r") as f:
        track = ""
        with open("track.txt", "r") as g:
            trackline = list(map(lambda x: x.replace("\n", ""), g.readlines()))
            track += trackline[0][1:]
            for i in range(1, len(trackline)-1):
                track += trackline[i][-1]
            track += trackline[-1][::-1]
            for i in range(len(trackline)-2, -1, -1):
                track += trackline[i][0]
        track = track * 10
        lines = list(map(lambda x: x.replace("\n", "").replace(",", ""), sorted(f.readlines())))
        for i in range(len(lines)):
            total = 0
            identity, plan = lines[i].split(":")
            while len(plan) != len(track):
                if len(plan) < len(track):
                    plan += plan
                else:
                    plan = plan[:len(track)]
            plan = Reconstruct(plan, track)
            power = 10
            for j in range(len(plan)):
                match plan[j]:
                    case "+":
                        power += 1
                    case "-":
                        if power > 0:
                            power -= 1
                total += power

            lines[i] = str(total) + identity
        racedict = dict()
        for i in range(len(lines)):
            racedict[lines[i][:-1]] = lines[i][-1]
        print(racedict)
        lines = list(map(lambda x: racedict.get(str(x)), sorted(list(map(lambda x: int(x[:-1]), lines)), reverse=True)))
        print(''.join(lines))

def MazeRunner(maze):
    direction = [-1j, 1, 1j, -1]
    Cdir = 1
    Odir = 3
    position = 0 + 0j
    sitting = ""
    output = ""
    while sitting != "S":
        NPos = position + direction[Cdir%4]
        if 0 <= NPos.imag < len(maze) and 0 <= NPos.real < len(maze[0]) and Cdir%4 != Odir%4 and maze[int(NPos.imag)][int(NPos.real)] != " ":
            position += direction[Cdir%4]
            sitting = maze[int(NPos.imag)][int(NPos.real)]
            output += sitting
            Odir = (Cdir+2)%4
        else:
            Cdir += 1
    return output

from functools import cache

@cache
def run(plan):
    total = 0
    power = 10
    for j in range(len(plan)):
        match plan[j]:
            case "+":
                power += 1
            case "-":
                if power > 0:
                    power -= 1
        total += power
    return total

def Solve3():
        with open(Parts[2], "r") as f:
            track = ""
            with open("track1.txt", "r") as g:
                track = MazeRunner(list(map(lambda x: x.replace("\n", ""), g.readlines())))
            track = track * 11 #Apparenly this works
            lines = list(map(lambda x: x.replace("\n", "").replace(",", ""), sorted(f.readlines())))
            Target = 0
            for i in range(len(lines)):
                plan = lines[i].split(":")[1]
                while len(plan) != len(track):
                    if len(plan) < len(track):
                        plan += plan
                    else:
                        plan = plan[:len(track)]
                plan = Reconstruct(plan, track)
                Target = run(plan)
            # Current = "2"*11
            # Trans = str.maketrans("012", "-=+")
            # Beat = 0
            # while int(Current, 3) != 0:
            Beat = 0
            from itertools import permutations
            possible = set(permutations("+++++---==="))
            possibilities = []
            for i in possible:
                if i not in possibilities:
                    possibilities.append(i)

            for i in possibilities:
                plan = ''.join(i)
                while len(plan) != len(track):
                    if len(plan) < len(track):
                        plan += plan
                    else:
                        plan = plan[:len(track)]
                plan = Reconstruct(plan, track)
                total = run(plan)
                if total > Target:
                    Beat += 1
                # Current = int(Current, 3) - 1
                # digits = []
                # while Current:
                #     digits.append(Current % 3)
                #     Current = Current // 3   
                # Current = "".join(list(map(str, list(reversed(digits)))))    
                # while len(Current) < 11:
                #     Current = "0" + Current


        print("\n\n\n")
        print(Beat)         



Solve3()