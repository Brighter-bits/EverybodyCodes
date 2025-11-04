# This is going to suck, I have to learn what a tree is
parts = ["everybody_codes_e1_q02_p1.txt", "everybody_codes_e1_q02_p2.txt", "everybody_codes_e1_q02_p3.txt"]

import sys
sys.setrecursionlimit(15000)

class TreeNode:
    def __init__(self, value, letter, id):
        self.value = value
        self.letter = letter
        self.id = id
        self.left = None
        self.right = None
    
    def insert(self, NValue, NLetter, Nid):
        if NValue < self.value:
            if self.left == None:
                self.left = TreeNode(NValue, NLetter, Nid)
            else:
                self.left.insert(NValue, NLetter, Nid)
        elif self.value < NValue:
            if self.right == None:
                self.right = TreeNode(NValue, NLetter, Nid)
            else:
                self.right.insert(NValue, NLetter, Nid)
        else:
            raise Exception("IDK????")
        
    
    def Swap(self, id, side):
        if self.id == id:
            if side == 0:
                self.value = RightDict[id][0]
                self.letter = RightDict[id][1]
            else:
                self.value = LeftDict[id][0]
                self.letter = LeftDict[id][1]
        else:
            if self.left != None:
                self.left.Swap(id, side)
            if self.right != None:
                self.right.Swap(id, side)
            

    def Copy(self, id, side):
        global LeftCache
        global RightCache
        if self.id == id:
            if side == 0:
                LeftCache.append(self)
            else:
                RightCache.append(self)
        if self.left != None:
            self.left.Copy(id, side)
        if self.right != None:
            self.right.Copy(id, side)
    
    def Paste(self, id, side, parent):
        global LeftCache
        global RightCache
        if self.id == id:
            if side == 0:
                if len(LeftCache) == 2:
                    if self == parent.left:
                        if parent.left == LeftCache[0]:
                            parent.left = LeftCache[1]
                        else:
                            parent.left = LeftCache[0]
                    else:
                        if parent.right == LeftCache[0]:
                            parent.right = LeftCache[1]
                        else:
                            parent.right = LeftCache[0]
                else:
                    if self == parent.left:
                        if parent.left == RightCache[0]:
                            parent.left = RightCache[1]
                        else:
                            parent.left = RightCache[0]
                    else:
                        if parent.right == RightCache[0]:
                            parent.right = RightCache[1]
                        else:
                            parent.right = RightCache[0]
            else:
                if len(RightCache) == 2:
                    if self == parent.left:
                        if parent.left == RightCache[0]:
                            parent.left = RightCache[1]
                        else:
                            parent.left = RightCache[0]
                    else:
                        if parent.right == RightCache[0]:
                            parent.right = RightCache[1]
                        else:
                            parent.right = RightCache[0]
                else:
                    if self == parent.left:
                        if parent.left == LeftCache[0]:
                            parent.left = LeftCache[1]
                        else:
                            parent.left = LeftCache[0]
                    else:
                        if parent.right == LeftCache[0]:
                            parent.right = LeftCache[1]
                        else:
                            parent.right = LeftCache[0]

        if self.left != None:
            self.left.Paste(id, side, self)
        if self.right != None:
            self.right.Paste(id, side, self)

    def __repr__(self):
        return (self.value, self.letter, self.id)

LeftDict = dict()
RightDict = dict()
def Solve(part):
    with open(parts[part-1], "r") as f:
        global LeftCache, RightCache, LeftDict, RightDict
        LeftDict = dict()
        RightDict = dict()

        inp = list(map(lambda x: x.split(), list(map(lambda x: x.replace("\n", ""), f.readlines()))))
        StartLeft = None
        StartRight = None
        for i in range(len(inp)):
            inp[i][1] = int(inp[i][1].replace("id=", ""))
            if inp[i][0] == "ADD":
                inp[i][3] = tuple(inp[i][3].replace("right=[", "").replace("]", "").split(","))
                inp[i][2] = tuple(inp[i][2].replace("left=[", "").replace("]", "").split(","))
                if StartLeft == None:
                    StartLeft = TreeNode(int(inp[i][2][0]), str(inp[i][2][1]), inp[i][1])
                    LeftDict[inp[i][1]] = (int(inp[i][2][0]), str(inp[i][2][1]), inp[i][1])
                else:
                    StartLeft.insert(int(inp[i][2][0]), str(inp[i][2][1]), inp[i][1])
                    LeftDict[inp[i][1]] = (int(inp[i][2][0]), str(inp[i][2][1]), inp[i][1])
                        
                        
                
                if StartRight == None:
                    StartRight = TreeNode(int(inp[i][3][0]), str(inp[i][3][1]), inp[i][1])
                    RightDict[inp[i][1]] = (int(inp[i][3][0]), str(inp[i][3][1]), inp[i][1])
                else:
                    StartRight.insert(int(inp[i][3][0]), str(inp[i][3][1]), inp[i][1])
                    RightDict[inp[i][1]] = (int(inp[i][3][0]), str(inp[i][3][1]), inp[i][1])
            else:
                if part == 2:
                    StartLeft.Swap(inp[i][1], 0)
                    StartRight.Swap(inp[i][1], 1)
                    
                    cache = LeftDict[inp[i][1]]
                    LeftDict[inp[i][1]] = RightDict[inp[i][1]]
                    RightDict[inp[i][1]] = cache
                else:
                    LeftCache = []
                    RightCache = []
                    StartLeft.Copy(inp[i][1], 0)
                    StartRight.Copy(inp[i][1], 1)
                    if inp[i][1] == 1:
                        StartLeft = RightCache[0]
                        StartRight = LeftCache[0]
                    else:
                        StartLeft.Paste(inp[i][1], 0, None)
                        StartRight.Paste(inp[i][1], 1, None)

                    
                    
        
        layertotals = [[], []]
        LayerWords = [[], []]
        def Search(CNode:TreeNode, layer:int, side):
            if CNode == None:
                return
            if len(layertotals[side]) <= layer:
                layertotals[side].append(1)
            else:
                layertotals[side][layer] += 1

            if len(LayerWords[side]) <= layer:
                LayerWords[side].append(CNode.letter)
            else:
                LayerWords[side][layer] += CNode.letter

            Search(CNode.left, layer + 1, side)
            Search(CNode.right, layer + 1, side)
        

        Search(StartLeft, 0, 0)
        Search(StartRight, 0, 1)
        print(layertotals[0], layertotals[1])
        print(LayerWords[0], LayerWords[1])
        print(str(max(LayerWords[0], key=len))+str(max(LayerWords[1], key=len)))
        
            
for i in range(1, 4):
    Solve(i)



                    



