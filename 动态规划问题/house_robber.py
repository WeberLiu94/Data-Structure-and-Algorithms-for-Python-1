#n个房子围成一排，每个房子里面有固定的财物m，选择第i个房子时， 不能选择其相邻的房子
#求财物总和k最大的选择方案
#考虑动态规划，我们维护一个一位数组dp，其中dp[i]表示到i位置时不相邻数能形成的最大和
#那么递推公式为dp[i] = max(num[i] + dp[i - 2], dp[i - 1])，因为选择i,就只能选择i-2或者只能选i-1。
#初始化第1个与第2个房子时最大的选择方案，则从3开始迭代到n，最终求出最佳的方案


def house_robber(value_list):
    length = len(value_list)
    total = [0]*length
    total[0] = value_list[0]
    total[1] = max(total[0], value_list[1])
    for i in range(2, length):
        total[i] = max(value_list[i] + total[i-2], value_list[i-1])

    return total[-1]



#第二种情况，房子围城一个圆圈，则选了第一个不能选最后一个，同理，选了第最后一个不能选第一个
#因为第一个与最后一个不能共存，所以可以把原来的序列变为1-n-1 与2-n,然后取比较两个结果的最大值就可以。
def house_robber_circle(value_list):
    return max(house_robber(value_list[:-1]), house_robber(value_list[1:]))


value_list = [6,4,1,6]
print(house_robber(value_list))
print(house_robber_circle(value_list))