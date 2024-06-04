table = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

while (n := int(input())) != 0:
    consumption = 0

    for i in range(n):
        text = input().split()
        quantity = int(text[0])
        fruit = " ".join(text[1:])
        consumption += table[fruit] * quantity

    if 110 <= consumption <= 130:
        print(f"{consumption} mg")
    elif consumption < 110:
        print(f"Mais {110 - consumption} mg")
    else:
        print(f"Menos {consumption - 130} mg")
