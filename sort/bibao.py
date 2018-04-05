# Matrix_information = input()
# Matrix_information= [int(i) for i in Matrix_information.split(" ")]
# Node_num, egde_num = Matrix_information[0], Matrix_information[1]
#
# #print(Node_num, egde_num)
# Matrix = [[0 for i in range(Node_num)] for j in range(Node_num)]
#
#
# for i in range((egde_num)):
#     egde_information = input()
#     egde_information = [int(i) for i in egde_information.split(" ")]
#     cordinate_x, cordinate_y = egde_information[0]-1, egde_information[1]-1
#     Matrix[cordinate_x][cordinate_y] = 1
#     Matrix[cordinate_y][cordinate_x] = 1
#
# #print(Matrix)
#
# #统计每个点的度数
# degree_list = []
# for i in Matrix:
#     degree_list.append(i.count(1))
# x = 0
# for i in range(Node_num):
#     for j in range(i+1,Node_num):
#         if degree_list[i] + degree_list[j] >= Node_num:
#             if Matrix[i][j] == 0:
#                 print("大于N，不相邻，添加一条边")
#                 Matrix[i][j] = 1
#                 Matrix[j][i] = 1
#                 x+=1
#             else:
#                 print("满足条件，不用添加")
#
# #print("最少需要添加%d条边"%x)
# print(x)
