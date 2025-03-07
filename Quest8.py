Parts = ["everybody_codes_e2024_q08_p1.txt", "everybody_codes_e2024_q08_p2.txt", "everybody_codes_e2024_q08_p3.txt"]

# Formula is 1 + 3 + 5 + 7 = 2n-1

def LyrFinder(Blocks):
    Layers = 0
    BlocksLeft = Blocks
    while BlocksLeft > 0 :
        BlocksLeft -= ((2*(Layers+1)) - 1)
        Layers += 1
    return Layers

LyrDiff = lambda Blocks, Layers: 0.5*Layers*(2 + 2*(Layers-1)) - Blocks # 0.5n(2a + (n-1)d)

def P1():
    with open(Parts[0], "r") as f:
        blocks = int(f.readline())    
        layer = LyrFinder(blocks)
        diff = int(LyrDiff(blocks, layer))
        print(diff*(2*layer-1))

def layermult(thickness):
    total = 0
    for layer in thickness[:-2]:
        total += thickness[-1]*2
                
    return total

def P2():
    with open(Parts[1], "r") as f:
        priests = int(f.readline())
        acolytes = 1111
        blocks = 20240000 - 1
        thickness = [1]
        while blocks > 0:
            thickness.append((thickness[-1] * priests) % acolytes)
            blocks -= ((thickness[-1])*3) + layermult(thickness)
        print(len(thickness))
        print(-blocks*(1+(2*(len(thickness)-1))))

def P3():
    with open(Parts[2], "r") as f:
        priests = int(f.readline())
        acolytes = 10
        blocks = 202400000 - 1
        thickness = [1]
        while blocks > 0:
            thickness.append(((thickness[-1] * priests) % acolytes) + acolytes)
            blocks -= ((thickness[-1])*3) + layermult(thickness)
        print(thickness)
        for height in thickness:
            

P3()
