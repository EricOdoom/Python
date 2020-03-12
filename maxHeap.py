class MaxHeap(object):
    def __init__(self):
        self.heap = [0]

    def getParent(self,i):
        return int(i/2)

    def getLeftChild(self, i):
        return 2*i

    def getRightChild(self, i):
        return (2*i)+1

    def hasParent(self,i):
        return self.getParent(i) > 0

    def hasLeftChild(self,i):
        return self.getLeftChild(i) < len(self.heap)

    def hasRightChild(self,i):
        return self.getRightChild(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap)-1)

    def heapify(self, i):
        while (self.hasParent(i) and self.heap[i] > self.heap[self.getParent(i)]):
            self.swap(i, self.getParent(i))
            i = self.getParent(i)

    def delete_root(self):
        if len(self.heap) == 1:
            return -1
        lastIndex = len(self.heap)-1
        self.swap(1, lastIndex)
        root = self.heap.pop()
        self.heapify_down(1)
        return root

    def heapify_down(self, i):
        while self.hasLeftChild(i):
            maxChildIndex = self.getMaxChildIndex(i)
            if maxChildIndex == -1:
                break
            if self.heap[i] < self.heap[maxChildIndex]:
                self.swap(i, maxChildIndex)
                i = maxChildIndex
            else:
                break
    def getMaxChildIndex(self, i):
        if self.hasLeftChild(i):
            left = self.getLeftChild(i)
            if self.hasRightChild(i):
                right = self.getRightChild(i)
                if self.heap[left] > self.heap[right]:
                    return left
                else:
                    return right
        return -1

    def printHeap(self):
        print(self.heap)

m = MaxHeap()
m.insert(5)
m.insert(7)
m.insert(2)
m.insert(3)
m.insert(9)
m.insert(-1)
m.insert(5)
m.printHeap()
