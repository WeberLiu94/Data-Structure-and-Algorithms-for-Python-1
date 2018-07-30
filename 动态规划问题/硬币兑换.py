#n中面值的硬币，k元有多少种兑换方法
#################################################################
# coin Combinations: using dynamic programming
#
# Basic idea:
# dp[i][j] = sum(dp[i-1][j-k#coins[i-1]]) for k = 1,2,..., j/coins[i-1]
# dp[0][j] = 1 for j = 0, 1, 2, ..., sum
#
# Input:
# coins[] - array store all values of the coins
# coinKinds - how many kinds of coins there are
# sum - the number you want to construct using coins
#
# Output:
# the number of combinations using coins construct sum
#
# c[3] = {1, 2, 5};
def combination(C,k,n):
    #初始化一个n行k列的二维数组
    num = [[0 for x in range(k+1)] for y in range(n+1)]
    #让num[0][0]为0，并且num[i][0]为1，为迭代的基础
    for i in range(n + 1):
        num[i][0] = 1
    #计算Num[1][1]至num[n][k]的值
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for p in range(j // C[i - 1] + 1):#j为当前最高的面值。即sum
                num[i][j] += num[i - 1][j - p*C[i - 1]] #递推公式，dp[i][j] = sum(dp[i-1][j-k#coins[i-1]]) for k = 1,2,..., j/coins[i-1]
    return num[n][k]

times = int(input())
for i in range(times):
    infor = list(map(int, input().split(" ")))
    cash_list = list(map(int, input().split(" ")))
    n = infor[0]
    k = infor[1]
    print(combination(cash_list,k,n))

