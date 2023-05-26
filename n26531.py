#
# 26531
# Simple Sum
# https://www.acmicpc.net/problem/26531

math = list(input().split(' '))

if int(math[0]) + int(math[2]) == int(math[4]):
    print("YES")
else:
    print("NO")