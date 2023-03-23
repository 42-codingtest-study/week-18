#
# 25858
# Divide the Cash
# https://www.acmicpc.net/problem/25858

import sys
input = sys.stdin.readline

n, d = map(int, input().split())
p = []

for _ in range(n):
    p.append(int(input()))

one = d // sum(p)

for i in p:
    print(i * one)