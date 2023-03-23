#
# 21612
# Boiling Water
# https://www.acmicpc.net/problem/21612

import sys
input = sys.stdin.readline

b = int(input())
p = 5 * b - 400

print(p)

if p == 100:
    print(0)
else:
    print(1 if p < 100 else -1)