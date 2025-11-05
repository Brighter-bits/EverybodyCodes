import regex as re
Parts = ["everybody_codes_e2025_q02_p1.txt", "everybody_codes_e2025_q02_p2.txt", "everybody_codes_e2025_q02_p3.txt"]

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])
def div(x, y):
    return (int(x[0]/y[0]),int(x[1]/y[1]))
def mul(x, y):
    return ((x[0] * y[0])-(x[1]*y[1]), (x[0] * y[1])+(x[1]*y[0]))
def checkMax(x):
    return True if abs(x[0]) > 1000000 or abs(x[1]) > 1000000 else False

def Cycle1(R, A):
    R = mul(R, R)
    R = div(R, [10, 10])
    return add(A, R)

def Cycle2(R, A):
    R = mul(R, R)
    R = div(R, [100000,100000])
    return add(A, R)

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = "".join(re.findall(r"[\-0-9\,]", f.readline()))
        inp = list(map(int, inp.split(",")))
        answer = [0, 0]
        if part == 1:
            for i in range(3):
                answer = Cycle1(answer, inp)
            print(f"[{answer[0]},{answer[1]}]")
        else:
            maximum = add(inp, [1000, 1000])
            # print(maximum, inp)
            spacing = (int((maximum[0]-inp[0])/(1000 if part == 3 else 100)), int((maximum[1]-inp[1])/(1000 if part == 3 else 100)))
            coords = []
            for i in range(1001 if part == 3 else 101):
                for j in range(1001 if part == 3 else 101):
                    check = [0, 0]
                    for a in range(100):
                        check = Cycle2(check, (inp[0]+(i*spacing[0]), inp[1]+(j*spacing[1])))
                        if checkMax(check):
                            break
                        if a == 99:
                            coords.append((i, j))
            print(len(coords))

for i in range(1, 4):
    Solve(i)