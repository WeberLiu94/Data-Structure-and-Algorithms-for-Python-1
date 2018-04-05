# N = input()
# direction = input()
# L = 0
# R = 0
# for i in direction:
#     if i == 'R':
#         R += 1
#     else:
#         L += 1
# if(R == L):
#     print("N")
# if(R > L):
#     right_nums = R - L
#     result = right_nums % 4
#     if(result == 0):
#         print("N")
#     if(result == 1):
#         print("E")
#     if (result == 2):
#         print("S")
#     if (result == 3):
#         print("W")
# else:
#     left_nums = L - R
#     result = left_nums % 4
#     if(result == 0):
#         print("N")
#     if(result == 1):
#         print("W")
#     if (result == 2):
#         print("S")
#     if (result == 3):
#         print("E")

# def generater(n): #产生需要的数字
#     list = []
#     for i in range(1, n+1):
#         list.append(str(i))
#     x = "".join(list)
#     return x
#
# def jugment(n,m): #输出结果
#     num = generater(n)
#     y = int(num)
#     if(y % 3 ==0):
#         k = 1
#     else:
#         k = 0
#     for i in range(n+1, m+1):
#         num = num + str(i)
#         y = int(num)
#         if y % 3 == 0:
#             k += 1
#     return k
#
# print(jugment(2,5))

class Solution:
    def push(self, node):
        pass
    def pop(self):
        pass