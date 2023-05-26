#
# 19602
# Dog Treats
# https://www.acmicpc.net/problem/19602

import sys
input = sys.stdin.readline

s = int(input())
m = int(input())
l = int(input())

happy = s + 2 * m + 3 * l

print("happy" if happy >= 10 else "sad")