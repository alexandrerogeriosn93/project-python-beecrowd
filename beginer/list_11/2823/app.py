n = int(input())
u = []

for _ in range(n):
    c, p = map(int, input().split())
    u.append(c / p)

print("OK" if sum(u) <= 1 else "FAIL")
