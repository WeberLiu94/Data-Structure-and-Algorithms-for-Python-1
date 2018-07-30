def merge(a, b): #需要有一个新的数组来合并两个原来有序的数组。
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    else:
        middle = len(lists) // 2
        left = merge_sort(lists[:middle])
        right = merge_sort(lists[middle:])
        result = merge(left, right)
    return result

#非递归版本
def merge_sort2(L):
    length = len(L)
    for i in range(length):
        L[i] = [L[i]] #将序列变成列表
    while(length!=1): #迭代合并数组
        c = []
        if length % 2 == 1:#若数组数量为单数，则先将后面的合并
            L[-2] = merge(L[-1], L[-2])
            L.pop() #将最后一个弹出
            length = len(L)#更新长度
        for i in range(0, length, 2): #数组两两合并
            c.append(merge(L[i], L[i+1]))
        L = c[:]#迭代获取最新的数组
        length = len(L)#更新数组长度，为下一次循环次数提供参考
    return c[0] #返回最终结果

if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9, 10]
    print(merge_sort2(a))