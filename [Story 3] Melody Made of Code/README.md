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

