#
# 24860
# Counting Antibodies
# https://www.acmicpc.net/problem/24860

import sys
input = sys.stdin.readline

v1, j1 = map(int, input().split())
v2, j2 = map(int, input().split())
vh, dh, jh = map(int, input().split())

print((vh * jh * dh) * (v1 * j1 + v2 * j2))