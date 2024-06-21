n = int(input())

cars = dolls = 0

for _ in range(n):
    name, op = input().split()

    match op:
        case "M":
            cars += 1
        case "F":
            dolls += 1

print(f"{cars} carrinhos\n{dolls} bonecas")
