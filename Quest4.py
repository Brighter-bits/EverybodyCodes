Parts = ["everybody_codes_e2024_q04_p1.txt", "everybody_codes_e2024_q04_p2.txt", "everybody_codes_e2024_q04_p3.txt"]

for i in range(2):
    with open(Parts[i], "r") as f:
        nails = f.readlines()
        nails = list(map(int, list(map(lambda x: x.replace("\n", ""), nails))))
        Target = min(nails)
        print(sum(list(map(lambda x: x-Target, nails))))

with open(Parts[2], "r") as f:
    nails = f.readlines()
    nails = list(map(int, list(map(lambda x: x.replace("\n", ""), nails))))
    import math
    Target = sorted(nails)[math.floor(len(nails)/2)]
    print(sum(list(map(lambda x: abs(x-Target), nails))))
    
