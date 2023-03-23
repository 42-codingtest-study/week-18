#
# 24196
# Gömda ord
# https://www.acmicpc.net/problem/24196

# 다시!

x = list(input())
result = []
next = 0

for i in x:
    if x.index(i) == next:
        result.append(i)
        if i == 'A':
            next += 1
        elif i == 'B':
            next += 2

print(result)