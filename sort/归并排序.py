def Merge_sort(L):
    def sort(L, L_copy_1, index_1, index_2):
        def merge(L, L_copy, index_1, index, index_2):

            #合并两个有序的序列
            i = index_1
            j = index + 1
            k = i
            while( i <= index and j <= index_2):
                if(L[i] < L[j]):
                    L_copy[k] = L[i]
                    i+=1
                else:
                    L_copy[k] = L[j]
                    j+=1
                k += 1
            if(i <= index):
                for x in range(0, index-i+1):
                    #print(i)
                    L_copy[k+x] = L[i+x] #加剩下的数
            if (j <= index_2):
                for x in range(0, index_2-j+1):
                    L_copy[k+x] = L[j+x] #加剩下的数
        #递归调用，先分治，再比较大小后排序，合并，再排序S
        L_copy_2 = [0]*len(L)
        if (index_1 == index_2):
            L_copy_1[index_1] = L[index_1]
        else:
             index = (index_1 + index_2) // 2
             sort(L, L_copy_2, index_1, index)
             sort(L, L_copy_2, index+1, index_2)
             merge(L_copy_2, L_copy_1, index_1, index, index_2)
    #调用函数，返回结果
    sort(L, L, 0, len(L) - 1)
    return L


alist = [54,26,93,17,77,31,44,55,20]

print(Merge_sort(alist))