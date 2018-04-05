#思路，考虑列表中第一个元素的其他元素的特殊性，直到列表的元素为1，还是不一样则返回true
def unique_element(S):
    length = len(S)
    if length == 2:
        if S[0] != S[1]:
            return True
        else:
            return False
    else:
        for i in range(1, length):
            if S[i] == S[0]:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
            return False
        else:
            return unique_element(S[1:length])


array = [2, 1, 6, 4, 8, 3, 9]
result = unique_element(array)
print(result)