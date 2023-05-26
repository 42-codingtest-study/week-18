#
# 21665
# Миша и негатив
# https://www.acmicpc.net/problem/21665

# 다시! - 예제 입력 2에서 오류

n, m = map(int, input().split())
pic = [0] * n
repic = [[0] * m] * n
check = [0] * n

for i in range(n):
    pic[i] = list(input())

for i in range(n):
    for j in range(m):
        if pic[i][j] == 'W':
            repic[i][j] = 'B'
        elif pic[i][j] == 'B':
            repic[i][j] = 'W'

input()

for i in range(n):
    check[i] = list(input())

cnt = 0
for i in range(n):
    for j in range(m):
        if repic[i][j] != check[i][j]:
            cnt += 1

print(cnt)