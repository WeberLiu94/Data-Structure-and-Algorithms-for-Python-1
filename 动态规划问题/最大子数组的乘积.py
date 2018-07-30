def FindGreatestProductOfSubArray(array):
    if array ==None:
        return 0
    res = array[0]
    max_num = array[0]
    min_num = array[0]
    for i in range(1, len(array)):
        tmax = max_num #用一个变量值来存原来的值，因为max_num值肯能会改变
        tmin = min_num #用一个变量值来存原来的值，因为min_num值肯能会改变
        max_num = max(max(array[i], array[i] * tmax), tmin * array[i])
        min_num = min(min(array[i], array[i] * tmax), tmin * array[i])
        res = max(res, max_num)
    return res

print(FindGreatestProductOfSubArray([1,2,3,-3,-4]))