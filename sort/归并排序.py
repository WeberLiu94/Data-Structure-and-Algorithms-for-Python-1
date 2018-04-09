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
        print(left)
        right = merge_sort(lists[middle:])
        print(right)
        result = merge(left, right)
        print(result)
    return result


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(merge_sort(a))