#
# 27239
# Шахматная доска
# https://www.acmicpc.net/problem/27239

import sys
input = sys.stdin.readline

n = int(input())
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = [1, 2, 3, 4, 5, 6, 7, 8]

x = a[n % 8 - 1]
y = (b[n // 8] if n % 8 != 0 else b[n // 8 - 1])

print(x, y, sep='')