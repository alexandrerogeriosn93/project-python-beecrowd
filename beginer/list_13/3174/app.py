n = int(input())
b = a = m = d = 0

for i in range(n):
    e, g, h = input().split()
    h = int(h)

    match g:
        case "bonecos":
            b += h
        case "arquitetos":
            a += h
        case "musicos":
            m += h
        case "desenhistas":
            d += h

res = b // 8 + a // 4 + m // 6 + d // 12
print(res)
