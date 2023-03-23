#
# 25494
# 단순한 문제 (Small)
# https://www.acmicpc.net/problem/25494

# 서로 나누었을 때 나머지가 같으려면 같은 수여야 한다

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    cnta = [i for i in range(1, a + 1)]
    cntb = [i for i in range(1, b + 1)]
    cntc = [i for i in range(1, c + 1)]

    print(min(a, b, c))