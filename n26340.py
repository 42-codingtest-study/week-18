#
# 26340
# Fold the Paper Nicely
# https://www.acmicpc.net/problem/26340

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("Data set:", a, b, c)

    while c > 0:
        if a >= b:
            a //= 2
        else:
            b //= 2

        c -= 1

    print(max(a, b), min(a, b))
    print()