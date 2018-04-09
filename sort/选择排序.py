def SelectSort(array): #遍历得在列表中找最小值，并且将最小值放到最前面
    length = len(array)
    for i in range(length):
        min = i #假设第一个值是最小值
        for j in range(i+1, length):
            if array[min] > array[j]: #如果后续值小于当前的最小值，则将最小值的下标给后续值
                min = j
        if i != min: #当遍历完一次，直接将最小值与第i个值交换，放入顺序表
            array[i], array[min] = array[min], array[i]
    return array


alist = [54,26,93,17,77,31,44,55,20]
print(SelectSort(alist))