Another year, another quest

# Quest 1

This one was quite fun. I think I overcomplicated it slightly, and for some reason, my code currently outputs the wrong answer, the correct answer was actually my 3rd largest value.

I HAVE FOUND MY PROBLEM, it is once again in my inability to read. I firstly found the sum of all of the lists, and then chose the largest one. What I was supposed to do, was find the list with the most DNA in it, then find the maximum of that.

# Quest 2

This one started off really easily, and then got much harder. I'm quite tired, and the code is very spaghetti like, but to do the boxing, I just kept flood filling boxes around the Current Point, and if it manages to hit a wall I had put down, then the box was not filled in.

For some reason, what messed me up in the end, was a piece of code I copied and pasted from when I first did the 2024 event.

```python
def FindPointList(Grid, Letter):
    array = []
    for y in range(0, len(Grid){-1}):
        for x in range(len(Grid[0])):
            if Grid[y][x] == Letter:
                array.append(complex(x, y))
    return array
```
For some inexplicable reason, I had put a -1 after the len(Grid), meaning the last line of bones wasn't taken into account. Other than this, there isn't really much else to say.


# Quest 3

I decided to use a class to handle the variables for this, and then use some simple recursion to get parts one and two done.

Part 3 was hell. Initially, I tried to build off of the code for parts one and two, but after a long time, these quickly spiralled out of control, to the point where they were unmanageable.

I rewrote it quite quickly however, building off of the fact that it's really just an in-order traversal. If I simply keep doing the traversal until everything is sorted into it's own spot, then it should be fine.

But it didn't work, until an hour ago, when I finally got a valid input... Turns out I had had an invalid input this entire time, which probably explains a lot. My old code stil was wrong though.