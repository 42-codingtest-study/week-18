res = 0
for i in range(5):
    num = int(input())
    if num < 40 :
        num = 40
    res += num
average = int(res / 5)
print(average)