#
# 23795
# 사장님 도박은 재미로 하셔야 합니다
# https://www.acmicpc.net/problem/23795

import sys
input = sys.stdin.readline

sum = 0

while 1:
    x = int(input())

    if x == -1:
        print(sum)
        exit()

    sum += x