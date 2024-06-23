from math import sqrt

def calc(a, b, c):
    delta = b ** 2 - 4 * a * c
    return (b + sqrt(delta)) / (2 * a)

l, k, t1, t2, h = map(float, input().split())

if l > h:
    min_max = (h, h)
else:
    f = calc(1, h + k * (t1 + t2), k * l * t1)
    if l < h:
        min_max = (f, f)
    else:
        min_max = (h, f)

print(f"{min_max[0]:.9f} {min_max[1]:.9f}")
