#
# 27182
# Rain Diary
# https://www.acmicpc.net/problem/27182

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n - 14 < 0:
    month = m + (14 - n) # 한 달 일수

    if m + 7 > month:
        print(m + 7 - month)
    else:
        print(m + 7)

else:
    print(n- 7)