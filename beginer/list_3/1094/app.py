def calc_percentual(rabbits, mouses, frogs, quantity):
    p_rabbits = rabbits / quantity * 100
    p_mouses = mouses / quantity * 100
    p_frogs = frogs / quantity * 100

    return p_rabbits, p_mouses, p_frogs


n = int(input())
rabbits = mouses = frogs = 0

for i in range(1, n + 1):
    quantity, type_animal = input().split()
    quantity = int(quantity)
    type_animal = str(type_animal).upper()

    match type_animal:
        case "C":
            rabbits += quantity
        case "R":
            mouses += quantity
        case "S":
            frogs += quantity

total = rabbits + mouses + frogs
p_rabbits, p_mouses, p_frogs = calc_percentual(rabbits, mouses, frogs, total)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {rabbits}")
print(f"Total de ratos: {mouses}")
print(f"Total de sapos: {frogs}")
print(f"Percentual de coelhos: {p_rabbits:.2f} %")
print(f"Percentual de ratos: {p_mouses:.2f} %")
print(f"Percentual de sapos: {p_frogs:.2f} %")
