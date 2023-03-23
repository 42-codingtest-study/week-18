#
# 26546
# Reverse
# https://www.acmicpc.net/problem/26546

for _ in range(int(input())):
    x = list(input().split(' '))

    word = x[0]
    start = int(x[1])
    end = int(x[2])

    delete = word[start:end]
    print(word.replace(delete, '', 1))