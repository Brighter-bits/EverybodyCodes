Parts = ["everybody_codes_e2025_q03_p1.txt", "everybody_codes_e2025_q03_p2.txt", "everybody_codes_e2025_q03_p3.txt"]

def Cycle(inp): # New is a set of unique numbers, while unused is a list containing all the numbers we have left over.
    new = []
    unused = []
    for i in inp:
        if i not in new:
            new.append(i)
        else:
            unused.append(i)
    return new, unused

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(int, f.readline().replace("\n","").split(",")))
        if part == 2:
            inp = sorted(inp)
        else:
            inp = sorted(inp, reverse=True)
        new, unused = Cycle(inp)
        if part == 1:
            return sum(new) # Yes I know I'm not being consistent as to whether my Solve function outputs the answer or whether it returns it
        elif part == 2:
            return sum(new[:20]) # Since the list is smallest to highest, we just need to take the first 20 items
        
        counter = 1
        while len(unused) != 0:
            _, unused = Cycle(unused)
            counter += 1
        return counter
    
for i in range(1, 4):
    print(Solve(i))
