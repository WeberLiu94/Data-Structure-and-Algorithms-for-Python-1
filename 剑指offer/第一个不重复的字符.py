def FirstNotRepeatingChar(s):
    # write code here
    str_list = list(s)
    temp = str_list[:]
    temp.sort()
    uiniqe = []
    if temp[0] != temp[1]:
        uiniqe.append(temp[0])
    for i in range(1, len(temp) - 1):
        if temp[i] != temp[i + 1] and temp[i] != temp[i - 1]:
            uiniqe.append(temp[i])
    if temp[-1] != temp[-2]:
        uiniqe.append(temp[-1])
    print(temp)
    print(uiniqe)
    for i in range(len(str_list)):
        if str_list[i] in uiniqe:
            return i


print(FirstNotRepeatingChar("kYVmIJVzYWPQLtIdKMmvkVSoKtqJANOfCCOfLVJEjjhbnPrDOwKCDeqhts"))