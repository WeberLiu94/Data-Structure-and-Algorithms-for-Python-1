class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    def _find(self, value, node):
        if node is None:
            return None
        elif value < node.value:
            return self._find(value, self.left)
        elif value > node.value:
            return self._find(value, self.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def singleLeftRotate(self, node): #单次左旋
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def singleRightRotate(self, node): #单次右旋
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def put(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self._put(value, self.root)

    def _put(self, value, node):
        if node is None:
            node = Node(value)
        elif value < node.value:
            node.left = self._put(value, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if value < node.left.value:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)

        elif value > node.value:
            node.right = self._put(value, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if value < node.right.value:
                    node = self.doubleRightRotate(node)
                else:
                    node = self.singleRightRotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def delete(self, value):
        self.root = self.remove(value, self.root)

    def remove(self, value, node):
        if node is None:
            raise ValueError('Error,value not in tree')
        elif value < node.value:
            node.left = self.remove(value, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1


        elif value > node.value:
            node.right = self.remove(value, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.value = minNode.value
                node.right = self.remove(node.value, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.value = maxNode.value
                node.left = self.remove(node.value, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left

        return node
    def InorderTraverse(self, Node):
        if Node is None:
            return
        self.InorderTraverse(Node.left)
        print(Node.value)
        self.InorderTraverse(Node.right)

arr = [88, 59, 6, 2, 45, 17, 8, 5, 6]
AVLTree = AVLTree()
for i in arr:
    AVLTree.put(i)
AVLTree.InorderTraverse(AVLTree.root)