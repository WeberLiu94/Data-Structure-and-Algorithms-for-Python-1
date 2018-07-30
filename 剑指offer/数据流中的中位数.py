class Solution:
    def __init__(self):
        self.array = []
        self.size = 0
    def Insert(self, num):
        # write code here
        if self.size == 0:
            self.array.append(num)
        count = 0
        while(count < self.size - 1):
            if self.array[count] > num:
                self.array.insert(num,count)
                break
            count += 1
        if count == self.size:
            self.array.append(num)
        self.size += 1
    def GetMedian(self):
        # write code here
        if self.size%2 == 1:
            return self.array[self.size // 2]
        else:
            return (self.array[self.size // 2] + self.array[self.size // 2 - 1]) / 2