def find_min_max(sequence, min, max):
    length = len(sequence)
    if length == 1:
        if sequence[0] < min : #最后只剩下一个元素
            min = sequence[length-1]
        if sequence[0] > max:
            max = sequence[length-1]
        result = (min, max)
        return result
    else:
        if sequence[0] < min:
            min = sequence[0]
        if sequence[0] > max:
            max = sequence[0]
        return find_min_max(sequence[1:length], min, max) #更新max, min的值，并继续递归列表，每次比较一个，便删除一个元素
                                                            #知道列表的元素值只剩下一个返回最后结果


array = [7, 5]
x = find_min_max(array[1:], array[0], array[0])
print(x)