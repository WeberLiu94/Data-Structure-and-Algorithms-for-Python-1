class Solution:
    def jumpFloor(self, number):
        # write code here
        one_time = number #选择1步的次数
        k = 0 #多少总跳法
        while(one_time >= 0):#当选择跳1的次数大于等于0:
            rest = number - one_time
            if rest % 2 == 0: #若1步与两步能组合成number
                tow_tiems = rest // 2
                k += self.jiecheng(tow_tiems + one_time) / (self.jiecheng(tow_tiems) * self.jiecheng(one_time))
                print(k)
            one_time -= 1
        return k

    def jiecheng(self, n):
        if n == 0:
            return 1
        else:
            return self.jiecheng(n-1) * n
s = Solution()
print(s.jumpFloor(3))