stack = []
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.listo = ['+','/','*','-']
        global stack

    def __str__(self):
        return str(self.data)

    def insert(self,data,node):
        stack.append(Node(data))
        if data in self.listo:
            node.left = stack[len(stack)-3]
            node.right = stack[len(stack)-2]
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(node)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = Node(data)
        self.root.insert(data,self.root)
        return self.root


    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printPrefix(self, node):
        if node != None:
            print(f'{node.data}', end='')
            self.printPrefix(node.left)
            self.printPrefix(node.right)

    def printInfix(self,node):
        if node != None:
            if node.data in ['+','/','*','-']:
                print('(',end='')
            self.printInfix(node.left)
            print(f'{node.data}',end='')
            self.printInfix(node.right)
            if node.data in ['+', '/', '*', '-']:
                print(')', end='')

T = BST()
inp = input('Enter Postfix : ')
for i in inp:
    root = T.insert(i)
print('Tree :')
T.printTree(root)
print('--------------------------------------------------')
print('Infix : ',end='')
T.printInfix(root)
print()
print('Prefix : ', end='')
T.printPrefix(root)
print()
