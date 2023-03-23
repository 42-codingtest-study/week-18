#
# 17388
# 와글와글 숭고한
# https://www.acmicpc.net/problem/17388

import sys
input = sys.stdin.readline

s, k, h = map(int, input().split())

if s + k + h >= 100:
    print("OK")
else:
    if min(s, k, h) == s:
        print("Soongsil")
    elif min(s, k, h) == k:
        print("Korea")
    elif min(s, k, h) == h:
        print("Hanyang")
