#
# 27262
# Лифт
# https://www.acmicpc.net/problem/27262

n, k, a, b = map(int, input().split())

ele = (k + n - 2) * b
stair = (n - 1) * a

print(ele, stair)