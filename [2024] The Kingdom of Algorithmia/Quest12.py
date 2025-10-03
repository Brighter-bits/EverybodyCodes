Parts = ["everybody_codes_e2024_q12_p1.txt", "everybody_codes_e2024_q12_p2.txt", "everybody_codes_e2024_q12_p3.txt"]
import os
PtoN = lambda x: complex(2*x, -x)
def solve12(part):
    with open(Parts[part-1]) as f:
        os.system("cls")
        inp = list(map(lambda x: list(x.replace("\n", "")), f.readlines()))
        Biases = ((3, complex(1, len(inp)-4)), (2, complex(1, len(inp)-3)), (1, complex(1, len(inp)-2))) # C bias, then B bias, then A bias
        HitDict = dict()
        for Bias in Biases:
            for i in range(1, 50):
                GravPoint:complex = PtoN(i) + Bias[1]
                while GravPoint.imag <= len(inp)-1:
                    HitDict[GravPoint] = Bias[0] * i
                    GravPoint += 1+1j
        Hitters = []
        for line in range(len(inp)):
            cindex = 0
            for i in range(inp[line].count("T")):
                cindex = inp[line].index("T", cindex)
                coord = complex(cindex, line)
                Hitters.append(coord)
                cindex += 1
            cindex = 0
            if part == 2:
                for j in range(inp[line].count("H")):
                    cindex = inp[line].index("H", cindex)
                    coord = complex(cindex, line)
                    Hitters.append(coord)
                    Hitters.append(coord)
                    cindex += 1
        CataPows = list(map(lambda x: HitDict[x], Hitters))
        print(sum(CataPows))
        
def Checker(listy:list[tuple[int, int]], new:tuple[int, int]): # If we find a way to get to the same coordinate with less score at the same time, then we replace the old method with the more effiecient one

    for i, (score, time) in enumerate(listy):
        if new[1] == time:
            if new[0] < score:
                listy[i] = new
            return listy
    listy.append(new)
    return listy

def Solve3():
    with open(Parts[2]) as f:
        inp = list(map(lambda x: list(map(int, x.replace("\n", "").split(" "))), f.readlines()))
        Meteors = dict()
        starindex = 0
        for star in inp:
            coords = []
            x = star[0]
            y = star[1]
            t = 0
            while x >= 0 and y >= 0:
                coords.append((complex(x, y), t))
                x -= 1
                y -= 1 
                t += 1
            Meteors[starindex] = coords
            starindex += 1
        Biases = [(3, complex(0, 2)), (2, complex(0, 1)), (1, complex(0, 0))]
        Hitdict: dict[complex, list] = {}
        for Bias in Biases:
            for i in range(3000):
                Gravpoint = Bias[1]
                t = 0
                for a in range(2):
                    for j in range(i):
                        if Gravpoint not in Hitdict:
                            Hitdict[Gravpoint] = [(Bias[0]*i, t)]
                        else:
                            Hitdict[Gravpoint] = Checker(Hitdict[Gravpoint], (Bias[0]*i, t))
                        Gravpoint += 1+1j if a == 0 else 1
                        t += 1
                while Gravpoint.real >= 0 and Gravpoint.imag >= 0:
                    if Gravpoint not in Hitdict:
                        Hitdict[Gravpoint] = [(Bias[0]*i, t)]
                    else:
                        Hitdict[Gravpoint] = Checker(Hitdict[Gravpoint], (Bias[0]*i, t))
                    Gravpoint -= -1+1j
                    t += 1
        for key, values in Meteors.items():
            Searching = True
            for coord in values:
                if not Searching:
                    break
                try:
                    Hits = Hitdict[coord[0]]
                except:
                    continue
                for Hit in Hits:
                    if Hit[1] <= coord[1]:
                        Searching = False
                        Meteors[key] = Hit[0]
                        break
        print(Meteors)
        breakpoint()
        print("HELP")
        print(sum(list(Meteors.values())))
            






Solve3()