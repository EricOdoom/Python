class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
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
        if self.root:
            found = self._find(value, self.root)
            if found:
                return found
            else:
                return not found
        return None

    def _find(self, value, currentNode):
        if value == currentNode.value:
            return True
        elif value < currentNode.value:
            if currentNode.left is None:
                return False
            else:
                self._find(value, currentNode.left)
        elif value > currentNode.value:
            if currentNode.right is None:
                return False
            else:
                self._find(value, currentNode.right)
    def delete(self, value):
        pass

    def preorder(self, start, traversal):

        if start:
            traversal += str(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return  traversal

    def inOrder(self, start, traversal):
        if start:
            traversal = self.inOrder(start.left, traversal)
            traversal += str(start.value)
            traversal = self.inOrder(start.right, traversal)
        return traversal

    def postOrder(self, start, traversal):
        if start:
            traversal = self.postOrder(start.left, traversal)
            traversal = self.postOrder(start.right, traversal)
            traversal += str(start.value)
        return traversal

    def levelOrder(self, start):
        if start is None:
            return
        queue = [start]
        traversal = ""
        while len(queue)>0:
            traversal += str(queue[0].value)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal

    def reverseLevelOrder(self, start):
        if start is None:
            return
        traversal = ""
        queue = [start]
        stack = []
        while len(queue) > 0:
            node = queue.pop(0)
            stack.append(node)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value)
        return traversal

    def getHeight(self, node):
        if node is None:
            return -1
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        return 1 + max(leftHeight, rightHeight)

    def getSizeIter(self):
        if self.root is None:
            return 0
        stack = [self.root]
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size+=1
                stack.append(node.left)
            if node.right:
                size+=1
                stack.append(node.right)
        return size

    def getSizeRecursive(self, node):
        if node is None:
            return 0
        return 1 + self.getSizeRecursive(node.left) + self.getSizeRecursive(node.right)


b = BinaryTree()
b.insert(5)
b.insert(4)
b.insert(3)
b.insert(2)
b.insert(1)
b.insert(6)
b.insert(7)
b.insert(8)
b.insert(9)
print(b.preorder(b.root, ""))
print(b.levelOrder(b.root))
print(b.reverseLevelOrder(b.root))
print(b.inOrder(b.root, ""))
print(b.postOrder(b.root, ""))
print(b.getHeight(b.root))
print(b.getSizeIter())
print(b.getSizeRecursive(b.root))
