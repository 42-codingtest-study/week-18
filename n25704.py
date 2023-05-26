#
# 25704
# 출석 이벤트
# https://www.acmicpc.net/problem/25704

import sys
input = sys.stdin.readline

n = int(input())
price = int(input())
p = [price]

if n >= 20:
    p.append(price * 0.75)
if n >= 15:
    p.append(price - 2000)
if n >= 10:
    p.append(price * 0.9)
if n >= 5:
    p.append(price - 500)


print(int(min(p)) if min(p) > 0 else 0)