def InsertSort(array):
    length = len(array)
    for i in range(1, length): #每次相当于把当前值插入到前面的有序序列中
        compare_value = array[i]
        for j in range(i-1, 0-1, -1): #让下标能取到0
            if array[j] > compare_value:
                array[j+1] = array[j] #如果大于比较值，当前值后退一步
                array[j] = compare_value #让比较值插入到自己前面
    return array

alist = [54,26,93,17,77,31,44,55,20]
print(InsertSort(alist))