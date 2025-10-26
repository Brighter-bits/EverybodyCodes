# Quest 1... Again

So, I'm going to have to sort these into folders properly later. This puzzle seems like a tree puzzle, with each child being the next peg. Easy enough

Easy enough sure, if I realised that the asterisks were the dropping slots, not the dots...

Turns out I was checking the x coordinate against the height of the machine, but it's fine now. Part 2 meanwhile, looks like I can just brute force it, though I feel like Part 3 I will need to do some caching.
Wait... Part 3 may actually be brutable. I did a bit of research and found "The Hungarian Algorithm", which makes sense until it starts trying to uncover edge cases. So while this would probably help me, I
don't want to have to implement it...

Turn out there is a function in itertools called product. Which is essentially just a fancy nested for loop... Nevermind that won't work...

Product gives you every single possible combination, including having the same element multiple times. Permutations does not allow that and is what I actually want.

# Quest 2

This one seems easy enough. Though I feel I can do better than just linearly going through it, so I'm using lstrip to strip the left side of anything. I was initially getting the wrong answer, but that was
because when a bolt hits a balloon of it's own colour, it goes through and will still pop the colour after it, even if it is different.

Part 2 was not too bad to implement, but there's a trick to it that I need to find somewhere for Part 3. I have a strange idea to do with columns that might work.

Thinking through it, I wouldn't know the placement of the balloon which was popped, which is quite important. I could also try filling the popped balloons with '0's so that the list doesn't have to keep moving
about, which is the reason it's so slow. The problem then is how do I calculate which balloon was popped?

It has to be something to do with the repeating pattern. The pattern seems to be 256 long, which is 2^8 and that may be helpful? It has to repeat at a point. After some testing, it doesn't seem to repeat when I
test it with the test input. I tried it with a repeating RGBRGBRG and it had a pattern, but this did not...

Anyway, it turns out that using "del array[index]" is way faster than doing "array = array[index:] + array[index+1:]" which is unexpected. I assumed del was weird and not correct, but if it's faster I won't
complain.

Apparently, people have used deques to do this. I'm pretty sure these are double ended queues, though I don't see how this helps? Sure one end is fine, but wouldn't doing the other end break it? I guess I could
just replace my list with a deque and see what happens?

Yes it does run faster, but not nearly enough to be tractable, there's a trick here where I can more easily remove the middle balloon. What if I had two deques? This would hopefully be really fast as deques
work best when you add from the exact start and end. Fun fact, you have to use itertools slice to split a deque because it's a linked list.

I got the wrong answer, but it was incredibly fast, wow. There was a slight problem, where I was deleting the first element of inp instead of the Fhalf, but it's fine.

It also turn out that you can't move the baloons to the first half every single shot, you have to do it every other shot.

# Quest 3

Final quest, it seems easy enough, it just looks complicated, I'll probably make a dice class and then work it through.

Part 2 was quite easy, but Part 3 looks like it's going to be much more difficult. The grid is around 500x500 which makes my attempts to create a Graph basically impossible for me.

There probably is a way to make the graph, but I have no clue how to do that. As such, I'm going to do this differently.

My next attempt is going quite well, I accidentally kept referencing the same Dice in memory, so I've used deepcopy to ensure that doesn't happen again. I also didn't read the quest properly, as you can
actually stay still on a square.

I have no clue if the functools cache will work, so I'll botch my own version together just in case.

Okay, it was definitely not working, the atrocious version I just put in got the answer in less than a second. The other one took half an hour...

On the actual input it takes a good couple minutes, but nothing atrocious.