#
# 17356
# 욱 제
# https://www.acmicpc.net/problem/17356

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

m = (b - a) / 400

print(1 / (1 + 10 ** m))