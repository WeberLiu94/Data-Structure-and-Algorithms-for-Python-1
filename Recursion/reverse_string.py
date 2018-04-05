#思路：两两交换，到中间就停下
def string_reverse(s, n, m):
    if n == m // 2:
        return str(s)
    else:
        s[n], s[m-n-1] = s[m-n-1], s[n]
        return string_reverse(s, n+1, m)


s = 'hel'
x = string_reverse(list(s), 0, len(s))
print(x)