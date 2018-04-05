#解题思路：每次剔除最后一个数，求剩下的子集，然后再加上剔除的数据，一直递归到只有最后一个数，此时子集就为空集与数本身
#再一层一层往上加。


def find_subset(array, subset_list, m, n):
    if n == 0:
        subset_list.append([array[n]])
        subset_list.append([])
        return find_subset(array, subset_list, m, n+1)
    elif n < m:
        subset_list = subset_list + [i + [array[n]] for i in subset_list]
        return find_subset(array, subset_list, m, n+1)
    else:
        return subset_list


set = [1, 2, 3, 4]
sub_set = find_subset(set, [], len(set), 0)
print(sub_set)


# a = [[1], [2], [3]]
# b = [[1], [2], [3]]
# a = a + [i + [6] for i in a] #无错误
# b = b + [i.append(6) for i in b ]#有错误 因为append会改变原来的数组，但是并不会返回结果。
# print(a)
# print(b)