#
# 18409
# 母音を数える (Counting Vowels)
# https://www.acmicpc.net/problem/18409

import sys
input = sys.stdin.readline

n = int(input())
str = input()

cnt = 0

for s in str:
    if s in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1

print(cnt)