#
# 26561
# Population
# https://www.acmicpc.net/problem/26561

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p, t = map(int, input().split())

    print(p - (t // 7) + (t // 4))