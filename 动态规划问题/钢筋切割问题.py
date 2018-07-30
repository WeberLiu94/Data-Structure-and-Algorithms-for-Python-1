#一段长度为n的钢筋，切割成不同的长度，每种长度有不同的价格，求收益最大的切割方案与收益值
#采用动态规划的思想
def cut(n,price_list):
    result_list = []#用来保存每一次迭代的结果，存储子问题的解
    cut = [0]*(n+1)#存储最佳的切割方案
    result_list.append(0)
    for sublength in range(1, n+1):#从子问题开始迭代求解
        total = 0
        for i in range(1, sublength+1):#子问题的左边开始切
            if total < price_list[i] + result_list[sublength-i]:
                total = price_list[i] + result_list[sublength-i]
                cut[sublength] = i
        result_list.append(total)
    return result_list, cut

n = 7
price_list = [0, 1, 5, 8, 9, 10, 15, 17, 20, 24, 30]
r, s = cut(n, price_list)
print(r,s)
while(n > 0):
    print(s[n])
    n = n -s[n]