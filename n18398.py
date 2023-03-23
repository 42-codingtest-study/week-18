#
# 18398
# HOMWRK
# https://www.acmicpc.net/problem/18398

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())

    for j in range(n):
        num = list(map(int, input().split()))
        print(num[0] + num[1], num[0] * num[1])