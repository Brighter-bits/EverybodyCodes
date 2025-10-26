Parts = ["everybody_codes_e2_q02_p1.txt", "everybody_codes_e2_q02_p2.txt", "everybody_codes_e2_q02_p3.txt"]
BOLT = ["R", "G", "B"]
import os

def Solve(part):
    with open(Parts[part-1]) as f:
        inp = f.readline().replace("\n", "")
        o = inp
        count = 0
        if part == 1:
            while len(inp) != 0:
                new = inp.lstrip(BOLT[count%len(BOLT)])
                inp = new
                inp = inp[1:]
                count += 1
        elif part == 2 or part == 3:
                from collections import deque
                ticker = False
                from itertools import islice
                inp = deque(''.join([inp for a in range(100 if part == 2 else 100000)]))
                Fhalf = deque(islice(inp, int(len(inp)/2)+1))
                Storage = deque(islice(inp, int(len(inp)/2)+1, len(inp)))
                os.system("cls")
                while len(Fhalf) != 0:
                    if (len(Fhalf)+len(Storage)) % 2 == 0 and Fhalf[0] == BOLT[count%len(BOLT)]:
                        try:
                            ticker = False
                            del Fhalf[-1]
                            try:
                                Fhalf.append(Storage.popleft())
                            except:
                                pass
                        except:
                            raise ValueError("NOOO")
                    del Fhalf[0]
                    if ticker:
                        ticker = False
                        try:
                            Fhalf.append(Storage.popleft())
                        except:
                            pass
                    else:
                        ticker = True
                    count += 1

                print(count)

Solve(3)
