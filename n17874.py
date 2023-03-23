#
# 17874
# Piece of Cake!
# https://www.acmicpc.net/problem/17874

import sys
input = sys.stdin.readline

n, h, v = map(int, input().split())

res = max(h, n-h) * max(v, n-v)

print(res*4)