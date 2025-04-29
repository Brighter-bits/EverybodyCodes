Parts = ["everybody_codes_e2024_q11_p1.txt", "everybody_codes_e2024_q11_p2.txt", "everybody_codes_e2024_q11_p3.txt"]
from collections import Counter

def GoTerm(termdefs, Letter, days):
    terms = Counter([Letter])
    cache = Counter()
    for i in range(days):
        termtypes = list(terms.keys())
        for termtype in termtypes:
            result = termdefs[termtype]
            for part in result:
                cache[part] += terms[termtype]
        terms = cache
        cache = Counter()
    return terms.total()

def Line2Termdefs(lines):
    termdefs = dict()
    for line in lines:
        pieces = line.split(":")
        listy = pieces[1].split(",")
        termdefs[pieces[0]] = listy
    return termdefs

def Solve(part):
    if part != 3:
        with open(Parts[part-1], "r") as f:
            letter = "A" if part == 1 else "Z"
            day = 4 if part == 1 else 10
            lines = list(map(lambda x: x.replace("\n", ""), f.readlines()))
            print(GoTerm(Line2Termdefs(lines), letter, day))
    else:
        with open(Parts[2], "r") as f:
            lines = list(map(lambda x: x.replace("\n", ""), f.readlines()))
            total = []
            Termdefs = Line2Termdefs(lines)
            for Termdef in list(Termdefs.keys()):
                try:
                    total.append(GoTerm(Termdefs, Termdef, 20))
                except:
                    pass
            print(max(total)-min(total))

for i in range(1, 4):
    Solve(i)