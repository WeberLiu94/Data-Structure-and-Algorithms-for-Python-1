# 构建二叉查找树(非平衡)
class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None): #key为索引值 val为存储的数据
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent= parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode): #递归建立二叉排序树
        if val < currentNode.payload:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v): #重载[]，使得可以索引赋值
        self.put(k, v)

    def get(self, payload):
        if self.root:
            res = self._get(payload, self.root)
            if res:
                print("Found Target!")
                return res.key
            else:
                print("Not Found!")
                return None
        else:
            return None

    def _get(self, payload, currentNode): #递归查到指定的项
        if not currentNode:
            return None
        elif currentNode.payload == payload:
            return currentNode
        elif payload < currentNode.payload:
            return self._get(payload, currentNode.leftChild)
        else:
            return self._get(payload, currentNode.rightChild)

    def __getitem__(self, payload): #重载[]，使得可以索引取值
        return self.get(payload)

    def __contains__(self, payload):
        if self._get(payload, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)


    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)
    def InorderTraverse(self, Node):
        if Node is None:
            return
        self.InorderTraverse(Node.leftChild)
        print(Node.payload)
        self.InorderTraverse(Node.rightChild)

mytree = BinarySearchTree()
#arr = [35, 37, 47, 51, 58, 62, 73, 88, 93, 99]
arr = [62, 58, 88, 47, 73, 99, 35, 51, 93, 37]#创建一个二分排序树
for i in range(len(arr)):
    mytree[i] = arr[i]

#print(mytree.root.payload)
mytree.InorderTraverse(mytree.root)