Matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]




def printMatrix(Matrix):
    list = print_Matrix(Matrix, [])
    return list



def print_Matrix(Matrix,list):
    length= len(Matrix)
    if length == 0:
        return list
    if length == 1:
        list.append(Matrix[0][0])
        return list
    else:
        for i in range(length):
            list.append(Matrix[0][i])
        for i in range(1, length-1):
            list.append(Matrix[i][length-1])
        for i in range(length-1, -1, -1):
            list.append(Matrix[length - 1][i])
        for i in range(length-2, 0, -1):
            list.append(Matrix[i][0])
        return print_Matrix([i[1:-1] for i in Matrix[1:-1]],list)


list = printMatrix([[1]])
print(list)