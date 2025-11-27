I have recently learnt that AOC will be having only 12 days this year and no global leaderboard... I am sad, I enjoyed waking up a stupid times to try and get a good score on the leaderboard. However, I
understand that the global leaderboard was sort of corrupted by AI, and making a puzzle is really difficult.

I guess EC will have to fill this hole in my heart.

# Day 1

A fun first quest, I did it quite quickly and had little trouble, I'm going to make the code a bit prettier though. And I did waste about two minutes because I hadn't incremented to the next part on the third
part.

Also, I'm actually really enjoying the theme and it's only been one day. Hopefully it's not dijkstra, dijkstra, dijkstra like last year.

# Day 2

I fell off hard here. I was doing great on an INCREDIBLY EASY PUZZLE. But then... disaster struck... I spent precious minutes losing 6 engravings off of the test input. It turns out, that when you floor a
negative fractional number, instead of just ignoring the fraction, it goes to the number below it...

It makes sense, but I'm still a bit annoyed that I could have just used a single different function and would have done way better. I guess this is how you learn. I'M COMING FOR YOU TONYA!!! (For reference,
this is the person now heading the UK, I **will** win... just give me time... maybe... unless the next puzzles are really difficult... then maybe not...)


# Day 3

Wow, I was clearly very tired yesterday, because I didn't even make the code spit out every single part correctly.

Another easy one, either I've gotten better, or the challenges are easier than last year. For the sake of my ego, I have decided it's the former. Once I understood what was going on, it was quite easy to
handle.


# Day 4

Geeze, I'm so sleepy that I can't do basic maths... This took me far longer than it should have, mostly because for my differences I kept finding the difference between the first and second numbers, over and
over and over, instead of finding the proper differences across the entire list.

Do not code while sleepy, bad idea.

# Day 5

Oops, got distracted by a pokemon game... probably not a good day to do that on, given this day was pretty challenging. I think it was a really unique puzzle, and I actually really enjoyed doing it. I didn't
have any headbanging errors, just a few that I managed to rubber duck my way through. Overall, nice and fun.

Oh my god, how do people do this puzzle that fast?? Ahhh, so, since all the SecondOrder items are going to have the same number of levels, you can just have a list of [quality, first level, second level, ..., id].
Instead of doing whatever the hell I just did. Touché, but now I've been knocked down once again. I must reclaim my throne (unlikely as it is, as stuff only gets harder from here.)

# Day 6

Wow, I'm being such an idiot today. I tried being fancy with regex and that lost me a lot of time. For the second part I copied my input incorrectly somehow? For the third part, an off by one error.

So, to calm myself down, I'm going to explain through the solution and actually comment my code for once...

<br><br>

The "real" input is structured:

```inp | inp | inp | inp | inp | ... | inp```
<br>

Let's say that our input is ```AaaaA```. So if we zoom in we get as a small example:

```AaaaA | AaaaA | AaaaA```

<br><br>
Let's say that the maximum distance is 2.

In the middle we have ```| AaaaA |``` which has 4 matches contained inside the input.
<br><br>
However, the matches can also overflow

```AaaaA | AaaaA``` , we can overflow backwards ```aA|A``` , for one match, and overflow forwards for one match ```A | Aa```.

If we had overflow forwards with something like ```Aa | Aa``` then we would have to count all of the ```a```'s to the right of the break and not count the one inside the inp, and the same backwards.

<br><br>

Okay, so we now have how many matches are inside the inp, how many overflow forwards and how many overflow backwards.

We have 1000 individual inputs, meaning we can overflow forward 999 times and backwards 999 times. We add all of these up, and we get the answer to part 3.

I spent over an hour on this.

# Day 7

I'm not doing documentation today

Today was really quite easy, meaning tomorrow is probably going to be the ramping up point. However... FIRST! I got first for part 1! I am exhilarated! I just saw it and thought "What if I did it manually?"

And so I did.

After that however, I had to code. Part 2 was easy enough. Part 3 however, I kept getting an error. It took me about 30 minutes to actually find the error... It was to do with the fact that ```abc``` and
```abcd``` would both eventually get ```abcdefg``` as a word they could make. The slight problem is that this is not a unique word both times. So I had to quickly come up with a janky way to get rid of any
duplicates.

# Day 8

... ahh... This day kicked my behind, my hatred for geometry has once again caught up with me.

My initial code was... certainly something to behold. Turns out a better solution was incredibly easy after looking at the Solution Spotlight for a bit. But my goodness I can't do geometry.

<p style="font-size:100px">I hate shapes, especially circles.<p>

Also, my part 3 is really inefficient. But I don't care, this took two hours longer than every other puzzle so far.

# Day 9

Overall, great fun, I do need to go to bed now however. It took a bit of time to think up what to do, but after the advice to "always make it a function", I think the code has gotten much better. My part 3 is a
bit slow, but it's fine overall.

I only ever encountered one problem, and that was that I always assumed that the scale number would be one digit... it was not.

# Day 10

I never thought it would be chess, but hey. I have WAY too many functions, that I'm going to clean up. I did it all, I used caching to speed up the end. It all works... hooray.

I feel as if there is a better method to do this rather than just brute forcing it, as it takes a minute or two to complete.

# Day 11

This is going quite well if my brain was actually functioning. For example, I just copied and pasted a line of code into the answer instead of my answer.

I can smell an optimisation problem coming up...

Okay, interestingly, part 3 already goes in ascending order and skips phase 1, so I actually just need to calculate how long phase 2 will go on for. So couldn't I just find the middle value they'll all get to
and then see how long it would take until they all reach that point?

Okay, I think it's something to do with the differences, I just don't know how. It's not in the differences, they look as if they follow a weird pattern until you look a bit closer and it just looks random...

I'm just going to keep using random formulae until I get the right answer at this point. There has to be something between the maximum, minimum and the middle number. Quartiles maybe?

I'm going to go out on a limb and say it's not standard deviation, or Variance, it's probably more to do with the sums of the numbers.

It might be something to do with the bottom and top halves of the list, as while they move erratically, they all need to move a certain number of spaces eventually. Nevermind, that can't be true, as the top
might be way out of whack compared to the bottom.

Turns out, if you get rid of all the negative ones, it works! Why? I don't know.

Okay, I just asked ChatGPT, and it has told me that apparently, I'm a dumb idiot who needs to go relearn how to do 1+1.
If 1 pass gets the columns which need more birds one extra bird. Then I just need to find out how many birds needs to be transferred down... It's easy...

Second part is incredibly slow, though I'm not sure how I would optimise it.

Wow I did terribly today. I'm now 6th (̥ ̥এ́ ̼ এ̥̀)̥̥ . Well, I guess I just have to do even better tomorrow, I should probably do some Euler or AOC for some practice, or finish that Codyssi thing.

# Day 12

Quite an easy quest honestly, it's just flood fill and then counting the flood fill. Also, learning pythons set operators was <b>really</b> useful, and it made this thing a breeze to do.

If you have the set ```{1, 2, 3, 4}``` and did ```{1, 2, 3, 4} - {1, 3, 5}``` you get  ```{2, 4}``` which is really useful when you need to get rid of all the barrels which have already been destroyed.

Placing bets now, tomorrow will be Dijkstra.

# Day 13

I was wrong, it was not Dijkstra. Unfortunately, as much as I would like to properly optimise my code, I have stuff to go and do. So it will have to stay inefficient for now. I would probably
make a custom mod function, which keeps subtracting the distance between the two input numbers until it reaches a negative. Then do the initial number + the leftover to get the final number the dial would turn
to.

# Day 14

I'm going to assume this pattern repeats at least some point right?

I'M SUCH AN IDIOT! It was such an easy puzzle and everything.

So, part 1 was quite easy, it was just setting up for part 2, which also ran incredibly quickly.

Part 3 was strange, I very quickly found the loop in the differences, having not at all read the hint like the dumb dumb I am. I then was unable to add for a while as the extraction of the middle was a bit
messed up.

And I thought that would be it for my troubles. For some reason, my answer was always too short and thus I immediately blamed my cycle checker. So I had the checker ensure it wasn't a false positive by checking
if the next number started another loop.

Then I decided that instead of seeing we have just repeated the exact same loop once, I checked if it had looped twice. Still, my answer was order of magnitude off of the correct answer. Why?

When the symbol shows up you are supposed to count every single active tile on the entire board, not just the ones inside the symbol. I spent an extra forty minutes on this error...

# Day 15

Dijkstra, I'm calling it now.

I was right, but I also can't code. Kept only reading the first number of the number of steps, which took me ages to spot. 
Now I just have to optimise this.

I don't even know+ why I use complex numbers at this point...

Drawing out all the walls in part 3 is intractable, so you really just have to use bounds to check it, which doesn't bode well for later.

I feel like the graph is way to big to do feasibly, so I can probably make this problem way shorter somehow, I can probably divide all of the distances by 7 or something.

Looking at the previous graphs, there are a whole load of thin corridors. (In hindsight what was I thinking)

Okay, just had a brilliant idea. If I always wall hug, then it will be the same distance due to the Manhattan distance's rules. So if I only make nodes next to walls, it should be fine?

Never mind, this also doesn't work as it's essentially just trying to draw all the walls again, but times 2.

What about just the corners? If I'm being speedy I would hug them anyway and I'll be going in straight lines as mentioned previously.

___


Alright, it's time to start searching stuff up...

Okay. So turns out I had a couple of simple spelling errors which caused fun combinations of idiocy. Using a little bit of AId, it appears that you can't just look at all the corners, but instead should find points of interest.

This means that I can hopefully do

```
########E########
#       ^       # 
#       |       # 
#       |       # 
S------ |       #
#################

```

Where you go upwards because the point shares a y coordinate with the End (or another wall in the actual code) and the point shares an x coordinate with the Start.


My original code used only the diagonals of each wall and the cardinals of the Start and End. Meaning I would have had to loop around the edge.

```
########E########
#       ^<------|# 
#               |# 
#               |# 
S-------------->|#
#################

or more likely

########E########
#|----->^        # 
#|               # 
#|               # 
S|               #
#################
```


Even with AId I still get things wrong. So, apparently, having the coordinates being adjacent cuts down the number of coordinates you need to look through significantly.
So I'm going to do that. I should probably get in the habit of ordering things when I first get them, instead of waiting and then having a billion min(a, b), max(a, b) everywhere.

Never make me do that again.

In other news. IT WAS DIJKSTRA, I CALLED IT! <p style="font-size: 8px">okay, I did say it was going to happen yesterday, but I'm a broken clock who's thinks it's going to be right twice a day, but then misses
even that low bar.</p>

Oh, I have only just realised this was Quest 15. Quest 15 last year (well, I actually did it a few months ago), absolutely destroyed me and had Dijkstra in it.

# Quest 16

This is the worst dev environment I have ever had to work with, it's small cramped and horrible. I need to finish setting up a proper environment on my new system.

Other than that, I don't even know how I got the last answer, I just decided to keep jumping and guessing until it worked.

# Quest 17

I want to explode, why is this so hard???

Every part of this kicked my butt, The first part was simple enough, it's just a for loop and a formula, but I kept switching between two methods of doing it, which certainly didn't help

The second was a pain because due to how circles work, it's not just a normal flood fill. I also had the problem of NOT READING THE QUESTION and thus causing me to not realise I stop once you hit the edges. So I set up loads of edge cases to ensure that I would correctly count the squares even if it reached the boundary. Which wasted time.

Now the third part I've had to have a long, hard think about, but thanks to the line of nines in the input, I had an idea.

I need to create a loop, thus the line must go through the middle line below the Volcano, as such take every single shortest distance between the start the middle line.

From there, for each part of the middle line we managed to get to, we check whether the line comes from the left or the right, we then temporarily put a river of "lava" on the side of the middle line we came from.

This forces the line to go around the other side and thus complete the loop.

It's still not working however, for some reason it works for two inputs, but generates an extra shorter path for the third input. Why? I don't know, but it's also messing up the proper puzzle input.

So, I may have found my problem. Sometimes, it's probably easier to double back to the left, before then swerving to the right and then returning to the start. My line was a bit too close so the program wouldn't like it.

FINALLY! I see I found the error it was the line thing above, strangely, it always seems to be the second answer which works, not the first. This is a very large error, but I have to wake up tomorrow, and it's stupid o'clock again, so it's a bug I will fix later (translation: Never).

# Quest 18

Thank goodness it was a good one for me today. I really enjoyed this puzzle actually (maybe because it wasn't graph traversal).

There's not much to say about it, other than for the final part, I had a sequence that only activated one free branch and then did the usual checking energy, but I didn't stop the energy if it was less than the thickness.
This showed me how each free branch contributed to the overall final score, you then take this and set all the positive values to 1 and negative values to 0, this gives you the perfect sequence.