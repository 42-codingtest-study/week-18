#
# 18408
# 3 つの整数 (Three Integers)
# https://www.acmicpc.net/problem/18408

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

if num.count(1) > num.count(2):
    print(1)
else:
    print(2)