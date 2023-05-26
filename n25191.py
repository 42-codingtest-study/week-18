#
# 25191
# 치킨댄스를 추는 곰곰이를 본 임스
# https://www.acmicpc.net/problem/25191

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

drink = a // 2 +  b

if drink <= n:
    print(drink)
else:
    print(n)