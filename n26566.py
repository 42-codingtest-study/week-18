#
# 26566
# Pizza
# https://www.acmicpc.net/problem/26566

from math import pi

for _ in range(int(input())):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())

    slice = a1 / p1
    hall = (r1 * r1 * pi) / p2

    if slice > hall:
        print("Slice of pizza")
    elif hall > slice:
        print("Whole pizza")