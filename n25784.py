#
# 25784
# Easy-to-Solve Expressions
# https://www.acmicpc.net/problem/25784

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def if_sum(a, b, c):
    if a + b == c:
        return 1
    if b + c == a:
        return 1
    if c + a == b:
        return 1

    return 0

def if_mul(a, b, c):
    if a * b == c:
        return 1
    if b * c == a:
        return 1
    if c * a == b:
        return 1

    return 0

if if_sum(a, b, c):
    print(1)
elif if_mul(a, b, c):
    print(2)
else:
    print(3)