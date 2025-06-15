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

Easy. So easy, did it in under 10 mins. And even then, I mistyped the input and so had to wait a minute to put in the correct answer.

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

Looks fine, all I need is justt a bit of maths, second part looks harder though.

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
I thought that a letter in the first grid could be taken from a letter twelve grids away on the same row (no, each grid is it's own independant thing)

One slight problem with this grid, is that if I solve a certain letter, that could have been used to make the previous grid possible to solve, I would have to go back. So I may have to do something similar to
bubble sort, where I keep track of whether I've made any new changes, and if not, I have my final answer.

Instead, I decided to just do it 1000 times. While my solution isn't very good, it works. At one point I did struggle with a slight problem of having two question marks on the same row/column.
As such, I have to abandon solving the grid, as I don't know which letter to place in which spot. As it could be either one. Later however, once more question marks are solved I can just go back and hopefully
my kerfuffle will be solved.

# Day 11

I don't know why I'm calling them days, I'm doing this over the course of months whenever I feel like it.

This quest however was nice and simple. All you need to use is Collection Counter, then adding the new generation multipled by the old generation.

Nice and simple, part three all you have to do is note down the different types of termites, loop through them all and do max–min.

# Day 12

.... This seems incredibly difficult. So, since this is coordinates I will be using imaginary numbers as they're less work than touples.
I can calculate where the projectile will start falling, because the targets are not close enough to the catapults to be hit while going up or across.

The calculation is just the power up and twice the power across. Nice and easy. I can then put every single coordinate into a dictionary.
Each coordinate corresponds to the ranking score of the projectile that would destroy it.

Then I find the coordinates of the targets, put it in, and bam, I get all my values.

Part 2 is simple enough, I just have to check for H and append the coordinate twice. I encountered a little error because the program found all the Ts then tried to start searching for Hs at the end of the row.

Part 3... NOW THE UPWARD AND SIDEWAYS values are necessary?! AND THERE'S A TIME COMPONENT??????? =( I'm going to spend far too long on this part.

I've done some thinking on this. I can give each meteor a list of all of its positions, alongside the time they will be there.
We can make our usual list of coordinates, but add a time component.
But since the projectiles can be launched at any time and with multiple at a time, we can compare the time component of the meteor's time component and the projectiles' time component.
If the time component of the projectile is less than that of the meteor, we can get all the projectiles that will work, we then choose the smallest out of all of these.

Had a problem where I was going backwards while descending. This is highly inefficient, my laptop is burning up. BUT IT IS WORKING!

# Day 19

They're not actual days. Okay, so today, the 2025 Quest and the first story were put onto the website. In my excitement, I clicked onto the story and then wondered why Sir Enigmaticus Enscriptus was in bold. I
clicked it and started Quest 19...

FOR THE LOVE OF EVERYTHING, LEARN TO READ!!!!! "From the beginning of the message key sequence".

Next part can't be brute force, however, since we go from the beginning of the message key sequence, each pass will be exactly the same.
E.g, the character in spot [4][4] will always be moved to spot [5][6]. If I can find the exact transformation, I can just apply it over and over, which is maybe faster?
It is faster, if I also compute where the character will go after 4000 passes, I can optimise it further.
Then again, it's only "optimised", the thing still takes over 10 minutes to run, but I'm happy with it.

# Day 13

Back to normal... Dijkstra again?!
Phew, 5 days and I've finally implemented my first A* algorithm... and now I'm getting recursion errors for my other function.
My current implementation uses recursion in order to essentially flood fill the entire grid, adding the time it takes for each step-

Nevermind, I can just say goodbye to safety and increase the recursion depth. What could go wrong?
Nothing apparently, it works perfectly fine now.

Okay, I've put the algorithm into a function with a start and end variable, then got all the possible start variables. I then spent an hour because I kept calculating the max time instead of the min.

# Day 14

Oh, this looks horrible. I'm going to need to create a Tensor class which can hold all of the information... and also expand dynamically.
I'm not too sure how to do this, but I'm going to spend some time on it.

This is ballooning out of control, I think I'll need to use a different method.
Since I only need the height, I'll only count the up and down commands as the rest are irrelevant.

Okay, part 1 complete, but part two looks like it will need a Tensor.

Spent more hours on that, don't use a Tensor, it is FAR too much work.
Instead, I'll have a dictionary which holds all of the points I have visited, if I get a new point, nothing will happen as it is already set to True.
I will then count how many items I have in the dictionary.

The next one is harder, I have paths, and I need to find the shortest distances......... A* again? Really? I just did that in the last quest...

Fine. I will check every single item in the dictionary and then check if the adjacent segments are in the dictionary, if they are, we set up a link between them.

# Day 15

Dijkstra again? This feels repetetive at this point.

Nevermind, I've been trying this for quite a while, maybe a double dijkstra?
Brute force methods are not working so well.
I've called in the AId and am now learning a dynamic programming method, similar to Day 9.

Unfortunately, the method is really, really, really slow. However, I can use Dijkstra to find the shortest length between every single herb, the other herbs, and the start.
This creates a sort of compressed graph without all the moving one space nonsense.

Nevermind, DP is terrible, I'm using brute force.

I can simplify the graph, by instead of having each individual square be a node, I have each herb being a node. This is taking far too long.

So, since the input is technically just the previous input but x3. So if I just find the shortest path around them all, making sure the middle one connects to the other two, I should be fine?
The only place the middle point connect to the other two is at the two "K"s. So I find the shortest path to get from the start, to all the herbs in the middle, as well as the "E" and the "R" which are next to
the "K"s.

