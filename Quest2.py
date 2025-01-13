import regex as re
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




with open("input2B.txt", "r") as f:
    Runes = f.readline().lstrip("WORDS:").rstrip("\n").split(",")
    for i in range(len(Runes)):
        if "." in Runes[i]:
            Runes[i] = Runes[i].replace(".", "\\.")
        Runes.append(Runes[i][::-1])
    f.readline()
    Shield = list(map(lambda x: x.replace("\n", ""), f.readlines()))
    for rune in Runes:
        for line in range(len(Shield)):
            Shield[line] = re.sub(f'{rune}', f"{rune[:-1]}#{rune[-1]}", Shield[line])
    line = ''.join(Shield)
    print(len(re.findall(r'#', line)))



with open("input2C.txt", "r") as f:
    pass