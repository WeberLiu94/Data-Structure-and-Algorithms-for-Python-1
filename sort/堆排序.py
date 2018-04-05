def heap_sort(L):
    #生成最大堆函数
    def heap_adjust(L, father_node, length):
        temp = L[father_node]
        index = father_node * 2 #此时指向左孩子
        while(index <= length):
            if index < length and L[index] < L[index+1]: #左孩子不是最后一个节点，且小于兄弟有孩子，如果是最后一个结点，就没有兄弟了。
                index += 1# 下标指向右孩子
            if temp < L[index]: #若父结点小于右孩子，交换
                L[father_node] = L[index] #父节点值更换为右孩子
                father_node = index #记录此时最小值应该插入的位置
            index*=2
        L[father_node] = temp #将最后的位置赋予最小的值

    #开始排序
    from collections import deque
    new_L = deque(L)
    new_L.appendleft(0)
    length = len(new_L)-1
    for j in range(length//2, 0, -1): #调整为最大堆
        heap_adjust(new_L, j, length)
        print(j)
    #print(new_L)
    for j in range(length, 1, -1):
        new_L[1], new_L[j] = new_L[j], new_L[1] #交换最大值与最小值的位置
        heap_adjust(new_L, 1, j-1) #把除去最大值后的堆排成最大推
    new_L.popleft()
    return new_L


alist = [54,26,93,17,77,31,44,55,20]

print(heap_sort(alist))
