#
# 20499
# Darius님 한타 안 함?
# https://www.acmicpc.net/problem/20499

import sys
input = sys.stdin.readline

k, d, a = map(int, input().split('/'))

if k + a < d or d == 0:
    print("hasu")
else:
    print("gosu")