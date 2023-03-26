import sys

input = sys.stdin.readline
hour_to_sec = 3600
min_to_sec = 60
while True:
    M, A, B = map(float, input().split())
    if M == A == B == 0:
        break
    t = round((M / A - M / B) * hour_to_sec)
    h = t // hour_to_sec
    m = (t % hour_to_sec) // min_to_sec
    s = t % min_to_sec
    print("%d:%02d:%02d" % (h, m, s))
