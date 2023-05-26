#
# 25703
# 포인터 공부
# https://www.acmicpc.net/problem/25703

import sys
input = sys.stdin.readline

n = int(input())

print("int a;")

for i in range(n):
    print("int", end=' ')
    print('*' * (i + 1), end='')
    print("ptr", end='')
    print((i + 1) if i != 0 else '', end=' ')
    print("= &", end='')
    print("ptr" if i != 0 else "a", end='')
    print(i if i >= 2 else '', end=';')

    if i != n - 1:
        print()
