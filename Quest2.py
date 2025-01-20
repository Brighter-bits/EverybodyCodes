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
                    



with open("input2C.txt", "r") as f:
    pass

P2()