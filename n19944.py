#
# 19944
# 뉴비의 기준은 뭘까?
# https://www.acmicpc.net/problem/19944

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if m <= 2:
    print("NEWBIE!")
elif m <= n:
    print("OLDBIE!")
else:
    print("TLE!")