#
# 20976
# 2 番目に大きい整数 (The Second Largest Integer)
# https://www.acmicpc.net/problem/20976

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num.sort()

print(num[1])