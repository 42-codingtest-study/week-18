#
# 18198
# Basketball One-on-One
# https://www.acmicpc.net/problem/18198

score = input()
a = 0
b = 0

for i in range(len(score)):
    if score[i] == 'A':
        a += int(score[i + 1])
    elif score[i] == 'B':
        b += int(score[i + 1])

print('A' if a > b else 'B')