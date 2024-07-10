quantity_positives = sum_positives = 0

for i in range(6):
    number = float(input())
    if number > 0:
        sum_positives += number 
        quantity_positives += 1

average_positives = sum_positives / quantity_positives

print(f"{quantity_positives} valores positivos\n{average_positives:.1f}")
