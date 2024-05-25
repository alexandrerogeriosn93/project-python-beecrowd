s, t, f = map(int, input().split())

if s == 0:
    s = 24

hour = (s + t + f) % 24

print(hour)
