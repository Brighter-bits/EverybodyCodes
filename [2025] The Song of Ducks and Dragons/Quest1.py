Parts = ["everybody_codes_e2025_q01_p1.txt", "everybody_codes_e2025_q01_p2.txt", "everybody_codes_e2025_q01_p3.txt"]
def StringToDir(str):
    if str[0] == "L":
        return -1 * int(str[1:])
    else:
        return int(str[1:])

def Solve(part):
    with open(Parts[part-1], "r") as f:
        names = f.readline().split(",")
        f.readline()
        instructs = f.readline().split(",")
        instructs = list(map(StringToDir, instructs))
        pointer = 0
        if part == 1:
            for num in instructs:
                pointer += num
                if pointer < 0:
                    pointer = 0
                if pointer > len(names)-1:
                    pointer = len(names)-1
            print(names[pointer])
        elif part == 2:
            for num in instructs:
                pointer += num
                if pointer < 0 or pointer > len(names)-1:
                    pointer %= len(names)
            print(names[pointer])
        elif part == 3:
            for num in instructs:
                pointer = num % len(names)
                names[0], names[pointer] = names[pointer], names[0]
            print(names[0])

for i in range(1,4):
    Solve(i)