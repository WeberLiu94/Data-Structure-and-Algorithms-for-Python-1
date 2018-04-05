#原始的冒泡排序 不断的两两比较，将最小的值传到数组的首位，然后减少比较的范围，知道最后一个树
def BubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1, i, -1):
            print("123")
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array



#改进版本，增加一个标志位来判断是否需要数据交换,若Flag为False，则说明序已经排好
def BubbleSort_advance(array):
    length = len(array)
    Flag = True
    for i in range(length):
        if Flag == True:
            Flag = False
            for j in range(length-1, i, -1):
                print("123")
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                    Flag = True
        else:
            continue
    return array

alist = [54,26,93,17,77,31,44,55,20]
alist2 = [2,1,3,4,5,8,6,7]
print(BubbleSort(alist2))
print("算法比较，上为不改进的循环次数")
print(BubbleSort_advance(alist2))