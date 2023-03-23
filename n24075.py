#
# 24075
# 計算 (Calculation)
# https://www.acmicpc.net/problem/24075

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

sum = a + b
minus = a - b

print(max(sum, minus))
print(min(sum, minus))