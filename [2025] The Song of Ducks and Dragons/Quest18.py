import os
from pathlib import Path
import sys
sys.setrecursionlimit(100000000)
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2025_q18_p1.txt", "everybody_codes_e2025_q18_p2.txt", "everybody_codes_e2025_q18_p3.txt"]
from itertools import permutations
from functools import cache

class Plant():
    def __init__(self, id, thickness):
        self.thickness = thickness
        self.id = id
        self.Connections = dict()
    def AddConnection(self, Destination, Thickness):
        self.Connections[Destination] = Thickness
    # Cache makes it so that even if the Node is queried again, it doesn't use up the iterable.
    @cache
    def CheckEnergy(self):
        global PlantDict, OnOff
        Energy = 0
        for Node, Thickness in self.Connections.items():
            if Node == -1:
                if OnOff[self.id-1] == 1:
                    Energy += 1
            else:
                Energy += Thickness * PlantDict[Node].CheckEnergy()
        return Energy if Energy >= self.thickness else 0

    @cache
    def Investigate(self):
        global PlantDict, OnOff
        Energy = 0
        for Node, Thickness in self.Connections.items():
            if Node == -1:
                if OnOff[self.id-1] == 1:
                    Energy += 1
            else:
                Energy += Thickness * PlantDict[Node].Investigate()
        return Energy

PlantDict: dict[int, Plant] = dict()
OnOff = []

def Solve(part):
    Plant.CheckEnergy.cache_clear()
    with open(Parts[part-1]) as f:
        global OnOff
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        Currentnode = -1
        CPlant = -1
        splitter = -1
        if part == 2 or part == 3:
            for i in range(len(inp)):
                if inp[i] == inp[i+1] and inp[i] == "":
                    splitter = i
                    break
            OnOffSequences = inp[splitter+2:]
            inp = inp[:splitter]
            OnOffSequences = list(map(lambda x: x.split(" "), OnOffSequences))
            for i in range(len(OnOffSequences)):
                OnOffSequences[i] = list(map(int, OnOffSequences[i]))

        for line in inp:
            if line == "":
                continue
            Thickness = -1
            Contents = line.split(" ")
            Thickness = int(Contents[-1].replace(":", ""))
            if line[0] == "P":
                CPlant = int(Contents[1])
                PlantDict[CPlant] = Plant(CPlant, Thickness)
            else:
                if Contents[1] == "free":
                    PlantDict[CPlant].AddConnection(-1, Thickness)
                else:
                    destination = int(Contents[4])
                    PlantDict[CPlant].AddConnection(destination, Thickness)
        if part == 1:
            OnOff = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            print(PlantDict[CPlant].CheckEnergy())
        elif part == 2 or part == 3:
            totals = []
            for sequence in OnOffSequences:
                Plant.CheckEnergy.cache_clear()
                OnOff = list(sequence)
                totals.append(PlantDict[CPlant].CheckEnergy())
            if part == 2:
                print(sum(totals))
            else:
                totals = [num for num in totals if num != 0]
                Contributions = []
                for i in range(len(OnOffSequences[0])):
                    Plant.Investigate.cache_clear()
                    OnOff = [0 for a in range(len(OnOffSequences[0]))]
                    OnOff[i] = 1
                    Contributions.append(PlantDict[CPlant].Investigate())
                for i in range(len(Contributions)):
                    Contributions[i] = 0 if Contributions[i] <= 0 else 1
                Plant.CheckEnergy.cache_clear()
                OnOff = list(Contributions)
                Perfect = PlantDict[CPlant].CheckEnergy()
                print(sum(list(map(lambda x: Perfect - x, totals))))



                



        





Solve(1)
Solve(2)
Solve(3)