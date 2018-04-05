class DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next


    def __init__(self):
        #创建一个新的双向链表
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_node(self, e, pred, succ):
        new = self._Node(e, pred, succ)
        pred._next = new
        succ._prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDeque(DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            pass
        else:
            return self._header._next._element

    def last(self):
        if self.is_empty():
            pass
        else:
            return self._trailer._prev._element

    def insert_first(self, e): #在头部插入数据
        self._insert_node(e, self._header, self._header._next)

    def insert_last(self, e): #在尾部插入数据
        self._insert_node(e, self._trailer._prev, self._trailer)

    def delete_first(self):   #弹出头部数据
        if self.is_empty():
            pass
        else:
            return self._delete_node(self._header._next)

    def delete_last(self):  #弹出尾部数据
        if self.is_empty():
            pass
        else:
            return self._delete_node(self._trailer._prev)

queue = LinkedDeque()
queue.insert_first('h')
queue.insert_first('e')
print(queue.first())
print(queue.last())
queue.delete_first()
print(queue.first())