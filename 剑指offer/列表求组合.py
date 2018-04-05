import sys
import copy
if __name__ == "__main__":
    # 读取第一行的n
    cordinate_list = []
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        cordinate = []
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        for v in values:
            cordinate.append(v)
        cordinate_list.append(cordinate)


    def combine(l, n):
        answers = []
        one = [0] * n

        def next_c(li=0, ni=0):
            if ni == n:
                answers.append(copy.copy(one))
                return
            for lj in range(li, len(l)):
                one[ni] = l[lj]
                next_c(lj + 1, ni + 1)

        next_c()
        return answers

    def fun(L):
        k = 0
        combine_list = combine(L, 3)
        length = len(combine_list)
        for i in range(length):
            x_10 = combine_list[i][1][0] - combine_list[i][0][0]
            x_21 = combine_list[i][2][0] - combine_list[i][1][0]
            y_10 = combine_list[i][1][1] - combine_list[i][0][1]
            y_21 = combine_list[i][2][1] - combine_list[i][1][1]
            if(x_10 == 0 and x_21 ==0 ):
                continue
            if( x_10 !=0 and x_21!=0):
                if((y_10 / x_10) == (y_21 / x_21)):
                    continue
                k += 1
            else:
                k += 1
        return k
    print(fun(cordinate_list))