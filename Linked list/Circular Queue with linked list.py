class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None  #创建一个新的队列，让尾部为空
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return  self._size == 0

    def enqueue(self, e):
        #向队列在尾部加入一个新的元素
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new #若为空，则自己连接自己
        else:
            new._next = self._tail._next #若不为空，则指向头部（上一个尾部的指向就是头部）
            self._tail._next = new #上一个尾部指向现在的尾部
        self._tail = new #成为新的尾部
        self._size += 1 #队列大小加1

    def dequeue(self):
        if self.is_empty():
            pass
        else:
            head = self._tail._next #获得头部节点
            if self._size == 1:
                self._tail = None #若只有一个数据，则弹出后尾部节点为None
            else:
                self._tail._next = self._tail._next._next #更新头部数据
            self._size -= 1 #队列元素大小减少1
        return head._element #返回头部数据

    def first(self):
        #返回头部的数据但不弹出
        if self.is_empty():
            pass
        else:
            return  self._tail._next._element

    def rotate(self):
        #将现在的头部数据移动到尾部
        if self._size > 0:
            self._tail = self._tail._next

    def over(self):
        return self._tail._element

letter = 'Queue'
queue = CircularQueue()
for i in letter:
    queue.enqueue(i)
    print(queue.over())
print(len(queue))
for i in range(0, len(queue)):
    print(queue.dequeue())
# print(len(queue))
