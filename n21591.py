#
# 21591
# Laptop Sticker
# https://www.acmicpc.net/problem/21591

import sys
input = sys.stdin.readline

wc, hc, ws, hs = map(int, input().split())

if wc - 2 >= ws and hc - 2 >= hs:
    print(1)
else:
    print(0)