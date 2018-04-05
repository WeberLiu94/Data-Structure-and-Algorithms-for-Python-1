# number_list = [1,2,3,4,3,3,2,1]
# def fun(number_list):
#     if len(number_list)==0 :
#         return
#     else:
#         exist_nums = len(number_list)
#         print(str(exist_nums) + "\n")
#         list_minus = [i-min(number_list) for i in number_list]
#         #list_pop_zero = [list_minus.pop(i) for i in range(len(list_minus)) if list_minus[i] == 0]
#         list_pop_zero = []
#         for i in list_minus:
#             if i != 0:
#                 list_pop_zero.append(i)
#         return fun(list_pop_zero)
# fun(number_list)
number_list = [1,3,-1,-3,5,3,6,7]
k = 3
n = 8
times = n - k + 1
for i in range(times):
    result = max(number_list[i:k+i]) - min(number_list[i:k+i])
    print(result)