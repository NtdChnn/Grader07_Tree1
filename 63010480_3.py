class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self,data,node):
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                node.right.insert(data, node.right)
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                node.left.insert(data, node.left)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data,self.root)
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def isK(self, node, k):
        if node != None:
            if node.data > k:
                node.data *= 3
            self.isK(node.left,k)
            self.isK(node.right,k)

T = BST()
inp,k = input("Enter Input : ").split('/')
ip = [int(i) for i in inp.split()]
for i in ip:
    root = T.insert(i)
T.printTree(root)
T.isK(root,int(k))
print("--------------------------------------------------")
T.printTree(root)