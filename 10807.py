total = int(input())
arr = list(map(int, input().split()))
v = int(input())
answer = 0

for i in range(total):
    if arr[i] == v:
        answer += 1
print(answer)