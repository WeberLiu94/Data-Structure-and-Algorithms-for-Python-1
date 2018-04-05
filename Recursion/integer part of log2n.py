def integer_log2n(number, result):
    if number < 2:
        return result
    else:
        return integer_log2n(number/2, result+1) #整数部分是元素能够整除2的次数


result = integer_log2n(12, 0)
print(result)