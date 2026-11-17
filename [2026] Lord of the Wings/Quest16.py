import os
from pathlib import Path
from collections import deque
os.chdir(Path(__file__).parent)

Parts = ["everybody_codes_e2026_q16_p1.txt", "everybody_codes_e2026_q16_p2.txt", "everybody_codes_e2026_q16_p3.txt"]

def GroupUp(books:list[list]): # This function essentially just does run length encoding on the, except no it doesn't. It just groups together consecutive books of the same colour into a list of books. Actual RLE would probably have been more efficient.
    newBooks = []
    try:
        currentColour = books[0][0] # If the first book is slightly wrong, just use the next one
    except:
        currentColour = books[1][0]
    newGroup = books[0]
    for i in range(1, len(books)):
        if currentColour == books[i][0]: # If it's the same colour, add it to the list
            newGroup.extend(books[i])
        else:
            newBooks.append(newGroup) # If it isn't then store the old group and make a new one
            newGroup = books[i]
            currentColour = books[i][0]
    newBooks.append(newGroup)
    return newBooks # All very simple

def Swap(books):
    global LastSwappedLocation, ColoursChecked
    notches = 0
    
    for i in range(len(books)):
        currentColour = books[i][0]

        if currentColour in ColoursChecked:
            continue
        
        placeToSwap = i + 1 # Since we keep grouping all of these colours up, the first group after the current colour must be a different colour
        for j in range(LastSwappedLocation-1, placeToSwap, -1): # Go backwards through the list
            if books[j][0] == currentColour: # Once we find our swapping position
                notches = CheckLengths(books[placeToSwap:j+1]) # Find how many books we're moving
                books[placeToSwap:j+1] = books[placeToSwap:j+1][::-1] # Swap the lists
                LastSwappedLocation = j + 1 # This was originally to try and make this code more efficient before I changed methods. It just makes it so that I don't go through the static end of the books
                break

        if notches != 0: # If we made a swap, break
            break

        ColoursChecked.append(currentColour) # We've now finished this colour so append it to the Colours we've completed, and also reset our starting position to the end of the list
        LastSwappedLocation = len(books)
    return books, notches

def FasterSwap(books):
    currentColour = books[0][0]

    NotContainingColour = [sublist if currentColour not in sublist else [""] for sublist in books] # First find all the groups which aren't the colour we're looking for
    NotContainingColour = GroupUp(NotContainingColour)

    directions = [[1, 0], [0, -1]]
    direction = 1
    total = 0
    
    newEnding = deque() # This will be the new ending to the list once we're done swapping
    indexes = [i for i, _ in enumerate(NotContainingColour) if _ == [""]] # This is the location of every one of the groups which contain the colour we're swapping
    NumOfCurrents = deque([sublist for sublist in books if currentColour in sublist]) # This contains all of the groups which do contain the colour we're swapping.
    CurrentSum = CheckLengths(NumOfCurrents) - len(NumOfCurrents.popleft()) # We find the current sum of all of the currentColours, then get rid of the first group which never moves

    if indexes[0] != 0: # These two if statements were necessary at some point, though I'm not sure if they're still needed and am too tired to find out.
        indexes.insert(0, 0)
    if indexes[-1] != len(NotContainingColour):
        indexes.append(len(NotContainingColour))
        
    pointers = [0, len(indexes)-1] # These slowly work inwards over the list
    counter = 0

    while pointers[0] != pointers[1]: # It's like quick sort, sort of, trust me

        if direction == 0:
            if CurrentSum != 0: # This is just here for a bit of safety
                CurrentSum -= len(NumOfCurrents.popleft()) # First delete from the CurrentSum (it doesn't really matter when this is deleted, as long as it is added enough times)
            ToAppend = list(reversed(NotContainingColour[indexes[pointers[0]-1] + 1:indexes[pointers[0]]])) # We find what we are going to append.
            total += (CheckLengths(ToAppend)) * counter + CurrentSum # We add the books that we are going to push to the end of the list, multiplied by the number of times they would have swapped, plus the number of correctly coloured books which we will be placing at the front.
            newEnding.appendleft(ToAppend) # Now actually place the books at the end

        else:
            if CurrentSum != 0: # This is the same but for the other side
                CurrentSum -= len(NumOfCurrents.pop())
            ToAppend = NotContainingColour[indexes[pointers[1]-1] + 1:indexes[pointers[1]]]
            total += (CheckLengths(ToAppend)) * counter + CurrentSum
            newEnding.appendleft(ToAppend)

        
        direction = (direction + 1) % 2 # Change which direction we're going from 
        pointers[0] += directions[direction][0] # Incremement the pointers and the counter
        pointers[1] += directions[direction][1]
        counter += 1


    return [a for a in newEnding if a != [""]], total



def CheckLengths(books: list[list]): # This is a simple function which just takes a list of groups and counts how many books are in them.
    total = 0
    for book in books:
        total += len(book)
    return total


def Solve(part):
    global LastSwappedLocation, ColoursChecked
    ColoursChecked = []
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))[0]
        total = 0
        match part: # Each part has it's own quirk. Part 1 wants a -1 on its loop, and the other two want multiples
            case 1:
                total -= 1
            case 2:
                inp *= 10
            case 3:
                inp *= 100


        if part != 3:
            inp = GroupUp([[a] for a in list(inp)]) # Group everything up
            LastSwappedLocation = len(inp) # Reset our limiter
            while True:
                inp = GroupUp(inp)
                if LastSwappedLocation > len(inp): # If our limit somehow gets longer than inp due to the grouping, we shrink it down
                    LastSwappedLocation = len(inp)
                inp, notches = Swap(inp)
                total += 1 if part == 1 else notches # Part 1 just adds one, while part 2 adds notches
                if notches == 0: # If we got no notches, then we didn't swap, so break
                    break
            
        else:
            total = 0
            inp = GroupUp([[a] for a in list(inp)]) # Bascially the same thing, but with FastSwap
            LastSwappedLocation = len(inp)
            while True:
                inp = GroupUp(inp)
                if LastSwappedLocation > len(inp):
                    LastSwappedLocation = len(inp)
                inp, notches = FasterSwap(inp) if part == 3 else Swap(inp) # For some reason the fast one doesn't work on part 2? 
                inp = [colour for group in inp for colour in group] # This just flattens the array a bit.
                total += notches
                if notches == 0 or inp == []:
                    break

        print(total)



for i in range(1, 4):
    Solve(i)