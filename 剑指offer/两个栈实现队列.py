class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
    def pop(self):

        if(len(self.stack1 == 0) and len(self.stack2 == 0)):
            return False
        if(self.stack2 == None):
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

