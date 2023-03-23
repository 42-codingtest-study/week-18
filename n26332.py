#
# 26332
# Buying in Bulk
# https://www.acmicpc.net/problem/26332

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c, p = map(int, input().split())
    price = 0

    print(c, p)
    if c == 1:
        print(p)
    else:
        print(p * c - 2 * (c - 1))