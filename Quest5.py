Parts = ["everybody_codes_e2024_q05_p1.txt", "everybody_codes_e2024_q05_p2.txt", "everybody_codes_e2024_q05_p3.txt"]

def Dance(lines, round):
    Target = lines[round%4][0]
    del(lines[round%4][0])
    TargetStore = Target
    for j in range(1, 5):
        if Target <= len(lines[(round+j)%4]):
            if j % 2 == 0:
                lines[(round+j)%4].insert(len(lines[(round+j)%4])-Target+1, TargetStore)
            else:
                lines[(round+j)%4].insert(Target-1, TargetStore)
            break
        else:
            Target -= len(lines[(round+j)%4])
    return lines

def Shout(lines):
    shout = ""
    for line in lines:
        # print(line[0], end="")
        shout += str(line[0])
    return shout

def P1():
    with open(Parts[0], "r") as f:
        lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(" "))), f.readlines()))
        lines = [list(tup) for tup in zip(*lines)]
        for i in range(10):
            lines = Dance(lines, i)
        print(lines)
        Shout(lines)

def P2():
    with open(Parts[1], "r") as f:
        lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(" "))), f.readlines()))
        lines = [list(tup) for tup in zip(*lines)]
        from collections import Counter
        ShoutCounter = Counter()
        ShoutCounter["null"] = 1
        round = 1
        while ShoutCounter.most_common(1)[0][1] != 2024:
            lines = Dance(lines, round)
            ShoutCounter[Shout(lines)] += 1
            round += 1
            if round % 50000 == 0:
                breakpoint() 
        print(int(Shout(lines)) * round)

        

P2()
        