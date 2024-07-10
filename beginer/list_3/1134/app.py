alcohol = gasoline = diesel = 0

while (code := int(input())) != 4:
    match code:
        case 1:
            alcohol += 1
        case 2:
            gasoline += 1
        case 3:
            diesel += 1

print(f"MUITO OBRIGADO\nAlcool: {alcohol}\nGasolina: {gasoline}\nDiesel: {diesel}")
