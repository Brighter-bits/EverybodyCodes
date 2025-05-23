Parts = ["everybody_codes_e2024_q14_p1.txt", "everybody_codes_e2024_q14_p2.txt", "everybody_codes_e2024_q14_p3.txt"]
# from collections import deque
# class Tensor():
#     def __init__(self):
#         self.values = deque()
#         self.values.append(deque())
#         self.values[0].append(deque())
#         self.values[0][0].append(False)
#         self.pointer = (0, 0, 0)
    
#     def __repr__(self):
#         return str(self.values)                      ################ Horrible Code, Ignore this ##########################

#     def Up(self, val):
#         for i in range(val):
#             try:
#                 self.values[self.pointer[0]][self.pointer[1]][self.pointer[2]] = True
#             except:
#                 self.values[self.pointer[0]].append(deque())
#                 for j in range(len(self.values[0][0])):
#                     self.values[self.pointer[0]][-1].append(False)
#                 self.values[self.pointer[0]][self.pointer[1]][self.pointer[2]] = True
#             self.pointer = (self.pointer[0], self.pointer[1] + 1, self.pointer[2])
    
                


def Solve1(): # For part one, only the highest point is needed
    with open(Parts[0], "r") as f:
        plant = list(map(lambda x: x.split(","), f.readlines()))[0] # Normalise the input
        highest = 0
        plant = [piece for piece in plant if "U" in piece or "D" in piece] # Extract all the instruction which go up or down
        height = 0
        for piece in plant:
            if "U" in piece:
                height += int(piece[1:])
            else:
                height -= int(piece[1:])
            if height > highest:
                highest = height
        print(highest)


def Solve(part):
    with open(Parts[part-1], "r") as f:
        plant = list(map(lambda x: x.split(","), f.readlines()))
        Area = dict()
        leaves = []
        for piece in plant:
            pointer = [0, 0, 0]
            for segment in piece:
                match segment[0]:
                    case "U":
                        for i in range(int(segment[1:])):
                            pointer[1] += 1
                            Area[tuple(pointer)] = True
                    case "D":
                        for i in range(int(segment[1:])):
                            pointer[1] -= 1
                            Area[tuple(pointer)] = True
                    case "L":
                        for i in range(int(segment[1:])):
                            pointer[0] -= 1
                            Area[tuple(pointer)] = True
                    case "R":
                        for i in range(int(segment[1:])):
                            pointer[0] += 1
                            Area[tuple(pointer)] = True
                    case "F":
                        for i in range(int(segment[1:])):
                            pointer[2] += 1
                            Area[tuple(pointer)] = True
                    case "B":
                        for i in range(int(segment[1:])):
                            pointer[2] -= 1
                            Area[tuple(pointer)] = True
            if part == 3:
                leaves.append((pointer[0], pointer[1], pointer[2]))
        if part == 2:
            print(len(list(Area.keys())))
        else:
            GraphDict = dict()
            for segment in Area.keys():
                GraphDict[segment] = []
                if (segment[0]+1, segment[1], segment[2]) in Area:
                    GraphDict[segment].append(((segment[0]+1, segment[1], segment[2]), 1))
                if (segment[0]-1, segment[1], segment[2]) in Area:
                    GraphDict[segment].append(((segment[0]-1, segment[1], segment[2]), 1))
                if (segment[0], segment[1]+1, segment[2]) in Area:
                    GraphDict[segment].append(((segment[0], segment[1]+1, segment[2]), 1))
                if (segment[0], segment[1]-1, segment[2]) in Area:
                    GraphDict[segment].append(((segment[0], segment[1]-1, segment[2]), 1))
                if (segment[0], segment[1], segment[2]+1) in Area:
                    GraphDict[segment].append(((segment[0], segment[1], segment[2]+1), 1))
                if (segment[0], segment[1], segment[2]-1) in Area:
                    GraphDict[segment].append(((segment[0], segment[1], segment[2]-1), 1))
            pointer = (0, 1, 0)
            Shortest = dict()
            import heapq
            while pointer in GraphDict:
                Distances = {node: float("infinity") for node in GraphDict.keys()}
                Distances[pointer] = 0
                queue = [(pointer, 0)]
                while queue:
                    CNode, CDistance = heapq.heappop(queue)
                    if CDistance > Distances[CNode]:
                        continue
                    for adjacent, weight in GraphDict[CNode]:
                        distance = CDistance + weight
                        if distance < Distances[adjacent]:
                            Distances[adjacent] = distance
                            heapq.heappush(queue, (adjacent, distance))
                Shortest[pointer] = Distances
                pointer = (0, pointer[1]+1, 0)
            pointer = (0, 1, 0)
            murk = []
            while pointer in GraphDict:
                total = 0
                for leaf in leaves:
                    total += Shortest[pointer][leaf]
                murk.append(total)
                pointer = (0, pointer[1]+1, 0)
            print(min(murk))
                




Solve(3)