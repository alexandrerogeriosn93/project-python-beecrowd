def validate_data(a, b, c, d):
    return b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0


a, b, c, d = map(int, input().split())

print("Valores aceitos" if validate_data(a, b, c, d) else "Valores nao aceitos")
