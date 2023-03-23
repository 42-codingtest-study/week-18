#
# 26500
# Absolutely
# https://www.acmicpc.net/problem/26500

import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(float, input().split())

    print("%.1f" %(abs(b - a)))