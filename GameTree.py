class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.p1points = 0
        self.p2points = 0
        self.turnCount = 0

    def addChild(self, node):
        node.p1points = self.p1points
        node.p2points = self.p2points
        node.turnCount = self.turnCount + 1
        self.children.append(node)

    # Atļauj mums salīdzināt mūsu TreeNodes objektus ar == operatoru, šobrīd vēl neizmantoju
    # ,bet kad vajadzēs salīdzināt nodes, lai neveidotu liekus aprēķinus gan jau noderēs
    def __eq__(self, other):
        return self.p1points == other.p1points and self.p2points == other.p2points and self.turnCount == other.turnCount and self.data == other.data

    def __hash__(self):
        return hash((self.data, self.p1points, self.p2points, self.turnCount))

def buildTree(startNumb):
    root = TreeNode(startNumb)
    createdNodes = set()
    createLevel(root, createdNodes) 
    return root

def createLevel(parentNode, createdNodes):
    number = parentNode.data
    if number >= 1200:
        return
    
    nodes = [TreeNode(number * 2), TreeNode(number * 3), TreeNode(number * 4)]

    for node in nodes:
        
        if node not in createdNodes:
            parentNode.addChild(node)
            addPoints(node)
            createdNodes.add(node)
            createLevel(node, createdNodes)

def addPoints(node):
    if node.turnCount % 2 == 1:
        if node.data % 2 == 0:
            node.p2points -= 1
        else:
            node.p1points += 1
    else:
        if node.data % 2 == 0:
            node.p1points -= 1
        else:
            node.p2points += 1

def printTree(root):
    for node in root.children:
        #if not node.children: 
        print("--"*node.turnCount + ">" + str(node.data)+ f" (P1: {node.p1points}, P2: {node.p2points})")
        printTree(node)

if __name__ == '__main__':
    Tree = buildTree(8)
    print(8)
    printTree(Tree)
    print(Tree)
