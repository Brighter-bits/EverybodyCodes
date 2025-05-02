Parts = ["everybody_codes_e2024_q12_p1.txt", "everybody_codes_e2024_q12_p2.txt", "everybody_codes_e2024_q12_p3.txt"]
import os
PtoN = lambda x: complex(2*x, -x)
def solve():
    with open(Parts[0]) as f:
        global inp
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
        print(HitDict)
        Hitters = []
        for line in range(len(inp)):
            cindex = 0
            for i in range(inp[line].count("T")):
                cindex = inp[line].index("T", cindex)
                coord = complex(cindex, line)
                Hitters.append(coord)
                cindex += 1
            cindex = 0
            for j in range(inp[line].count("H")):
                cindex = inp[line].index("H", cindex)
                coord = complex(cindex, line)
                Hitters.append(coord)
                Hitters.append(coord)
                cindex += 1
        CataPows = list(map(lambda x: HitDict[x], Hitters))
        print(sum(CataPows))
        
solve()