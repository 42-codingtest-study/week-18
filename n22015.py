#
# 22015
# 金平糖 (Konpeito)
# https://www.acmicpc.net/problem/22015

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

x = max(a, b, c)

print((x - a) + (x - b) + (x - c))