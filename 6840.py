a = int(input())
b = int(input())
c = int(input())
answer = 0

if a > b :
    if a > c:
        if b > c:
            print(b)
        else :
            print(c)
    else :
        print(a)

else :
    if c > b:
        print(b)
    else :
        if a > c :
            print(a)
        else :
            print(c)
