#
# 26532
# Acres
# https://www.acmicpc.net/problem/26532

a, b = map(int, input().split())

field = a * b
acre = field / 4840
print(int(acre / 5) + 1)