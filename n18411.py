#
# 18411
# 試験 (Exam)
# https://www.acmicpc.net/problem/18411

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

print(max(a + b, b + c, c + a))