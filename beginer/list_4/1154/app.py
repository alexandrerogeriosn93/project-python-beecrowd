sum_ages, counter = 0, 0

while (age := int(input())) >= 0:
    sum_ages += age
    counter += 1

print(f"{(sum_ages / counter):.2f}")
