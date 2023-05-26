#
# 25932
# Find the Twins
# https://www.acmicpc.net/problem/25932

for _ in range(int(input())):
    num = list(map(int, input().split()))

    print(*num)

    mack = 0
    zack = 0

    if 17 in num:
        zack += 1
    if 18 in num:
        mack += 1

    if mack == 1:
        if zack == 1:
            print("both")
        else:
            print("mack")
    else:
        if zack == 1:
            print("zack")
        else:
            print("none")

    print()