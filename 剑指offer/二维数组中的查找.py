# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        columns = len(array[0])
        if(columns == 0):
            return False
        if target < array[0][0] or target > array[row-1][columns-1]:  # 检测是否在范围内
            return False
        else:
            return self.find_re(array, target, 0, row-1)
    def binary_find(self,array, target, low, high):
        if low > high:  # 所有数都比较完毕
            return low  # 返回最近大于目标的数的下标
        else:
            mid = (low + high) // 2
            if target == array[mid]:
                return 'Y'
            elif target < array[mid]:
                return self.binary_find(array, target, low, mid - 1)
            else:
                return self.binary_find(array, target, mid + 1, high)

    def find_re(self,array,target, min, max):
        length = len(array)
        if length == 1:
            result = self.binary_find(array[0], target, 0, len(array[0]) - 1)
            if result == 'Y':
                print("Found Target")
                return True
            else:
                return False
        maxnum_list = [i[max] for i in array]
        minnum_list = [i[min] for i in array]
        max_index = self.binary_find(maxnum_list, target, 0, len(maxnum_list)-1)
        min_index = self.binary_find(minnum_list, target, 0, len(minnum_list)-1)
        if max_index == 'Y' or min_index == 'Y':
            return True
        else:
            if(min + 1 == max):
                return False
            else:
                return self.find_re([i[min+1:max] for i in array[max_index:min_index]], target, 0, max - 2)


#这个题用递归有点大材小用了，反而会影响运行时间，直接用循环来搜索,直接走Z字形找。
    def Find_2(self, target, array):
        Row = len(array)
        Columns = len(array[0])
        if (Columns == 0):
            return False
        else:
            row = Row - 1
            columns = 0
            while (row >= 0 and columns < Columns):
                if (target > array[row][columns]):
                    columns += 1
                elif (target < array[row][columns]):
                    row -= 1
                elif (target == array[row][columns]):
                    return True
        return False

