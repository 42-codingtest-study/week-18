N = int(input())
O = int(input())
O *= N / (N - 1)
flag = int(O % 1 == 0)
O = int(O)
print(O - flag, O)