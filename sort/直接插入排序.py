def InsertSort(array):
    length = len(array)
    for i in range(1, length): #每次相当于把当前值插入到前面的有序序列中
        if array[i] < array[i-1]: #表示需要将当前插入前面的有序表
            insert_value = array[i]
            j = i - 1
            while(array[j] > insert_value and j >= 0):#若遍历的有序表中，值一直大于temp,则所有值往后退
                array[j+1] = array[j]
                j -= 1
            #此时的j的值小于temp，那么将temp的值插入到j+1的位置
        array[j+1] = insert_value
    return array

alist = [54,26,93,17,77,31,44,55,20]
print(InsertSort(alist))