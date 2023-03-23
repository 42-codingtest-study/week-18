#
# 17863
# FYI
# https://www.acmicpc.net/problem/17863

import sys
input = sys.stdin.readline

call = input()

if call.find("555", 0, 3) == 0:
    print("YES")
else:
    print("NO")