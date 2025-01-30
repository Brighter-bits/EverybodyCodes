import regex as re
def P1():
    with open("input2A.txt", "r") as f:
        Runes = f.readline().lstrip("WORDS:").rstrip("\n").split(",")
        for i in range(len(Runes)):
            if "." in Runes[i]:
                Runes[i] = Runes[i].replace(".", "\\.")
        f.readline()
        Helmet = f.readline()
        total = 0
        for rune in Runes:
            Power = re.findall(f'{rune}', Helmet)
            total += len(Power)
        print(total)



def P2():
    with open("input2B.txt", "r") as f:
        Runes = f.readline().replace("WORDS:", "").rstrip("\n").split(",")
        for i in range(len(Runes)):
            Runes.append(Runes[i][::-1])
        f.readline()
        print(Runes)
        Shield = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        UpAndDown = list(Shield)
        for i in range(len(UpAndDown)):
            UpAndDown[i] = re.sub(r"[\w\W]", ".", UpAndDown[i])
        # print(UpAndDown)
        for i in range(len(Shield)):
            # breakpoint()
            Ranges = []
            for Rune in Runes:
                for Match in re.finditer(f'{Rune}', Shield[i], overlapped=True):
                    Ranges.append([Match.start(0), Match.end(0)])
            for Range in Ranges:
                for j in range(Range[0], Range[1]):
                    UpAndDown[i] = UpAndDown[i][:j] + '#' + UpAndDown[i][j+1:]
            # breakpoint()
        # print(UpAndDown)
        total = 0
        for line in UpAndDown:
            total += line.count("#")
            print(len(line))
        print(total)
                    
def Follow(Rune, x, y, Direction, Scale):
    global Activated
    valid = True
    match Direction:
        case "U":
            for i in range(0, len(Rune)):
                if Scale[y-i][x] != Rune[i]:
                    valid = False
        
        case "D":
            for i in range(0, len(Rune)):
                if Scale[y+i][x] != Rune[i]:
                    valid = False
        
        case "R":
            for i in range(0, len(Rune)):
                if Scale[y][(x+i)%len(Scale[0])] != Rune[i]:
                    valid = False

        case "L":
            for i in range(0, len(Rune)):
                if Scale[y][x-i] != Rune[i]:
                    valid = False
    if valid:
        match Direction:
            case "U":
                for i in range(len(Rune)):
                    Activated[(y-i , x)] = 1
            
            case "D":
                for i in range(len(Rune)):
                    Activated[(y+i , x)] = 1
            
            case "R":
                for i in range(len(Rune)):
                    Activated[(y , ((x+i)%len(Scale[0])))] = 1

            case "L":
                for i in range(len(Rune)):
                    if x-i >= 0:
                        Activated[(y , x-i)] = 1
                    else:
                        Activated[(y , len(Scale[0]) + (x-i))] = 1



def RoundCheck(Rune, x, y, Scale):
    if y >= len(Rune) - 1 and Scale[y-1][x] == Rune[1]:
        Follow(Rune, x, y, "U", Scale)
    if (len(Scale)-y) >= len(Rune) and Scale[y+1][x] == Rune[1]:
        Follow(Rune, x, y, "D", Scale)
    if Scale[y][(x+1)%len(Scale[0])] == Rune[1]:
        Follow(Rune, x, y, "R", Scale)
    if Scale[y][x-1] == Rune[1]:
        Follow(Rune, x, y, "L", Scale)

def P3():
    with open("input2C.txt", "r") as f:
        global Activated
        Runes = f.readline().replace("WORDS:", "").rstrip("\n").split(",")
        f.readline()
        Scale = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        Activated = dict()
        for rune in Runes:
            for y in range(len(Scale)):
                for x in range(len(Scale[y])):
                    if Scale[y][x] == rune[0]:
                        if len(rune) == 1:
                            Activated[(y , x)] = 1
                        else:
                            RoundCheck(rune, x, y, Scale)
        print(len(Activated.keys()))



P3()