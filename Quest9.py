Parts = ["everybody_codes_e2024_q09_p1.txt", "everybody_codes_e2024_q09_p2.txt", "everybody_codes_e2024_q09_p3.txt"]

def Old()
with open("Q9B.txt", "r") as f:
    # bugs = [3, 5, 10]
    bugs = [3, 5, 10, 15, 16, 20, 24, 25, 30]
    sparks = list(map(lambda x: int(x.replace("\n", "")), f.readlines()))
    total = 0
    for Spark in sparks:
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
        dp = [float('int')] * (Spark+1)
        old = [[] for a in range(Spark+1)]
        for i in range(1, Spark + 1):
            for 

    print(total)

