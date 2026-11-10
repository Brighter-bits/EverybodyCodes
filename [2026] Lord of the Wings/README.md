2026 is here, and it's bringing one of my favourite books along for the ride!
(Even though there and back again was written by Bilbo about his journey to Erebor, it had nothing to do with Frodo. But I digress).

# Quest 1 

A generation fumble from me, where I completely forgot how to use the map function, and bumbled about with that for a while. Other than that, a relatively light quest.
Part 1 was find the next square.
Part 2 was find the next multiple of four.
Part 3 was find the next odd square - 1.

I'm going to make my code a bit prettier (I ***will*** comment my code this year). I'll also do the write-up of the digital atelier while I'm at it.

# Quest 2

I keep forgetting it takes time to warm up for these events. But still, this one was pretty rough for something so easy.

My first instinct was to start placing down numbers, then reordering them as I place new ones in.

I quickly gave up on this idea, and instead went for a different idea. I would keep track of how many numbers were greater than the current one, then order them by how many numbers were greater than them. And the first digit would be the only one not in the list (a fact I forgot about and had to go add back in).

Once we got to Part 2, I completed the same algorithm, and the smallest two numbers would always be tied. So I simply had the program check which one had the other in its list of greater numbers, then appended -1 to that list, so that the order was now corrected.

Part 3 got more complicated. After a couple ideas, I had the idea that the appending -1 was sort of like giving baggage. I then realised I should give baggage relative to how small the number was, to drag numbers which were thought to be high, down to the bottom.

However, this wouldn't always work, as sometimes, the baggage would be applied from a to b while a was small; then a would grow enormous (as it was supposed to), and b got off scot free. So, since these small differences would eventually compound, I ran the algorithm ten times and hey presto, it worked.

Not too proud of this one.

Looking at other solutions, the best solutions seem to be using graph theory... Which sort of makes sense? Kahn's algorithm for sorting seems to make the most sense to me.

# Quest 3

This one was quite fun.

Most of my time loss was due to silly mistakes, and also having a working solution 9 edits back, but I kept thinking it was wrong because I was still using the example input.

Part one was quite simple, it was just two lists and then working on the both of them.
Part two I just turned the bases into a cycle that could be reused.
Part three I finally put the computation into its own function.

One of the first things I did was reverse all the lists so that my for-loop which would add in the powers worked upwards rather than downwards. This, like most of my ideas, only added in further complexity down the road. I need to learn to try and not edit the input too much, or else I paint myself into an inflexible corner.

# Quest 4

At first, this looked not too bad. Part 1 is the kind of thing I'm used to, calculate the value, then sort and multiply.

Part 2 was a bit more interesting, and very helpfully "python sort by two keys one reverse" is a common google search.

It was Part 3 that made me realise this was a very meta quest (no, not the VR headset), twenty quests split up into three parts with a scoring system that decreases by one for each solve.
This was pretty cool, except for the fact, that there was a little green box which gave an extra example. Something awful was going to happen next.

I eventually managed to complete it though. There wasn't really anything too novel in the code, except for the tying mechanic, but even then, that's not very interesting.

# Quest 5

I don't know why, but my first instinct was to make a Flood Fill. I then promptly ignored this to try and do passes of a window of values. Then went back to flood fill when I realised it would be way easier.

I honestly thought I would be using the Flood Fill for more than just the very first part, but it didn't seem to be so.

I actually liked how this puzzle built upon itself, though I'm a bit annoyed on how the final part doesn't like it if I start in the central square.

# Quest 6

Okay, this was quite a fun one, which I did try to optimise too early, and completely misread the problem.
I didn't realise that the ingredients would loop, and I thought I only wanted the base ingredients so I just set up a simple search that would return 1 once it got to the bottommost ingredient.
This was completely incorrect and I wasted about 10 minutes coding it, afterwards it got a bit more straightforward.

The second part simply required me to run the Check function over every recipe, and returning True if there was a NULL.

Now, I'm quite proud of my third part. Rather than using a tuple of True's and False's, I realised that it would be best to use some binary to keep track of my NULLs. Each bit is a type of NULL, with 1 being present and 0 being missing.
From there I simply used the Bitwise OR operator, so that if a new NULL type was found, it would be merged into the running total and nothing would be overwritten. Then it was a simple case of checking if the binary number was equal to three or greater than 4, in which case, we had more than one NULL and could add 1 to the total.

# Quest 7

This one was quite enjoyable. I initially went for a recursive solution, but then transferred over to using Counters (my beloved).

I did unfortunately, blunder quite horribly and spent at least half an hour trying to figure out why Counter.update was not updating the NextStageClouds Counter.

The Part 3 solution is the only interesting bit:

I set it up so that there were two phases, in the first phase, energy would be added up and explosions would occur. All of the impulses created by the explosion is stored in a list. Then in the second phase, we calculate all of the impulses that will occur in the next Stage.

We then add any clouds that have exploded to the ban list, and then begin the next Stage with the impulses we calculated last time.

I did like how I counted these impulses though. I used a Counter which had a composite key of the Cloud's id and the impulse's strength. That way, if I had a cloud which had 10 impulses with a strength of two, rather than try and calculate them all one by one, I just multiply everything by 10.

# Quest 8

Just by reading the description, I knew I was in for a doozy. I hate geometry, there is nothing I despise more than shapes, and this puzzle is quite obviously shape related.

My first idea was to flatten the hexagon down into a nice square that I could split into lines, though with the wording of Part 1, I knew I was going to have to be ready to edit it. In the end, I just copy-pasted the function four times. Though hopefully I've cleaned it up to be a bit nicer now.

For part 2, I misread the puzzle, as I always do, and thought that it wanted the number of unique ents which received energy. That was not the case, but it would be quite useful in the next part.

This part wasn't as bad, though I did spend a while thinking I wanted the number of rounds. This definitely isn't my best work, and the code is probably going to remain messy, just like this description.

# Quest 9

This wasn't even a hard quest, and I absolutely butchered it. I immediately knew this would be a Counter problem from the start, it just had that vibe. I knew that I would need to keep track of the number of branches, and then split the branches.

My first mistake was my usual fatal flaw of not reading, and then misunderstanding what I needed to do. This was mostly due to how I thought that I had to split the top half evenly. For example, if I had a growth of 7, then I would have to split it like so:

```
 \   /
  \ /
   +
   |
   |
   |
```

I got very confused as to how I would know whether to add one to the bottom "trunk" or the upper branch. I eventually realised that the second branch always had a length of one, and from there it wasn't so bad.

Part 2 was perfectly fine to be honest, and for Part 3 I successfully predicted that it would just be "more trees, go do it again". I hoped just adding a cached function would help, but I eventually realised that the for loop over my counter was my real issue.

And so I did the obvious thing and rather than doing every single individual loop, I would skip to the next time a growth split happened.

I then spent an entire hour because my increment of the total value was indented slightly incorrectly...

Suffice to say, this was a perfect puzzle for me, if only I were less stupid.

# Quest 10 

I'm writing this the day I completed quest 11, I completely forgot to write this part.

Overall, I think I overcomplicated this quest, especially my loop, which I don't even remember how I fixed. I do know how my code works though, so I have commented it.


# Quest 11

Okay, so I did predict this earlier, but due to the fact I didn't commit this earlier I guess I can't claim it.

So essentially, every week seems to be focused on a different theme. I felt this a bit in 2024 too. Last week was about Dynamic Programming, and skipping parts of loops and making up the difference.

This week though, I predict is going to be full of Dijkstra and A*.

Unfortunately, I didn't have any time over the weekend to go over Dijkstra, so I sort of fumbled about for the first part of the puzzle.
For Part 2 I just iterated through every single possible new connection.
Part 3 was much more interesting, though only because I had to think about how to actually learn how to make unique pairings, then realised that it wasn't that bad.

Good fun puzzle.