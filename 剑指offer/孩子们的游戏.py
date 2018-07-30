def LastRemaining_Solution(n, m):
    # write code here
    number_list = list(range(n))
    index = -1 #从0开始循环
    count = 1
    length = n
    while (length != 0):
        index += 1
        if index == n:
            index = 0
        if number_list[index] == -1:
            continue
        if count % m == 0:
            print(number_list)
            print("count:%d,index:%d"%(count, index))
            number_list[index] = - 1 #标记去掉的数
            length -= 1
        count += 1
    return index
print(LastRemaining_Solution(5,3))
