#
# 25893
# Majestic 10
# https://www.acmicpc.net/problem/25893

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a, b, c)

    if max(a, b, c) < 10:
        print("zilch")
    elif min(a, b, c) >= 10:
        print("triple-double")
    elif (a >= 10 and max(b, c) < 10) or (b >= 10 and max(c, a) < 10) or (c >= 10 and max(a, b) < 10):
        print("double")
    elif (a < 10 and min(b, c) >= 10) or (b < 10 and min(c, a) >= 10) or (c < 10 and min(a, b) >= 10):
        print("double-double")

    print()