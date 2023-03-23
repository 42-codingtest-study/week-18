#
# 20215
# Cutting Corners
# https://www.acmicpc.net/problem/20215

import sys
input = sys.stdin.readline

w, h = map(int, input().split())

print((w + h) - (w ** 2 + h ** 2) ** 0.5)