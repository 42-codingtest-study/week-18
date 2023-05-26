#
# 26530
# Shipping
# https://www.acmicpc.net/problem/26530

import sys
input = sys.stdin.readline

for _ in range(int(input())):

    total = 0

    for _ in range(int(input())):
        n, x, p = input().split()
        total += int(x) * float(p)

    print("$", end='')
    print("%.2f" %(total))