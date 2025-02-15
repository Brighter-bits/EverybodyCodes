Parts = ["everybody_codes_e2024_q05_p1.txt", "everybody_codes_e2024_q05_p2.txt", "everybody_codes_e2024_q05_p3.txt"]

def Dance(lines, round):
    Target = lines[round%4][0]
    del(lines[round%4][0])
    Turns = Target//len(lines[(round+1)%4])
    Place = Target%(len(lines[(round+1)%4]))
    if Turns % 2 == 0:
        if Place == 0:
            lines[(round+1)%4].insert(1, Target)
        else:
            lines[(round+1)%4].insert(Place-1, Target)
    else:
        if Place == 0:
            lines[(round+1)%4].insert(len(lines[(round+1)%4])-1, Target)
        else:
            lines[(round+1)%4].insert(len(lines[(round+1)%4])-Place+1, Target)
    return lines

def Shout(lines):
    shout = ""
    for line in lines:
        # print(line[0], end="")
        try:
            shout += str(line[0])
        except:
            breakpoint()
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
        round = 0
        while ShoutCounter.most_common(1)[0][1] != 2024:
            lines = Dance(lines, round)
            ShoutCounter[Shout(lines)] += 1
            round += 1
            if round % 50000 == 0:
                ShoutCounter = Counter({k: c for k, c in ShoutCounter.items() if c >= (7*(round//50000))})
                # breakpoint()
        print(int(Shout(lines)) * round)

        
def P3():
    with open(Parts[2], "r") as f:
        lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(" "))), f.readlines()))
        lines = [list(tup) for tup in zip(*lines)]
        round = 0
        from collections import Counter
        ShoutCounter = Counter()
        ShoutCounter["null"] = 1
        round = 0
        while ShoutCounter.most_common(1)[0][1] != 3035:
            lines = Dance(lines, round)
            ShoutCounter[Shout(lines)] += 1
            round += 1
        numbers = list(ShoutCounter.keys())
        numbers[0] = -5
        print(max(list(map(int, numbers))))
        
P3()