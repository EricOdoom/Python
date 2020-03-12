class Node(object):
    def __init__(self, value):
        self.value = None
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(value)
            else:
                self._insert(value, currentNode.left)
        elif value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self._insert(value, currentNode.right)

    def find(self, value):
        if self.root is None:
            return None
        elif self.root.value == value:
            return True
        else:
            return self._find(self.root, value)

    def _find(self, currentNode, value):
        if value  == currentNode.value:
            return True
        elif value < currentNode.value:
            if currentNode.left is None:
                return False
            else:
                return self._find(currentNode.left, value)
        elif value > currentNode.value:
            if currentNode.right is None:
                return False
            else:
                return self._find(currentNode.right, value)
        else:
            return False

    def inorder(self, tree):
        if tree:
            self.inorder(tree.left)
            print(tree.root.value)
            self.inorder(tree.right)


b = BST()
b.insert(5)
b.insert(4)
b.insert(3)
b.insert(2)
b.insert(1)
b.insert(6)
b.insert(7)
b.insert(8)
b.insert(9)
b.inorder(b)
