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

# Quest 12

This one was quite interesting. I personally found it quite tough, and judging by my placement, it seems everyone else did as well.

The first thing I tried was to create a custom class that would hold the coordinates of the top-left and bottom-left corners of each block. This worked fine for the first part, but I quickly got stumped on part 2. I did start coding something to take into account each side-length and then try and split the block into two smaller blocks, but then I stopped doing that and had a think.

I eventually decided to gamble on if a greedy algorithm would do the trick, and surprisingly it did. Firstly a flood fill to find all the coordinates of each block, then finding every single possible spell and then choosing the one which leaves the smallest number of coordinates left worked really well.

After this for Part 3, I implemented two more functions which find which coordinates are valid taking into account any holes, then using the set intersect to make sure that the spell doesn't cross any gaps.

I would also like to tack onto my previous prediction flood fill, really I just predict that this week will be more about 2D grids. But maybe I'm just hallucinating links and patterns in my head.

# Quest 13

Lessons to Learn: Use Google to find niche algorithms rather than trying to do 8 bajillion edge cases; Include everything in the hash, even stuff that you think is already covered.

Ohhh I hated this puzzle. Oh I hated it. This week has not been fun and I am dreading the next. (I am having fun though, sort of...).

At first, I tried doing weird edge cases, but that kept failing. Luckily, stack overflow helped, unluckily, the AI overview spoiled it for me first. Thinking about it, the gap stuff does make complete sense, so it's not some crazy algorithm I need to remember.

This one was tough, and honestly I wouldn't have been able to do it without the test data in Part 2, which I got access to because I got lucky guessing the answer to Part 1 =D.

# Quest 14

I'm so annoyed with myself!

I quickly understood that this was a graph traversal problem, and that you could essentially model this as a graph with the frame at its centre. The only problem was that I thought of Prim's algorithm, went back to read it on Wikipedia from my old README. And then decided that Prim's wasn't the answer, but instead some sort of modified Dijkstra would do the trick.

It was a Prim's algorithm puzzle.

# Quest 15

As soon as I saw this puzzle, I had a flashback. Gathering herbs in Quest 15 2024 was a 2D grid where you had to collect items and then get from the start to the end. Gathering sulphur in Quest 15 2026 was a 2D grid where you had to collect items and then get from the start to the end.

So the first thing I did was a flood fill on the entire map, and Dijkstra'd every point. What I had not realised was that turning does not take a second, and you cannot turn around in place.

I eventually realised that Dijkstra was not a good idea. I then had the idea to gamble on the hope that the layout of the mines wouldn't change. I went along the centre line, eventually calculating every loop, and turning the map into a 2D line, where you can move left and right between points, and some points allow you to teleport to other points, where teleporting gives you an amount of sulphur.

From there things were still tricky, but I eventually decided it was best to use memoisation for this, and that got me the first two. I don't remember much of it to be honest, but the code I'm pushing is a lot neater than it was at the time I submitted Part 3.

Part 3 was interesting because I distinctly remember looking at the puzzle input and going: "If the first part of the loop is sulphur, the feelers won't go down it." and then completely forgetting about that until an hour later. And even better, I kept thinking I was getting the puzzle completely wrong, because I was using the test input and hadn't realised it.

The trick with Part 3 was to realise that there was probably an optimal loop that the cart would just keep going round and round in. So all you need to do is find that loop, then calculate it rather than doing it by brute force.

# Quest 16

Now this was an interesting puzzle. I looked at it and immediately thought Deques were going to come in handy, so I imported them and then didn't use them at all for part 1.

With part one I just did the simple method of finding the sublist we swap, and then reversing it and reinserting it.

With Part 2 however, I realised this felt close to that problem where you sort things using two pointers, or something close to that one bit in quicksort. I did do some searching and came across pancake sort, but that is something completely different. Essentially, every time you swap you leave behind some books that won't be sorted until a new colour is chosen, and we can abuse this to more quickly calculate the final state of our shelf.

First I started with two pointers going inwards, then I realised I could just find the index of all of the Colour we're looking for, and then take sublists from there.

It was however, very slow, and then I remembered that at the very beginning, I had gone and imported Deques, so I used that, and that heavily sped up my code. I was now getting the correct sorting done, the only problem was that I had no way to count it.

I eventually realised that the first section I had would never be swapped, the next one would be swapped once, the next one twice and so on. Then I just needed to find how large the group of the currentColour I was swapping was, and adding that on, and I got the answer. For some reason it doesn't work with Part 2? I put my answer to Part 3 in on a whim and was surprised that it was right when the part 2 was wrong. But anyway, I've completed the puzzle, and now I can start commenting my code, then go to sleep.

Is it efficient? No. Is it performant? No. Did it get the right answer? Yes.

# Quest 17

My goodness I'm an idiot.

I jumped around a bunch of ideas for this puzzle, mostly because I've been rather tired.

The first thing I did was copy and paste some old code, and then spent 20 minutes to eventually find I had an old bug where I had a > rather than a >=. For some reason, I feel as if I've done this before; because I definitely have.

So Part 1 was just Dijkstra and FloodFill
Part 2 I was going to find every single edge and then traverse them. Then I realised I could just count all the edges I had without traversing them.
Part 3 I tried to connect them all up, and this created some problems with chequerboard patterns like this:
```
#.
.#
```
So instead, I inverted how I created the lines. I instead went along the edge, found every single gap, and then followed it as far as it went. 

# Quest 18

Thank god I'm not going to pull a late one.

For some reason, the last two puzzles have been strangely easy. I did spend a long time on Quest 18, but it was relatively simple in my opinion.

This puzzle was much nicer.

Before part 1, I already knew that implementing this by actually drawing out wasn't going to work, as the puzzle was eventually going to get too large (and how right I was).

It was relatively simple to make the logic for connecting stacks. I accidentally set it up so that only the highest stack would be able to roll over (continue above another stack), but I easily fixed that by just turning it into a list.

For part 2 I just appended the line to the list multiple times, and then added a buffer that would make sure that the distance between the next stack and the current one wasn't too large.
Part 3 wasn't difficult either. I had it so that the large widths were simply set as an integer. Then when my code found the integer, it would multiply the stack's height by the length, and then just keep going.

I'm liking how relaxed it's been these last two days. My sleep has not been going well for the previous couple puzzles.

# Quest 19

.... Well that was easy? Why wasn't that in the first week? (I'm laughing now, I'm dreading what diabolical puzzle has been cooked up for tomorrow.)

Firstly the 2D grid format isn't very important, we can flatten the two grids into two lines.

Then, we simply iterate over them, applying the rule and counting using a Counter object.

That's the entirety of Part 1.
Part 2 I simply got every single possible method, tried them all and then got the total.
Part 3 was actually incredibly easy. In order to get the highest number, you want your three numbers to be as close as possible to each other. I was very lucky in that my K was the smallest group, meaning I could just completely ignore it.
I took the three numbers, found their mean, turned that into an even distribution of integers, multiplied them all together, and managed to come 11th. Which is pretty good in my opinion.

Since I didn't do part 3 correctly, I've just bashed out some code which essentially does what I've said above, but probably isn't foolproof.

# Quest 20

Another easy one? I really thought that this was going to be a stress inducing all-nighter for the final challenge. But it wasn't. It was a nice simple puzzle.

For Part 1, I made a dictionary which converted symbols to the amount of segments they take to create. The actual equation part was relatively easy.
For Part 2, Python has a built in way to convert strings in different bases to base 10; the only difficult bit was converting from base 10 to base 11 for the answer. And that wasn't really all that bad either.
For Part 3, I already had a dictionary, so I decided to make three more of them. One for taking away a segment, one for giving a segment, and one for rearranging a segment within a single symbol. In the end, the solution worked really well.

And that's the end of another year. I was hoping to get some rest after AoC, but GridOS is now happening straight after. Which annoys me a bit, I'm not too tired really, but I always want to compete.

Making predictions now, next year I think Ascalgar is going to be the main character, possibly travelling with the egg. This year's story quite nicely leads into 2025, and 2025 was loosely connected to 2024. So what comes next?

I guess I'll find out next year.