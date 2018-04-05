def SelectSort(array):
    length = len(array)
    min = 0
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if array[min] > array[j]:
                min = j
        if i != min:
            array[i],array[min] = array[min],array[i]
    return array


alist = [54,26,93,17,77,31,44,55,20]
print(SelectSort(alist))