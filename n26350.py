#
# 26350
# Good Coin Denomination
# https://www.acmicpc.net/problem/26350

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = list(map(int, input().split()))
    num = x[0]
    coin = x[1:]

    print("Denominations:", *coin)

    chk = 0
    for i in range(num):
        if i != num - 1:
            if coin[i + 1] < 2 * coin[i]:
                chk = 1


    print("Good coin denominations!" if chk == 0 else "Bad coin denominations!")
    print()