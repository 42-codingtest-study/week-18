N, X = map(int, input().split())
arr = list(map(int, input().split()))
answer = ''

for i in range(0, N):
    if arr[i] < X:
        print(arr[i], end = ' ')