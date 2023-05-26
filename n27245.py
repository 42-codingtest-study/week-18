#
# 27245
# Комната
# https://www.acmicpc.net/problem/27245

import sys
input = sys.stdin.readline

w = int(input())
l = int(input())
h = int(input())

if min(w, l) >= 2 * h and max(w, l) <= 2 * min(w, l):
    print("good")
else:
    print("bad")