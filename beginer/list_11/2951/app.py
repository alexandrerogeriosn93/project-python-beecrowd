n, g = map(int, input().split())
runes_values = dict()

for _ in range(n):
    r, v = input().split()
    runes_values[r] = int(v)

x = int(input())
runes = input().split()

v = 0

for c in range(x):
    v += runes_values[runes[c]]

print(v)
print("My precioooous" if v < g else "You shall pass!")
