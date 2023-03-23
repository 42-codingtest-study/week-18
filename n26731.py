#
# 26731
# Zagubiona litera
# https://www.acmicpc.net/problem/26731

from string import ascii_uppercase

alpha = list(ascii_uppercase)
result = alpha

word = input()

for w in word:
    for a in alpha:
        if a == w:
            result.remove(a)
print(*result)