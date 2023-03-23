#
# 21354
# Äpplen och päron
# https://www.acmicpc.net/problem/21354

import sys
input = sys.stdin.readline

a, p = map(int, input().split())

x = a * 7
y = p * 13

if x > y:
    print("Axel")
elif x < y:
    print("Petra")
else:
    print("lika")