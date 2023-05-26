#
# 27855
# Cornhole
# https://www.acmicpc.net/problem/27855

import sys
input = sys.stdin.readline

h1, b1 = map(int, input().split())
h2, b2 = map(int, input().split())

a = h1 * 3 + b1 * 1
b = h2 * 3 + b2 * 1

if a > b:
    print(1, a - b)
elif b > a:
    print(2, b - a)
else:
    print("NO SCORE")