#
# 20839
# Betygsättning
# https://www.acmicpc.net/problem/20839

import sys
input = sys.stdin.readline

x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

if y1 == y2: # A, B, C등급
    if x1 == x2: # A등급
        print("A")
    elif x2 >= x1 / 2: # B등급
        print("B")
    else:
        print("C")
else: # D, E등급
    if y2 >= y1 / 2:
        print("D")
    else:
        print("E")