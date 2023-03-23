#
# 27110
# 특식 배부
# https://www.acmicpc.net/problem/27110

import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())

people = 0

if a >= n:
    people += n
else:
    people += a

if b >= n:
    people += n
else:
    people += b

if c >= n:
    people += n
else:
    people += c

print(people)