import os
from pathlib import Path
from collections import defaultdict
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q04_p1.txt", "everybody_codes_e2026_q04_p2.txt", "everybody_codes_e2026_q04_p3.txt"]

class record(): # A small class for collecting the different parts together.
    def __init__(self):
        self.parts = 0
        self.time = 0
        self.points = 0

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", "").split(" "), f.readlines()))
        QuestDict: dict[int, record] = defaultdict(record)
        total = 0
        if part != 3:
            for quest in inp: # Parse each line and then create a record for each ID, how many parts it has done, and the time it took for them to complete all of those parts
                id = int(quest[0].replace("id=", ""))
                time = int(quest[3].replace("time=", ""))
                QuestDict[id].parts += 1
                QuestDict[id].time += time

            if part == 1:
                QuestDict = sorted(QuestDict.items(), key=lambda x: x[1].time) # Sort by time only
            elif part == 2:
                QuestDict = sorted(QuestDict.items(), key=lambda x: (-x[1].parts, x[1].time)) # Sort by largest number of parts, and then by time

            for i in range(len(QuestDict)):
                total += (i+1) * QuestDict[i][1].time # Add the time multiplied by it's position
        
        else:
            total = SolvePart3(inp, QuestDict)

        print(total)

def SolvePart3(inp:str, QuestDict: dict[int, record]):
    ids, questList = MakeQuestList(inp) # This is a simple function which creates a set of every ID in the list, and also every quest and part in a tuple of (QuestNum, PartNum)

    currentQuest = -1
    for Puzzle in questList:
        CompletedPart = set() # A set which holds who has completed this part.

        if Puzzle[0] != currentQuest: # If we have moved on to a new quest, then get rid of the previous times
            currentQuest = Puzzle[0]
            for id in ids:
                QuestDict[id].time = 0

        for quest in inp:
            id = int(quest[0].replace("id=", ""))
            time = int(quest[3].replace("time=", ""))
            questID = int(quest[1].replace("quest=", ""))
            part = int(quest[2].replace("part=", ""))

            if questID == Puzzle[0] and part == Puzzle[1]: # If this line is of the right quest and part, we add on the time to the competitors current time. We also add them to the list of those who completed the course
                QuestDict[id].time += time
                CompletedPart.add(id)
    
        for id in ids - CompletedPart: # For every competitor who didn't finish the Part, we set their time to zero.
            QuestDict[id].time = 0

        SortedQuests = sorted(QuestDict.items(), key=lambda x: x[1].time if x[1].time != 0 else float('inf')) # Now we sort the competitors by time, but everyone who didn't complete the Part goes to the very back

        match Puzzle[1]: # Calculate how much this part is worth
            case 1:
                maxPoints = 50
            case 2:
                maxPoints = 100
            case 3: 
                maxPoints = 150

        skip = 0 # Skip holds how many places we need to skip if there is a tie.
        for placement in range(len(SortedQuests)):
            if skip > 0:
                skip -= 1
                continue

            Participant = SortedQuests[placement]
            
            if Participant[1].time == 0: # If the participant didn't complete the part, then they and everyone else after them don't get any score
                break
            
            counter = 1
            while True: # This continually checks the current participant against those behind it.
                try:
                    NextPlace = SortedQuests[placement+counter]
                except: # If we have reached the end of the Participants, then stop
                    break


                if Participant[1].time == NextPlace[1].time: # If there is a tie
                    skip += 1 # Add one to the skip
                    counter += 1 # Add one to the counter, so the next loop, we check if there is a three (or later four, etc.) way tie
                    QuestDict[NextPlace[0]].points += maxPoints # Give the NextPlace the right score
                else:
                    break # If there are no more ties, then stop

            QuestDict[Participant[0]].points += maxPoints # We give the Participant the score they deserve.
            maxPoints -= 1

            if skip:
                maxPoints -= skip # If there were skips, then we decrease the score by the number of skips we need to do.

            if maxPoints <= 0:
                break

    QuestDict = sorted(QuestDict.items(), key=lambda x: x[1].points, reverse=True) # We now sort by points to get the true leaderboard

    return CalculatePointTotal(QuestDict)

def MakeQuestList(inp): # A very simple function that parses the quests, and then sorts them by quest and then part.
    ids = set()
    questList = set()
    for quest in inp:
        id = int(quest[0].replace("id=", ""))
        ids.add(id)

        questID = int(quest[1].replace("quest=", ""))
        part = int(quest[2].replace("part=", ""))
        questList.add((questID, part))
    questList = sorted(list(questList), key=lambda x: (x[0], x[1]))
    return ids, questList

def CalculatePointTotal(QuestDict):
    total = 0
    skip = 0
    for i in range(len(QuestDict)):
        if skip > 0:
            skip -= 1
            continue
        CurrentPlace = QuestDict[i][1] # This part here is very similar to the placement code, as it fullfills basically the same function. 
        counter = 1
        while True:
            try:
                NextPlace = QuestDict[i+counter][1]
            except:
                break

            if CurrentPlace.points == NextPlace.points:
                skip += 1
                counter += 1
                total += (i+1) * NextPlace.points
            else:
                break

        total += (i+1) * CurrentPlace.points
    return total

for i in range(1, 4):
    Solve(i)