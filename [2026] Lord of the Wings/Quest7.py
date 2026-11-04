import os
from pathlib import Path
from copy import deepcopy
from collections import Counter # Oh look, it's my favourite class
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e2026_q07_p1.txt", "everybody_codes_e2026_q07_p2.txt", "everybody_codes_e2026_q07_p3.txt"]

CloudDict: dict[int, Cloud] = {}
DeadClouds = [] # Clouds that have exploded

class Cloud: # A class containing energy and connections
    def __init__(self, energy:int, connections:list[int]):
        self.energy = energy
        self.connections:list[int] = connections

def Follow(cloudID: int, strenght:int): # A function which does a depth first adding of energy to each cloud
    global CloudDict
    CloudDict[cloudID].energy += strenght # Add the charge to the cloud

    if strenght != 1: # If we stil have enough charge
        for connection in CloudDict[cloudID].connections:
            Follow(connection, strenght - 1) # Follow through to the next connection.


def GiveEnergy(cloudID, strenght, multiplier): # Phase 1: Add the energy to all of the clouds, and if we need to murder a cloud, then we push the explosion charge to it's connections, and then add it to murdered at the end of this Stage
    global CloudDict, DeadClouds, CloudsToBeKilled
    CloudDict[cloudID].energy += strenght * multiplier # Add the charge multiplied by the number of incoming impulses.
    cloudsToBeStaged = Counter()

    if CloudDict[cloudID].energy > 1000000: # If the energy has gotten too high
        CloudsToBeKilled.append(cloudID) # Add the cloud to be murdered at the end of the stage
        for connection in CloudDict[cloudID].connections: # And send the 10 pulse to every cloud which is not dead.
            if connection not in DeadClouds:
                cloudsToBeStaged[(connection, 10)] = 1
    return cloudsToBeStaged

def TrackStage(cloudID, strength, multiplier): # Phase 2: We now update which impulses will occur next Stage. It's mostly identical to the Follow procedure
    global CloudDict, DeadClouds
    cloudsToBeStaged = Counter()

    if strength != 1:
        for connection in CloudDict[cloudID].connections:
            if connection not in DeadClouds:
                cloudsToBeStaged[(connection, strength - 1)] = multiplier
    return cloudsToBeStaged
    
def Solve(part):
    global CloudDict, DeadClouds, CloudsToBeKilled
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split(","), f.readlines()))
        CloudDict = {}
        for cloud in inp: # Parse the input into a dictionary which maps an ID to a cloud
            id = int(cloud[0].replace("id=", ""))
            energy = int(cloud[1].replace("energy=", ""))
            connections = list(map(int, [cloud[2].replace("connections=", "")] + cloud[3:]))
            CloudDict[id] = Cloud(energy, connections)
        FirstCloud = max(list(CloudDict.items()), key=lambda x: len(x[1].connections)) # Find the first cloud, which for parts 1 and 2 is the one with the most connections.
        if part == 1:
            Follow(FirstCloud[0], 5)
            print(sum([x[1].energy for x in list(CloudDict.items())]))
        elif part == 2:
            Follow(FirstCloud[0], 10) # This is quite slow, but not slow enough for me to want to port the part 3 over.
            print(sum([x[1].energy for x in list(CloudDict.items())]))
        elif part == 3:
            PowerTotals = [] # The total power of the alive clouds
            StartingCloudDict = deepcopy(CloudDict) # Copy the starting conditions, so that we can reset back to the beginning.
            for FirstCloud in CloudDict.keys():
                CloudDict = deepcopy(StartingCloudDict) # Reset the CloudDict
                DeadClouds = [] # These are the exploded clouds
                CloudsToBeKilled = [] # This holds the clouds which will explode this Stage
                StagedClouds = Counter() # This holds the instructions we need to carry out this Stage
                StagedClouds[(FirstCloud, 10)] = 1 # This is our first cloud. Essentially, what this says is. We have 1 impulse on the FirstCloud which has strength 10
                while StagedClouds: # While there are still impulses
                    NextStageClouds = Counter()
                    for cloud in StagedClouds: # Phase 1
                        if cloud[0] not in DeadClouds: # If the cloud is still un-exploded
                            NextStageClouds.update(GiveEnergy(*cloud, StagedClouds[cloud]))

                    for cloud in StagedClouds: # Phase 2
                        if cloud[0] not in DeadClouds:
                            NextStageClouds.update(TrackStage(*cloud, StagedClouds[cloud]))

                    StagedClouds = NextStageClouds # Set our caluclated impulses so that they can be used next Stage
                    DeadClouds.extend(CloudsToBeKilled) # And add the exploded clouds to the banlist

                PowerTotals.append(sum([x[1].energy for x in list(CloudDict.items()) if x[0] not in DeadClouds])) # Add the total energy of the unexploded clouds to Powertotals
            print(max(PowerTotals)) # Print our maximum
                


for i in range(1, 4):
    Solve(i)