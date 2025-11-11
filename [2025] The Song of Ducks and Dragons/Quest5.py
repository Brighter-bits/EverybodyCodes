Parts = ["everybody_codes_e2025_q05_p1.txt", "everybody_codes_e2025_q05_p2.txt", "everybody_codes_e2025_q05_p3.txt"]
from collections import defaultdict
class leaf:
    left = -1
    right = -1
    middle = -1
    down = -1
    FirstOrder = -1
    SecondOrder = []
    ThirdOrder = -1
    def __init__(self, id=-1):
        self.ThirdOrder = id+1
    def Attach(self, num):
        if self.middle == -1:
            self.middle = num
        elif num < self.middle and self.left == -1:
            self.left = num
        elif num > self.middle and self.right == -1:
            self.right = num
        elif self.down == -1:
            self.down = leaf()
            self.down.Attach(num)
        else:
            self.down.Attach(num)
    def Reveal(self):
        if self.down == -1:
            return str(self.middle)
        else:
            return str(self.middle) + str(self.down.Reveal())
    def Sideways(self):
        answer = ""
        if self.left != -1:
            answer += str(self.left)
        answer += str(self.middle)
        if self.right != -1:
            answer += str(self.right)
        if self.down == -1:
            return answer
        else:
            return answer + "," + self.down.Sideways()

def compare(a:leaf, b:leaf):
    counter = 0
    AOrder = list(map(int, a.SecondOrder.split(",")))
    BOrder = list(map(int, b.SecondOrder.split(",")))
    while True:
        try:
            if AOrder[counter] > BOrder[counter]:
                return [a, b]
            elif AOrder[counter] < BOrder[counter]:
                return [b, a]
            counter += 1

        except:
            return -1

def Solve1n2(part):
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.split(":")[1].replace("\n", "").split(","), f.readlines()))
        for i in range(len(inp)):
            inp[i] = list(map(int, inp[i]))
        boneyboys:list[leaf] = []
        for i in range(len(inp)):
            Start = leaf(i)
            for i in inp[i]:
                Start.Attach(i)
            boneyboys.append(Start)
        if part == 1:
            print(boneyboys[0].Reveal())
        else:
            boneyboys = list(map(lambda x: int(x.Reveal()), boneyboys))
            print(int(max(boneyboys)) - int(min(boneyboys)))


def Solve3():
    with open(Parts[2]) as f:
        inp = list(map(lambda x: x.split(":")[1].replace("\n", "").split(","), f.readlines()))
        for i in range(len(inp)):
            inp[i] = list(map(int, inp[i]))
        boneyboys:list[leaf] = []
        for i in range(len(inp)):
            Start = leaf(i)
            for i in inp[i]:
                Start.Attach(i)
            Start.FirstOrder = Start.Reveal()
            Start.SecondOrder = Start.Sideways()
            boneyboys.append(Start)
        FinalDict = defaultdict(list)
        for bone in boneyboys:
            FinalDict[bone.FirstOrder].append(bone)
        results = sorted(list(FinalDict.items()), reverse=True, key=lambda x: int(x[0]))
        for i in range(len(results)):
            if len(results[i][1]) > 1:
                answer = ""
                if len(results[i][1]) == 2:
                    answer = compare(results[i][1][0], results[i][1][1])
                    if answer == -1:
                        answer = sorted(results[i][1],reverse=True, key= lambda x: x.ThirdOrder)
                else: # If statement gore
                    A, B, C = results[i][1][0], results[i][1][1], results[i][1][2]
                    if compare(A, B) == -1:
                        if compare(B, C) == -1:
                            answer = sorted([A, B, C], reverse=True, key=lambda x: x.ThirdOrder)
                        elif compare(B, C) == [C, B]:
                            answer = [C]
                            answer.extend(sorted([A, B], reverse=True, key=lambda x: x.ThirdOrder))
                        elif compare(B, C) == [B, C]:
                            answer = sorted([A, B], reverse=True, key=lambda x: x.ThirdOrder)
                            answer.append(C)
                    elif compare(A, B) == [A, B]:
                        if compare(B, C) == -1:
                            answer = [A]
                            answer.extend(sorted([B, C], reverse=True, key=lambda x: x.ThirdOrder))
                        elif compare(B, C) == [B, C]:
                            answer = [A, B, C]
                        elif compare(B, C) == [C, B]:
                            if compare(A, C) == -1:
                                answer = sorted([A, C], reverse=True, key=lambda x: x.ThirdOrder)
                                answer.append(B)
                            elif compare(A, C) == [A, C]:
                                answer = [A, C, B]
                            elif compare(C, A) == [C, A]:
                                answer = [C, A, B]
                    elif compare(A, B) == [B, A]:
                        if compare(A, C) == -1:
                            answer = [B]
                            answer.extend(sorted([A, C], reverse=True, key=lambda x: x.ThirdOrder))
                        elif compare(A, C) == [A, C]:
                            answer = [B, A, C]
                        elif compare(A, C) == [C, A]:
                            if compare(B, C) == -1:
                                answer = sorted([B, C], reverse=True, key=lambda x: x.ThirdOrder)
                                answer.append(A)
                            elif compare(B, C) == [B, C]:
                                answer = [B, C, A]
                            elif compare(B, C) == [C, B]:
                                answer = [C, B, A]
                results[i] = (results[i][0], answer)
        checksum = 0
        counter = 1
        for i in range(len(results)):
            if len(results[i][1]) == 1:
                checksum += (counter) * results[i][1][0].ThirdOrder
            if len(results[i][1]) == 2:
                checksum += (counter) * results[i][1][0].ThirdOrder
                counter += 1
                checksum += (counter) * results[i][1][1].ThirdOrder
            if len(results[i][1]) == 3:
                checksum += (counter) * results[i][1][0].ThirdOrder
                counter += 1
                checksum += (counter) * results[i][1][1].ThirdOrder
                counter += 1
                checksum += (counter) * results[i][1][2].ThirdOrder
            counter += 1
        print(checksum)

        

Solve1n2(1)
Solve1n2(2)
Solve3()

