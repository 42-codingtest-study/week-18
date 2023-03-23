#
# 19698
# 헛간 청약
# https://www.acmicpc.net/problem/19698

import sys
input = sys.stdin.readline

n, w, h, l = map(int, input().split())

ans = (w // l) * (h // l)

if n < ans:
    print(n)
else:
    print(ans)