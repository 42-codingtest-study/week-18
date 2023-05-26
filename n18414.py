#
# 18414
# X に最も近い値 (The Nearest Value)
# https://www.acmicpc.net/problem/18414

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

num.sort()

print(num[1])