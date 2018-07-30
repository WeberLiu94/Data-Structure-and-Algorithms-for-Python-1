import math
def StrToInt(s):
    # write code here
    list_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    position = 0
    number = 0
    for i in range(len(s) - 1, 0, -1):
        if s[i] <= '9' and s[i] >= '0':
            number += list_str.index(s[i]) * math.pow(10, position)
            position += 1
        else:
            return 0
    if s[0] in list_str:
        number += list_str.index(s[0]) * math.pow(10, position)
    return number

print(StrToInt("999"))