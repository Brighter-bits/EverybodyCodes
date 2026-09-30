I completely forgot this existed.

# Quest 1

I feel as if I overcomlpicated this one. I can probably condense the three Weave functions into a single function, but that's not for today.


# Quest 2

This one is quite interesting, but it should be easily doable, as finding the halfway point between two coordinates is just finding the mean of both of them. Rereading the third part I initially thought it wanted the largest number of fireflies. That's incorrect, it wants every possible beacon position then fireflies. That makes this a much easier flood-fill sort of thing.

# Quest 3

This one's a bit of a challenge. I wanted to do this mathematically, not by making a grid, because I felt that the last part would likely be "Here's a bigger version". And I was right.

My solution essentially goes along, cell by cell, and checks the coordinates against the offset and if they all line up, it's an isolated square. The colours bit made it a bit trickier, but all you need to do is look for where there is a dividing line, as past that will be a different colour.

At this point, it's likely that I need to find a piece of the pattern, and then multiply it out, rather than doing it one by one.

It would make sense if the pattern repeats every two cycles, and that seems to be the case from counting. Actually, it seems to only be a single cycle, with each cycle switching between the two colours.

```
GOG
OGO
GOG
```

It's been so long, that I can't really explain my code. It uses a 2x2 grid (which basically automatically pairs up the cycles) and then does it's thing.