# class LinkedBinaryTree():
#     class _Node:
#         __slots__ = '_element', '_parent', '_right', '_left'
#
#         def __init__(self, element, parent=None, right=None, left=None):
#             self._element = element
#             self._parent = parent
#             self._right = right
#             self._left = left
#
#     def __init__(self):
#         self._root = None
#         self._size = 0
#
#     def root(self):
#         return self.root
#
#     def parent(self, node):
#         return node._parent
#
#     def right(self, node):
#         return node._right
#
#     def left(self, node):
#         return node._left
#
#     def num_children(self, node):
#         count = 0
#         if node._right is not None:
#             count += 1
#         if node._left is not None:
#             count += 1
#         return count
#
#     def _add_root(self, e):
#         if self._root is not None:
#             raise ValueError('Root exists')
#         self._size = 1
#         self._root = self._Node(e)
#         return self._root
#
#     def _add_left(self, node, e):
#         if node._left is not None:
#             raise ValueError('Left child exists')
#         self._size += 1
#         node._left = self._Node(e, node)
#         return node._left
#
#     def _add_right(self, node, e):
#         if node._right is not None:
#             raise ValueError('Right child exists')
#         self._size += 1
#         node._right = self._Node(e, node)
#         return node._right
#
#     def _repalce(self, node, e):
#         old = node._element
#         node._element = e
#         return old
#
#     def _delete_(self, node):
#         if self.num_children(node) == 2:
#             raise ValueError('Node has two children')
#         if self.num_children(node) == 0:
#             parent = node._parent
#             if node is parent._right:
#                 parent._right = None
#             if node is parent._left:
#                 parent._left = None
#             self._size -= 1
#             return node._element
#         else:
#             child = node._right if node._right else node._left
#             if node is self._root:
#                 self._root = child
#             else:
#                 parent = node._parent
#                 child._parent = parent
#                 if node is parent._right:
#                     parent._right = child
#                 if node is parent._left:
#                     parent._left = child
#                 self._size -= 1
#                 return node._element
#
# my_tree = LinkedBinaryTree()
# root = my_tree._add_root('皇帝')
# ge_1_left = my_tree._add_left(root, '大将军')
# ge_1_right = my_tree._add_right(root, '丞相')
# ge_2_left = my_tree._add_left(ge_1_left, "小将军")
#
# print(ge_1_right._element)
# print(ge_1_left._element)
# print(root._right._element)
# print(root._left._element)
# print(ge_1_left._parent._element)
# print(ge_1_right._parent._element)
# print(ge_1_left._left._element)
#
# my_tree._delete_(ge_1_left)
# print(root._left._element)
# print(ge_2_left._parent._element)




# -*- coding: utf-8 -*-
from collections import deque
class Node:
  def __init__(self,val,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right
  #setter and getter
  def get_val(self):
    return self.val
  def set_val(self,val):
    self.val=val
  def get_left(self):
    return self.left
  def set_left(self,left):
    self.left=left
  def get_right(self):
    return self.right
  def set_right(self,right):
    self.right=right
class Tree:
  def __init__(self,list):
    list=sorted(list)
    self.root=self.build_tree(list)
  #递归建立平衡二叉树
  def build_tree(self,list):
    l=0
    r=len(list)-1
    if(l>r):
      return None
    if(l==r):
      return Node(list[l])
    mid=(l+r)//2
    root=Node(list[mid])
    root.left=self.build_tree(list[:mid])
    root.right=self.build_tree(list[mid+1:])
    return root
  #前序遍历
  def preorder(self,root):
    if(root is None):
      return
    print(root.val)
    self.preorder(root.left)
    self.preorder(root.right)
  #后序遍历
  def postorder(self,root):
    if(root is None):
      return
    self.postorder(root.left)
    self.postorder(root.right)
    print(root.val)
  #中序遍历
  def inorder(self,root):
    if(root is None):
      return
    self.inorder(root.left)
    print(root.val)
    self.inorder(root.right)
  #层序遍历
  def levelorder(self,root):
    if root is None:
      return
    queue =deque([root])
    while(len(queue)>0):
      size=len(queue)
      for i in range(size):
        node =queue.popleft()
        print(node.val)
        if node.left is not None:
          queue.append(node.left)
        if node.right is not None:
          queue.append(node.right)
list=[35, 37, 47, 51, 58, 62, 73, 88, 93, 99]
tree=Tree(list)

# tree.inorder(tree.root)
#
# tree.levelorder(tree.root)
#
# tree.preorder(tree.root)
#
# tree.postorder(tree.root)

print(tree.root.val)