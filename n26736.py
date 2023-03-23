#
# 26736
# Wynik meczu
# https://www.acmicpc.net/problem/26736

import sys
input = sys.stdin.readline

word = input()

a = word.count('A')
b = word.count('B')

print(a, ":", b)