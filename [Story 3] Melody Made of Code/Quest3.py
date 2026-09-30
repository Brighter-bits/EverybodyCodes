import os
from pathlib import Path
os.chdir(Path(__file__).parent)
Parts = ["everybody_codes_e3_q03_p1.txt", "everybody_codes_e3_q03_p2.txt", "everybody_codes_e3_q03_p3.txt", "everybody_codes_e3_q03_p4.txt"]
import sys
sys.setrecursionlimit(100000000)
class Node: # A node class which holds all the info, arrays work as such: [Colour, Shape, Pointer to the Node]
    def __init__(self, _id, _base, _leftSocket, _rightSocket, _data):
        self.id = _id
        self.base = _base.split(" ")
        self.leftSocket = _leftSocket.split(" ")
        self.rightSocket = _rightSocket.split(" ")
        self.data = _data

def BranchSearch1(newNode:Node, CNode:Node):
    running = True
    if type(CNode.leftSocket) != list and running: # If the leftsocket has been filled in, then go down it
        running = BranchSearch1(newNode, CNode.leftSocket)
    else:
        if CNode.leftSocket == newNode.base: # If there's a space and it fits, put it in and then set running to false, stopping any extra insertions.
            CNode.leftSocket = newNode
            return False
    
    if not running:
        return False

    if type(CNode.rightSocket) != list:
        running = BranchSearch1(newNode, CNode.rightSocket)
    else:
        if CNode.rightSocket == newNode.base:
            CNode.rightSocket = newNode
            return False
    
    if not running:
        return False

    return True

def BranchSearch2(newNode:Node, CNode:Node):
    running = True
    if type(CNode.leftSocket) != list and running:
        running = BranchSearch2(newNode, CNode.leftSocket)
    else:
        if CNode.leftSocket[0] == newNode.base[0] or CNode.leftSocket[1] == newNode.base[1]: # Same thing as earlier, but this time, it can be either the shape or the colour
            CNode.leftSocket = newNode
            return False
    
    if not running:
        return False

    if type(CNode.rightSocket) != list:
        running = BranchSearch2(newNode, CNode.rightSocket)
    else:
        if CNode.rightSocket[0] == newNode.base[0] or CNode.rightSocket[1] == newNode.base[1]:
            CNode.rightSocket = newNode
            return False
    
    if not running:
        return False

    return True

outputList = []
NodeList: list[Node] = []


# def BranchSearch3(newNode:Node, CNode:Node, right = True, left = True, memory = 0):
#     global NodeList
#     running = True

#     if left:
#         if CNode.leftSocket[0] == newNode.base[0] and CNode.leftSocket[1] == newNode.base[1] and not (len(CNode.leftSocket) > 2 and CNode.leftSocket[0] == CNode.leftSocket[2].base[0] and CNode.leftSocket[1] == CNode.leftSocket[2].base[1]):
#             if len(CNode.leftSocket) > 2:
#                 orphanNode = CNode.leftSocket[2]
#                 CNode.leftSocket[2] = newNode
#                 if len(newNode.base) > 2:
#                     newNode.base[2] = CNode
#                 else:
#                     newNode.base.append(CNode)
#                 BranchSearch3(orphanNode, orphanNode.base[2], left=False)
#             else:
#                 CNode.leftSocket.append(newNode)
#                 if len(newNode.base) > 2:
#                     newNode.base[2] = CNode
#                 else:
#                     newNode.base.append(CNode)
#             return False
#         else:
#             if len(CNode.leftSocket) > 2:
#                 running = BranchSearch3(newNode, CNode.leftSocket[2])
#             else:
#                 if CNode.leftSocket[0] == newNode.base[0] or CNode.leftSocket[1] == newNode.base[1]:
#                     CNode.leftSocket.append(newNode)
#                     if len(newNode.base) > 2:
#                         newNode.base[2] = CNode
#                     else:
#                         newNode.base.append(CNode)
#                     return False
    
#     if not running:
#         return False

#     if right:
#         if CNode.rightSocket[0] == newNode.base[0] and CNode.rightSocket[1] == newNode.base[1] and not (len(CNode.rightSocket) > 2 and CNode.rightSocket[0] == CNode.rightSocket[2].base[0] and CNode.rightSocket[1] == CNode.rightSocket[2].base[1]):
#             if len(CNode.rightSocket) > 2:
#                 orphanNode = CNode.rightSocket[2]
#                 CNode.rightSocket[2] = newNode
#                 if len(newNode.base) > 2:
#                     newNode.base[2] = CNode
#                 else:
#                     newNode.base.append(CNode)
                
#                 newBase = orphanNode.base[2]
#                 while True:
#                     if len(newBase.base) == 2: # If at root node
#                         BranchSearch3(orphanNode, newBase)
#                         break
#                     elif newBase == newBase.base[2].leftSocket[2]: # If this base is the left of it's parent, then we go to the right of the new base
#                         newBase = newBase.base[2]
#                         BranchSearch3(orphanNode, newBase, left = False)
#                         break
#                     else:
#                         newBase = newBase.base[2]

#             else:
#                 CNode.rightSocket.append(newNode)
#                 if len(newNode.base) > 2:
#                     newNode.base[2] = CNode
#                 else:
#                     newNode.base.append(CNode)
#             return False
#         else:
#             if len(CNode.rightSocket) > 2:
#                 running = BranchSearch3(newNode, CNode.rightSocket[2])
#             else:
#                 if CNode.rightSocket[0] == newNode.base[0] or CNode.rightSocket[1] == newNode.base[1]:
#                     CNode.rightSocket.append(newNode)
#                     if len(newNode.base) > 2:
#                         newNode.base[2] = CNode
#                     else:
#                         newNode.base.append(CNode)
#                     return False
    
#     if not running:
#         return False

#     if len(newNode.base) > 2: # This means we have reached the end for the first time and need to loop back somewhere
#         print(memory)
#         newBase = CNode.base[2]
#         if CNode == newBase.leftSocket[2]:
#             BranchSearch3(newNode, newBase, left = False, memory=memory+1)
#         else:
#             while True:
#                 if len(newBase.base) == 2: # If at root node
#                     BranchSearch3(newNode, newBase)
#                     break
#                 elif newBase == newBase.base[2].leftSocket[2]: # If this base is the left of it's parent, then we go to the right of the new base
#                     newBase = newBase.base[2]
#                     BranchSearch3(newNode, newBase, left = False, memory=memory+1)
#                     break
#                 else:
#                     newBase = newBase.base[2]


#     return True

def BranchSearch3(newNode: Node, CNode: Node):
    if CNode.leftSocket[:2] == newNode.base[:2]: # If strongly linked
        if len(CNode.leftSocket) > 2: # If the socket is filled
            if not (CNode.leftSocket[:2] == CNode.leftSocket[2].base[:2]): # And the current node is weak
                orphanNode = CNode.leftSocket[2] # Kick em out!
                CNode.leftSocket[2] = newNode
                if len(CNode.leftSocket[2].base) > 2:
                    CNode.leftSocket[2].base[2] = CNode
                else:
                    CNode.leftSocket[2].base.append(CNode)
                newNode = orphanNode
            else:
                newNode = BranchSearch3(newNode, CNode.leftSocket[2])
                if newNode is None:
                    return None
        else:
            CNode.leftSocket.append(newNode)
            newNode.base.append(CNode)
            return None
    elif len(CNode.leftSocket) > 2:
        newNode = BranchSearch3(newNode, CNode.leftSocket[2])
        if newNode is None:
            return None
    elif (newNode.base[0] == CNode.leftSocket[0]) or (newNode.base[1] == CNode.leftSocket[1]):
        CNode.leftSocket.append(newNode)
        newNode.base.append(CNode)
        return None
        
    if CNode.rightSocket[:2] == newNode.base[:2]:
        if len(CNode.rightSocket) > 2:
            if not (CNode.rightSocket[:2] == CNode.rightSocket[2].base[:2]):
                orphanNode = CNode.rightSocket[2]
                CNode.rightSocket[2] = newNode
                if len(CNode.rightSocket[2].base) > 2:
                    CNode.rightSocket[2].base[2] = CNode
                else:
                    CNode.rightSocket[2].base.append(CNode)
                newNode = orphanNode
            else:
                newNode = BranchSearch3(newNode, CNode.rightSocket[2])
                if newNode is None:
                    return None
        else:
            CNode.rightSocket.append(newNode)
            newNode.base.append(CNode)
            return None
    elif len(CNode.rightSocket) > 2:
        newNode = BranchSearch3(newNode, CNode.rightSocket[2])
        if newNode is None:
            return None
    elif (newNode.base[0] == CNode.rightSocket[0]) or (newNode.base[1] == CNode.rightSocket[1]):
        CNode.rightSocket.append(newNode)
        newNode.base.append(CNode)
        return None
    
    return newNode
    


def InOrder(CNode:Node): # An in order traversal which outputs what I need
    global outputList
    if type(CNode.leftSocket) != list:
        InOrder(CNode.leftSocket)

    outputList.append(CNode.id)

    if type(CNode.rightSocket) != list:
        InOrder(CNode.rightSocket)

def InOrder2(CNode:Node): # Same as previously, just now taking into account the third part's list structure.
    global outputList
    if len(CNode.leftSocket) > 2:
        InOrder2(CNode.leftSocket[2])

    outputList.append(CNode.id)

    if len(CNode.rightSocket) > 2:
        InOrder2(CNode.rightSocket[2])

def SongOutput(CNode:Node): # I can't believe it took checking my answer with someone else's code to realise that the Data part is in fact important. Oh... it's just the default song.
    if len(CNode.leftSocket) > 2:
        SongOutput(CNode.leftSocket[2])

    outputList.append(CNode.data)

    if len(CNode.rightSocket) > 2:
        SongOutput(CNode.rightSocket[2])



def Solve(part):
    global outputList, NodeList
    with open(Parts[part-1]) as f:
        inp = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        NodeList = []
        for line in inp:
            values = line.split(", ")
            values = list(map(lambda x: x.split("=")[1], values))
            NodeList.append(Node(*values))
        CNode = NodeList[0]
        if part == 1:
            for i in range(1, len(NodeList)):
                BranchSearch1(NodeList[i], CNode)
        elif part == 2:
            for i in range(1, len(NodeList)):
                BranchSearch2(NodeList[i], CNode)
        elif part == 3 or part == 4:
            for i in range(1, len(NodeList)):
                # print(f"Starting{i}")
                newNode = BranchSearch3(NodeList[i], CNode)
                while newNode != None:
                    newNode = BranchSearch3(newNode, CNode)
                         

        outputList = []
        if part <= 2:
            InOrder(CNode)
        elif part == 3:
            InOrder2(CNode)
        else:
            SongOutput(CNode)
            open("SongOutput.txt", "w").write("\n".join(outputList))
        total = 0
        if part != 4:
            for i in range(len(outputList)):
                total += (i+1)*int(outputList[i])
            print(total)
        
        
    



Solve(1) # Actual Part one and two
Solve(2)

Solve(3)
Solve(4)