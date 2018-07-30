#给定一个载重量为m，n个物品，其重量为wi，价值为vi，
#1<=i<=n，要求:把物品装入背包，并使包内物品价值最大
#思路
#在0 / 1背包问题中，物体或者被装入背包，或者不被装入背包，只有两种选择。
#循环变量i，j意义：前i个物品能够装入载重量为j的背包中
#(n + 1) * (m + 1)
#数组value意义：value[i][j]
#表示前i个物品能装入载重量为j的背包中物品的最大价值
#若w[i] > j，第i个物品不装入背包
#则，若w[i] <= j且第i个物品装入背包后的价值 > value[i - 1][j]，则记录当前最大价值（替换为第i个物品装入背包后的价值）


def Bag(value_list,weight_list,m,n):
    #求最大值的矩阵
    max_matrix = [[0 for x in range(m+1)] for y in range(n+1)]
    c = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            if weight_list[i-1] > j:
                max_matrix[i][j] = max_matrix[i-1][j]
            else:
                max_matrix[i][j] = max(max_matrix[i-1][j],
                                       max_matrix[i-1][j-weight_list[i-1]] + value_list[i-1])

    #逆推具体方案
    for i in range(n, 0, -1):
        if max_matrix[i][m] > max_matrix[i-1][m]:
            c.append(i)
            m -= weight_list[i-1]
    return max_matrix[-1][-1], c


n = 4
m = 10
weight_list = [2, 3, 4, 7]
value_list = [1, 3, 5, 9]
print(Bag(value_list, weight_list, m, n))
