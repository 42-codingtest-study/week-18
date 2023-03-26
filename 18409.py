_ = int(input())
str = input()
res= 0

for i in str:
    if i in ['a','e','i','o','u']:
        res = res+1
print(res)