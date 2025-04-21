# EverybodyCodes
A horrendous EverybodyCodes repo, because I'm having withdrawal symptoms from AOC


# Day 1

Yes, starting from day 1, I know. Anyway, first bit is just counting the number of chars of each type. I may have been procrastinating on this, so the timer says I took several days to think up the solution.
I didn't.

# Oh right, I was supposed to be documenting this

# Day 2

A bit of a pain, its just a wordsearch at the end of the day though

# Day 3

Really like this puzzle actually, it forced me to do some interesting stuff with functions.

# Day 4

Easy. So easy, did it in under 10 mins. And even then, the I mistyped the input and so had to wait a minute to put in the correct answer.

There, caught up.

# Day 5

What is this?????????

The most annoying part is when the dancer wraps around to the other column, but then if the last column wraps around to the start, everything breaks...

I swear this is impossible, every single time one of the columns just empties, how did I even do part one.

........................ Okay. So, when the clapper goes to the next column, they don't switch to the next one once they get to the end.
The clapper just circles the exact same column multiple times until they are assimilated into the hivemind.

I am very annoyed.

Okay, part 3... There's almost certainly a mathematical pattern, where it all begins to repeat. However, checking if it's repeating will probably cause a memory error. So instead, we'll just go on for a long
time and then use the largest one, and hope it's right

# Day 6

DIJKSTRA!!!!

Okay, maybe it's a bit overkill for Dijkstra. However, it's always good to practice. However, the algorithm can't differentiate between each different apple, so I've given each a unique AppleID!

Okay, while implementing dijkstra may have taken some time, it obliterated parts 2 and 3, so I think it was worth it.

Cleaned up the code a bit so that I don't have to manually look at the length of each branch.

# Day 7

It doesn't look like Dijkstra... yet.

First bit was fine, the dictionary may not have been necessary though. 

Part 2 looks more complicated, but it's just applying a mask over another list.


I completely forgot that powers can't go negative, I have wasted hours on trying to find the error...
But I did see some other person's code which had some really funky cool stuff, that I actually kind of understand now (didn't help my solution though).

Pre-emptive celebration, that did not change my output.....

It's too late at night, I'm calling in the AId.

The AId is being useless, again... AI truly is the future.

I believe I now know, still need to implement it however. Every time I completed a lap, I went back to the start of the plan, what I probably should have done, is gone to the next part instead.

Brute force 4ever!!!!!!

I can't read. I've brute forced twice, 26 hours in total. Just to realise it's only those which contain 5 "+"s, 3 "-"s and 3 "="s

# Day 8

Looks fine, all I need is jsut a bit of maths, second part looks harder though.

Okay, in my opinion EveryBody Codes has some really confusing wording sometimes. For this one, I thought
that the extra blocks on the side couldn't be higher than the layer. I WAS WRONG. It's far easier!

I spent 2 hours of "Volunteering" on this...

# Day 9

This one seems easy enough, all you need to do is subtract and subtract until you get the answer. I bet that eventually I'm going to run into the problem where just going down the list won't find me the
smallest combination.

Called it. No clue what to do though... prime factors or factor trees perhaps?

Turns out this is called the coin change problem, and has a very specific solution.

For the third part, the possibilities ranged between the target halved - 50 and the target halved + 50. And each possibility has only one specific pair which can be used to create the target.
So in reality there's only around 100 possibilities per number

I did begin running into errors on part 3, but that was an off by one error when rounding odd numbers/2.

# Day 10

Today is quite simple, it's just picross really, but with words.

Okay, this is a bit harder. After a lot of careful reading- Just kidding, I haven't learnt my lesson and am still not reading the questions properly, I misunderstood the question.

One slight problem with this grid, is that if I solve a certain letter, that could have been used to make the previous grid possible to solve, I would have to go back. So I may have to do something similar to
bubble sort, where I keep track of whether I've made any new changes, and if not, I have my final answer.

Instead, I decided to just do it 1000 times. While my solution isn't very good, it works. At one point I did struggle with a slight problem of having two question marks on the same row/column.
As such, I have to abandon solving the grid, as I don't know which letter to place in which spot. As it could be either one. Later however, once more question marks are solved I can just go back and hopefully
my kerfuffle will be solved.