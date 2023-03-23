#
# 25828
# Corona Virus Testing
# https://www.acmicpc.net/problem/25828

import sys
input = sys.stdin.readline

g, p, t = map(int, input().split())

personal = g * p
group = g + p * t

if personal > group:
    print(2)
elif personal < group:
    print(1)
else:
    print(0)