def SlopeCheck(Y, X, num, diag = False):
    global Grid
    global NewGrid
    global swapped
    if num <= 9:
        digit = str(num)
    else:
        match num:
            case 10:
                digit = "A"
            case 11:
                digit = "B"
            case 12:
                digit = "C"
            case 13:
                digit = "D"
            case 14:
                digit = "E"
            case 15:
                digit = "F"
    
    work = False
    if diag == False and Y > 1 and Y < len(Grid)-1 and X > 1 and X < len(Grid[0]) - 1 and Grid[Y][X-1] == digit and Grid[Y][X+1] == digit and Grid[Y-1][X] == digit and Grid[Y+1][X] == digit:
        work = True
    elif diag == True and Y > 1 and Y < len(Grid)-1 and X > 1 and X < len(Grid[0]) - 1 and Grid[Y][X-1] == digit and Grid[Y][X+1] == digit and Grid[Y-1][X] == digit and Grid[Y+1][X] == digit and Grid[Y+1][X+1] == digit and Grid[Y+1][X-1] == digit and Grid[Y-1][X-1] == digit and Grid[Y-1][X+1] == digit:
        work = True
    if work:
        if num <= 8:
            NewGrid[Y] = NewGrid[Y][:X] + str(num+1) + NewGrid[Y][X+1:]
        else:
            match digit:
                case "9":
                    NewGrid[Y] = NewGrid[Y][:X] + "A" + NewGrid[Y][X+1:]
                case "A":
                    NewGrid[Y] = NewGrid[Y][:X] + "B" + NewGrid[Y][X+1:]
                case "B":
                    NewGrid[Y] = NewGrid[Y][:X] + "C" + NewGrid[Y][X+1:]
                case "C":
                    NewGrid[Y] = NewGrid[Y][:X] + "D" + NewGrid[Y][X+1:]
                case "D":
                    NewGrid[Y] = NewGrid[Y][:X] + "E" + NewGrid[Y][X+1:]
                case "E":
                    NewGrid[Y] = NewGrid[Y][:X] + "F" + NewGrid[Y][X+1:]
        swapped = True               

Parts = ["everybody_codes_e2024_q03_p1.txt", "everybody_codes_e2024_q03_p2.txt", "everybody_codes_e2024_q03_p3.txt"]

def Solve(Part):
    global Grid
    global swapped
    global NewGrid
    if Part == 3:
        Diag = True
    else:
        Diag = False
    with open(Parts[Part-1], "r") as f:
        Grid = list(map(lambda x: x.replace("\n", "").replace("#", "1"), f.readlines()))
        Grid.insert(0, ("." * len(Grid[0])))
        Grid.insert(0, ("." * len(Grid[0])))
        Grid = list(map(lambda x: "." + x, Grid))
        Grid = list(map(lambda x: x + ".", Grid))
        swapped = False
        Hole = 2
        NewGrid = list(Grid)
        while True:
            for Y in range(len(Grid)):
                for X in range(len(Grid[0])):
                    if Grid[Y][X] == str(Hole-1):
                        SlopeCheck(Y, X, Hole-1, Diag)
            Grid = list(NewGrid)
            if swapped == False:
                break
            Hole += 1
            swapped = False
        total = 0
        for Y in range(len(Grid)):
            for X in range(len(Grid[0])):
                if Grid[Y][X] != ".":
                    if Grid[Y][X].isdigit():
                        total += int(Grid[Y][X])
                    else:
                        match Grid[Y][X]:
                            case "A":
                                total += 10
                            case "B":
                                total += 11
                            case "C":
                                total += 12
                            case "D":
                                total += 13
                            case "E":
                                total += 14
                            case "F":
                                total += 15
        print("\n\n\n")
        for i in Grid:
            print(i)
        print(total)

Solve(1)
Solve(2)
Solve(3)