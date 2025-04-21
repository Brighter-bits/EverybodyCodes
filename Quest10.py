Parts = ["everybody_codes_e2024_q10_p1.txt", "everybody_codes_e2024_q10_p2.txt", "everybody_codes_e2024_q10_p3.txt"]
def WordMaker(grid, where=None):
    global inp
    rows = list(map(lambda x: str(x.replace(".", "")), grid[2:6]))
    CMaker = lambda x, b: ''.join(x[a][b] for a in range(0, len(x))).replace(".", "")
    columns:str = []
    for i in range(2, 6):
        columns.append(CMaker(grid, i))
    word = ""
    rowsl = list(rows)
    columnsl = list(columns)
    for row in range(len(rows)):
        for column in range(len(columns)):
            count=0
            for letter in rows[row]:
                if letter in columns[column]:
                    word += letter
                    rowsl[row] = rowsl[row].replace(letter, "", 1)
                    columnsl[column] = columnsl[column].replace(letter, "", 1)
                    break
                count += 1
                if count == 4:
                    word += "?"
    if "?" in word:
        valid = True
        for i in rowsl:
            if len(i) > 1:
                valid = False # If we have two or more letters in a row, we won't which letter to put first, so we skip
        for i in columnsl:
            if len(i) > 1:
                valid = False    
        if valid:    
            for i in range(word.count("?")): # If the variable ends in "l" it contains the letters that need to be substituted
                index = word.index("?")
                row = index // 4 if index // 4 != 4 else 3
                column = index % 4
                if "?" in rows[row] and "?" in columns[column]:
                    print("Oh no")
                    exit()
                elif "?" in rows[row]:
                    rows[row] = rows[row].replace("?", columnsl[column])
                    word = word.replace("?", columnsl[column], 1)
                elif "?" in columns[column]:
                    columns[column] = columns[column].replace("?", rowsl[row])
                    word = word.replace("?", rowsl[row], 1)
            # print(word)
            rowsn = [] # These rows just turn the row into a format compatible with inp
            columnsn = []
            if "?" not in word: # If we've completed a word
                for row in rows:
                    rowsn.append((row[:2],row[2:4]))
                columns = "".join(columns)
                for i in range(4):
                    columnsn.append(''.join(columns[i:16:4]))
                inp[0+(6*(where//20))][where%20] = columnsn[0]
                inp[1+(6*(where//20))][where%20] = columnsn[1]
                inp[6+(6*(where//20))][where%20] = columnsn[2]
                inp[7+(6*(where//20))][where%20] = columnsn[3]
                for j in range(4):
                    for a in range(2):
                        inp[j+2+(6*(where//20))][(where%20)+a] = rowsn[j][a]
            


    return word

WTI = dict()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    WTI[letters[i]] = i+1

def WordBreaker(word):
    total = 0
    for i in range(len(word)):
        total += (i+1) * WTI[word[i]]
    return total


def P1n2():
    with open(Parts[0], "r") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        print(WordMaker(inp))
    with open(Parts[1], "r") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        inp = list(map(lambda x: x.split(" "), inp))
        inp = [a for a in inp if a != [""]]
        grids = []
        for a in range(7):
            for i in range(15):
                Cgrid = []
                for j in range(a*8, (a+1)*8):
                    Cgrid.append(inp[j][i])
                grids.append(Cgrid)
        words = list(map(WordMaker, grids))
        nums = list(map(WordBreaker, words))
        print(sum(nums))

def P3():
    global inp # What in the world does this all do?
    with open(Parts[2], "r") as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines())) # Split them up into lines
        inp = list(map(lambda x: x.split("*") if "*" in x else x.split("."), inp)) # This splits them up into more pieces,  
        for j in range(len(inp)):
            inp[j] = [a for a in inp[j] if a != ""] # Gets rid of any empty spaces created due to there being four dots inbetween each piece
        words = []
        for p in range(1000): #This is probably enough times
            words = [] # Just keep resetting it until the last one, inefficient? Yes
            for i in range(200): # Recreate a grid then put it into the wordMaker
                gride = ["**"+inp[0+(6*(i//20))][i%20]+"**"] + ["**"+inp[1+(6*(i//20))][i%20]+"**"]
                for j in range(4):
                    gride.append('....'.join(inp[j+2+(6*(i//20))][i%20:(i%20)+2]))
                gride.append("**"+inp[6+(6*(i//20))][i%20]+"**")
                gride.append("**"+inp[7+(6*(i//20))][i%20]+"**")
                words.append(WordMaker(gride, i))
        nums = list(map(lambda x: WordBreaker(x) if "?" not in x else 0, words))
        print(sum(nums))

# P1n2()
P3()

#['**Q?T?**', '**FWRS**', 'BX....RV', 'WL....TD', 'MQ....CH', 'GN....FS', '**BX?H**', '**?GML**']
# BXRVDWTLQCMHFGNS

#['**PXML**', '**QCSG**', 'RV....G?', 'TD....?X', 'CH....?M', 'FS....QN', '**HNVF**', '**DRTB**']
# ?RVGDXT?HCM?QNSF

# ['**VRBN**', '**CFWG**', 'GP....JR', 'LX....FV', 'BM....TC', 'QN....WS', '**PSMX**', '**TQJL**']
# PRJGVF?LT?B??QWN