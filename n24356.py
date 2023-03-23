#
# 24356
# ЧАСОВНИК
# https://www.acmicpc.net/problem/24356

t1, m1, t2, m2 = map(int, input().split())

a = t1 * 60 + m1
b = t2 * 60 + m2

if a > b:
    t2 += 24
    b = t2 * 60 + m2

m = b - a
n = m // 30

print(m, n)