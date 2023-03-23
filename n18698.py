#
# 18698
# The Walking Adam
# https://www.acmicpc.net/problem/18698

import sys
input = sys.stdin.readline

result = 0

for _ in range(int(input())):
    t = input()

    for j in range(len(t)):
        if t[j] == "U":
            result += 1
        else:
            break
    print(result)
    result = 0