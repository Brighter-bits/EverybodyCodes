# Quest 1... Again

So, I'm going to have to sort these into folders properly later. This puzzle seems like a tree puzzle, with each child being the next peg. Easy enough

Easy enough sure, if I realised that the asterisks were the dropping slots, not the dots...

Turns out I was checking the x coordinate against the height of the machine, but it's fine now. Part 2 meanwhile, looks like I can just brute force it, though I feel like Part 3 I will need to do some caching.
Wait... Part 3 may actually be brutable. I did a bit of research and found "The Hungarian Algorithm", which makes sense until it starts trying to uncover edge cases. So while this would probably help me, I
don't want to have to implement it...

Turn out there is a function in itertools called product. Which is essentially just a fancy nested for loop... Nevermind that won't work...

Product gives you every single possible combination, including having the same element multiple times. Permutations does not allow that and is what I actually want.