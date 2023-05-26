#
# 25600
# Triathlon
# https://www.acmicpc.net/problem/25600

import sys
input = sys.stdin.readline

score = []

for _ in range(int(input())):
    a, d, g = map(int, input().split())

    s = a * (d + g)

    if a == d + g:
        score.append(s * 2)
    else:
        score.append(s)

print(max(score))
