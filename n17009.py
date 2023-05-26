#
# 17009
# Winning Score
# https://www.acmicpc.net/problem/17009

import sys
input = sys.stdin.readline

apple = 0
banana = 0

check = 3
for _ in range(3):
    x = int(input())
    apple += x * check

    check -= 1

check = 3
for _ in range(3):
    x = int(input())
    banana += x * check

    check -= 1

if apple > banana:
    print("A")
elif apple == banana:
    print("T")
else:
    print("B")