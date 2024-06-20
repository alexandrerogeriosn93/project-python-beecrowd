from math import ceil

v, n = map(int, input().split())

p = (v * n) / 10
values = []

for _ in range(9):
    values.append(ceil(p))
    p += (v * n) / 10

print(*values, sep=" ", end="\n")
