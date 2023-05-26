#
# 26592
# Triangle Height
# https://www.acmicpc.net/problem/26592

for _ in range(int(input())):
    a, b = map(float, input().split())

    h = 2 * a / b

    print("The height of the triangle is %.2f units" %h)