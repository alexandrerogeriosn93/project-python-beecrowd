list_numbers = []

for i in range(100):
    list_numbers.append(int(input()))

max_value = max(list_numbers)
max_value_position = list_numbers.index(max_value) + 1

print(f"{max_value}\n{max_value_position}")
