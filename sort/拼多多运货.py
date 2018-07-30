input_string = input() #输入的字符串，空格为区分
array = [int(x) for x in input_string.split(" ")]#根据空格拆分并且转化为Int型的数组
length = len(array) #获取长度
array.sort()
max = length - 1
min = 0
car = 0
if length == 0:
    print(0)
else:
    while(min < max):
        sum = array[min] + array[max]
        if sum > 300:
            car = car + 1
            max = max - 1
        else:
            while(sum <= 300 and min < max):
                min = min + 1
                sum = sum + array[min]
            max = max - 1
            car += 1
    if min == max:
        car += 1
    print(car)



