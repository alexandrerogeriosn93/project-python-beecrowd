from math import log

n = int(input())

p = n / log(n)
m = 1.25506 * p

print(f"{p:.1f} {m:.1f}")
