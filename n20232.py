#
# 20232
# Archivist
# https://www.acmicpc.net/problem/20232

import sys
input = sys.stdin.readline

y = int(input())

champion = ["ITMO", "SPbSU", "SPbSU", "ITMO", "ITMO", "SPbSU", "ITMO", "ITMO", "ITMO", "ITMO", "ITMO", "PetrSU, ITMO", "SPbSU", "SPbSU", "ITMO", "ITMO", "ITMO", "ITMO", "SPbSU", "ITMO", "ITMO", "ITMO", "ITMO", "SPbSU", "ITMO"]

print(champion[y - 1995])