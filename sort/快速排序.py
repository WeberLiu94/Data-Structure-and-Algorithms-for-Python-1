#快速排序
def Partition(L, low, high):
    #三数取中，防止形成不平衡的递归斜树
    median = low + (high - low) // 2
    if(L[low] > L [high]):  #保证左边要小
        L[low], L[high] = L[high], L[low]

    if (L[median] >L[high]): #保证中间要小
        L[median], L[high] = L[high], L[median]

    if ( L[median]>L[low] ): #保证左边要小
        L[low], L[median] = L[median], L[low]



    pivotkey = L[low]  #此时L[low] 为三个数的中间数
    while(low != high):
        while(low < high and L[high] >= pivotkey):
            high -= 1
        L[low] = L[high]
        while (low < high and L[low] <= pivotkey):
            low += 1
        L[high] = L[low]
    L[low] = pivotkey
    return low


def QuickSort(L, low, high):
    if low < high:
        pivot = Partition(L, low, high)
        QuickSort(L, low, pivot-1)
        QuickSort(L, pivot+1, high)


    #优化后的递归：
# while(low < high):
#     pivot = Partition(L, low, high)
#     sort(L, low, pivot - 1)
#     low = pivot + 1 #减少了一个递归的分支。


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
QuickSort(alist, 0, len(alist)-1)
print(alist)