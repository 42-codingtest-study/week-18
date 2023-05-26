#
# 24183
# Affischutskicket
# https://www.acmicpc.net/problem/24183

import sys
input = sys.stdin.readline

a, b, c = map(float, input().split())

envelop = 229 * 324 * a * 2
poster = 297 * 420 * b * 2
sheet = 210 * 297 * c

print(("%.6f" %((envelop + poster + sheet) * 0.000001)))