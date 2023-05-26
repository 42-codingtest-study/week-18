#
# 21631
# Checkers
# https://www.acmicpc.net/problem/21631

import sys
input = sys.stdin.readline

w, b = map(int, input().split())

print(b if w >= b else w + 1)