arr = [0] * 30

for _ in range(0, 28):
    a = int(input())
    arr[a-1] = 1

for i in range(0, 30):
    if arr[i] == 0:
        print(i + 1)