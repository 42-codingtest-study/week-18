arr = input()
res = [0] * 26

for i in arr :
    res[ord(i) - 97] += 1
print(*res)