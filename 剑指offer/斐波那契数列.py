class Solution:
    def Fibonacci(self, n):
        # write code here
        # if n == 0:
        #     return 0
        # if n<=2:
        #     return 1
        # else:
        #     return self.Fibonacci(n-1) + self.Fibonacci(n-2)
        #循环版本
        fn_1 = 1
        fn_2 = 0
        while(n > 1):
            fn_1 = fn_1 + fn_2
            fn_2 = fn_1 - fn_2
            n -= 1
        return fn_1


s = Solution()
print(s.Fibonacci(6))