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
        self.queueShowB = []

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

    def printPreorder(self,node):
        if node != None:
            print(f'{node.data} ',end='')
            self.printPreorder(node.left)
            self.printPreorder(node.right)

    def printInorder(self,node):
        if node != None:
            self.printInorder(node.left)
            print(f'{node.data} ',end='')
            self.printInorder(node.right)

    def printPostorder(self,node):
        if node != None:
            self.printPostorder(node.left)
            self.printPostorder(node.right)
            print(f'{node.data} ',end='')

    def printBreadth(self,node):
        if node != None:
            if node == self.root:
                self.queueShowB.append(node)
            if len(self.queueShowB) > 0:
                if node.left is not None:
                    self.queueShowB.append(node.left)
                if node.right is not None:
                    self.queueShowB.append(node.right)
                print(f'{self.queueShowB[0].data} ',end='')
                self.queueShowB.pop(0)
                if len(self.queueShowB) > 0:
                    self.printBreadth(self.queueShowB[0])


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('Preorder : ', end='')
T.printPreorder(root)
print()
print('Inorder : ',end='')
T.printInorder(root)
print()
print('Postorder : ',end='')
T.printPostorder(root)
print()
print('Breadth : ',end='')
T.printBreadth(root)
print()