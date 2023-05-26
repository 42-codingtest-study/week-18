#
# 25625
# 샤틀버스
# https://www.acmicpc.net/problem/25625

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

if y > x:
    print(y - x)
else:
    print(x + y)