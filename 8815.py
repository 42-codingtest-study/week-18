s = "ABCBCDCDADAB"
for _ in range(int(input())) :
    n = int(input())
    print(s[n % 12 - 1])
