#
# 25881
# Electric Bill
# https://www.acmicpc.net/problem/25881

a, b= map(int, input().split())
n = int(input())

for _ in range(n):
    energy = int(input())
    cost = 0

    if energy <= 1000:
        cost = a * energy
    else:
        cost = a * 1000 + b * (energy - 1000)

    print(energy, cost)