#
# 17362
# 수학은 체육과목 입니다 2
# https://www.acmicpc.net/problem/17362

import sys
input = sys.stdin.readline

n = int(input())

ans = n % 8

if ans == 1:
    print(1)
elif ans == 2 or ans == 0:
    print(2)
elif ans == 3 or ans == 7:
    print(3)
elif ans == 4 or ans == 6:
    print(4)
else:
    print(5)