#
# 20867
# Rulltrappa
# https://www.acmicpc.net/problem/20867

import sys
input = sys.stdin.readline

m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split())

walkwait = l / a
standwait = r / b

walk = m / g + 1 if m % g else m / g
stand = m / s + 1 if m % s else m / s


if walk + walkwait < stand + standwait:
    print("friskus")
else:
    print("latmask")