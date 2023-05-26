#
# 23825
# SASA 모형을 만들어보자
# https://www.acmicpc.net/problem/23825

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = n // 2
a = m // 2

print(min(s, a))