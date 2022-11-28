#||------------------------------------ПОСТРОЕНИЕ ДЕРЕВА С НУЛЯ------------------------------------||
'''
class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
    def AddNode(self, obj):
        self.children.append(obj)

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    def AddNode(self, obj):
        self.children.append(obj)


FunCorp = Tree('Head Honcho') # СОЗДАНИЕ ДЕРЕВА И
                              # ДОБАВЛЕНИЕ ДАННЫХ В КОРЕНЬ
FunCorp.AddNode(Node('Zhopa')) #ДОБАВЛЕНИЕ КЛАССА NODE В КЛАСС TREE
FunCorp.AddNode(Node('pupa'))
FunCorp.AddNode(Node('dupenpynya'))
print(FunCorp.root)
print(f"C suite: {', '.join(str(child.data) for child in FunCorp.children)}")
FunCorp.children[0].AddNode(Node('General VUPA of DUPA'))
print(f"Our {FunCorp.children[2].data} is {FunCorp.children[0].children[0].data}")
'''

class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
        self.Nodes = []
    def AddNode(self, obj):
        self.children.append(obj)

    def getAllNodes(self):
        self.Nodes.append(self.root)
        for child in self.children:
            self.Nodes.append(child.data)
        for child in self.children:
            if child.getChildNodes(self.Nodes) != None:
                child.getChildNodes(self.Nodes)
        print(*self.Nodes, sep= '\n')
        print('Tree Size: ' + str(len(self.Nodes)))
        print(f'{self.children[0].data} is a {self.children[0].children[0].data}')


class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    def AddNode(self, obj):
        self.children.append(obj)
    def getChildNodes(self, Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)

FunCorp = Tree('Head Honcho')
FunCorp.AddNode(Node(1))
FunCorp.AddNode(Node(2))
FunCorp.AddNode(Node(3))
FunCorp.children[0].AddNode(Node('x = 250, y = 100'))
FunCorp.children[1].AddNode(Node('Neutral charge'))
FunCorp.children[2].AddNode(Node('Negative charge'))
FunCorp.children[0].children[0].AddNode(Node('Subway'))
FunCorp.children[0].children[0].children[0].AddNode(Node('Employee of the month'))

FunCorp.getAllNodes()




