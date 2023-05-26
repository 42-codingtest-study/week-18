#
# 27541
# 末尾の文字 (Last Letter)
# https://www.acmicpc.net/problem/27541

n = int(input())
s = input()

if s[n - 1] == 'G':
    s = s[:-1]
    print(s)
else:
    s += 'G'
    print(s)