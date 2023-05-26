#
# 25628
# 햄버거 만들기
# https://www.acmicpc.net/problem/25628

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

print(min(a // 2, b))