#
# 22155
# Простая задача
# https://www.acmicpc.net/problem/22155

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    i, f = map(int, input().split())

    if i <= 1 and f <= 2:
        print("Yes")
    elif i <= 2 and f <= 1:
        print("Yes")
    else:
        print("No")