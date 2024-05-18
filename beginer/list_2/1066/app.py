evens, odds, positives, negatives = 0, 0, 0, 0

for i in range(5):
    number = int(input())
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1

    if number > 0:
        positives += 1

    if number < 0:
        negatives += 1

print(f"{evens} valor(es) par(es)\n{odds} valor(es) impar(es)\n{positives} valor(es) positivo(s)\n{negatives} valor(es) negativo(s)")
