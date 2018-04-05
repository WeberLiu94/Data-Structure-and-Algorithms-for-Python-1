class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    class Empty(Exception):
        pass
#Stack methods

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise self.Empty('Stack is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return  result

    def top(self):
        if self.is_empty():
            raise self.Empty('Stack is empty')
        return self._head._element
    def seconde(self):
        return  self._head._next._element

stack = LinkedStack()
letter = 'Stack'
for i in letter:
    stack.push(i)

# for i in range(0, len(stack)):
#     print(stack.pop())
x = stack.seconde()
print(x)