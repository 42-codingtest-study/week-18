#
# 25591
# 푸앙이와 종윤이
# https://www.acmicpc.net/problem/25591

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100

print(a, b, c, d, q, r)
print(c + q, r)