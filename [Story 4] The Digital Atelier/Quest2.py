import os
from pathlib import Path
import sys
sys.setrecursionlimit(1000000)
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e4_q02_p1.txt", "everybody_codes_e4_q02_p2.txt", "everybody_codes_e4_q02_p3.txt"]

class Coord():
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def __hash__(self):
        return hash((self.X, self.Y))
    def __eq__(self, value):
        if not isinstance(value, Coord):
            return NotImplemented
        return self.X == value.X and self.Y == value.Y

def FindHalfway(C1: Coord, C2: Coord):
    return Coord(int((C1.X + C2.X)/2), int((C1.Y + C2.Y)/2))

def AddFireflies(places: set[Coord]):
    fireflyPlaces = set()
    for place in places:
        fireflyPlaces.add(Coord(place.X + 1, place.Y))
        fireflyPlaces.add(Coord(place.X - 1, place.Y))
        fireflyPlaces.add(Coord(place.X, place.Y + 1))
        fireflyPlaces.add(Coord(place.X, place.Y - 1))
    return fireflyPlaces


def FireFill(Bug):
    global P3Places, Beacons
    if Bug in P3Places:
        return
    P3Places.add(Bug)
    for beacon in Beacons.values():
        FireFill(FindHalfway(Bug, beacon))



def Solve(part):
    global P3Places, Beacons
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split("="), f.readlines()))
        Beacons = {}
        Bug = Coord(*list(map(int, inp[0][1].strip("[]").split(","))))
        for beacon in inp[1:-1] if part != 3 else inp[1:]:
            Beacons[beacon[0]] = Coord(*list(map(int, beacon[1].strip("[]").split(","))))
        Places = set([Bug])
        if part != 3:
            Instructions = inp[-1][1]
            for beacon in Instructions:
                Bug = FindHalfway(Bug, Beacons[beacon])
                Places.add(Bug)
        if part == 1:
            print(len(Places))
        elif part == 2:
            fireflyPlaces = AddFireflies(Places)
            print(len(fireflyPlaces - Places))
        elif part == 3:
            P3Places = set()
            FireFill(Bug)
            FinalSky = AddFireflies(P3Places)
            print(len(FinalSky - P3Places))

for i in range(1, 4):
    Solve(i)