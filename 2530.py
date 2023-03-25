t, m, s = map(int, input().split())
hour = int(input())

s += hour
m += s // 60
t += m // 60
print(t % 24, m  % 60, s % 60)