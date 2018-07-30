# def FindNumbersWithSum(array, tsum):
#     # write code here
#     num = []
#     num_ji = []
#     j = 1
#     boundary = len(array)
#     if tsum < array[0] or array == []:
#         return []
#     for i in range(len(array)):
#         j = i + 1
#         while (j < boundary):
#             if array[i] + array[j] == tsum:
#                 num.append([array[i], array[j]])
#                 num_ji.append(array[i] * array[j])
#                 boundary = j
#                 break
#             if array[i] + array[j] > tsum:
#                 boundary = j
#                 break
#             j += 1
#     #if len(num) == 0:
#         #return None
#     #return num[num_ji.index(min(num_ji))]
#     return num
def FindNumbersWithSum(array, tsum):
    if array == []:
        return []
    i = 0
    j = len(array) - 1
    while (i < j):
        print(i,j)
        if array[i] + array[j] < tsum:
            i += 1
        if array[i] + array[j] > tsum:
            j -= 1
        if array[i] + array[j] == tsum:
            return [array[i], array[j]]
    return []
print(FindNumbersWithSum([1,2,4,7,11,15],15))

