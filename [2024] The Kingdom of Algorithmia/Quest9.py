import math
Parts = ["everybody_codes_e2024_q09_p1.txt", "everybody_codes_e2024_q09_p2.txt", "everybody_codes_e2024_q09_p3.txt"]

def solve(part):
    with open(Parts[part], "r") as f:
        bugs = [[1, 3, 5, 10], [1, 3, 5, 10, 15, 16, 20, 24, 25, 30], [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]][part]
        sparks = list(map(lambda x: int(x.replace("\n", "")), f.readlines()))
        total = 0
        highest = max(sparks)
        dp = [float('inf')] * (highest+1) # This is an array containing the best ways to make certain numbers
        dp[0] = 0 # To make zero, you need only zero
        for i in range(1, highest + 1): # For every number up to the target, including the target itself
            for insect in bugs:
                if i >= insect and dp[i-insect] != float('inf'): # If the number we're trying to make is larger than a possible stamp and we could add the insect to a previous sum
                    dp[i] = min(dp[i], dp[i-insect]+1) # For the new number, which is smaller, the old smallest method, or the number it took to get a previous sum plus the new insect?
        for Spark in sparks:
            if part == 2:
                possibilities = []
                if Spark % 2 == 0:
                    for i in range(int(Spark/2)-50, int(Spark/2)+50): # Possibilities have a max range of 100, as such they can be only 50 either side of the midpoint between 0 and the number
                        if abs(Spark - i - i) > 100:
                            raise ValueError
                        possibilities.append(dp[i] + dp[Spark-i])
                else:
                    for i in range(math.ceil(Spark/2)-50, math.floor(Spark/2)+50):
                        if abs(Spark - i - i) > 100:
                            raise ValueError
                        possibilities.append(dp[i] + dp[Spark-i])
                total += min(possibilities)
            else:
                total += dp[Spark]


    print(total)

for i in range(3):
    solve(i)

    #     dots = len(bugs) - 1
    #     while True:
    #         if Spark >= bugs[dots]:
    #             Spark -= bugs[dots]
    #             total += 1
    #         elif dots == 0:
    #             total += Spark
    #             break
    #         else:
    #             dots -= 1