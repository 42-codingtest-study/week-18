#
# 24072
# 帰省 (Homecoming)
# https://www.acmicpc.net/problem/24072

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c < a: # 방문 전에 갈 경우
    print(0)
elif c >= b: # 방문 후에 갈 경우
    print(0)
else:
    print(1)