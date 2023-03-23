#
# 25377
# 빵
# https://www.acmicpc.net/problem/25377

import sys
input = sys.stdin.readline

cnt = []

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a <= b:
        cnt.append(b)

if len(cnt) != 0:
    print(min(cnt))
else:
    print(-1)