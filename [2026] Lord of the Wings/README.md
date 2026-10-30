2026 is here, and it's bringing one of my favourite books along for the ride!
(Even though there and back again was written by Bilbo about his journey to Erebor, it had nothing to do with Frodo. But I digress).

# Quest 1 

A generation fumble from me, where I completely forgot how to use the map function, and bumbled about with that for a while. Other than that, a relatively light quest.
Part 1 was find the next square.
Part 2 was find the next multiple of four.
Part 3 was find the next odd square - 1.

I'm going to make my code a bit prettier (I ***will*** comment my code this year). I'll also do the writeup of the digital atelier while I'm at it.

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

One of the first things I did was reverse all the lists so that my for loop which would add in the powers worked upwards rather than downwards. This, like most of my ideas, only added in further complexity down the road. I need to learn to try and not edit the input too much, or else I paint myself into an inflexible corner.

# Quest 4

At first, this looked not too bad. Part 1 is the kind of thing I'm used to, calculate the value, then sort and multiply.

Part 2 was a bit more interesting, and very helpfully "python sort by two keys one reverse" is a common google search.

It was Part 3 that made me realise this was a very meta quest (no, not the VR headset), twenty quests split up into three parts with a scoring system that decreases by one for each solve.
This was pretty cool, except for the fact, that there was a little green box which gave an extra example. Something awful was going to happen next.

I eventually managed to complete it though. There wasn't really anything too novel in the code, except for the tieing mechanic, but even then, that's not very interesting.