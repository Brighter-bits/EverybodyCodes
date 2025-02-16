Parts = ["everybody_codes_e2024_q06_p1.txt", "everybody_codes_e2024_q06_p2.txt", "everybody_codes_e2024_q06_p3.txt"]

def Shortest(Target):
    global ShortestParent
    Truepath = []
    node = Target
    while node != None:
        Truepath.append(node)
        node = ShortestParent[node]
    Truepath.reverse()
    return Truepath

def Solve():
    global ShortestParent
    for part in range(3):
        with open(Parts[part], "r") as f:
            branches = list(map(lambda x: x.replace("\n", "").split(":"), f.readlines()))
            Paths = {}
            AppleID = 0
            for branch in branches:
                if branch[0] == "BUG" or branch[0] == "ANT":
                    continue
                pathways = branch[1].split(",")
                pathdict = dict()
                for path in pathways:
                    if path == "BUG" or path == "ANT":
                        continue
                    if path == "@":
                        path = "@"+str(AppleID)
                        AppleID += 1
                    pathdict[path] = 1
                Paths[branch[0]] = pathdict
            Paths["@"] = {}

            Distances = {node: float("infinity") for node in Paths}
            Distances["RR"] = 0
            import heapq
            queue = [("RR", 0)]
            ShortestParent = {node: None for node in Paths}
            while queue:
                CNode, CDistance = heapq.heappop(queue)
                if CDistance > Distances[CNode]:
                    continue
                if CNode not in Paths:
                    Paths[CNode] = {}
                for adjacent, weight in Paths[CNode].items():
                    distance = CDistance + weight
                    if adjacent not in Distances:
                        Distances[adjacent] = float("infinity")
                    if distance < Distances[adjacent]:
                        Distances[adjacent] = distance
                        ShortestParent[adjacent] = CNode
                        heapq.heappush(queue, (adjacent, distance))

        possibilities = []
        for i in range(AppleID):
            possibilities.append(Shortest("@" + str(i)))
        key = lambda x: len(x)
        possibilities.sort(key=key)
        answer = ""
        for i in range(0, len(possibilities), 2):
            if len(possibilities[i]) != len(possibilities[i+1]):
                answer = possibilities[i]
                break
        output = ""
        if part == 0:
            output = ''.join(answer)
            print(output[:-1])
        else:
            for part in answer:
                output += part[0]
            print(output)

Solve()