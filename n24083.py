#
# 24083
# 短針 (Hour Hand)
# https://www.acmicpc.net/problem/24083

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

start = a + b

print((start % 12) if (start % 12) else 12)