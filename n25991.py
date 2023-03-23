#
# 25991
# Lots of Liquid
# https://www.acmicpc.net/problem/25991

# 다시!

n = int(input())
container = list(map(float, input().split()))

for i in container:
    i **= 3

print(sum(container) ** 0.3333333333333)
