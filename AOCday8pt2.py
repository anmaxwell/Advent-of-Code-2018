#%%

class Node:
    'Common base class for all nodes'

    def __init__(self, name):
        self.name = name
        self.metadata = []
        self.children = []
        self.totalMeta = 0
        
    def addMeta(self, value):
        self.metadata.append(int(value))
        
    def addChild(self,childNode):
        self.children.append(childNode)
        
    def getChildAtPos(self, value):
        return self.children[value]
    
    def sumMeta(self, value):
        self.totalMeta+=int(value)
      
    def __repr__(self):
        return "Node:{}, children:{}, metadata: {}, summeta: {}".format(self.name, len(self.children), 
                     self.metadata, self.totalMeta )


def createInput():

    with open('/Users/account1/Desktop/trees/day8input.txt', 'r') as myfile:
        filecntent = myfile.readlines()
    inputlist = filecntent[0].split()
    
    return inputlist



def createNode(myList, pointer):
    theNode = Node(pointer)
    
    noChild = int(myList[pointer])
    noMeta = int(myList[pointer+1])
    
    pointer+=2
    
    for i in range(noChild):
        newNode, pointer = createNode(myList, pointer)
        theNode.addChild(newNode)
#        print(newNode, pointer)
    
    metaSlice = myList[pointer:(pointer+noMeta)]
    
    for item in metaSlice:
        theNode.addMeta(item)
        theNode.sumMeta(item)
        pointer+=1
        
    return theNode, pointer

def returnValue(node):
    
    value = 0
    
    if len(node.children) == 0:
        value = node.totalMeta
        
    else:
        for item in node.metadata:
            if item <= len(node.children):
                cnode = node.children[item-1]
                value += returnValue(cnode)     
    
    return value


myList = createInput()
rootNode, pointer = createNode(myList, 0)    
totalsum = returnValue(rootNode)
print(totalsum)