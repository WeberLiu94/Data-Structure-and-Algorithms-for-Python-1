class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._back = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            pass
        return self._head._element

    def dequeue(self): #从头部弹出数据
        if self.is_empty():
            pass
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._back = None
        return  result

    def enqueue(self, e): ##从尾部加入数据
        new = self._Node(e, None)
        if self.is_empty(): #若队列为空，则头部与尾部都是这个数据。
            self._head = new
        else:
            self._back._next = new #使原来的尾部指向现在的尾部
        self._back = new #更新尾部
        self._size += 1


letter = 'Queue'
queue = LinkedQueue()
for i in letter:
    queue.enqueue(i)
print(len(queue))
for i in range(0, len(queue)):
    print(queue.dequeue())
print(len(queue))