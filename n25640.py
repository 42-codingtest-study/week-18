#
# 25640
# MBTI
# https://www.acmicpc.net/problem/25640

import sys
input = sys.stdin.readline

mbti = input()
cnt = 0

for _ in range(int(input())):
    friend = input()

    if mbti == friend:
        cnt += 1

print(cnt)