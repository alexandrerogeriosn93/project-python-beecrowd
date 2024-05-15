def validate_data(a, b, c, d):
    return b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0

a, b, c, d = [int(x) for x in input().split()]

print("Valores aceitos") if validate_data(a, b, c, d) else print("Valores nao aceitos")
