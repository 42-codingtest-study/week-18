#
# 20833
# Kuber
# https://www.acmicpc.net/problem/20833

n = int(input())
ans = 0

for i in range(1, n + 1):
    ans += i ** 3

print(ans)