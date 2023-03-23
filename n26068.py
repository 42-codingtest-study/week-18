#
# 26068
# 치킨댄스를 추는 곰곰이를 본 임스 2
# https://www.acmicpc.net/problem/26068

emoji = []

for _ in range(int(input())):
    x = input()
    emoji.append(x.lstrip("D-"))

day = list(map(int, emoji))

cnt = 0
for i in day:
    if i <= 90:
        cnt += 1

print(cnt)