def max_value(number_list,n,k,d):
    max_matrix = [[0]*k for i in range(n)]
    min_matrix = [[0]*k for i in range(n)]

    #初始化选择1个数字的情况
    for i in range(n):
        max_matrix[i][0] = number_list[i]
        min_matrix[i][0] = number_list[i]
    #开始递推
    for i in range(n):
        for p in range(1, k):
            for x in range(max(0, i-d), i):#从i-d到i-1为结尾的选中k-1个的最大值遍历：
                max_matrix[i][p] = max(max_matrix[i][p],
                                       max(max_matrix[x][p-1]*number_list[i],min_matrix[x][p-1]*number_list[i]))
                min_matrix[i][p] = min(min_matrix[i][p],
                                       min(max_matrix[x][p-1]*number_list[i],min_matrix[x][p-1]*number_list[i]))
    return max([max_matrix[x][k-1] for x in range(n)]) #输出每个位置选择k个数的最大值

import sys
res = []
s = sys.stdin.readline().strip("\n")
while s != "":
    res.append(s)
    s = sys.stdin.readline().strip("\n")
#print(res)
n = int(res[0])
number_list = list(map(int, res[1].split(" ")))
k_d = list(map(int, res[2].split(" ")))
k = k_d[0]
d = k_d[1]
print(max_value(number_list,n,k,d))