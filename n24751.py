#
# 24751
# Betting
# https://www.acmicpc.net/problem/24751

import sys
input = sys.stdin.readline

a = int(input())

print("%0.10f" %(100 / a))
print("%0.10f" %(100 / (100 - a)))