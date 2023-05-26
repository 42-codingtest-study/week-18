#
# 27590
# Sun and Moon
# https://www.acmicpc.net/problem/27590

import sys
input = sys.stdin.readline

d1, y1 = map(int, input().split())
d2, y2 = map(int, input().split())

sun = y1 - d1
moon = y2 - d2

for i in range(5001):
    sun -= 1
    moon -= 1

    if not sun and not moon:
        print(i + 1)
        break
    elif not sun and moon:
        sun += y1
    elif sun and not moon:
        moon += y2