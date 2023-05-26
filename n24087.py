#
# 24087
# アイスクリーム (Ice Cream)
# https://www.acmicpc.net/problem/24087

import math
import sys
input = sys.stdin.readline

s = int(input())
a = int(input())
b = int(input())

money = 250

if s <= a:
    print(money)
else:
    print(money + 100 * math.ceil((s - a)/b))