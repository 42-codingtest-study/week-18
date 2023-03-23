#
# 21631
# Bank Transfer
# https://www.acmicpc.net/problem/21631

import sys
input = sys.stdin.readline

k = int(input())
money = 25 + k * 0.01

if money < 100:
    print(100)
elif money > 2000:
    print(2000)
else:
    print("%.2f" %(money))