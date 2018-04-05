#思路与上题差不多，两两比较，到中间停下。

def palindrome(s, m, n):
    if n == m // 2:
        return True
    else:
        if s[n] == s[m-n-1]:
            return palindrome(s, m, n+1)
        else:
            return False
s = 'racecar'

result = palindrome(s, len(s), 0)
print(result)