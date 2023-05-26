#
# 20233
# Bicycle
# https://www.acmicpc.net/problem/20233

import sys
input = sys.stdin.readline

a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

b1 = a
b2 = b

if t > 30:
    b1 += x * (t - 30) * 21

if t > 45:
    b2 += y * (t - 45) * 21

print(b1, b2)