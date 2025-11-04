parts = ["everybody_codes_e1_q03_p1.txt", "everybody_codes_e1_q03_p2.txt", "everybody_codes_e1_q03_p3.txt"]
import numpy as np
linear = [[], []]

def Modder(Start):
    for i in range(len(linear[1])):
        if (Start-linear[0][i])%linear[1][i] != 0:
            return 0
    print(Start)
    return Start

# def GPUModder(Start):


with open(parts[1], "r") as f:
    inp = list(map(lambda x: x.split(), list(map(lambda x: x.replace("=", "").replace("x", "").replace("y", "").replace("\n", ""), f.readlines()))))
    results = []

    for snail in inp:
        x = int(snail[0]) - 1
        y = int(snail[1]) - 1
        track = x + y + 1
        # if type(linear) != np.ndarray:
        #     linear = np.array([y, track])
        # else:
        #     cache = np.array([y, track])
        #     linear = np.vstack([linear, cache])
        #     print(linear)
        linear[0].append(y); linear[1].append(track)
        x = ((x+100) % track) + 1
        y = ((y-100) % track) + 1
        results.append(x + (y * 100))
    print(sum(results))

    # rightArray = np.array([linear[0][0]])
    # for i in range(1, len(linear)):
    #     rightArray = np.hstack([rightArray, linear[i][0]])
    # leftArray = np.array([1, -linear[1][0]])
    # for i in range(1, len(linear)):
    #     leftArray = np.vstack([leftArray, [1, -linear[i][1]]])
    # answers = []
    # for i in range(len(rightArray)-1):
    #     for j in range(i+1, len(rightArray)):
    #         try:
    #             answers.append(np.matmul(np.linalg.inv([leftArray[i], leftArray[j]]), np.array([rightArray[i], rightArray[j]])))
    #         except:
    #             pass
    # xs = []
    # ys = []
    # import math
    # for i in answers:
    #     xs.append(math.ceil(abs(i[0])))
    #     ys.append(math.ceil(abs(i[1])))
    # print(math.prod(xs))
    # print(math.prod(ys))
    from multiprocessing import Pool
    counter = 1
    if __name__ == '__main__':
        with Pool(6) as p:
            for res in p.imap(Modder, range(int(9*(10**10)), 10**11), chunksize=1000):
                if res > 0:
                    print(res)
                    exit()

    # counter=int(9.8*(10**11))
    # while True:
    #     if Modder(counter):
    #         print(counter)
    #         break
    #     counter += 1
            