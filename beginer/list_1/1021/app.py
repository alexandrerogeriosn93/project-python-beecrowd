reais, cents = map(int, input().split("."))
cents += reais * 100

notes = [100, 50, 20, 10, 5, 2]
coins = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for note in notes:
    print(f"{cents//(note * 100)} nota(s) de R$ {note}.00")
    cents = cents % (note * 100)

print("MOEDAS:")
for coin in coins:
    print(f"{cents//coin} moeda(s) de R$ {coin // 100}.{coin % 100:02}")
    cents = cents % coin
