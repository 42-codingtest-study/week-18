#
# 17903
# Counting Clauses
# https://www.acmicpc.net/problem/17903

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

print("satisfactory" if m >= 8 else "unsatisfactory")