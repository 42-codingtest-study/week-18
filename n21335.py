#
# 21335
# Another Eruption
# https://www.acmicpc.net/problem/21335

from math import pi
import sys
input = sys.stdin.readline

n = int(input())

print((n / pi) ** 0.5 * 2 * pi)