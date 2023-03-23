#
# 18330
# Petrol
# https://www.acmicpc.net/problem/18330

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

x = min(k + 60, n)

print(x * 1500 + (n - x) * 3000)