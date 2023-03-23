#
# 26768
# H4x0r
# https://www.acmicpc.net/problem/26768

import sys
input = sys.stdin.readline

dict = {'a' : '4',
        'e' : '3',
        'i' : '1',
        'o' : '0',
        's' : '5'}

word = list(input())
find = ['a', 'e', 'i', 'o', 's']
result = []

for i in word:
    chk = 0
    for j in find:
        if i == j:
            chk += 1

    if chk == 0:
        result.append(i)
    else:
        result.append(dict[i])

print(''.join(result))