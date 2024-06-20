n = int(input())
g = v = 0

for _ in range(n):
    t, c = input().split()

    match t.upper():
        case "G":
            g += int(c)
        case "V":
            v += int(c)

print("A greve vai parar." if v >= g else "NAO VAI TER CORTE, VAI TER LUTA!")
