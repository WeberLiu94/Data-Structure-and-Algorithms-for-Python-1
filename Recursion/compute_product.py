#计算两个正数的乘积，只能使用加法与减法
def compute_product(m, n, result):
    if m == 0:
        return result
    else:
        return compute_product(m-1, n, result+n)


x = compute_product(4, 5, 0)
print(x)